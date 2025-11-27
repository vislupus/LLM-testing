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

### Windows 11 clone
**Make a clone of the Windows 11 desktop. Use the original wallpaper. On the desktop, there should be icons for MS Word, Paint, Calculator, Notepad, File Explorer and Chrome. Each program should work. Use working images. Put everything in a standalone HTML file**

| Model                 | Score    |
| --------------------- | -------- |
| [**Gemini 3**](https://vislupus.github.io/LLM-testing/Windows%2011%20clone/gemini_3.html)          | **4/10** |
| [**ChatGPT 5.1**](https://vislupus.github.io/LLM-testing/Windows%2011%20clone/chatgpt_5_1.html)       | **3/10** |
| [**Grok 4.1**](https://vislupus.github.io/LLM-testing/Windows%2011%20clone/grok_4_1.html)          | **3/10** |
| [**Claude Opus 4.5**](https://vislupus.github.io/LLM-testing/Windows%2011%20clone/claude_opus_4_5.html)   | **5/10** |

---

### Excel clone
**Create a functional clone of Microsoft Excel in a single standalone HTML file (no external dependencies except CSS/JS embedded or via CDN). The UI should resemble a modern spreadsheet app with a toolbar at the top, a formula bar, column headers (A, B, C, …), row numbers (1, 2, 3, …), and a scrollable grid of editable cells. Each cell must support entering values and formulas (starting with =), with basic formula support for arithmetic (+ - * /), cell references (e.g. =A1+B2), and simple functions like SUM, AVERAGE, MIN, MAX over ranges (e.g. =SUM(A1:A10)). While editing a formula in the formula bar, allow the user to click or drag-select cells/ranges so their addresses (e.g. A1, B2, A1:A10) are automatically inserted into the formula. Implement automatic recalculation of dependent cells whenever a referenced cell changes, and display the currently selected cell’s address and formula/value in the formula bar. Include basic features such as: selecting cells with mouse, dragging to select ranges, double-click to edit, keyboard navigation with arrow keys/Enter/Tab, resizing columns, and support for multiple sheets (with sheet tabs and the ability to add/rename/delete sheets). Add a minimal toolbar with actions like bold/italic text, background color for cells, clear contents, and a simple “Download as CSV” and “Upload CSV” for the active sheet. Make the design clean and responsive, visually inspired by Excel but without using any copyrighted assets, and ensure everything runs smoothly in the browser without a backend.**

| Model                 | Score    |
| --------------------- | -------- |
| [**Gemini 3**](https://vislupus.github.io/LLM-testing/Excel%20clone/gemini_3.html)          | **5/10** |
| [**ChatGPT 5.1**](https://vislupus.github.io/LLM-testing/Excel%20clone/chatgpt_5_1.html)       | **3/10** |
| **Grok 4.1**          | **0/10** |
| [**Claude Sonnet 4.5**](https://vislupus.github.io/LLM-testing/Excel%20clone/claude_sonnet_4_5.html) | **5/10** |

---

### Photoshop clone
**Create a clone of photoshop with all the basic tools. Include brushes, layers, edit history, filters, blending options, and more. Put everything in a standalone html file**

| Model                 | Score    |
| --------------------- | -------- |
| [**Gemini 3**](https://vislupus.github.io/LLM-testing/Photoshop%20clone/gemini_3.html)          | **7/10** |
| [**ChatGPT 5.1**](https://vislupus.github.io/LLM-testing/Photoshop%20clone/chatgpt_5_1.html)       | **4/10** |
| [**Grok 4.1**](https://vislupus.github.io/LLM-testing/Photoshop%20clone/grok_4_1.html)          | **2/10** |
| [**Claude Opus 4.5**](https://vislupus.github.io/LLM-testing/Photoshop%20clone/claude_opus_4_5.html)   | **8/10** |

---

### City simulation
**Make a 3D visual simulation of a growing city using WebGL or Three.js, showing buildings appearing, roads forming, traffic flow, and people/vehicles moving around. Include sliders to control city size (population/density), traffic intensity, and development speed, updating the simulation in real time. Put everything in a single standalone HTML file with all HTML, CSS, and JavaScript embedded (no external assets).**

| Model                 | Score    |
| --------------------- | -------- |
| **Gemini 3**          | **0/10** |
| **ChatGPT 5.1**       | **0/10** |
| **Grok 4.1**          | **0/10** |
| **Claude Opus 4.5**   | **0/10** |

---

### Space shooter game
**Create a space shooter game where players pilot a ship through asteroid fields, dodging debris and firing lasers at alien invaders. Make it visually stunning with particle explosions. Use publicly available assets. Put everything in a standalone html file.**

| Model                 | Score    |
| --------------------- | -------- |
| [**Gemini 3**](https://vislupus.github.io/LLM-testing/Space%20shooter%20game/gemini_3.html)          | **8/10** |
| [**ChatGPT 5.1**](https://vislupus.github.io/LLM-testing/Space%20shooter%20game/chatgpt_5_1.html)       | **6/10** |
| [**Grok 4.1**](https://vislupus.github.io/LLM-testing/Space%20shooter%20game/grok_4_1.html)          | **4/10** |
| [**Claude Opus 4.5**](https://vislupus.github.io/LLM-testing/Space%20shooter%20game/claude_opus_4_5.html)   | **3/10** |

---

### Tetris game
**Create a complete Tetris game inside one standalone HTML file with all code (HTML, CSS, JS) embedded and no external assets. Include all tetromino shapes, movement, rotation, line clearing, scoring, speed increase, and a restartable game-over screen. Use clean, simple, procedurally drawn graphics and smooth animations.**

| Model                 | Score    |
| --------------------- | -------- |
| **Gemini 3**          | **0/10** |
| **ChatGPT 5.1**       | **0/10** |
| **Grok 4.1**          | **0/10** |
| **Claude Opus 4.5**   | **0/10** |

---

### 3D scene
**High-poly 3D floating island diorama with a large medieval stone castle at the center. Around it: a cozy medieval village with wooden houses, tavern, market stalls, and a riverside mill. Steep rocky cliffs, lush grass, pine trees, turquoise river with wooden bridges, waterfalls, and a ruined watchtower at the edge. Vibrant stylized colors, soft lighting, handcrafted tabletop-miniature look. Use Babylon.js as a single standalone HTML file (all HTML/CSS/JS in one file; Babylon.js may be loaded from a CDN).**

| Model                 | Score    |
| --------------------- | -------- |
| **Gemini 3**          | **3/10** |
| **ChatGPT 5.1**       | **4/10** |
| **Grok 4.1**          | **3/10** |
| **Claude Opus 4.5**   | **5/10** |
| **Glm 4.6**           | **3/10** |

---

### 3D terrain scene
**Create a 3D terrain scene in **Babylon.js** as a single standalone HTML file (all HTML/CSS/JS in one file; Babylon.js may be loaded from a CDN). Use the provided images `Osogovo Height Map (Merged).png` as the height map and `Osogovo_map.jpg` as the diffuse texture to build a realistic 3D map, then place three visible marker points on several of the highest peaks, each with a text label that always faces the camera (billboard) so it is always readable. The terrain should act as the top surface (lid) of a box/pedestal. The walls should extend downward from the edges of the terrain, creating a diorama-style display case or terrain sample effect. The bottom of the box should be flat and closed. Make sure the whole scene is orbit-camera controlled, nicely lit, and fully working when the HTML file is opened in a browser.**

| Model                 | Score    |
| --------------------- | -------- |
| **Gemini 3**          | **5/10** |
| **ChatGPT 5.1**       | **8/10** |
| **Grok 4.1**          | **6/10** |
| **Claude Opus 4.5**   | **7/10** |

---

### Ray tracing simulation
**Develop a real-time ray tracing simulation featuring 2 metallic spheres suspended above a street scene. Use any publicly available 3D street view environment, and allow adjustable parameters such as reflectivity, roughness, and other material properties of the sphere. Put everything in a standalone html file.**

| Model                 | Score    |
| --------------------- | -------- |
| **Gemini 3**          | **0/10** |
| **ChatGPT 5.1**       | **0/10** |
| **Grok 4.1**          | **0/10** |
| **Claude Opus 4.5**   | **0/10** |

---

### create-DAW
**Create a DAW. Include multiple instruments and drums. Include a step grid and piano roll. Include tempo control, multiple tracks, effects (reverb, delay), volume sliders, and more. Put everything in a standalone html file**

| Model                 | Score    |
| --------------------- | -------- |
| **Gemini 3**          | **0/10** |
| **ChatGPT 5.1**       | **0/10** |
| **Grok 4.1**          | **0/10** |
| **Claude Sonnet 4.5** | **0/10** |

---

### Financial analysis report
**make a comprehensive financial analysis report on the attached data. Include interactive charts and/or graphs. Make it visually appealing. Use advanced algorithms to suggest price forecasts, providing rationale and confidence intervals. Put everything in a standalone html file.**

| Model                 | Score    |
| --------------------- | -------- |
| **Gemini 3**          | **0/10** |
| **ChatGPT 5.1**       | **0/10** |
| **Grok 4.1**          | **0/10** |
| **Claude Sonnet 4.5** | **0/10** |

---

### Builder like Figma
**Develop a drag-and-drop UI builder like Figma. Include snap-to-grid and alignment guides. Include many advanced settings. Include an export option to HTML.**

| Model                 | Score    |
| --------------------- | -------- |
| **Gemini 3**          | **0/10** |
| **ChatGPT 5.1**       | **0/10** |
| **Grok 4.1**          | **0/10** |
| **Claude Sonnet 4.5** | **0/10** |

---

### Three-body problem
**Create a p5.js simulation of a multi-body gravitational system centered on the Sun, Earth, and Jupiter, using realistic Newtonian gravity and ensuring all three bodies stay within the canvas while moving smoothly. Use a background value of 220, apply noStroke(), and render persistent orbital trails to clearly visualize the motion of each object over time. Add a spacecraft that starts on Earth, then departs to complete a clear loop around the Sun, and finally travels on a physically plausible trajectory to reach Jupiter. Configure the initial positions, velocities, and masses so that the planetary orbits are chaotic and non-stable (not like the real solar system), yet still remain bounded and visually coherent. The final simulation should behave as an interactive, visually engaging, physics-consistent environment where all bodies and the spacecraft move dynamically, without drifting off to infinity or collapsing into unnatural clusters. Put everything in a standalone html file.**

| Model                 | Score    |
| --------------------- | -------- |
| [**Gemini 3**](https://vislupus.github.io/LLM-testing/Three-body%20problem/gemini_3.html)          | **3/10** |
| [**ChatGPT 5.1**](https://vislupus.github.io/LLM-testing/Three-body%20problem/chatgpt_5_1.html)       | **6/10** |
| [**Grok 4.1**](https://vislupus.github.io/LLM-testing/Three-body%20problem/grok_4_1.html)          | **2/10** |
| [**Claude Sonnet 4.5**](https://vislupus.github.io/LLM-testing/Three-body%20problem/claude_sonnet_4_5.html) | **2/10** |

---

### Galaxy simulation
**Create a p5.js simulation of galaxy formation where all entities are rendered as simple circles with varying sizes and brightness, using 10 000 particles that gradually self-organize into a physically plausible galaxy. The background should use a base color of 220 and stay visually subtle so the particle dynamics are clearly visible. Use p5.Vector for all motion and forces, apply gravity between particles with merging and mass conservation, and use a Quadtree (or similar spatial partitioning) to keep the simulation performant. A collapsing protogalactic cloud should evolve into a roughly spiral-like galaxy, with particles representing stars orbiting a central region in a Keplerian-like way (inner orbits faster than outer ones), influenced by an invisible dark matter halo and a central massive core or black hole. Ensure smooth animation and clear motion trails so the evolution of the galaxy remains visually captivating and grounded in physics-based behavior despite the large particle count. Put everything in a standalone html file.**

| Model                 | Score    |
| --------------------- | -------- |
| **Gemini 3**          | **8/10** |
| **ChatGPT 5.1**       | **3/10** |
| **Grok 4.1**          | **0/10** |
| **Claude Sonnet 4.5** | **2/10** |

---

### 2D Diffusion-Limited Aggregation
**Create an animated 2D Diffusion-Limited Aggregation (DLA) simulation that starts with 100 particles and continuously spawns new ones as each particle becomes fixed. Particles appear around the cluster, move randomly with a slight inward bias, and stick upon touching the existing structure. The animation must show the particles’ motion in real time, and growth stops when the cluster reaches 50 pixels from the canvas edge. The canvas should update smoothly, using efficient rendering to avoid lag. Optionally, allow adjustable settings such as particle count, movement speed, and bias strength. Put everything in a standalone html file.**

| Model                 | Score    |
| --------------------- | -------- |
| **Gemini 3**          | **7/10** |
| **ChatGPT 5.1**       | **5/10** |
| **Grok 4.1**          | **0/10** |
| **Claude Sonnet 4.5** | **2/10** |
