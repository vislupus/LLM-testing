(async () => {
  // Намира вероятните VR/XR бутони
  const buttons = [...document.querySelectorAll('button')].filter(b => {
    const id = (b.id || '').toLowerCase();
    const text = (b.textContent || '').toLowerCase();

    return [
      'vrbtn',
      'enter',
      'entervr',
      'enterxr',
      'xrbtn',
      'vrbutton'
    ].includes(id) ||
    /enter\s*(immersive\s*)?(vr|xr)|start\s*(vr|xr)|immersive\s*vr/i.test(text);
  });

  // Намира status полето, ако има такова
  const status =
    document.getElementById('stat') ||
    document.getElementById('status') ||
    document.querySelector('[id*="status" i]') ||
    document.querySelector('[id*="stat" i]');

  console.log('🔎 VR buttons found:', buttons);

  if (!navigator.xr) {
    console.error('❌ navigator.xr не съществува');
    if (status) status.textContent = '❌ WebXR unavailable';
    return;
  }

  try {
    const ok = await navigator.xr.isSessionSupported('immersive-vr');

    console.log(
      ok
        ? '✅ immersive-vr AVAILABLE'
        : '❌ immersive-vr NOT AVAILABLE'
    );

    buttons.forEach(button => {
      button.disabled = !ok;

      if (ok) {
        button.removeAttribute('disabled');
        button.removeAttribute('aria-disabled');
        button.setAttribute('aria-disabled', 'false');
      }
    });

    if (status) {
      status.textContent = ok
        ? '✅ Headset detected — VR ready'
        : '❌ No immersive VR detected';
    }

    console.log(`VR buttons activated: ${ok ? buttons.length : 0}`);

  } catch (err) {
    console.error('❌ WebXR check failed:', err);

    if (status) {
      status.textContent = '❌ WebXR check failed: ' + err.message;
    }
  }
})();