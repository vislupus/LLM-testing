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
| **Gemini 3**          | **4/10** |
| **ChatGPT 5.2**       | **6/10** |
| **ChatGPT 5.1**       | **3/10** |
| **Grok 4.1**          | **3/10** |
| **Claude Opus 4.5**   | **5/10** |
| **Glm 4.7**           | **4/10** |
| **Glm 4.6**           | **3/10** |
| **Kimi K2.5**         | **5/10** |
| **Kimi K2 Turbo**     | **4/10** |
| **Deepseek 3.2**      | **5/10** |
| **Мinimax m2.1**      | **6/10** |
| **Мimo 2**            | **3/10** |

---

### Excel clone
**Create a functional clone of Microsoft Excel in a single standalone HTML file (no external dependencies except CSS/JS embedded or via CDN). The UI should resemble a modern spreadsheet app with a toolbar at the top, a formula bar, column headers (A, B, C, …), row numbers (1, 2, 3, …), and a scrollable grid of editable cells. Each cell must support entering values and formulas (starting with =), with basic formula support for arithmetic (+ - * /), cell references (e.g. =A1+B2), and simple functions like SUM, AVERAGE, MIN, MAX over ranges (e.g. =SUM(A1:A10)). While editing a formula in the formula bar, allow the user to click or drag-select cells/ranges so their addresses (e.g. A1, B2, A1:A10) are automatically inserted into the formula. Implement automatic recalculation of dependent cells whenever a referenced cell changes, and display the currently selected cell’s address and formula/value in the formula bar. Include basic features such as: selecting cells with mouse, dragging to select ranges, double-click to edit, keyboard navigation with arrow keys/Enter/Tab, resizing columns, and support for multiple sheets (with sheet tabs and the ability to add/rename/delete sheets). Add a minimal toolbar with actions like bold/italic text, background color for cells, clear contents, and a simple “Download as CSV” and “Upload CSV” for the active sheet. Make the design clean and responsive, visually inspired by Excel but without using any copyrighted assets, and ensure everything runs smoothly in the browser without a backend.**

| Model                 | Score    |
| --------------------- | -------- |
| **Gemini 3**          | **3/10** |
| **ChatGPT 5.2**       | **4/10** |
| **ChatGPT 5.1**       | **3/10** |
| **Grok 4.1**          | **1/10** |
| **Claude Opus 4.5**   | **2/10** |
| **Glm 4.7**           | **2/10** |
| **Glm 4.6**           | **2/10** |
| **Kimi K2.5**         | **2/10** |
| **Kimi K2 Turbo**     | **2/10** |
| **Deepseek 3.2**      | **3/10** |
| **Мinimax m2.1**      | **2/10** |
| **Мimo 2**            | **0/10** |

---

### Photoshop clone
**Create a clone of photoshop with all the basic tools. Include brushes, layers, edit history, filters, blending options, and more. Put everything in a standalone html file**

| Model                 | Score    |
| --------------------- | -------- |
| **Gemini 3**          | **7/10** |
| **ChatGPT 5.2**       | **8/10** |
| **ChatGPT 5.1**       | **4/10** |
| **Grok 4.1**          | **2/10** |
| **Claude Opus 4.5**   | **8/10** |
| **Glm 4.7**           | **3/10** |
| **Glm 4.6**           | **0/10** |
| **Kimi K2.5**         | **6/10** |
| **Kimi K2 Turbo**     | **0/10** |
| **Deepseek 3.2**      | **5/10** |
| **Мinimax m2.1**      | **1/10** |
| **Мimo 2**            | **0/10** |

---

### Climate‑change dashboard
**Create a single‑file HTML climate dashboard for Sofia that loads local data from the CSV file temperature_Sofia_2809794_1952-01-01 - 2021-11-28.csv (same folder as the HTML file) using JavaScript in the browser. Parse the columns DATE, TAVG, TMAX, and TMIN, convert them from tenths of degrees to °C, and compute aggregates such as yearly mean temperature, yearly extremes (max/min), monthly means, and counts of very hot days (e.g., TMAX ≥ 30°C) and very cold days (e.g., TMIN ≤ −10°C). Visualize these metrics with interactive charts (for example, line charts for annual and monthly means and a bar chart for hot/cold days) using an external library like Chart.js or D3 loaded from a CDN, and include simple summary statistics (overall mean, estimated warming trend). Provide UI controls in the same page to choose a year range (start/end year) and automatically update all charts and statistics when the range changes. All HTML, CSS, and JavaScript should be self-contained in one HTML file.**

| Model                 | Score    |
| --------------------- | -------- |
| **Gemini 3**          | **8/10** |
| **ChatGPT 5.2**       | **5/10** |
| **ChatGPT 5.1**       | **6/10** |
| **Grok 4.1**          | **2/10** |
| **Claude Opus 4.5**   | **9/10** |
| **Glm 4.7**           | **2/10** |
| **Glm 4.6**           | **0/10** |
| **Kimi K2.5**         | **2/10** |
| **Kimi K2 Turbo**     | **0/10** |
| **Deepseek 3.2**      | **6/10** |
| **Мinimax m2.1**      | **6/10** |
| **Мimo 2**            | **0/10** |

---

### UI Builder
**Develop a single-file, standalone HTML/JavaScript application for a drag-and-drop UI builder, similar to Figma, complete with advanced settings, drag-and-drop placement, snap-to-grid, canvas resizing, and alignment guides. The application must include a comprehensive library of UI components, such as Buttons, Inputs, Text Fields, Checkboxes, Dropdowns, Sliders, Steppers, and Progress Bars, alongside basic geometric shapes like rectangular, Circle, Triangle, and Line. Users must be able to resize any element directly on the canvas using drag handles and configure advanced visual settings, including border radius and box shadows, via a dedicated properties panel. The builder is required to support dynamic flowcharting, allowing users to connect two elements with adjustable lines that automatically maintain their attachment points when the elements are moved or resized. All components, shapes, styles, and defined connections must be cleanly exported into a single, runnable HTML file.**

| Model                 | Score    |
| --------------------- | -------- |
| **Gemini 3**          | **9/10** |
| **ChatGPT 5.2**       | **8/10** |
| **ChatGPT 5.1**       | **6/10** |
| **Grok 4.1**          | **1/10** |
| **Claude Opus 4.5**   | **7/10** |
| **Glm 4.7**           | **3/10** |
| **Glm 4.6**           | **0/10** |
| **Kimi K2.5**         | **4/10** |
| **Kimi K2 Turbo**     | **0/10** |
| **Deepseek 3.2**      | **4/10** |
| **Мinimax m2.1**      | **3/10** |
| **Мimo 2**            | **0/10** |

---

### Educational game
**Create a complete, self-contained educational board game implemented entirely in a single HTML file. The game should be original, engaging, and creatively designed for learning (any subject is acceptable — choose one you find inspiring). Use SVG.js to draw and animate all visual elements directly inside the HTML. Make the gameplay intuitive and fun, with clear objectives, interactive elements, and visually appealing components. Include all HTML, CSS, JavaScript, and SVG.js code in one file. Do not copy existing games; invent something unique, imaginative, and educational. Feel free to design the board layout, rules, characters, challenges, progression systems, or any additional creative mechanics that enhance learning. The final output should be a fully working one-file HTML board game using SVG.js.**

| Model                 | Score    |
| --------------------- | -------- |
| **Gemini 3**          | **4/10** |
| **ChatGPT 5.2**       | **3/10** |
| **ChatGPT 5.1**       | **5/10** |
| **Grok 4.1**          | **2/10** |
| **Claude Opus 4.5**   | **5/10** |
| **Glm 4.7**           | **1/10** |
| **Glm 4.6**           | **3/10** |
| **Kimi K2.5**         | **4/10** |
| **Kimi K2 Turbo**     | **0/10** |
| **Deepseek 3.2**      | **5/10** |
| **Мinimax m2.1**      | **1/10** |
| **Мimo 2**            | **0/10** |

---

### Maze game
**Create a complete interactive maze game for kindergarten children in a single HTML file using svg.js. The maze must be randomly generated at 20×20 size each time and always have a valid solution. The player controls a cute animated hero using the keyboard arrow keys, and the hero must not move through walls. Add friendly-looking monsters that move in the maze and defeat the hero if they reach him, causing the game to restart. The hero should leave a trail of small circles at regular time intervals while moving. The entire drawing and animation must be done with svg.js inside one HTML file. Include a button that shows the correct solution path of the current maze when pressed. The style should be colorful and child-friendly. Add clear comments in the code and keep everything fully contained in a single HTML file.**

| Model                 | Score    |
| --------------------- | -------- |
| **Gemini 3**          | **6/10** |
| **ChatGPT 5.2**       | **3/10** |
| **ChatGPT 5.1**       | **8/10** |
| **Grok 4.1**          | **2/10** |
| **Claude Opus 4.5**   | **3/10** |
| **Glm 4.7**           | **7/10** |
| **Glm 4.6**           | **3/10** |
| **Kimi K2.5**         | **1/10** |
| **Kimi K2 Turbo**     | **0/10** |
| **Deepseek 3.2**      | **10/10** |
| **Мinimax m2.1**      | **9/10** |
| **Мimo 2**            | **0/10** |

---

### Nonogram game
**Create a complete interactive nonogram (picross) puzzle game in a single HTML file using svg.js for all drawing. The puzzle grid must be 20×20 cells, with row and column clues shown at the top and left of the grid. Use svg.js to draw the grid, the clue numbers, and the filled or marked cells. Allow the player to left-click to fill a cell and right-click (or an alternative) to mark a cell with an X. Include logic to check whether the player’s solution matches the predefined 20×20 pattern and display a success message when the puzzle is solved correctly. All code (HTML, CSS, JavaScript) must be contained in one file and use only vanilla JavaScript plus svg.js. The visual style should be clean, readable, and suitable for an educational puzzle game.**

| Model                 | Score    |
| --------------------- | -------- |
| **Gemini 3**          | **5/10** |
| **ChatGPT 5.2**       | **2/10** |
| **ChatGPT 5.1**       | **4/10** |
| **Grok 4.1**          | **2/10** |
| **Claude Opus 4.5**   | **8/10** |
| **Glm 4.7**           | **3/10** |
| **Glm 4.6**           | **2/10** |
| **Kimi K2.5**         | **2/10** |
| **Kimi K2 Turbo**     | **0/10** |
| **Deepseek 3.2**      | **4/10** |
| **Мinimax m2.1**      | **6/10** |
| **Мimo 2**            | **0/10** |

---

### Space shooter game
**Create a space shooter game where players pilot a ship through asteroid fields, dodging debris and firing lasers at alien invaders. Make it visually stunning with particle explosions. Use publicly available assets. Put everything in a standalone html file.**

| Model                 | Score    |
| --------------------- | -------- |
| **Gemini 3**          | **8/10** |
| **ChatGPT 5.2**       | **4/10** |
| **ChatGPT 5.1**       | **6/10** |
| **Grok 4.1**          | **4/10** |
| **Claude Opus 4.5**   | **3/10** |
| **Glm 4.7**           | **6/10** |
| **Glm 4.6**           | **0/10** |
| **Kimi K2.5**         | **7/10** |
| **Kimi K2 Turbo**     | **0/10** |
| **Deepseek 3.2**      | **1/10** |
| **Мinimax m2.1**      | **7/10** |
| **Мimo 2**            | **0/10** |

---

### Tetris game
**Create a complete Tetris game inside one standalone HTML file with all code (HTML, CSS, JS) embedded and no external assets. Include all tetromino shapes, movement, rotation, line clearing, scoring, speed increase, and a restartable game-over screen. Use clean, simple, procedurally drawn graphics and smooth animations.**

| Model                 | Score    |
| --------------------- | -------- |
| **Gemini 3**          | **8/10** |
| **ChatGPT 5.2**       | **1/10** |
| **ChatGPT 5.1**       | **8/10** |
| **Grok 4.1**          | **4/10** |
| **Claude Opus 4.5**   | **10/10** |
| **Glm 4.7**           | **5/10** |
| **Glm 4.6**           | **0/10** |
| **Kimi K2.5**         | **6/10** |
| **Kimi K2 Turbo**     | **0/10** |
| **Deepseek 3.2**      | **10/10** |
| **Мinimax m2.1**      | **3/10** |
| **Мimo 2**            | **0/10** |

---

### Pirates island
**Create a single‑file 3D browser game prototype using Babylon.js where the player commands three pirate ships protecting a small tropical island in the middle of an ocean. The scene should include a stylized water plane, a small green island with a few simple props (like rocks or palms), and three friendly ships arranged around it; the camera is freely orbiting above the scene. Each friendly ship can be selected (keys 1–3), steered around the island, and upgraded between waves (e.g., increased cannon damage, fire rate, or movement speed). Enemy ships periodically spawn from the horizon and sail toward the island; friendly ships automatically or manually fire cannonballs at enemies, and if enemies reach the island they damage its health. Everything (HTML, CSS, JavaScript, Babylon.js setup, basic UI overlay for gold, wave, HP and upgrade buttons) should be contained in one .html file, ready to open directly in a browser.**

| Model                 | Score    |
| --------------------- | -------- |
| **Gemini 3**          | **7/10** |
| **ChatGPT 5.2**       | **4/10** |
| **ChatGPT 5.1**       | **7/10** |
| **Grok 4.1**          | **1/10** |
| **Claude Opus 4.5**   | **9/10** |
| **Glm 4.7**           | **1/10** |
| **Glm 4.6**           | **8/10** |
| **Kimi K2.5**         | **3/10** |
| **Kimi K2 Turbo**     | **0/10** |
| **Deepseek 3.2**      | **7/10** |
| **Мinimax m2.1**      | **1/10** |
| **Мimo 2**            | **0/10** |

---

### 3D castle scene
**High-poly 3D floating island diorama with a large medieval stone castle at the center. Around it: a cozy medieval village with wooden houses, tavern, market stalls, and a riverside mill. Steep rocky cliffs, lush grass, pine trees, turquoise river with wooden bridges, waterfalls, and a ruined watchtower at the edge. Vibrant stylized colors, soft lighting, handcrafted tabletop-miniature look. Use Babylon.js as a single standalone HTML file (all HTML/CSS/JS in one file; Babylon.js may be loaded from a CDN).**

| Model                 | Score    |
| --------------------- | -------- |
| **Gemini 3**          | **3/10** |
| **ChatGPT 5.2**       | **1/10** |
| **ChatGPT 5.1**       | **4/10** |
| **Grok 4.1**          | **3/10** |
| **Claude Opus 4.5**   | **5/10** |
| **Glm 4.7**           | **3/10** |
| **Glm 4.6**           | **3/10** |
| **Kimi K2.5**         | **4/10** |
| **Kimi K2 Turbo**     | **0/10** |
| **Deepseek 3.2**      | **5/10** |
| **Мinimax m2.1**      | **1/10** |
| **Мimo 2**            | **0/10** |

---

### 3D terrain scene
**Create a 3D terrain scene in **Babylon.js** as a single standalone HTML file (all HTML/CSS/JS in one file; Babylon.js may be loaded from a CDN). Use the provided images `Osogovo Height Map (Merged).png` as the height map and `Osogovo_map.jpg` as the diffuse texture to build a realistic 3D map, then place three visible marker points on several of the highest peaks, each with a text label that always faces the camera (billboard) so it is always readable. The terrain should act as the top surface (lid) of a box/pedestal. The walls should extend downward from the edges of the terrain, creating a diorama-style display case or terrain sample effect. The bottom of the box should be flat and closed. Make sure the whole scene is orbit-camera controlled, nicely lit, and fully working when the HTML file is opened in a browser.**

| Model                 | Score    |
| --------------------- | -------- |
| **Gemini 3**          | **5/10** |
| **ChatGPT 5.2**       | **4/10** |
| **ChatGPT 5.1**       | **8/10** |
| **Grok 4.1**          | **6/10** |
| **Claude Opus 4.5**   | **7/10** |
| **Glm 4.7**           | **1/10** |
| **Glm 4.6**           | **0/10** |
| **Kimi K2.5**         | **5/10** |
| **Kimi K2 Turbo**     | **0/10** |
| **Deepseek 3.2**      | **1/10** |
| **Мinimax m2.1**      | **1/10** |
| **Мimo 2**            | **0/10** |

---

### City simulation
**Make a 3D visual simulation of a growing city using **Babylon.js**, showing buildings appearing, roads forming, traffic flow, and people/vehicles moving around. Include sliders to control city size (population/density), traffic intensity, and development speed, updating the simulation in real time. Put everything in a single standalone HTML file with all HTML, CSS, and JavaScript embedded (no external assets).**

| Model                 | Score    |
| --------------------- | -------- |
| **Gemini 3**          | **6/10** |
| **ChatGPT 5.2**       | **3/10** |
| **ChatGPT 5.1**       | **6/10** |
| **Grok 4.1**          | **3/10** |
| **Claude Opus 4.5**   | **3/10** |
| **Glm 4.7**           | **1/10** |
| **Glm 4.6**           | **5/10** |
| **Kimi K2.5**         | **5/10** |
| **Kimi K2 Turbo**     | **0/10** |
| **Deepseek 3.2**      | **7/10** |
| **Мinimax m2.1**      | **1/10** |
| **Мimo 2**            | **0/10** |

---

### Space battle simulation
**A 3D space battle scene in **Babylon.js** as a single standalone HTML file (all HTML/CSS/JS in one file; Babylon.js may be loaded from a CDN). Between two opposing fleets, each with 10 ships. Every fleet has one larger flagship and nine smaller escort ships. The flagships are clearly bigger and more detailed, positioned at the center of each formation. Each ship has a visible health bar above it; when health reaches zero the ship explodes in a spectacular way, with bright fire, sparks, shockwaves and debris. If another ship is within roughly one ship‑width of the explosion, it also detonates in a chain reaction. Ships constantly move and maneuver in three‑dimensional space, turning and accelerating as they try to destroy the enemy fleet. One fleet fires bright blue glowing projectiles, the other fires bright red glowing projectiles, clearly distinguishing the two sides. Normal ships fire a single projectile every 3 seconds, while the two flagships fire two projectiles at once every 3 seconds. The scene should feel dynamic and cinematic, with trails behind projectiles, directional lighting from engine thrusters, and a starfield or nebula background. Make sure the whole scene is orbit-camera controlled, nicely lit, and fully working when the HTML file is opened in a browser.**

| Model                 | Score    |
| --------------------- | -------- |
| **Gemini 3**          | **9/10** |
| **ChatGPT 5.2**       | **1/10** |
| **ChatGPT 5.1**       | **7/10** |
| **Grok 4.1**          | **2/10** |
| **Claude Opus 4.5**   | **7/10** |
| **Glm 4.7**           | **1/10** |
| **Glm 4.6**           | **0/10** |
| **Kimi K2.5**         | **1/10** |
| **Kimi K2 Turbo**     | **0/10** |
| **Deepseek 3.2**      | **4/10** |
| **Мinimax m2.1**      | **1/10** |
| **Мimo 2**            | **0/10** |

---

### Ray tracing simulation
**Develop a real-time ray tracing simulation in **Babylon.js** as a single standalone HTML file, featuring 2 metallic spheres suspended above a street scene. Use any publicly available 3D street view environment, and allow adjustable parameters such as reflectivity, roughness, and other material properties of the sphere. Put everything in a standalone html file.**

| Model                 | Score    |
| --------------------- | -------- |
| **Gemini 3**          | **5/10** |
| **ChatGPT 5.2**       | **5/10** |
| **ChatGPT 5.1**       | **6/10** |
| **Grok 4.1**          | **1/10** |
| **Claude Opus 4.5**   | **8/10** |
| **Glm 4.7**           | **0/10** |
| **Glm 4.6**           | **0/10** |
| **Kimi K2.5**         | **0/10** |
| **Kimi K2 Turbo**     | **0/10** |
| **Deepseek 3.2**      | **1/10** |
| **Мinimax m2.1**      | **1/10** |
| **Мimo 2**            | **0/10** |

---

### Three-body problem
**Create a p5.js simulation of a multi-body gravitational system centered on the Sun, Earth, and Jupiter, using realistic Newtonian gravity and ensuring all three bodies stay within the canvas while moving smoothly. Use a background value of 220, apply noStroke(), and render persistent orbital trails to clearly visualize the motion of each object over time. Add a spacecraft that starts on Earth, then departs to complete a clear loop around the Sun, and finally travels on a physically plausible trajectory to reach Jupiter. Configure the initial positions, velocities, and masses so that the planetary orbits are chaotic and non-stable (not like the real solar system), yet still remain bounded and visually coherent. The final simulation should behave as an interactive, visually engaging, physics-consistent environment where all bodies and the spacecraft move dynamically, without drifting off to infinity or collapsing into unnatural clusters. Put everything in a standalone html file.**

| Model                 | Score    |
| --------------------- | -------- |
| **Gemini 3**          | **3/10** |
| **ChatGPT 5.2**       | **4/10** |
| **ChatGPT 5.1**       | **6/10** |
| **Grok 4.1**          | **2/10** |
| **Claude Opus 4.5**   | **7/10** |
| **Glm 4.7**           | **0/10** |
| **Glm 4.6**           | **4/10** |
| **Kimi K2.5**         | **0/10** |
| **Kimi K2 Turbo**     | **3/10** |
| **Deepseek 3.2**      | **1/10** |
| **Мinimax m2.1**      | **5/10** |
| **Мimo 2**            | **0/10** |

---

### Galaxy simulation
**Create a p5.js simulation of galaxy formation where all entities are rendered as simple circles with varying sizes and brightness, using 10 000 particles that gradually self-organize into a physically plausible galaxy. The background should use a base color of 220 and stay visually subtle so the particle dynamics are clearly visible. Use p5.Vector for all motion and forces, apply gravity between particles with merging and mass conservation, and use a Quadtree (or similar spatial partitioning) to keep the simulation performant. A collapsing protogalactic cloud should evolve into a roughly spiral-like galaxy, with particles representing stars orbiting a central region in a Keplerian-like way (inner orbits faster than outer ones), influenced by an invisible dark matter halo and a central massive core or black hole. Ensure smooth animation and clear motion trails so the evolution of the galaxy remains visually captivating and grounded in physics-based behavior despite the large particle count. Put everything in a standalone html file.**

| Model                 | Score    |
| --------------------- | -------- |
| **Gemini 3**          | **8/10** |
| **ChatGPT 5.2**       | **2/10** |
| **ChatGPT 5.1**       | **3/10** |
| **Grok 4.1**          | **1/10** |
| **Claude Opus 4.5**   | **4/10** |
| **Glm 4.7**           | **0/10** |
| **Glm 4.6**           | **2/10** |
| **Kimi K2.5**         | **0/10** |
| **Kimi K2 Turbo**     | **1/10** |
| **Deepseek 3.2**      | **3/10** |
| **Мinimax m2.1**      | **2/10** |
| **Мimo 2**            | **0/10** |

---

### 2D Diffusion-Limited Aggregation
**Create an animated 2D Diffusion-Limited Aggregation (DLA) simulation that starts with 100 particles and continuously spawns new ones as each particle becomes fixed. Particles appear around the cluster, move randomly with a slight inward bias, and stick upon touching the existing structure. The animation must show the particles’ motion in real time, and growth stops when the cluster reaches 50 pixels from the canvas edge. The canvas should update smoothly, using efficient rendering to avoid lag. Optionally, allow adjustable settings such as particle count, movement speed, and bias strength. Put everything in a standalone html file.**

| Model                 | Score    |
| --------------------- | -------- |
| **Gemini 3**          | **7/10** |
| **ChatGPT 5.2**       | **0/10** |
| **ChatGPT 5.1**       | **5/10** |
| **Grok 4.1**          | **3/10** |
| **Claude Opus 4.5**   | **10/10** |
| **Glm 4.7**           | **0/10** |
| **Glm 4.6**           | **4/10** |
| **Kimi K2.5**         | **0/10** |
| **Kimi K2 Turbo**     | **3/10** |
| **Deepseek 3.2**      | **0/10** |
| **Мinimax m2.1**      | **0/10** |
| **Мimo 2**            | **0/10** |

---

### 2D Fluid simulation
**Create a 2D fluid simulation in p5.js with realistic fluid dynamics that mimic real‑world liquid motion, including swirling, spreading, and natural‑looking patterns over time. The simulation should support either particle‑based or grid‑based methods (e.g., Navier–Stokes or SPH), with varying density and velocity, plus smooth color diffusion so differently colored fluids mix visually. Allow interactive control: the mouse can inject velocity or disturb the fluid, while keys can add different colors, forces, adjust viscosity, reset the scene, or toggle vortex behavior. Render the fluid in a visually appealing, smooth way using efficient techniques so it remains responsive even with many particles or a high‑resolution grid, and optionally include obstacles and real‑time shader effects to enhance realism. Put everything in a standalone html file.**

| Model                 | Score    |
| --------------------- | -------- |
| **Gemini 3**          | **4/10** |
| **ChatGPT 5.2**       | **0/10** |
| **ChatGPT 5.1**       | **1/10** |
| **Grok 4.1**          | **1/10** |
| **Claude Opus 4.5**   | **4/10** |
| **Glm 4.7**           | **0/10** |
| **Glm 4.6**           | **6/10** |
| **Kimi K2.5**         | **0/10** |
| **Kimi K2 Turbo**     | **1/10** |
| **Deepseek 3.2**      | **0/10** |
| **Мinimax m2.1**      | **0/10** |
| **Мimo 2**            | **0/10** |

---

### 2D Heat‑diffusion simulation
**Create a 2D heat‑diffusion simulation in p5.js that numerically solves the heat equation ∂T/∂t = α∇²T on a grid using finite‑difference methods (explicit or implicit), so temperature diffuses smoothly over time and can vary by material with different thermal conductivities. Represent temperature as a grid‑based field visualized with a heatmap gradient (blue = cold, red = hot), where heat naturally spreads and fades into realistic thermal patterns under configurable boundary conditions such as insulated edges or constant‑temperature borders. Let the user add heat sources by clicking, cool regions via keyboard input, and adjust parameters like conductivity, diffusion speed, resolution, and optionally convection strength. Ensure the update loop is efficient enough for real‑time interaction, and optionally support multiple heat sources, material presets, and GPU‑accelerated shaders to keep the simulation smooth at higher resolutions. Put everything in a standalone html file.**

| Model                 | Score    |
| --------------------- | -------- |
| **Gemini 3**          | **4/10** |
| **ChatGPT 5.2**       | **0/10** |
| **ChatGPT 5.1**       | **5/10** |
| **Grok 4.1**          | **4/10** |
| **Claude Opus 4.5**   | **9/10** |
| **Glm 4.7**           | **0/10** |
| **Glm 4.6**           | **2/10** |
| **Kimi K2.5**         | **0/10** |
| **Kimi K2 Turbo**     | **0/10** |
| **Deepseek 3.2**      | **0/10** |
| **Мinimax m2.1**      | **0/10** |
| **Мimo 2**            | **0/10** |

---

### 2D Fluid‑flow animation
**Create a computer‑generated 2D fluid‑flow animation in p5.js that simulates fluid moving through a tube past an obstacle and clearly shows the formation of a von Kármán vortex street (alternating vortices shed behind the object). Represent the fluid on a grid or with particles and solve a simple Navier–Stokes–style or lattice‑Boltzmann approximation so the flow bends around the shape and vortices naturally appear in its wake. The obstacle should not be fixed: allow the user to move it with the mouse, change its size and shape (e.g., from circle to ellipse/rectangle), and rotate it freely through 360 degrees, with the flow and vortex pattern updating in real time as the object moves. Use color or velocity vectors to visualize the flow field and vorticity, while keeping the simulation efficient enough for smooth, interactive frame rates in the browser. Put everything in a standalone html file.**

| Model                 | Score    |
| --------------------- | -------- |
| **Gemini 3**          | **7/10** |
| **ChatGPT 5.2**       | **0/10** |
| **ChatGPT 5.1**       | **4/10** |
| **Grok 4.1**          | **1/10** |
| **Claude Opus 4.5**   | **8/10** |
| **Glm 4.7**           | **0/10** |
| **Glm 4.6**           | **4/10** |
| **Kimi K2.5**         | **0/10** |
| **Kimi K2 Turbo**     | **0/10** |
| **Deepseek 3.2**      | **0/10** |
| **Мinimax m2.1**      | **0/10** |
| **Мimo 2**            | **0/10** |

---

### 2D Monte Carlo simulation
**Create a 2D Monte Carlo simulation in p5.js that models the evolution of an ecosystem on a grid, where each cell can contain different entities such as plants, herbivores, and predators. Use probabilistic rules for birth, death, movement, feeding, and mutation: at each time step, randomly select individuals and stochastically decide their actions based on parameters like energy, local population density, and resource availability. Allow traits (speed, vision range, reproduction rate, etc.) to mutate slightly during reproduction so that species can evolve over many generations, and visualize these traits with color or size variations. Let the user adjust parameters such as mutation rate, carrying capacity, initial populations, and interaction strengths via sliders or keys, and display simple statistics (population curves, average traits) alongside the main view. Keep the update loop efficient so large grids and many agents can run in real time, illustrating emergent patterns like extinction events, predator–prey cycles, and adaptation. Put everything in a standalone html file.**

| Model                 | Score    |
| --------------------- | -------- |
| **Gemini 3**          | **7/10** |
| **ChatGPT 5.2**       | **6/10** |
| **ChatGPT 5.1**       | **5/10** |
| **Grok 4.1**          | **2/10** |
| **Claude Opus 4.5**   | **9/10** |
| **Glm 4.7**           | **0/10** |
| **Glm 4.6**           | **8/10** |
| **Kimi K2.5**         | **0/10** |
| **Kimi K2 Turbo**     | **1/10** |
| **Deepseek 3.2**      | **0/10** |
| **Мinimax m2.1**      | **0/10** |
| **Мimo 2**            | **0/10** |

---

### Tesseract animation
**Create an interactive 4D tesseract animation in p5.js: render a wireframe projection of a rotating tesseract onto 2D, using a 4D → 3D → 2D projection pipeline (homogeneous coordinates or rotation matrices in 4D space). Animate continuous rotation around multiple 4D axes so the shape constantly morphs between cube‑within‑cube and other characteristic projections, with smooth interpolation and adjustable rotation speed. Let the user control parameters via mouse/keyboard: pause/resume rotation, change which 4D planes are rotating, adjust projection distance, and toggle between orthographic and perspective‑style projection. Use clean lines, subtle shading, and optional color gradients to distinguish inner and outer edges, keeping the frame rate high for a fluid, educational visualization of a tesseract. Put everything in a standalone html file.**

| Model                 | Score    |
| --------------------- | -------- |
| **Gemini 3**          | **7/10** |
| **ChatGPT 5.2**       | **3/10** |
| **ChatGPT 5.1**       | **4/10** |
| **Grok 4.1**          | **1/10** |
| **Claude Opus 4.5**   | **9/10** |
| **Glm 4.7**           | **0/10** |
| **Glm 4.6**           | **8/10** |
| **Kimi K2.5**         | **0/10** |
| **Kimi K2 Turbo**     | **4/10** |
| **Deepseek 3.2**      | **0/10** |
| **Мinimax m2.1**      | **0/10** |
| **Мimo 2**            | **0/10** |

---

### Equal Earth projection
**Create a single‑file interactive world map using SVG.js that renders the Earth in the Equal Earth projection and supports full coordinate ↔ screen conversion. The app should draw a clean vector world map in Equal Earth, with zoom and pan (mouse wheel + drag) that keep the projection mathematically correct at any scale. Implement forward projection: given geographic coordinates (latitude, longitude in degrees), convert them to projected x,y in the Equal Earth projection and plot a small SVG circle/marker at the correct location on the map. Implement inverse projection as well: when the user clicks on any point of the map (taking into account current zoom and pan), compute the corresponding latitude and longitude for that position and display them in a small overlay or console readout. All logic (HTML, CSS, JavaScript, SVG.js setup, projection formulas, zoom/pan handling, marker drawing and coordinate display) must be contained in a single self‑contained HTML file that runs directly in the browser.**

| Model                 | Score    |
| --------------------- | -------- |
| **Gemini 3**          | **3/10** |
| **ChatGPT 5.2**       | **3/10** |
| **ChatGPT 5.1**       | **2/10** |
| **Grok 4.1**          | **1/10** |
| **Claude Opus 4.5**   | **5/10** |
| **Glm 4.7**           | **0/10** |
| **Glm 4.6**           | **2/10** |
| **Kimi K2.5**         | **0/10** |
| **Kimi K2 Turbo**     | **2/10** |
| **Deepseek 3.2**      | **0/10** |
| **Мinimax m2.1**      | **0/10** |
| **Мimo 2**            | **0/10** |

---

### 2D Gas simulation
**Create a single‑file 2D gas simulation in p5.js that illustrates ideas from statistical mechanics as accurately as possible while still running in real time. Represent gas molecules as many small disks moving in a rectangular box with perfectly elastic collisions between particles and with the walls; conserve momentum and kinetic energy in each collision, and support adjustable particle mass and radius. Allow the user to change key parameters via on‑screen controls or keyboard: number of particles, initial temperature (speed distribution), box size, particle mass ratio (for mixture of species), and whether collisions are enabled/disabled. Continuously compute and display macroscopic quantities derived from the microscopic motion – e.g., kinetic‑energy‑based temperature, pressure on the walls (force per unit length or area), and simple histograms of speed distribution approaching a Maxwell–Boltzmann‑like curve. Everything (HTML, CSS, JavaScript, p5.js setup, UI, physics update and visualization) must be contained in a single self‑contained file that can be opened directly in the browser.**

| Model                 | Score    |
| --------------------- | -------- |
| **Gemini 3**          | **6/10** |
| **ChatGPT 5.2**       | **3/10** |
| **ChatGPT 5.1**       | **4/10** |
| **Grok 4.1**          | **1/10** |
| **Claude Opus 4.5**   | **8/10** |
| **Glm 4.7**           | **0/10** |
| **Glm 4.6**           | **5/10** |
| **Kimi K2.5**         | **0/10** |
| **Kimi K2 Turbo**     | **1/10** |
| **Deepseek 3.2**      | **0/10** |
| **Мinimax m2.1**      | **0/10** |
| **Мimo 2**            | **0/10** |

---

### Strandbeest legs
**Create a single‑file 3D demo in Babylon.js that uses a genetic algorithm to evolve walking Strandbeest‑style leg mechanisms. Represent each creature as a simple body with two or more multi‑segment legs in a plane, where each leg is defined by a genome encoding joint lengths, pivot positions, and possibly phase offsets for the leg cycle; decode the genome into a Babylon.js rig made of boxes/cylinders connected by rotating joints. Simulate a walking cycle on a flat ground plane using basic forward kinematics and simple physics or kinematic constraints, then evaluate each individual’s fitness by how far its body moves forward in a fixed time while remaining stable. Implement a full GA loop in JavaScript (selection, crossover, mutation, generation stepping), with controls to start/pause evolution, adjust population size, mutation rate, and cycle duration, and the option to highlight or replay the current best individual in the Babylon.js scene. All HTML, CSS, JavaScript, Babylon.js setup, GA logic, and visualization should live in one standalone .html file that runs directly in the browser.**

| Model                 | Score    |
| --------------------- | -------- |
| **Gemini 3**          | **4/10** |
| **ChatGPT 5.2**       | **4/10** |
| **ChatGPT 5.1**       | **3/10** |
| **Grok 4.1**          | **4/10** |
| **Claude Opus 4.5**   | **7/10** |
| **Glm 4.7**           | **0/10** |
| **Glm 4.6**           | **1/10** |
| **Kimi K2.5**         | **0/10** |
| **Kimi K2 Turbo**     | **2/10** |
| **Deepseek 3.2**      | **0/10** |
| **Мinimax m2.1**      | **0/10** |
| **Мimo 2**            | **0/10** |



- [ ] Notion-like app в един HTML файл с drag-and-drop блокове.
Create a single-file, offline, Notion-like app entirely in one HTML file with all CSS and JavaScript embedded. The app should use modern, clean design with a centered content column and light/dark mode. It must support editable content blocks similar to Notion, with headings, text, checklists, lists, quotes, dividers, and code blocks. Users should be able to type "/" to open a small command menu for choosing block types and press Enter to create new blocks. Implement smooth drag-and-drop for reordering blocks with a visible drop indicator. Add keyboard shortcuts like Ctrl+B/I/U for formatting and simple markdown triggers like "# " or "- ". All data should automatically save and load from localStorage. Include a top bar with a title and a "clear workspace" button. The entire interface should feel polished, fluid, and “cool,” with subtle animations for editing and dragging.

- [ ] Kanban board с drag-and-drop, цветове, тагове, търсене и offline съхранение.
- [ ] Vector graphics editor с bezier curves, слоеве и експортиране в SVG.
- [ ] 3D UI dashboard на Babylon.js с стил “glassmorphism”.
- [ ] Music sequencer + piano roll в един HTML файл.
- [ ] Code diff/merge tool с синтактично оцветяване и “intelligent merge”.
- [ ] 3D Pac-Man clone в Babylon.js с AI призраци.
- [ ] Age of Empires-микро RTS прототип (единици събират ресурси, строят, атакуват).
- [ ] Tower defense игра с procedural map generation.
- [ ] Physics-based Angry Birds clone (cannon, gravity, destruction).
- [ ] Ray-casting 2.5D Wolfenstein engine в canvas.
- [ ] Chess engine + UI с реално търсене (minimax).
- [ ] Turn-based RPG battle system с ефекти, анимации и инвентар.
- [ ] Asteroids + gravity wells + black holes за по-странна динамика.
- [ ] Fluid simulation с WebGL shaders (един HTML файл).
- [ ] 3D N-body simulation с GPU ускорение чрез Babylon.js shaders.
- [ ] Automaton ecosystem (Conway + expanding rules).
- [ ] Procedural terrain erosion (thermal + hydraulic).
- [ ] 3D solar system с орбити, наклони и оси на въртене.
- [ ] Traffic simulation (lights, queues, collisions).
- [ ] Boids + predator-prey model с параметри.
Create a single self-contained HTML file (no external JS/CSS) that shows a Boids + Predator–Prey simulation on an HTML5 canvas using only vanilla JavaScript. Include classic boid rules (separation, alignment, cohesion) plus fleeing from predators. Add predators that chase and eat boids using a catch radius. Include optional reproduction and starvation rules for both boids and predators. Make the simulation run with requestAnimationFrame and use simple shapes (triangles or circles). Add a small UI panel with sliders/inputs for boid parameters, predator parameters, and global controls like pause, speed, and reset. Keep the code clean, commented, and efficient enough for ~200 boids. Implement edge wrapping or bouncing. Ensure everything (HTML, CSS, JS) is inside one file and ready to save.


- [ ] Genetic algorithm for car hill-climbing (NEAT-style).
- [ ] Weather simulation (cloud convection, rain particles).
- [ ] Wave simulation using 2D PDE solver.
- [ ] Heat + fluid coupled simulation (buoyancy-driven flows).
- [ ] 3D L-system plant growth simulation.
- [ ] SQL engine emulator във браузъра – мини SQLite clone.
- [ ] Audio FFT visualizer с filers и spectrogram.
- [ ] Mini machine-learning notebook, подобно на Google Colab, но в HTML.
- [ ] Vector tile renderer за OpenStreetMap данни (без външен backend).
- [ ] Full offline-first knowledge base app
Create a single-page, offline-first knowledge base app in a single HTML file using IndexedDB for storage. Users must be able to create, edit, tag, and search notes, with full-text search implemented manually (no external search libraries). Implement bidirectional cross-links between notes (wiki-style), tag filtering, and a graph view of notes using canvas or SVG. Include automatic incremental backup to localStorage and an import/export to a single JSON file that preserves all links and metadata.
- [ ] Local-only password manager
Build a single-file HTML/JS password manager that stores all data encrypted in localStorage using AES-GCM. Include master password, password strength meter, per-entry notes, tags, and search. Implement proper key-derivation (PBKDF2 or similar) in JS, and never store the master password or derived key directly. Users must be able to export/import an encrypted backup file. Include a security explanation overlay describing how it works.
- [ ] Visual regular expression debugger
Create a standalone HTML/JS tool that lets users enter a regex and a test string, then visually highlights all matches and capture groups. Support live updating, flags (g, i, m, s, u), explanations of the pattern (basic parsing of tokens), and step-by-step simulation of the matching engine (NFA/DFA-like visualization on a canvas).
- [ ] Spreadsheet + SQL hybrid
Implement a single-file web app that combines a spreadsheet grid (like a basic Excel clone) with a SQL-like query pane. Users can type SQL-like queries over the sheet data (e.g., SELECT ColA, SUM(ColB) GROUP BY ColA) and see results in a separate grid. Implement a mini SQL parser and execution engine in JS (support SELECT, WHERE, GROUP BY, ORDER BY, basic aggregations). No external SQL engines.
- [ ] Multi-file project code editor with tabs and dependencies
Create a browser-based code editor (HTML/JS/CSS) that supports multiple “virtual files” (tabs), where files can import each other using ES module style imports. Implement a "run project" button that bundles the files on the fly (simple dependency resolver) and executes them in an iframe sandbox. Include syntax highlighting for JS and a console panel that captures console.log from the sandbox.
- [ ] Interactive REST API designer + mock server
Build a single-page app that allows users to define REST endpoints (methods, paths, sample responses). The app should generate a live mock API server in the browser using Service Workers: calls to configured routes should return the defined sample data. Include autogenerated API docs, an interactive test console (like mini Postman), and import/export of the whole API spec as JSON.
- [ ] WebAssembly playground (no server)
Develop a single-file HTML app that lets the user type a tiny subset of C-like code, compiles it to WebAssembly (by translating to a pseudo-bytecode you define) and executes it in the browser. Implement your own minimal “compiler” in JS (parser, bytecode generator, interpreter or WASM module generator). Show memory state and variables while stepping through execution.
- [ ] 2D vector drawing tool with boolean operations
Using SVG.js, implement a vector editor with rectangles, circles, polygons, and freehand paths. Add boolean operations between shapes (union, subtract, intersect, xor) using your own polygon clipping implementation or a minimal algorithm (no external clipping libraries). Allow exporting the final drawing to a single SVG file.
- [ ] 3D CAD-like parametric modeling tool
Create a mini CAD system in Babylon.js where users can define parametric primitives (boxes, cylinders, extruded profiles) via numeric parameters, combine them with boolean operations (union, subtract, intersect), and generate a final mesh. Provide a tree view of operations and update the model in real time when parameters change.
- [ ] Realistic day-night lighting and sky in Babylon.js
Create a single-file Babylon.js demo that simulates a full day-night cycle: moving sun, changing sky color, stars at night, and dynamic lighting/shadows on a small terrain with trees/houses. Include a time slider and “real-time” speed control. Use physically-inspired light intensities and smooth transitions.
- [ ] Node-based 2D shader editor (canvas-based)
Create a node editor (similar to Unreal’s material editor) which compiles the node graph into a fragment shader implemented in JS over a canvas (manual shader emulation per pixel, no WebGL). Support nodes: color, noise, transform, blend, time, etc. The user edits the graph and sees the result in real time.
- [ ] Procedural city mesh generator
In a single Babylon.js HTML file, procedurally generate an entire low-poly city: building footprints, heights, simple street layout, parks. Provide sliders for density, average height, and randomness. Allow regenerating the city and flying around with a free camera.
- [ ] Full 2D Navier–Stokes solver (grid-based) in p5.js
Implement a 2D fluid simulation using a stable fluids Navier–Stokes solver (pressure projection, incompressibility, advection, diffusion) with adjustable viscosity and timestep. Visualize both velocity (vector field) and dye concentration. Provide UI controls for injecting fluid, changing parameters, and toggling visualizations.
- [ ] Multi-species reaction–diffusion system
Create a single-file p5.js simulation of a 2D Gray–Scott-like reaction-diffusion model, but supporting three interacting chemicals with configurable reaction matrices. Let users change parameters in real time and see pattern transitions. Display phase diagrams or parameter presets that result in known pattern types (spots, stripes, chaos).
- [ ] 3D N-body gravity + relativistic correction
Implement a 3D N-body gravitational simulation with Barnes–Hut tree optimization in JavaScript (visualized in Babylon.js or p5.js). Add a simple relativistic correction (e.g. precession-like perturbation). Let users spawn bodies, change masses and initial velocities, and toggle different integrators (Euler, Verlet, RK4).
- [ ] Multi-layer neural network from scratch with training visualization
Create a neural network playground in a single HTML file without using any ML libraries. Implement forward and backward propagation for fully connected layers, training via gradient descent, on a 2D classification toy dataset. Visualize decision boundaries, loss over time, and neuron activations across layers.
- [ ] Symbolic algebra mini-CAS in JS
Implement a tiny computer algebra system in one HTML file: parse and manipulate algebraic expressions (polynomials, simple rational functions). Support simplification, expansion, factoring of polynomials, derivative, and maybe integration for simple forms. Provide a text input and show step-by-step transformations.
- [ ] Genetic programming for symbolic regression
Implement a genetic programming system in JS that evolves mathematical expressions to fit a target function (e.g., sin(x) * x^2 + 3). Visualize generations, fitness distribution, and best expression over time. Allow the user to define the target function as a JS expression.
- [ ] RL agent playing a custom gridworld
Build a single-file JS app with a gridworld environment and a reinforcement learning agent (tabular Q-learning or SARSA) that learns to reach a goal while avoiding traps. Visualize the Q-values as colored overlays and let users tweak learning rate, discount factor, and exploration.
- [ ] Multi-agent traffic simulation with RL
Simulate a road network with multiple intersections and traffic lights. Train RL agents (per light) to minimize total waiting time for cars. Visualize queues, waiting times, and learned behaviors. Everything must run in-browser, no backend.
- [ ] Interactive linear algebra visualizer
Create a tool that lets users define 2D or 3D matrices and vectors and see transformations applied visually: rotation, shear, scaling, projections. Show eigenvectors/eigenvalues when applicable, and animate repeated application (matrix powers).
- [ ] Tiny programming language with interpreter and debugger
Design a small imperative language (variables, if, while, functions). In a single HTML file, implement a tokenizer, parser to AST, interpreter, and a step-by-step debugger (breakpoints, stepping), with variable watch. Provide a code editor and execution console.
- [ ] WebAssembly text (WAT) editor + visualizer
Create an in-browser WAT (WebAssembly text format) editor that assembles simple modules to binary using a JS implementation. Visualize functions, locals, control flow (graph of blocks). Allow stepping through execution of a test function with live local and stack view.
- [ ] Regex-to-DFA visual converter
Design a tool that takes a regex, builds an NFA (Thompson’s construction), then converts it to a DFA (subset construction) and minimizes it. Show each step graphically, with states and transitions, and a final minimized DFA.
- [ ] Code formatter (pretty-printer) for a mini language
Create a language with blocks and expressions, then write a parser and a pretty-printer that formats ugly code into a canonical style (proper indentation, newlines, spaces). Provide side-by-side view: raw input vs formatted output.
- [ ] Natural language → DSL translator + validator
Define a simple DSL for scheduling tasks (like “TASK name AT time REPEAT …”). Implement a parser and executor. Then build a natural language front-end: user types “Every Monday at 9, backup the database”, and the app suggests one or more DSL translations, which the user can edit and validate.
- [ ] Diff-based auto-grader for HTML/CSS tasks
Create a tool where the “instructor” defines an expected DOM structure and CSS constraints. The “student” writes HTML/CSS in an editor. The app compares rendered output + DOM tree against the teacher spec, pointing out mismatches (missing elements, wrong classes, differences in computed styles for key selectors).
- [ ] Logical puzzle solver with explanation generator
Implement a solver for logic grid puzzles (like “who owns the zebra”) using constraint satisfaction in JS. The user enters puzzle clues in a structured form; the solver finds all solutions and auto-generates a human-readable explanation of the deduction steps.
- [ ] Interactive SAT solver visualizer
Implement a Boolean SAT solver (DPLL or CDCL-lite) in JS and visualize the solving process: variable assignments, decision levels, conflicts, backtracking. Users can input CNF formulas manually or via a small builder UI.
- [ ] Multi-agent negotiation simulator
Create a simulation where several agents negotiate over dividing a set of items with different utilities. Implement different strategies (Nash bargaining, naive, greedy) and show the timeline of offers, concessions, and final allocation. Visualize utilities and fairness metrics (e.g., envy-freeness).
- [ ] Data cleaning + transformation workshop
Build a robust CSV/JSON data wrangling web app: users can define a pipeline of transformations (filter, map, group, pivot, merge, deduplicate, normalize). Each step is represented as a node in a pipeline graph. Show intermediate results per step, and export the final dataset as CSV/JSON.
- [ ] Mini-Assembler VM върху WebAssembly
Create a single-file HTML/JS application that implements a tiny assembly-like language and executes it on top of WebAssembly.
The app should:
Define a simple stack-based assembly language with instructions such as: PUSH <number>, ADD, SUB, MUL, DIV, DUP, SWAP, JMP <label>, JZ <label>, PRINT, HALT.
Include a text editor area where the user can type assembly programs, with labels and comments.
Implement a parser that converts the text into an internal instruction representation, resolving labels.
Generate WebAssembly Text (WAT) code from this instruction list, compile it in the browser using WebAssembly.instantiate (no server), and execute it.
Provide a “Run”, “Step”, and “Reset” button, and show the current instruction pointer, the stack contents, and printed output in real time.
All code (HTML, CSS, JavaScript, WAT generation) must be contained in a single standalone HTML file that runs directly in the browser.
Ensure the assembly language, code generation, and execution pipeline are clearly structured and well commented.
- [ ] Fortran → WebAssembly demo (концептуално + код)
Explain and implement a minimal toolchain to compile a simple Fortran numerical kernel to WebAssembly and run it in the browser.
The answer must:
Choose a concrete Fortran compiler that can target WebAssembly (for example, via LLVM) and describe exactly which commands to run to compile a sample Fortran file (e.g. a function that multiplies two matrices or solves a small system of linear equations) to a .wasm module.
Provide a complete Fortran example program with at least one function that can be called from the host (e.g. subroutine matmul(n, A, B, C) with explicit interfaces).
Show a complete HTML + JavaScript example that loads the compiled .wasm module in the browser and calls the Fortran function, passing arrays from JavaScript to WebAssembly memory and reading back the results.
Explain how memory is laid out and how to handle Fortran’s column-major arrays vs JavaScript’s typed arrays.
Include all HTML and JavaScript in a single HTML file (the .wasm can be loaded as an external binary), and make sure the JS code is sufficient to run the example in a modern browser.
Create a single-file HTML/JavaScript application that implements a tiny assembly-like programming language and executes it using a custom virtual machine written in JavaScript (no real WebAssembly code generation required).
The entire app must be contained in one standalone HTML file.
- [ ] JLPT N5 Full Mock Test (Real Exam Format)
Create a complete JLPT N5 mock test in authentic exam style.
Include the three sections: Vocabulary (もじ・ごい), Grammar/Reading (ぶんぽう・どっかい), and Listening (ちょうかい).
Each section must include instructions in Japanese, questions formatted like the official JLPT, answer choices, and a separate answer key.
The listening section may use text-based dialogues instead of audio.
At the end of the test, include a small section labeled “More Tests” with working text-links to placeholder pages: N5 Test B, N4 Test, N3 Test, Listening Drills, Kanji Drills, Grammar Drills.
Everything must resemble a real JLPT paper test.
- [ ] JLPT N5 Vocabulary Trainer
Create an interactive JLPT N5 vocabulary training module.
The module should randomly present one N5-level word, show four possible meanings, accept the user’s answer, track the score, and give immediate feedback.
Use only authentic N5 vocabulary.
Provide at least 50 questions.
No external dependencies.
- [ ] Hiragana Speed Test
Generate a full Hiragana Speed Test.
Present random hiragana characters one at a time, each with four possible romanized readings.
Include at least 100 questions, track response time, and calculate accuracy and speed rating in the end.
Make it look like an online quiz app.
- [ ] Katakana Recognition Exam
Create a Katakana Recognition Exam designed for beginners.
Include 60–100 katakana items, mixed with foreign-loan words.
For each question, show a katakana word and provide four possible English meanings.
Include a full answer key at the end.
- [ ] N5 Kanji Drill (103 Kanji)
Create a JLPT N5 Kanji drill covering all 103 official N5 kanji.
For each kanji, include:
its meaning, onyomi and kunyomi readings, and one example word.
Then create a quiz section with 50 multiple-choice questions using these kanji.
Provide an answer key.
- [ ] Japanese Verb Conjugation Drills
Create a verb conjugation drill set for JLPT N5 learners.
Include exercises for: masu-form, dictionary form, te-form, negative form, and past tense.
Provide 40–60 questions and a separate answer sheet.
Use only N5-level verbs.
- [ ] N5 Grammar Exercise Pack
Create a JLPT N5 grammar practice set.
Include explanations (in simple English) for major N5 grammar points such as 〜です, 〜ます, あります/います, 〜たい, から/まで, に/へ, で, と, の, 〜てください, 〜ましょう.
After the explanations, create 40 grammar questions in JLPT exam style with answer choices and a key.
- [ ] N5 Reading Practice Stories
Write 5 short reading passages appropriate for JLPT N5 students.
Each passage should be 80–150 characters long, include furigana on all kanji, and come with 3–5 comprehension questions.
Include answer keys.
- [ ] Daily Japanese Dialogue Simulator
Generate 10 everyday Japanese dialogues suitable for N5 learners.
Each dialogue should be 6–10 lines long, include furigana on kanji, and be followed by multiple-choice comprehension questions.
At the end, include a vocabulary list for each dialogue.
- [ ] JLPT Study Hub Page Generator
Create a “JLPT Study Hub” page that lists links to multiple study resources.
Include links (text-only) to: N5 Mock Test A, N5 Mock Test B, N4 Test, N3 Test, Vocabulary Drills, Grammar Drills, Kanji Drills, Listening Practice, Reading Practice, and Verb Conjugation Trainer.
Each link should point to a placeholder section on the same page.
The goal is to simulate a real study-website navigation structure.
- [ ] Habit Tracker with Jetpack Compose and Room
Create a complete Android habit-tracking app in Kotlin using Jetpack Compose and Room.
The app should allow users to:
Add, edit, and delete habits (name, description, target days per week, icon/color).
Mark habits as done for each day on a calendar-like view.
See statistics for each habit (completion rate, streaks, best streak, last 7/30 days).
Use MVVM architecture, a single-activity approach with Compose navigation, and Room as the local database. Implement dark mode, state handling for configuration changes, and simple unit tests for the ViewModel layer. Provide all necessary Kotlin code, including data models, DAOs, database setup, ViewModels, and Composables.
- [ ] Offline Japanese Vocabulary Trainer (N5 Level)
Build an Android app in Kotlin that works completely offline and helps users practice JLPT N5 vocabulary.
Use Jetpack Compose for the UI and store vocabulary in a local Room database (or pre-populated database).
The app should support:
Browsing vocabulary by category (e.g., numbers, family, verbs, adjectives).
Flashcard mode (word → meaning, meaning → word).
Quiz mode with 4 multiple-choice answers and score tracking.
A “favorite” list for difficult words.
Use MVVM, handle screen rotation correctly, and include a simple settings screen (e.g., toggle furigana, show/hide romaji).
- [ ] Personal Finance Tracker with Charts
Create an Android personal finance tracker app in Kotlin using Jetpack Compose and the MPAndroidChart (or similar) library for charts.
Features:
Add/ edit/ delete expenses and incomes (amount, category, date, note).
Filter by date range and category.
Show monthly summary with pie chart (spending by category) and line chart (balance over time).
Export all transactions to a CSV file and share it.
Use Room for persistent storage, MVVM for architecture, and Kotlin coroutines/Flow for reactive updates. Provide full example code, including repository, ViewModels, and Composables.
- [ ] Fitness Workout Planner with Notifications
Build an Android fitness workout planner in Kotlin.
Requirements:
Users can create workouts (name, list of exercises, reps/sets/time).
Schedule workouts on specific days and times.
Use Android’s AlarmManager or WorkManager to trigger local notifications reminding the user of their next workout.
A “Today” screen showing today’s planned workouts and completion toggles.
Use XML or Jetpack Compose for UI (you may choose), MVVM architecture, and Room for storage. Include code for setting and cancelling notifications when workouts are added/edited/deleted.
- [ ] Notes App with Markdown Support and Search
Build a note-taking Android app in Kotlin with support for Markdown formatting.
Specifications:
Users can create, edit, and delete notes with title and body.
Notes support basic Markdown (bold, italics, headings, bullet lists).
Live preview of the rendered Markdown.
Search notes by title and content.
Use Room for storing notes, MVVM for architecture, and Jetpack Compose for UI. You may use an existing Kotlin Markdown library, but show full integration code. Implement a simple color theme switcher (light/dark).
- [ ] Task Manager with Drag-and-Drop Kanban Board
Create an Android task manager app in Kotlin that displays tasks in a Kanban-style board (e.g., “To Do”, “In Progress”, “Done”).
Requirements:
Use Jetpack Compose for UI.
Users can create, edit, and delete tasks (title, description, due date, priority).
Implement drag-and-drop to move tasks between columns.
Persist data with Room, and load it on startup.
Use MVVM architecture with proper state management for the Kanban board. Provide clear code for drag-and-drop logic in Compose.
- [ ] Language Learning App with Spaced Repetition (SRS)
Design an Android language-learning app in Kotlin that uses a simple spaced repetition algorithm for vocabulary.
Features:
Users can add custom words and translations.
Each word has a review schedule and review history.
Daily review screen: show due words, and let the user rate each review (e.g., “easy”, “good”, “hard”).
Adjust next review date based on rating using a basic SRS algorithm (you can implement a simplified SM-2).
Use Room for storage, MVVM + repository pattern, and Jetpack Compose for UI.
- [ ] Camera-based QR Code Scanner with History
Create an Android QR code scanner app in Kotlin using CameraX and a QR code detection library (e.g., ML Kit or ZXing).
The app should:
– Use CameraX to show a live camera preview.
– Continuously scan the preview for QR codes and detect their content.
– When a QR code is detected, display its content, provide buttons to copy it, open it as a URL (if applicable), and save it to a local history.
– Implement a history screen using Room to store previously scanned codes with timestamp and type (URL, text, etc.).
– Use Jetpack Compose for the UI and MVVM architecture for state management.
- [ ] AR Measurement Tool Using Camera and Sensors
Develop an Android app in Kotlin that approximates measuring distances using the device camera and motion sensors (gyroscope/accelerometer).
The app should:
– Use the camera to show a live preview.
– Use the device’s orientation sensors to estimate pitch and roll.
– Allow the user to tap on the screen to mark two points and estimate the horizontal distance between them using basic trigonometry (assuming the device height from the ground as a parameter).
– Display the estimated distance on screen with a simple overlay, and keep a small history of recent measurements.
– Clearly comment all sensor-related math and assumptions in the code.
A fully precise AR implementation is not required, but the app should be logically consistent and demonstrate sensor integration.
- [ ] Step Counter & Activity Tracker Using Accelerometer
Create an Android step counter app in Kotlin that uses the device’s accelerometer (and optionally the step detector sensor) to track steps and daily activity.
The app should:
– Register the appropriate sensors and count steps in the background while the app is open.
– Display the current step count, estimated distance, and estimated calories burned based on user profile (height, weight, gender).
– Show a simple daily bar chart (steps per hour) for the current day using Jetpack Compose.
– Handle sensor registration/unregistration properly in lifecycle-aware components.
– Use DataStore or Room to persist daily step counts and reload them when the app is restarted.
- [ ] Environmental Sensor Dashboard (Light, Proximity, Temperature)
Build an Android “Environmental Sensor Dashboard” app in Kotlin that reads and displays data from available device sensors such as ambient light, proximity, and ambient temperature (if present).
The app should:
– Detect which of these sensors are available on the device and show a card for each one.
– Continuously display live sensor readings with units (e.g., lux, cm, °C).
– Plot a short time-series graph (last 60 seconds) for each sensor in a simple line chart.
– Use lifecycle-aware components and MVVM architecture.
– Provide a settings screen allowing the user to adjust the update interval and enable/disable specific sensors to save battery.
- [ ] Camera Photo App with Filters and Gallery
Create an Android camera app in Kotlin using CameraX that allows users to take photos, apply simple filters, and view them in a gallery.
The app should:
– Use CameraX for capturing still images.
– After capturing a photo, show a preview screen where the user can apply basic filters (e.g., grayscale, sepia, brightness/contrast adjustment) implemented via Bitmap processing or RenderScript/RenderEffect.
– Save the processed images to local storage in an app-specific folder.
– Provide a gallery screen to browse, view, and delete saved photos.
– Use Jetpack Compose for the UI and handle runtime permissions for camera and storage correctly.
- [ ] Compass App Using Magnetometer and Accelerometer
Build a fully functional compass app in Kotlin for Android.
The app should:
– Use the magnetometer and accelerometer sensors to compute the device’s orientation and heading (azimuth).
– Display a compass UI with a rotating needle pointing to magnetic north.
– Show the current heading in degrees and cardinal direction (N, NE, E, etc.).
– Apply basic sensor smoothing/low-pass filtering to avoid jitter.
– Handle sensor registration and unregistration properly in the activity/fragment lifecycle.
Optionally, include a simple calibration screen or instructions if the sensor readings appear off.
- [ ] Interval Reminder App
Create a complete Android application in Kotlin that allows the user to set custom interval reminders and receive notifications at the chosen repeating interval. The user should be able to enter a reminder title, a short description, and select any interval such as every few minutes, every hour, or every day. The app should store reminders persistently using Room or DataStore and allow enabling, disabling, editing, and deleting them. Use Jetpack Compose for all UI screens and MVVM architecture with ViewModel, Repository, and Kotlin coroutines. Use WorkManager to schedule repeating notifications that continue to run even after the app is closed. The app must include all required Kotlin code, including the database setup, entities, DAOs, ViewModels, the WorkManager worker, notification channels for Android 13+, and the Compose screens for listing reminders and creating a new reminder. The final answer should provide a fully working example project.
- [ ] Meditation Timer App
Create a fully functional Android meditation timer application written in Kotlin using Jetpack Compose and MVVM. The app should let the user choose a meditation duration in minutes, start and pause the countdown, and receive a gentle notification or sound when the timer finishes. The timer must continue to run correctly during screen rotation or backgrounding using a ViewModel and coroutines. Every completed meditation session should be saved in persistent storage using Room or DataStore, including the date and duration. The app should display a history screen showing all past sessions and a statistics screen showing total time meditated, the longest session, and average session length. Provide complete Kotlin code for all ViewModels, repositories, data models, database configuration, Compose screens, navigation, and notification handling. The final output should be a complete example project.
