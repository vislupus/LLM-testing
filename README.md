# LLM-testing
Testing different LLMs to do software tasks

## **Model Evaluation Scale (1–10)**

| Score  | Meaning                                                              |
| ------ | -------------------------------------------------------------------- |
| **1**  | Completely unusable output; fails to follow instructions.            |
| **2**  | Output is extremely poor; major errors and missing functionality.    |
| **3**  | Works, but the result is not good; significant issues remain.        |
| **4**  | Mostly works, but quality is still poor; inconsistent or incomplete. |
| **5**  | The result is okay; acceptable but needs noticeable improvement.     |
| **6**  | The result is okay; generally functional with minor issues.          |
| **7**  | Good output; reliable and mostly accurate.                           |
| **8**  | Very good quality; strong performance with small limitations.        |
| **9**  | Excellent output; high accuracy and completeness.                    |
| **10** | Near-perfect result; exceptional clarity, accuracy, and execution.   |

## Prompts

### 02 - Excel clone
**Create a functional clone of Microsoft Excel in a single standalone HTML file (no external dependencies except CSS/JS embedded or via CDN). The UI should resemble a modern spreadsheet app with a toolbar at the top, a formula bar, column headers (A, B, C, …), row numbers (1, 2, 3, …), and a scrollable grid of editable cells. Each cell must support entering values and formulas (starting with =), with basic formula support for arithmetic (+ - * /), cell references (e.g. =A1+B2), and simple functions like SUM, AVERAGE, MIN, MAX over ranges (e.g. =SUM(A1:A10)). While editing a formula in the formula bar, allow the user to click or drag-select cells/ranges so their addresses (e.g. A1, B2, A1:A10) are automatically inserted into the formula. Implement automatic recalculation of dependent cells whenever a referenced cell changes, and display the currently selected cell’s address and formula/value in the formula bar. Include basic features such as: selecting cells with mouse, dragging to select ranges, double-click to edit, keyboard navigation with arrow keys/Enter/Tab, resizing columns, and support for multiple sheets (with sheet tabs and the ability to add/rename/delete sheets). Add a minimal toolbar with actions like bold/italic text, background color for cells, clear contents, and a simple “Download as CSV” and “Upload CSV” for the active sheet. Make the design clean and responsive, visually inspired by Excel but without using any copyrighted assets, and ensure everything runs smoothly in the browser without a backend.**

| Model                 | Score    |
| --------------------- | -------- |
| **Gemini 3.7 flash**  | **7/10** |
| **Gemini 3.6 flash**  | **3/10** |
| **Gemini 3.5 flash**  | **4/10** |
| **Gemini 3.1**        | **1/10** |
| **Gemini 3 flash**    | **3/10** |
| **Gemini 2.5**        | **1/10** |
| **Gemma 4 31B**       | **2/10** |
| **ChatGPT 5.6**       | **5/10** |
| **ChatGPT 5.5**       | **2/10** |
| **ChatGPT 5.4**       | **6/10** |
| **ChatGPT 5.3**       | **3/10** |
| **ChatGPT 5.2**       | **4/10** |
| **ChatGPT 5.1**       | **3/10** |
| **ChatGPT 5**         | **1/10** |
| **ChatGPT o3**        | **3/10** |
| **ChatGPT 4.1**       | **1/10** |
| **GPT-OSS-120b**      | **1/10** |
| **GPT-OSS-20b**       | **0/10** |
| **Grok 4.6**          | **9/10** |
| **Grok 4.5**          | **8/10** |
| **Grok 4.3**          | **3/10** |
| **Grok 4.2**          | **4/10** |
| **Grok 4.1**          | **1/10** |
| **Claude Fable 5**    | **8/10** |
| **Claude Opus 5**     | **8/10** |
| **Claude Opus 4.8**   | **8/10** |
| **Claude Opus 4.7**   | **8/10** |
| **Claude Opus 4.6**   | **7/10** |
| **Claude Opus 4.5**   | **2/10** |
| **Claude Opus 4.1**   | **2/10** |
| **Claude Opus 3**     | **2/10** |
| **Glm 5.2**           | **2/10** |
| **Glm 5.1**           | **6/10** |
| **Glm 5**             | **3/10** |
| **Glm 4.7**           | **2/10** |
| **Glm 4.6**           | **2/10** |
| **Kimi K3**           | **7/10** |
| **Kimi K2.7 code**    | **1/10** |
| **Kimi K2.6**         | **7/10** |
| **Kimi K2.5**         | **2/10** |
| **Kimi K2 Turbo**     | **2/10** |
| **Deepseek 4 flash**  | **1/10** |
| **Deepseek 4**        | **4/10** |
| **Deepseek 3.2**      | **3/10** |
| **Мinimax m3**        | **5/10** |
| **Мinimax m2.7**      | **2/10** |
| **Мinimax m2.5**      | **3/10** |
| **Мinimax m2.1**      | **2/10** |
| **Мinimax m2**        | **2/10** |
| **Мinimax m1**        | **2/10** |
| **Qwen 3.8 Max**      | **5/10** |
| **Qwen 3.7 Max**      | **4/10** |
| **Qwen 3.6 Max**      | **5/10** |
| **Qwen 3.6**          | **4/10** |
| **Qwen 3.5 Max**      | **0/10** |
| **Qwen 3.5**          | **4/10** |
| **Qwen 3 Max**        | **1/10** |
| **Qwen 3.5 122b a10b**| **1/10** |
| **Qwen 3.5 35b a3b**  | **2/10** |
| **Qwen 3.6 27b**      | **3/10** |
| **MiMo 2.5**          | **3/10** |
| **MiMo 2**            | **3/10** |
| **LongCat 2**         | **4/10** |
| **Nemotron 3 ultra**  | **1/10** |
| **Trinity**           | **3/10** |
| **HY3**               | **4/10** |
| **Laguna S 2.1**      | **1/10** |
| **Muse Spark 1.1**    | **4/10** |
| **Muse Glimmer**      | **1/10** |
| **Inkling**           | **2/10** |
| **Mistral Large 3**   | **2/10** |
| **Mistral Medium 3.5**| **1/10** |

---

### 12 - 3D castle scene
**High-poly 3D floating island diorama with a large medieval stone castle at the center. Around it: a cozy medieval village with wooden houses, tavern, market stalls, and a riverside mill. Steep rocky cliffs, lush grass, pine trees, turquoise river with wooden bridges, waterfalls, and a ruined watchtower at the edge. Vibrant stylized colors, soft lighting, handcrafted tabletop-miniature look. Use Babylon.js as a single standalone HTML file (all HTML/CSS/JS in one file; Babylon.js may be loaded from a CDN).**

| Model                 | Score    |
| --------------------- | -------- |
| **Gemini 3.7 flash**  | **3/10** |
| **Gemini 3.6 flash**  | **1/10** |
| **Gemini 3.5 flash**  | **4/10** |
| **Gemini 3.1**        | **1/10** |
| **Gemini 3 flash**    | **3/10** |
| **Gemini 2.5**        | **2/10** |
| **Gemma 4 31B**       | **1/10** |
| **ChatGPT 5.6**       | **6/10** |
| **ChatGPT 5.5**       | **2/10** |
| **ChatGPT 5.4**       | **5/10** |
| **ChatGPT 5.3**       | **2/10** |
| **ChatGPT 5.2**       | **1/10** |
| **ChatGPT 5.1**       | **4/10** |
| **ChatGPT 5**         | **3/10** |
| **ChatGPT o3**        | **1/10** |
| **ChatGPT 4.1**       | **1/10** |
| **GPT-OSS-120b**      | **1/10** |
| **GPT-OSS-20b**       | **0/10** |
| **Grok 4.6**          | **7/10** |
| **Grok 4.5**          | **4/10** |
| **Grok 4.3**          | **3/10** |
| **Grok 4.2**          | **1/10** |
| **Grok 4.1**          | **3/10** |
| **Claude Fable 5**    | **7/10** |
| **Claude Opus 5**     | **7/10** |
| **Claude Opus 4.8**   | **8/10** |
| **Claude Opus 4.7**   | **7/10** |
| **Claude Opus 4.6**   | **7/10** |
| **Claude Opus 4.5**   | **5/10** |
| **Claude Opus 4.1**   | **1/10** |
| **Claude Opus 3**     | **2/10** |
| **Glm 5.2**           | **2/10** |
| **Glm 5.1**           | **6/10** |
| **Glm 5**             | **1/10** |
| **Glm 4.7**           | **3/10** |
| **Glm 4.6**           | **3/10** |
| **Kimi K3**           | **6/10** |
| **Kimi K2.7 code**    | **5/10** |
| **Kimi K2.6**         | **1/10** |
| **Kimi K2.5**         | **4/10** |
| **Kimi K2 Turbo**     | **3/10** |
| **Deepseek 4 flash**  | **1/10** |
| **Deepseek 4**        | **3/10** |
| **Deepseek 3.2**      | **5/10** |
| **Мinimax m3**        | **1/10** |
| **Мinimax m2.7**      | **7/10** |
| **Мinimax m2.5**      | **4/10** |
| **Мinimax m2.1**      | **1/10** |
| **Мinimax m2**        | **2/10** |
| **Мinimax m1**        | **1/10** |
| **Qwen 3.8 Max**      | **1/10** |
| **Qwen 3.7 Max**      | **3/10** |
| **Qwen 3.6 Max**      | **1/10** |
| **Qwen 3.6**          | **1/10** |
| **Qwen 3.5 Max**      | **1/10** |
| **Qwen 3.5**          | **1/10** |
| **Qwen 3 Max**        | **1/10** |
| **Qwen 3.5 122b a10b**| **1/10** |
| **Qwen 3.5 35b a3b**  | **1/10** |
| **Qwen 3.6 27b**      | **1/10** |
| **MiMo 2.5**          | **4/10** |
| **MiMo 2**            | **1/10** |
| **LongCat 2**         | **1/10** |
| **Nemotron 3 ultra**  | **3/10** |
| **Trinity**           | **1/10** |
| **HY3**               | **2/10** |
| **Laguna S 2.1**      | **1/10** |
| **Muse Spark 1.1**    | **2/10** |
| **Muse Glimmer**      | **2/10** |
| **Inkling**           | **2/10** |
| **Mistral Large 3**   | **1/10** |
| **Mistral Medium 3.5**| **1/10** |

---

### 15 - Space battle simulation
**A 3D space battle scene in **Babylon.js** as a single standalone HTML file (all HTML/CSS/JS in one file; Babylon.js may be loaded from a CDN). Between two opposing fleets, each with 10 ships. Every fleet has one larger flagship and nine smaller escort ships. The flagships are clearly bigger and more detailed, positioned at the center of each formation. Each ship has a visible health bar above it; when health reaches zero the ship explodes in a spectacular way, with bright fire, sparks, shockwaves and debris. If another ship is within roughly one ship‑width of the explosion, it also detonates in a chain reaction. Ships constantly move and maneuver in three‑dimensional space, turning and accelerating as they try to destroy the enemy fleet. One fleet fires bright blue glowing projectiles, the other fires bright red glowing projectiles, clearly distinguishing the two sides. Normal ships fire a single projectile every 3 seconds, while the two flagships fire two projectiles at once every 3 seconds. The scene should feel dynamic and cinematic, with trails behind projectiles, directional lighting from engine thrusters, and a starfield or nebula background. Make sure the whole scene is orbit-camera controlled, nicely lit, and fully working when the HTML file is opened in a browser.**

| Model                 | Score    |
| --------------------- | -------- |
| **Gemini 3.7 flash**  | **7/10** |
| **Gemini 3.6 flash**  | **4/10** |
| **Gemini 3.5 flash**  | **1/10** |
| **Gemini 3.1**        | **4/10** |
| **Gemini 3 flash**    | **1/10** |
| **Gemini 2.5**        | **1/10** |
| **Gemma 4 31B**       | **1/10** |
| **ChatGPT 5.6**       | **9/10** |
| **ChatGPT 5.5**       | **8/10** |
| **ChatGPT 5.4**       | **7/10** |
| **ChatGPT 5.3**       | **2/10** |
| **ChatGPT 5.2**       | **1/10** |
| **ChatGPT 5.1**       | **7/10** |
| **ChatGPT 5**         | **1/10** |
| **ChatGPT o3**        | **1/10** |
| **ChatGPT 4.1**       | **1/10** |
| **GPT-OSS-120b**      | **1/10** |
| **GPT-OSS-20b**       | **0/10** |
| **Grok 4.6**          | **8/10** |
| **Grok 4.5**          | **7/10** |
| **Grok 4.3**          | **1/10** |
| **Grok 4.2**          | **1/10** |
| **Grok 4.1**          | **2/10** |
| **Claude Fable 5**    | **9/10** |
| **Claude Opus 5**     | **10/10** |
| **Claude Opus 4.8**   | **9/10** |
| **Claude Opus 4.7**   | **10/10** |
| **Claude Opus 4.6**   | **9/10** |
| **Claude Opus 4.5**   | **7/10** |
| **Claude Opus 4.1**   | **1/10** |
| **Claude Opus 3**     | **3/10** |
| **Glm 5.2**           | **5/10** |
| **Glm 5.1**           | **1/10** |
| **Glm 5**             | **3/10** |
| **Glm 4.7**           | **1/10** |
| **Glm 4.6**           | **1/10** |
| **Kimi K3**           | **8/10** |
| **Kimi K2.7 code**    | **5/10** |
| **Kimi K2.6**         | **5/10** |
| **Kimi K2.5**         | **1/10** |
| **Kimi K2 Turbo**     | **1/10** |
| **Deepseek 4 flash**  | **1/10** |
| **Deepseek 4**        | **4/10** |
| **Deepseek 3.2**      | **4/10** |
| **Мinimax m3**        | **5/10** |
| **Мinimax m2.7**      | **5/10** |
| **Мinimax m2.5**      | **1/10** |
| **Мinimax m2.1**      | **1/10** |
| **Мinimax m2**        | **3/10** |
| **Мinimax m1**        | **4/10** |
| **Qwen 3.8 Max**      | **5/10** |
| **Qwen 3.7 Max**      | **1/10** |
| **Qwen 3.6 Max**      | **1/10** |
| **Qwen 3.6**          | **3/10** |
| **Qwen 3.5 Max**      | **0/10** |
| **Qwen 3.5**          | **1/10** |
| **Qwen 3 Max**        | **4/10** |
| **Qwen 3.5 122b a10b**| **1/10** |
| **Qwen 3.5 35b a3b**  | **1/10** |
| **Qwen 3.6 27b**      | **1/10** |
| **MiMo 2.5**          | **1/10** |
| **MiMo 2**            | **1/10** |
| **LongCat 2**         | **1/10** |
| **Nemotron 3 ultra**  | **1/10** |
| **Trinity**           | **1/10** |
| **HY3**               | **5/10** |
| **Laguna S 2.1**      | **1/10** |
| **Muse Spark 1.1**    | **3/10** |
| **Muse Glimmer**      | **2/10** |
| **Inkling**           | **1/10** |
| **Mistral Large 3**   | **1/10** |
| **Mistral Medium 3.5**| **1/10** |

---

### 25 - Equal Earth projection
**Create a single‑file interactive world map using SVG.js that renders the Earth in the Equal Earth projection and supports full coordinate ↔ screen conversion. The app should draw a clean vector world map in Equal Earth, with zoom and pan (mouse wheel + drag) that keep the projection mathematically correct at any scale. Implement forward projection: given geographic coordinates (latitude, longitude in degrees), convert them to projected x,y in the Equal Earth projection and plot a small SVG circle/marker at the correct location on the map. Implement inverse projection as well: when the user clicks on any point of the map (taking into account current zoom and pan), compute the corresponding latitude and longitude for that position and display them in a small overlay or console readout. All logic (HTML, CSS, JavaScript, SVG.js setup, projection formulas, zoom/pan handling, marker drawing and coordinate display) must be contained in a single self‑contained HTML file that runs directly in the browser.**

| Model                 | Score    |
| --------------------- | -------- |
| **Gemini 3.7 flash**  | **0/10** |
| **Gemini 3.6 flash**  | **0/10** |
| **Gemini 3.5 flash**  | **0/10** |
| **Gemini 3.1**        | **2/10** |
| **Gemini 3 flash**    | **3/10** |
| **Gemini 2.5**        | **1/10** |
| **Gemma 4 31B**       | **0/10** |
| **ChatGPT 5.6**       | **9/10** |
| **ChatGPT 5.5**       | **5/10** |
| **ChatGPT 5.4**       | **5/10** |
| **ChatGPT 5.3**       | **3/10** |
| **ChatGPT 5.2**       | **3/10** |
| **ChatGPT 5.1**       | **2/10** |
| **ChatGPT 5**         | **2/10** |
| **ChatGPT o3**        | **1/10** |
| **ChatGPT 4.1**       | **0/10** |
| **GPT-OSS-120b**      | **0/10** |
| **GPT-OSS-20b**       | **0/10** |
| **Grok 4.6**          | **0/10** |
| **Grok 4.5**          | **10/10** |
| **Grok 4.3**          | **2/10** |
| **Grok 4.2**          | **3/10** |
| **Grok 4.1**          | **1/10** |
| **Claude Fable 5**    | **8/10** |
| **Claude Opus 5**     | **10/10** |
| **Claude Opus 4.8**   | **0/10** |
| **Claude Opus 4.7**   | **10/10** |
| **Claude Opus 4.6**   | **6/10** |
| **Claude Opus 4.5**   | **5/10** |
| **Claude Opus 4.1**   | **2/10** |
| **Claude Opus 3**     | **0/10** |
| **Glm 5.2**           | **1/10** |
| **Glm 5.1**           | **5/10** |
| **Glm 5**             | **6/10** |
| **Glm 4.7**           | **1/10** |
| **Glm 4.6**           | **2/10** |
| **Kimi K3**           | **0/10** |
| **Kimi K2.7 code**    | **5/10** |
| **Kimi K2.6**         | **1/10** |
| **Kimi K2.5**         | **5/10** |
| **Kimi K2 Turbo**     | **2/10** |
| **Deepseek 4 flash**  | **0/10** |
| **Deepseek 4**        | **3/10** |
| **Deepseek 3.2**      | **3/10** |
| **Мinimax m3**        | **0/10** |
| **Мinimax m2.7**      | **1/10** |
| **Мinimax m2.5**      | **5/10** |
| **Мinimax m2.1**      | **1/10** |
| **Мinimax m2**        | **0/10** |
| **Мinimax m1**        | **0/10** |
| **Qwen 3.8 Max**      | **7/10** |
| **Qwen 3.7 Max**      | **1/10** |
| **Qwen 3.6 Max**      | **1/10** |
| **Qwen 3.6**          | **2/10** |
| **Qwen 3.5 Max**      | **0/10** |
| **Qwen 3.5**          | **2/10** |
| **Qwen 3 Max**        | **0/10** |
| **Qwen 3.5 122b a10b**| **0/10** |
| **Qwen 3.5 35b a3b**  | **0/10** |
| **Qwen 3.6 27b**      | **1/10** |
| **MiMo 2.5**          | **0/10** |
| **MiMo 2**            | **3/10** |
| **LongCat 2**         | **1/10** |
| **Nemotron 3 ultra**  | **0/10** |
| **Trinity**           | **1/10** |
| **HY3**               | **0/10** |
| **Laguna S 2.1**      | **1/10** |
| **Muse Spark 1.1**    | **3/10** |
| **Muse Glimmer**      | **0/10** |
| **Inkling**           | **0/10** |
| **Mistral Large 3**   | **1/10** |
| **Mistral Medium 3.5**| **1/10** |

---

### 32 - SVG pagoda with dragon
**Create a complex standalone SVG illustration of a traditional Chinese pagoda in a beautiful garden. The pagoda should have 7 or 8 floors, inspired by important classical Chinese pagoda architecture. It should be symmetrical, elegant, and highly detailed. The SVG must include layered roofs with curved eaves, decorative tiles, wooden beams, balconies, lanterns, windows, carved ornaments, and traditional Chinese architectural details. Around the pagoda, draw a large Chinese dragon coiling gracefully around the structure. The dragon should have a serpentine body, scales, horns, whiskers, claws, flowing mane, and an expressive face. It should wrap around the pagoda without hiding the entire building. Place the pagoda in a peaceful garden with rocks, bamboo, pine trees, flowers, a small pond, clouds, mist, and decorative pathways. Use gradients, shadows, patterns, and fine line details to make the SVG visually rich and complex. The final result should be a single valid SVG file, scalable, cleanly structured, and readable. Use only SVG elements, no external images. Style: detailed vector art, elegant Chinese fantasy atmosphere, balanced composition, rich colors, gold and red accents, ornamental but clean.**

| Model                 | Score    |
| --------------------- | -------- |
| **Gemini 3.7 flash**  | **3/10** |
| **Gemini 3.6 flash**  | **4/10** |
| **Gemini 3.5 flash**  | **4/10** |
| **Gemini 3.1**        | **3/10** |
| **Gemini 3 flash**    | **3/10** |
| **Gemini 2.5**        | **3/10** |
| **Gemma 4 31B**       | **2/10** |
| **ChatGPT 5.6**       | **6/10** |
| **ChatGPT 5.5**       | **4/10** |
| **ChatGPT 5.4**       | **3/10** |
| **ChatGPT 5.3**       | **2/10** |
| **ChatGPT 5.2**       | **2/10** |
| **ChatGPT 5.1**       | **3/10** |
| **ChatGPT 5**         | **3/10** |
| **ChatGPT o3**        | **2/10** |
| **ChatGPT 4.1**       | **2/10** |
| **GPT-OSS-120b**      | **2/10** |
| **GPT-OSS-20b**       | **0/10** |
| **Grok 4.6**          | **5/10** |
| **Grok 4.5**          | **5/10** |
| **Grok 4.3**          | **3/10** |
| **Grok 4.2**          | **4/10** |
| **Grok 4.1**          | **2/10** |
| **Claude Fable 5**    | **7/10** |
| **Claude Opus 5**     | **8/10** |
| **Claude Opus 4.8**   | **6/10** |
| **Claude Opus 4.7**   | **5/10** |
| **Claude Opus 4.6**   | **4/10** |
| **Claude Opus 4.5**   | **0/10** |
| **Claude Opus 4.1**   | **0/10** |
| **Claude Opus 3**     | **2/10** |
| **Glm 5.2**           | **4/10** |
| **Glm 5.1**           | **3/10** |
| **Glm 5**             | **4/10** |
| **Glm 4.7**           | **3/10** |
| **Glm 4.6**           | **2/10** |
| **Kimi K3**           | **5/10** |
| **Kimi K2.7 code**    | **4/10** |
| **Kimi K2.6**         | **4/10** |
| **Kimi K2.5**         | **3/10** |
| **Kimi K2 Turbo**     | **3/10** |
| **Deepseek 4 flash**  | **3/10** |
| **Deepseek 4**        | **3/10** |
| **Deepseek 3.2**      | **2/10** |
| **Мinimax m3**        | **4/10** |
| **Мinimax m2.7**      | **4/10** |
| **Мinimax m2.5**      | **4/10** |
| **Мinimax m2.1**      | **3/10** |
| **Мinimax m2**        | **3/10** |
| **Мinimax m1**        | **3/10** |
| **Qwen 3.8 Max**      | **8/10** |
| **Qwen 3.7 Max**      | **4/10** |
| **Qwen 3.6 Max**      | **4/10** |
| **Qwen 3.6**          | **3/10** |
| **Qwen 3.5 Max**      | **3/10** |
| **Qwen 3.5**          | **3/10** |
| **Qwen 3 Max**        | **2/10** |
| **Qwen 3.5 122b a10b**| **3/10** |
| **Qwen 3.5 35b a3b**  | **1/10** |
| **Qwen 3.6 27b**      | **3/10** |
| **MiMo 2.5**          | **3/10** |
| **MiMo 2**            | **2/10** |
| **LongCat 2**         | **3/10** |
| **Nemotron 3 ultra**  | **2/10** |
| **Trinity**           | **2/10** |
| **HY3**               | **3/10** |
| **Laguna S 2.1**      | **2/10** |
| **Muse Spark 1.1**    | **4/10** |
| **Muse Glimmer**      | **2/10** |
| **Inkling**           | **3/10** |
| **Mistral Large 3**   | **2/10** |
| **Mistral Medium 3.5**| **3/10** |

---

### 33 - SVG infographic
**Create a single-page static SVG infographic about Japan, 1200×1800, with no JavaScript, no external assets, and no raster images. Use a modern editorial style with an interesting soft background, subtle waves, cards, icons, gradients, labels, and a clean hierarchy. Layout: top title “Japan at a glance”; first row: a stylized map of Japan on the left with the four largest cities placed approximately correctly and labeled: Tokyo, Yokohama, Osaka, Nagoya; on the right, a short explanatory text about Japan. Under this row, add one full-width paragraph. Next row: text on the left and a bar chart on the right showing Japan’s nominal GDP in current US$ trillions for 2015–2024: 2015 4.44, 2016 5.00, 2017 4.93, 2018 5.04, 2019 5.12, 2020 5.05, 2021 5.04, 2022 4.26, 2023 4.21, 2024 4.03. Bottom row: a pie/donut chart on the left for population composition by nationality/ethnic grouping: Japanese 97.5%, Chinese 0.6%, Vietnamese 0.4%, South Korean 0.3%, Other 1.2%; on the right, text about what to visit in Japan: Tokyo, Kyoto, Osaka, Hiroshima/Miyajima, Mount Fuji/Hakone, and Hokkaido. Add legends, concise captions, and a small source note. Final output must be only one valid static SVG document.**

| Model                 | Score    |
| --------------------- | -------- |
| **Gemini 3.7 flash**  | **7/10** |
| **Gemini 3.6 flash**  | **5/10** |
| **Gemini 3.5 flash**  | **5/10** |
| **Gemini 3.1**        | **5/10** |
| **Gemini 3 flash**    | **4/10** |
| **Gemini 2.5**        | **3/10** |
| **Gemma 4 31B**       | **3/10** |
| **ChatGPT 5.6**       | **7/10** |
| **ChatGPT 5.5**       | **6/10** |
| **ChatGPT 5.4**       | **3/10** |
| **ChatGPT 5.3**       | **2/10** |
| **ChatGPT 5.2**       | **3/10** |
| **ChatGPT 5.1**       | **3/10** |
| **ChatGPT 5**         | **2/10** |
| **ChatGPT o3**        | **3/10** |
| **ChatGPT 4.1**       | **3/10** |
| **GPT-OSS-120b**      | **2/10** |
| **GPT-OSS-20b**       | **0/10** |
| **Grok 4.6**          | **5/10** |
| **Grok 4.5**          | **6/10** |
| **Grok 4.3**          | **4/10** |
| **Grok 4.2**          | **3/10** |
| **Grok 4.1**          | **3/10** |
| **Claude Fable 5**    | **8/10** |
| **Claude Opus 5**     | **9/10** |
| **Claude Opus 4.8**   | **6/10** |
| **Claude Opus 4.7**   | **5/10** |
| **Claude Opus 4.6**   | **4/10** |
| **Claude Opus 4.5**   | **0/10** |
| **Claude Opus 4.1**   | **0/10** |
| **Claude Opus 3**     | **2/10** |
| **Glm 5.2**           | **5/10** |
| **Glm 5.1**           | **4/10** |
| **Glm 5**             | **4/10** |
| **Glm 4.7**           | **3/10** |
| **Glm 4.6**           | **2/10** |
| **Kimi K3**           | **6/10** |
| **Kimi K2.7 code**    | **4/10** |
| **Kimi K2.6**         | **3/10** |
| **Kimi K2.5**         | **4/10** |
| **Kimi K2 Turbo**     | **0/10** |
| **Deepseek 4 flash**  | **3/10** |
| **Deepseek 4**        | **3/10** |
| **Deepseek 3.2**      | **2/10** |
| **Мinimax m3**        | **6/10** |
| **Мinimax m2.7**      | **4/10** |
| **Мinimax m2.5**      | **3/10** |
| **Мinimax m2.1**      | **3/10** |
| **Мinimax m2**        | **3/10** |
| **Мinimax m1**        | **4/10** |
| **Qwen 3.8 Max**      | **7/10** |
| **Qwen 3.7 Max**      | **4/10** |
| **Qwen 3.6 Max**      | **4/10** |
| **Qwen 3.6**          | **3/10** |
| **Qwen 3.5 Max**      | **2/10** |
| **Qwen 3.5**          | **3/10** |
| **Qwen 3 Max**        | **3/10** |
| **Qwen 3.5 122b a10b**| **2/10** |
| **Qwen 3.5 35b a3b**  | **2/10** |
| **Qwen 3.6 27b**      | **4/10** |
| **MiMo 2.5**          | **3/10** |
| **MiMo 2**            | **2/10** |
| **LongCat 2**         | **4/10** |
| **Nemotron 3 ultra**  | **4/10** |
| **Trinity**           | **2/10** |
| **HY3**               | **5/10** |
| **Laguna S 2.1**      | **2/10** |
| **Muse Spark 1.1**    | **4/10** |
| **Muse Glimmer**      | **2/10** |
| **Inkling**           | **2/10** |
| **Mistral Large 3**   | **3/10** |
| **Mistral Medium 3.5**| **2/10** |

---

### 34 - SVG learning interface
**Create a single-page static SVG drag-and-drop learning interface for flower anatomy, fully self-contained with no JavaScript, no external assets, and no images. The SVG must simulate interactivity using only structure, layers, visibility toggles, and anchor-based navigation. Design a 1800×1200 SVG styled like a modern textbook UI with soft background gradients, clean typography, and clear educational hierarchy. The screen shows a detailed vector illustration of a flower with arrows pointing to labeled target areas for parts such as petal, sepal, stamen, pistil, anther, filament, ovary, style, stigma, receptacle. Include at least 10 draggable-style label tiles (petal, sepal, stamen, pistil, anther, filament, ovary, style, stigma, receptacle) presented in a word bank as rounded SVG buttons. The layout must include a top title “Flower Anatomy Drag & Drop”, a central diagram area with the flower and empty label slots, a right-side instruction panel explaining the task, and a bottom or side word bank containing the labels. Simulated interactivity must include at least three buttons: Hint, Check Answer, Reset. Each button opens a hidden SVG popup panel implemented with <g> groups toggled via internal links or viewBox shifts. Each popup must have a close button. Add arrows connecting labels to flower parts, with clean infographic styling. Include a small extra educational inset diagram showing pollination or plant reproduction. The entire output must be a single valid SVG document only, fully static, visually rich, and structured to resemble a professional educational tool, with no JavaScript or external dependencies.**

| Model                 | Score    |
| --------------------- | -------- |
| **Gemini 3.7 flash**  | **1/10** |
| **Gemini 3.6 flash**  | **5/10** |
| **Gemini 3.5 flash**  | **3/10** |
| **Gemini 3.1**        | **4/10** |
| **Gemini 3 flash**    | **2/10** |
| **Gemini 2.5**        | **2/10** |
| **Gemma 4 31B**       | **3/10** |
| **ChatGPT 5.6**       | **7/10** |
| **ChatGPT 5.5**       | **5/10** |
| **ChatGPT 5.4**       | **4/10** |
| **ChatGPT 5.3**       | **2/10** |
| **ChatGPT 5.2**       | **2/10** |
| **ChatGPT 5.1**       | **2/10** |
| **ChatGPT 5**         | **3/10** |
| **ChatGPT o3**        | **2/10** |
| **ChatGPT 4.1**       | **1/10** |
| **GPT-OSS-120b**      | **1/10** |
| **GPT-OSS-20b**       | **0/10** |
| **Grok 4.6**          | **6/10** |
| **Grok 4.5**          | **6/10** |
| **Grok 4.3**          | **3/10** |
| **Grok 4.2**          | **4/10** |
| **Grok 4.1**          | **2/10** |
| **Claude Fable 5**    | **8/10** |
| **Claude Opus 5**     | **9/10** |
| **Claude Opus 4.8**   | **6/10** |
| **Claude Opus 4.7**   | **6/10** |
| **Claude Opus 4.6**   | **4/10** |
| **Claude Opus 4.5**   | **0/10** |
| **Claude Opus 4.1**   | **0/10** |
| **Claude Opus 3**     | **2/10** |
| **Glm 5.2**           | **5/10** |
| **Glm 5.1**           | **3/10** |
| **Glm 5**             | **4/10** |
| **Glm 4.7**           | **4/10** |
| **Glm 4.6**           | **1/10** |
| **Kimi K3**           | **7/10** |
| **Kimi K2.7 code**    | **5/10** |
| **Kimi K2.6**         | **4/10** |
| **Kimi K2.5**         | **2/10** |
| **Kimi K2 Turbo**     | **3/10** |
| **Deepseek 4 flash**  | **4/10** |
| **Deepseek 4**        | **4/10** |
| **Deepseek 3.2**      | **3/10** |
| **Мinimax m3**        | **4/10** |
| **Мinimax m2.7**      | **3/10** |
| **Мinimax m2.5**      | **2/10** |
| **Мinimax m2.1**      | **2/10** |
| **Мinimax m2**        | **2/10** |
| **Мinimax m1**        | **2/10** |
| **Qwen 3.8 Max**      | **9/10** |
| **Qwen 3.7 Max**      | **6/10** |
| **Qwen 3.6 Max**      | **4/10** |
| **Qwen 3.6**          | **3/10** |
| **Qwen 3.5 Max**      | **0/10** |
| **Qwen 3.5**          | **3/10** |
| **Qwen 3 Max**        | **2/10** |
| **Qwen 3.5 122b a10b**| **1/10** |
| **Qwen 3.5 35b a3b**  | **1/10** |
| **Qwen 3.6 27b**      | **4/10** |
| **MiMo 2.5**          | **5/10** |
| **MiMo 2**            | **2/10** |
| **LongCat 2**         | **2/10** |
| **Nemotron 3 ultra**  | **2/10** |
| **Trinity**           | **2/10** |
| **HY3**               | **4/10** |
| **Laguna S 2.1**      | **2/10** |
| **Muse Spark 1.1**    | **3/10** |
| **Muse Glimmer**      | **3/10** |
| **Inkling**           | **2/10** |
| **Mistral Large 3**   | **1/10** |
| **Mistral Medium 3.5**| **1/10** |

---

### 36 - Voxel world
**Create or improve a single self-contained HTML file that renders a cinematic Minecraft-inspired medieval fantasy voxel world using pure WebGPU, without external engines. Make it smooth and fully explorable with chunked voxel terrain, optimized hidden-face meshing, fly/walk camera controls, mouse and keyboard navigation, dramatic aerial starting view, cinematic orbit mode, and showcase screenshot mode. Design a handcrafted miniature diorama with a large castle on a terraced hill, moat, bridge, gates, walls, towers, battlements, chapel, royal keep, courtyard, flags, gardens, glowing windows, and torches. Add a dense medieval village by a wide curved river with 25–35 varied houses, curved streets, marketplace, blacksmith, tavern, chapel, farms, docks, boats, watermill, fences, wells, carts, barrels, lanterns, and a stone bridge to the castle road. Surround it with animated reflective water, waterfalls, reeds, varied forests, ruins, caves, cliffs, hills, hidden paths, snowy mountains, mist, lookout posts, watchtowers, and a dramatic volcano with basalt, glowing lava, smoke, ash, dead trees, red lighting, and ancient ruins. Improve the atmosphere with dawn/day/dusk/night buttons, warm sunlight, shadows, fog, atmospheric perspective, color variation, glowing lights, flickering fire, flowing water, moving flags, drifting clouds, birds, optional bloom, tone mapping, and vignette. The final scene should feel coherent, handcrafted, colorful but slightly realistic, impressive immediately on load, and fully explorable like a rich low-poly voxel fantasy map.**

| Model                 | Score    |
| --------------------- | -------- |
| **Gemini 3.7 flash**  | **7/10** |
| **Gemini 3.6 flash**  | **5/10** |
| **Gemini 3.5 flash**  | **1/10** |
| **Gemini 3.1**        | **1/10** |
| **Gemini 3 flash**    | **1/10** |
| **Gemini 2.5**        | **1/10** |
| **Gemma 4 31B**       | **1/10** |
| **ChatGPT 5.6**       | **6/10** |
| **ChatGPT 5.5**       | **5/10** |
| **ChatGPT 5.4**       | **1/10** |
| **ChatGPT 5.3**       | **2/10** |
| **ChatGPT 5.2**       | **1/10** |
| **ChatGPT 5.1**       | **2/10** |
| **ChatGPT 5**         | **1/10** |
| **ChatGPT o3**        | **1/10** |
| **ChatGPT 4.1**       | **1/10** |
| **GPT-OSS-120b**      | **1/10** |
| **GPT-OSS-20b**       | **0/10** |
| **Grok 4.6**          | **1/10** |
| **Grok 4.5**          | **3/10** |
| **Grok 4.3**          | **1/10** |
| **Grok 4.2**          | **1/10** |
| **Grok 4.1**          | **1/10** |
| **Claude Fable 5**    | **8/10** |
| **Claude Opus 5**     | **9/10** |
| **Claude Opus 4.8**   | **8/10** |
| **Claude Opus 4.7**   | **5/10** |
| **Claude Opus 4.6**   | **5/10** |
| **Claude Opus 4.5**   | **0/10** |
| **Claude Opus 4.1**   | **0/10** |
| **Claude Opus 3**     | **1/10** |
| **Glm 5.2**           | **1/10** |
| **Glm 5.1**           | **1/10** |
| **Glm 5**             | **1/10** |
| **Glm 4.7**           | **1/10** |
| **Glm 4.6**           | **1/10** |
| **Kimi K3**           | **0/10** |
| **Kimi K2.7 code**    | **1/10** |
| **Kimi K2.6**         | **1/10** |
| **Kimi K2.5**         | **1/10** |
| **Kimi K2 Turbo**     | **0/10** |
| **Deepseek 4 flash**  | **1/10** |
| **Deepseek 4**        | **1/10** |
| **Deepseek 3.2**      | **1/10** |
| **Мinimax m3**        | **2/10** |
| **Мinimax m2.7**      | **1/10** |
| **Мinimax m2.5**      | **1/10** |
| **Мinimax m2.1**      | **1/10** |
| **Мinimax m2**        | **1/10** |
| **Мinimax m1**        | **1/10** |
| **Qwen 3.8 Max**      | **1/10** |
| **Qwen 3.7 Max**      | **4/10** |
| **Qwen 3.6 Max**      | **1/10** |
| **Qwen 3.6**          | **1/10** |
| **Qwen 3.5 Max**      | **1/10** |
| **Qwen 3.5**          | **1/10** |
| **Qwen 3 Max**        | **1/10** |
| **Qwen 3.5 122b a10b**| **1/10** |
| **Qwen 3.5 35b a3b**  | **1/10** |
| **Qwen 3.6 27b**      | **1/10** |
| **MiMo 2.5**          | **1/10** |
| **MiMo 2**            | **1/10** |
| **LongCat 2**         | **1/10** |
| **Nemotron 3 ultra**  | **1/10** |
| **Trinity**           | **1/10** |
| **HY3**               | **1/10** |
| **Laguna S 2.1**      | **3/10** |
| **Muse Spark 1.1**    | **4/10** |
| **Muse Glimmer**      | **1/10** |
| **Inkling**           | **1/10** |
| **Mistral Large 3**   | **1/10** |
| **Mistral Medium 3.5**| **1/10** |

---

### 42 - VR alien planet
**Build an immersive WebXR experience where the player can freely explore a mysterious alien planet in VR. Include strange biomes, caves, ruins, wildlife, weather, glowing vegetation, artifacts, and physical interactions focused on exploration and discovery. Use no libraries, no fallback APIs, and implement the entire experience in a single HTML file.**

| Model                 | Score    |
| --------------------- | -------- |
| **Gemini 3.7 flash**  | **5/10** |
| **Gemini 3.6 flash**  | **3/10** |
| **Gemini 3.5 flash**  | **1/10** |
| **Gemini 3.1**        | **1/10** |
| **Gemini 3 flash**    | **2/10** |
| **Gemini 2.5**        | **1/10** |
| **Gemma 4 31B**       | **1/10** |
| **ChatGPT 5.6**       | **1/10** |
| **ChatGPT 5.5**       | **3/10** |
| **ChatGPT 5.4**       | **1/10** |
| **ChatGPT 5.3**       | **3/10** |
| **ChatGPT 5.2**       | **2/10** |
| **ChatGPT 5.1**       | **2/10** |
| **ChatGPT 5**         | **3/10** |
| **ChatGPT o3**        | **1/10** |
| **ChatGPT 4.1**       | **1/10** |
| **GPT-OSS-120b**      | **2/10** |
| **GPT-OSS-20b**       | **0/10** |
| **Grok 4.6**          | **3/10** |
| **Grok 4.5**          | **3/10** |
| **Grok 4.3**          | **1/10** |
| **Grok 4.2**          | **1/10** |
| **Grok 4.1**          | **1/10** |
| **Claude Fable 5**    | **4/10** |
| **Claude Opus 5**     | **6/10** |
| **Claude Opus 4.8**   | **4/10** |
| **Claude Opus 4.7**   | **1/10** |
| **Claude Opus 4.6**   | **1/10** |
| **Claude Opus 4.5**   | **0/10** |
| **Claude Opus 4.1**   | **0/10** |
| **Claude Opus 3**     | **1/10** |
| **Glm 5.2**           | **1/10** |
| **Glm 5.1**           | **1/10** |
| **Glm 5**             | **1/10** |
| **Glm 4.7**           | **1/10** |
| **Glm 4.6**           | **1/10** |
| **Kimi K3**           | **5/10** |
| **Kimi K2.7 code**    | **2/10** |
| **Kimi K2.6**         | **2/10** |
| **Kimi K2.5**         | **1/10** |
| **Kimi K2 Turbo**     | **0/10** |
| **Deepseek 4 flash**  | **1/10** |
| **Deepseek 4**        | **1/10** |
| **Deepseek 3.2**      | **2/10** |
| **Мinimax m3**        | **2/10** |
| **Мinimax m2.7**      | **1/10** |
| **Мinimax m2.5**      | **1/10** |
| **Мinimax m2.1**      | **1/10** |
| **Мinimax m2**        | **1/10** |
| **Мinimax m1**        | **1/10** |
| **Qwen 3.8 Max**      | **1/10** |
| **Qwen 3.7 Max**      | **1/10** |
| **Qwen 3.6 Max**      | **1/10** |
| **Qwen 3.6**          | **1/10** |
| **Qwen 3.5 Max**      | **0/10** |
| **Qwen 3.5**          | **1/10** |
| **Qwen 3 Max**        | **1/10** |
| **Qwen 3.5 122b a10b**| **1/10** |
| **Qwen 3.5 35b a3b**  | **1/10** |
| **Qwen 3.6 27b**      | **1/10** |
| **MiMo 2.5**          | **3/10** |
| **MiMo 2**            | **1/10** |
| **LongCat 2**         | **1/10** |
| **Nemotron 3 ultra**  | **1/10** |
| **Trinity**           | **2/10** |
| **HY3**               | **1/10** |
| **Laguna S 2.1**      | **1/10** |
| **Muse Spark 1.1**    | **1/10** |
| **Muse Glimmer**      | **1/10** |
| **Inkling**           | **1/10** |
| **Mistral Large 3**   | **1/10** |
| **Mistral Medium 3.5**| **1/10** |

---

### 43 - SVG Spacecraft Schematic
**Create a highly detailed technical spacecraft schematic as a single SVG, presented like a professional aerospace engineering blueprint. Show top, side, front, rear, and cutaway views of the same spacecraft, with consistent geometry and proportions across all views. Include labeled engines, propellant tanks, crew module, cockpit, airlocks, docking port, radiators, solar arrays, antennas, landing gear, cargo bay, avionics, and life-support systems. Add dimensions, callouts, section lines, scale markers, structural details, and a clear technical visual hierarchy.**

| Model                 | Score    |
| --------------------- | -------- |
| **Gemini 3.7 flash**  | **6/10** |
| **Gemini 3.6 flash**  | **6/10** |
| **Gemini 3.5 flash**  | **4/10** |
| **Gemini 3.1**        | **4/10** |
| **Gemini 3 flash**    | **2/10** |
| **Gemini 2.5**        | **5/10** |
| **Gemma 4 31B**       | **0/10** |
| **ChatGPT 5.6**       | **5/10** |
| **ChatGPT 5.5**       | **4/10** |
| **ChatGPT 5.4**       | **3/10** |
| **ChatGPT 5.3**       | **4/10** |
| **ChatGPT 5.2**       | **2/10** |
| **ChatGPT 5.1**       | **3/10** |
| **ChatGPT 5**         | **3/10** |
| **ChatGPT o3**        | **2/10** |
| **ChatGPT 4.1**       | **3/10** |
| **GPT-OSS-120b**      | **3/10** |
| **GPT-OSS-20b**       | **2/10** |
| **Grok 4.6**          | **6/10** |
| **Grok 4.5**          | **9/10** |
| **Grok 4.3**          | **3/10** |
| **Grok 4.2**          | **3/10** |
| **Grok 4.1**          | **0/10** |
| **Claude Fable 5**    | **8/10** |
| **Claude Opus 5**     | **0/10** |
| **Claude Opus 4.8**   | **0/10** |
| **Claude Opus 4.7**   | **0/10** |
| **Claude Opus 4.6**   | **0/10** |
| **Claude Opus 4.5**   | **0/10** |
| **Claude Opus 4.1**   | **0/10** |
| **Claude Opus 3**     | **0/10** |
| **Glm 5.2**           | **5/10** |
| **Glm 5.1**           | **0/10** |
| **Glm 5**             | **6/10** |
| **Glm 4.7**           | **5/10** |
| **Glm 4.6**           | **0/10** |
| **Kimi K3**           | **0/10** |
| **Kimi K2.7 code**    | **4/10** |
| **Kimi K2.6**         | **1/10** |
| **Kimi K2.5**         | **3/10** |
| **Kimi K2 Turbo**     | **0/10** |
| **Deepseek 4 flash**  | **4/10** |
| **Deepseek 4**        | **4/10** |
| **Deepseek 3.2**      | **0/10** |
| **Мinimax m3**        | **6/10** |
| **Мinimax m2.7**      | **3/10** |
| **Мinimax m2.5**      | **3/10** |
| **Мinimax m2.1**      | **3/10** |
| **Мinimax m2**        | **2/10** |
| **Мinimax m1**        | **1/10** |
| **Qwen 3.8 Max**      | **6/10** |
| **Qwen 3.7 Max**      | **2/10** |
| **Qwen 3.6 Max**      | **3/10** |
| **Qwen 3.6**          | **2/10** |
| **Qwen 3.5 Max**      | **0/10** |
| **Qwen 3.5**          | **0/10** |
| **Qwen 3 Max**        | **2/10** |
| **Qwen 3.5 122b a10b**| **2/10** |
| **Qwen 3.5 35b a3b**  | **2/10** |
| **Qwen 3.6 27b**      | **2/10** |
| **MiMo 2.5**          | **5/10** |
| **MiMo 2**            | **0/10** |
| **LongCat 2**         | **3/10** |
| **Nemotron 3 ultra**  | **1/10** |
| **Trinity**           | **1/10** |
| **HY3**               | **0/10** |
| **Laguna S 2.1**      | **2/10** |
| **Muse Spark 1.1**    | **6/10** |
| **Muse Glimmer**      | **2/10** |
| **Inkling**           | **3/10** |
| **Mistral Large 3**   | **2/10** |
| **Mistral Medium 3.5**| **3/10** |