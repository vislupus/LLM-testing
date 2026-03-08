#!/usr/bin/env bash
set -euo pipefail

# Usage:
#   ./make_csv.sh INPUT.md [OUTPUT.csv] [OUTPUT_TABLE.md]
#
# Defaults:
#   INPUT.md           -> README.md
#   OUTPUT.csv         -> scores_by_model.csv
#   OUTPUT_TABLE.md    -> scores_by_model_table.md

in="${1:-README.md}"
out_csv="${2:-scores_by_model.csv}"
out_md="${3:-scores_by_model_table.md}"

if [[ ! -f "$in" ]]; then
  echo "Input file not found: $in" >&2
  echo "Usage: $0 INPUT.md [OUTPUT.csv] [OUTPUT_TABLE.md]" >&2
  exit 1
fi

awk -v OUTCSV="$out_csv" -v OUTMD="$out_md" '
function trim(s) { sub(/^[ \t\r\n]+/, "", s); sub(/[ \t\r\n]+$/, "", s); return s }
function clean(s){ gsub(/\*\*/, "", s); gsub(/\*/, "", s); return trim(s) }
function csvq(s){ gsub(/"/, "\"\"", s); return "\"" s "\"" }

BEGIN {
  prompt=0; in_table=0; need_sep=0;
  # Always output exactly 31 prompt columns as requested
  P=31;

  # Clear output files
  close(OUTCSV); close(OUTMD);
  system("> \"" OUTCSV "\"");
  system("> \"" OUTMD "\"");
}

/^\|[ \t]*Model[ \t]*\|[ \t]*Score/ {
  prompt++; in_table=1; need_sep=1; next
}

in_table && need_sep && /^\|[ \t]*-+/ { need_sep=0; next }

in_table && !need_sep && /^\|/ {
  line=$0
  sub(/^\|/, "", line)
  sub(/\|[ \t]*$/, "", line)
  n=split(line, a, /\|/)

  model=clean(a[1])
  score=clean(a[2])

  if (model != "" && score != "") {
    if (!seen[model]++) order[++mcount]=model

    # Extract numeric before "/10" (portable awk)
    valstr=""
    if (match(score, /[0-9]+(\.[0-9]+)?[ \t]*\/[ \t]*10/)) {
      s = substr(score, RSTART, RLENGTH)
      sub(/[ \t]*\/.*/, "", s)   # remove "/10"
      valstr = s
      val = s + 0
      sum[model] += val
      cnt[model] += 1
    } else {
      # If it is not like x/10, keep empty (or you can set valstr=score)
      valstr=""
    }

    key = model SUBSEP prompt
    vals[key] = valstr
  }
  next
}

in_table && !/^\|/ { in_table=0; need_sep=0; next }

END {
  # --- CSV header (English)
  printf "Model" >> OUTCSV
  for (j=1; j<=P; j++) printf ",Prompt%02d", j >> OUTCSV
  printf ",SUM,AVG\n" >> OUTCSV

  # --- MD table header
  printf "| Model " >> OUTMD
  for (j=1; j<=P; j++) printf "| Prompt%02d ", j >> OUTMD
  printf "| SUM | AVG |\n" >> OUTMD

  printf "|---" >> OUTMD
  for (j=1; j<=P; j++) printf "|---" >> OUTMD
  printf "|---|---|\n" >> OUTMD

  # --- Rows
  for (i=1; i<=mcount; i++) {
    model = order[i]

    # CSV row
    printf "%s", csvq(model) >> OUTCSV
    for (j=1; j<=P; j++) {
      key = model SUBSEP j
      v = (key in vals) ? vals[key] : ""
      if (v == "") printf "," >> OUTCSV
      else printf ",%s", v >> OUTCSV
    }
    ssum = (model in sum) ? sum[model] : 0
    c = (model in cnt) ? cnt[model] : 0
    avg = (c>0) ? (ssum/c) : 0
    printf ",%.2f,%.2f\n", ssum, avg >> OUTCSV

    # MD row
    printf "| %s ", model >> OUTMD
    for (j=1; j<=P; j++) {
      key = model SUBSEP j
      v = (key in vals) ? vals[key] : ""
      printf "| %s ", v >> OUTMD
    }
    printf "| %.2f | %.2f |\n", ssum, avg >> OUTMD
  }

  if (prompt != P) {
    print "WARN: Found " prompt " prompt tables in input, but output is fixed to " P " columns." > "/dev/stderr"
  }
}
' "$in"

echo "✅ Wrote CSV: $out_csv"
echo "✅ Wrote Markdown table: $out_md"
