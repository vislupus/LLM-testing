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
| **ChatGPT 5.1**       | **3/10** |
| **Grok 4.1**          | **3/10** |
| **Claude Opus 4.5**   | **5/10** |

---

### Excel clone
**Create a functional clone of Microsoft Excel in a single standalone HTML file (no external dependencies except CSS/JS embedded or via CDN). The UI should resemble a modern spreadsheet app with a toolbar at the top, a formula bar, column headers (A, B, C, …), row numbers (1, 2, 3, …), and a scrollable grid of editable cells. Each cell must support entering values and formulas (starting with =), with basic formula support for arithmetic (+ - * /), cell references (e.g. =A1+B2), and simple functions like SUM, AVERAGE, MIN, MAX over ranges (e.g. =SUM(A1:A10)). While editing a formula in the formula bar, allow the user to click or drag-select cells/ranges so their addresses (e.g. A1, B2, A1:A10) are automatically inserted into the formula. Implement automatic recalculation of dependent cells whenever a referenced cell changes, and display the currently selected cell’s address and formula/value in the formula bar. Include basic features such as: selecting cells with mouse, dragging to select ranges, double-click to edit, keyboard navigation with arrow keys/Enter/Tab, resizing columns, and support for multiple sheets (with sheet tabs and the ability to add/rename/delete sheets). Add a minimal toolbar with actions like bold/italic text, background color for cells, clear contents, and a simple “Download as CSV” and “Upload CSV” for the active sheet. Make the design clean and responsive, visually inspired by Excel but without using any copyrighted assets, and ensure everything runs smoothly in the browser without a backend.**

| Model                 | Score    |
| --------------------- | -------- |
| **Gemini 3**          | **5/10** |
| **ChatGPT 5.1**       | **3/10** |
| **Grok 4.1**          | **1/10** |
| **Claude Sonnet 4.5** | **5/10** |

---

### Photoshop clone
**Create a clone of photoshop with all the basic tools. Include brushes, layers, edit history, filters, blending options, and more. Put everything in a standalone html file**

| Model                 | Score    |
| --------------------- | -------- |
| **Gemini 3**          | **7/10** |
| **ChatGPT 5.1**       | **4/10** |
| **Grok 4.1**          | **2/10** |
| **Claude Opus 4.5**   | **8/10** |

---

### Climate‑change dashboard
**Create a single‑file HTML climate dashboard for Sofia that loads local data from the CSV file temperature_Sofia_2809794_1952-01-01 - 2021-11-28.csv (same folder as the HTML file) using JavaScript in the browser. Parse the columns DATE, TAVG, TMAX, and TMIN, convert them from tenths of degrees to °C, and compute aggregates such as yearly mean temperature, yearly extremes (max/min), monthly means, and counts of very hot days (e.g., TMAX ≥ 30°C) and very cold days (e.g., TMIN ≤ −10°C). Visualize these metrics with interactive charts (for example, line charts for annual and monthly means and a bar chart for hot/cold days) using an external library like Chart.js or D3 loaded from a CDN, and include simple summary statistics (overall mean, estimated warming trend). Provide UI controls in the same page to choose a year range (start/end year) and automatically update all charts and statistics when the range changes. All HTML, CSS, and JavaScript should be self-contained in one HTML file.**

| Model                 | Score    |
| --------------------- | -------- |
| **Gemini 3**          | **8/10** |
| **ChatGPT 5.1**       | **6/10** |
| **Grok 4.1**          | **2/10** |
| **Claude Opus 4.5**   | **9/10** |

---

### UI Builder
**Develop a single-file, standalone HTML/JavaScript application for a drag-and-drop UI builder, similar to Figma, complete with advanced settings, drag-and-drop placement, snap-to-grid, canvas resizing, and alignment guides. The application must include a comprehensive library of UI components, such as Buttons, Inputs, Text Fields, Checkboxes, Dropdowns, Sliders, Steppers, and Progress Bars, alongside basic geometric shapes like rectangular, Circle, Triangle, and Line. Users must be able to resize any element directly on the canvas using drag handles and configure advanced visual settings, including border radius and box shadows, via a dedicated properties panel. The builder is required to support dynamic flowcharting, allowing users to connect two elements with adjustable lines that automatically maintain their attachment points when the elements are moved or resized. All components, shapes, styles, and defined connections must be cleanly exported into a single, runnable HTML file.**

| Model                 | Score    |
| --------------------- | -------- |
| **Gemini 3**          | **9/10** |
| **ChatGPT 5.1**       | **6/10** |
| **Grok 4.1**          | **1/10** |
| **Claude Opus 4.5**   | **7/10** |

---

### DAW clone
**Create a DAW. Include multiple instruments and drums. Include a step grid and piano roll. Include tempo control, multiple tracks, effects (reverb, delay), volume sliders, and more. Put everything in a standalone html file**

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
| **Gemini 3**          | **8/10** |
| **ChatGPT 5.1**       | **6/10** |
| **Grok 4.1**          | **4/10** |
| **Claude Opus 4.5**   | **3/10** |

---

### Tetris game
**Create a complete Tetris game inside one standalone HTML file with all code (HTML, CSS, JS) embedded and no external assets. Include all tetromino shapes, movement, rotation, line clearing, scoring, speed increase, and a restartable game-over screen. Use clean, simple, procedurally drawn graphics and smooth animations.**

| Model                 | Score    |
| --------------------- | -------- |
| **Gemini 3**          | **8/10** |
| **ChatGPT 5.1**       | **8/10** |
| **Grok 4.1**          | **4/10** |
| **Claude Opus 4.5**   | **10/10** |

---

### Pirates island
**Create a single‑file 3D browser game prototype using Babylon.js where the player commands three pirate ships protecting a small tropical island in the middle of an ocean. The scene should include a stylized water plane, a small green island with a few simple props (like rocks or palms), and three friendly ships arranged around it; the camera is freely orbiting above the scene. Each friendly ship can be selected (keys 1–3), steered around the island, and upgraded between waves (e.g., increased cannon damage, fire rate, or movement speed). Enemy ships periodically spawn from the horizon and sail toward the island; friendly ships automatically or manually fire cannonballs at enemies, and if enemies reach the island they damage its health. Everything (HTML, CSS, JavaScript, Babylon.js setup, basic UI overlay for gold, wave, HP and upgrade buttons) should be contained in one .html file, ready to open directly in a browser.**

| Model                 | Score    |
| --------------------- | -------- |
| **Gemini 3**          | **0/10** |
| **ChatGPT 5.1**       | **7/10** |
| **Grok 4.1**          | **0/10** |
| **Claude Opus 4.5**   | **9/10** |

---

### 3D castle scene
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

### City simulation
**Make a 3D visual simulation of a growing city using **Babylon.js**, showing buildings appearing, roads forming, traffic flow, and people/vehicles moving around. Include sliders to control city size (population/density), traffic intensity, and development speed, updating the simulation in real time. Put everything in a single standalone HTML file with all HTML, CSS, and JavaScript embedded (no external assets).**

| Model                 | Score    |
| --------------------- | -------- |
| **Gemini 3**          | **6/10** |
| **ChatGPT 5.1**       | **6/10** |
| **Grok 4.1**          | **3/10** |
| **Claude Opus 4.5**   | **3/10** |
| **Glm 4.6**           | **5/10** |

---

### Space battle simulation
**A 3D space battle scene in **Babylon.js** as a single standalone HTML file (all HTML/CSS/JS in one file; Babylon.js may be loaded from a CDN). Between two opposing fleets, each with 10 ships. Every fleet has one larger flagship and nine smaller escort ships. The flagships are clearly bigger and more detailed, positioned at the center of each formation. Each ship has a visible health bar above it; when health reaches zero the ship explodes in a spectacular way, with bright fire, sparks, shockwaves and debris. If another ship is within roughly one ship‑width of the explosion, it also detonates in a chain reaction. Ships constantly move and maneuver in three‑dimensional space, turning and accelerating as they try to destroy the enemy fleet. One fleet fires bright blue glowing projectiles, the other fires bright red glowing projectiles, clearly distinguishing the two sides. Normal ships fire a single projectile every 3 seconds, while the two flagships fire two projectiles at once every 3 seconds. The scene should feel dynamic and cinematic, with trails behind projectiles, directional lighting from engine thrusters, and a starfield or nebula background. Make sure the whole scene is orbit-camera controlled, nicely lit, and fully working when the HTML file is opened in a browser.**

| Model                 | Score    |
| --------------------- | -------- |
| **Gemini 3**          | **9/10** |
| **ChatGPT 5.1**       | **7/10** |
| **Grok 4.1**          | **2/10** |
| **Claude Opus 4.5**   | **7/10** |
| **Glm 4.6**           | **0/10** |

---

### Ray tracing simulation
**Develop a real-time ray tracing simulation in **Babylon.js** as a single standalone HTML file, featuring 2 metallic spheres suspended above a street scene. Use any publicly available 3D street view environment, and allow adjustable parameters such as reflectivity, roughness, and other material properties of the sphere. Put everything in a standalone html file.**

| Model                 | Score    |
| --------------------- | -------- |
| **Gemini 3**          | **5/10** |
| **ChatGPT 5.1**       | **6/10** |
| **Grok 4.1**          | **1/10** |
| **Claude Opus 4.5**   | **8/10** |

---

### Three-body problem
**Create a p5.js simulation of a multi-body gravitational system centered on the Sun, Earth, and Jupiter, using realistic Newtonian gravity and ensuring all three bodies stay within the canvas while moving smoothly. Use a background value of 220, apply noStroke(), and render persistent orbital trails to clearly visualize the motion of each object over time. Add a spacecraft that starts on Earth, then departs to complete a clear loop around the Sun, and finally travels on a physically plausible trajectory to reach Jupiter. Configure the initial positions, velocities, and masses so that the planetary orbits are chaotic and non-stable (not like the real solar system), yet still remain bounded and visually coherent. The final simulation should behave as an interactive, visually engaging, physics-consistent environment where all bodies and the spacecraft move dynamically, without drifting off to infinity or collapsing into unnatural clusters. Put everything in a standalone html file.**

| Model                 | Score    |
| --------------------- | -------- |
| **Gemini 3**          | **3/10** |
| **ChatGPT 5.1**       | **6/10** |
| **Grok 4.1**          | **2/10** |
| **Claude Sonnet 4.5** | **2/10** |

---

### Galaxy simulation
**Create a p5.js simulation of galaxy formation where all entities are rendered as simple circles with varying sizes and brightness, using 10 000 particles that gradually self-organize into a physically plausible galaxy. The background should use a base color of 220 and stay visually subtle so the particle dynamics are clearly visible. Use p5.Vector for all motion and forces, apply gravity between particles with merging and mass conservation, and use a Quadtree (or similar spatial partitioning) to keep the simulation performant. A collapsing protogalactic cloud should evolve into a roughly spiral-like galaxy, with particles representing stars orbiting a central region in a Keplerian-like way (inner orbits faster than outer ones), influenced by an invisible dark matter halo and a central massive core or black hole. Ensure smooth animation and clear motion trails so the evolution of the galaxy remains visually captivating and grounded in physics-based behavior despite the large particle count. Put everything in a standalone html file.**

| Model                 | Score    |
| --------------------- | -------- |
| **Gemini 3**          | **8/10** |
| **ChatGPT 5.1**       | **3/10** |
| **Grok 4.1**          | **1/10** |
| **Claude Sonnet 4.5** | **2/10** |

---

### 2D Diffusion-Limited Aggregation
**Create an animated 2D Diffusion-Limited Aggregation (DLA) simulation that starts with 100 particles and continuously spawns new ones as each particle becomes fixed. Particles appear around the cluster, move randomly with a slight inward bias, and stick upon touching the existing structure. The animation must show the particles’ motion in real time, and growth stops when the cluster reaches 50 pixels from the canvas edge. The canvas should update smoothly, using efficient rendering to avoid lag. Optionally, allow adjustable settings such as particle count, movement speed, and bias strength. Put everything in a standalone html file.**

| Model                 | Score    |
| --------------------- | -------- |
| **Gemini 3**          | **7/10** |
| **ChatGPT 5.1**       | **5/10** |
| **Grok 4.1**          | **3/10** |
| **Claude Sonnet 4.5** | **2/10** |

---

### 2D Fluid simulation
**Create a 2D fluid simulation in p5.js with realistic fluid dynamics that mimic real‑world liquid motion, including swirling, spreading, and natural‑looking patterns over time. The simulation should support either particle‑based or grid‑based methods (e.g., Navier–Stokes or SPH), with varying density and velocity, plus smooth color diffusion so differently colored fluids mix visually. Allow interactive control: the mouse can inject velocity or disturb the fluid, while keys can add different colors, forces, adjust viscosity, reset the scene, or toggle vortex behavior. Render the fluid in a visually appealing, smooth way using efficient techniques so it remains responsive even with many particles or a high‑resolution grid, and optionally include obstacles and real‑time shader effects to enhance realism. Put everything in a standalone html file.**

| Model                 | Score    |
| --------------------- | -------- |
| **Gemini 3**          | **0/10** |
| **ChatGPT 5.1**       | **0/10** |
| **Grok 4.1**          | **0/10** |
| **Claude Opus 4.5**   | **0/10** |

---

### 2D Heat‑diffusion simulation
**Create a 2D heat‑diffusion simulation in p5.js that numerically solves the heat equation ∂T/∂t = α∇²T on a grid using finite‑difference methods (explicit or implicit), so temperature diffuses smoothly over time and can vary by material with different thermal conductivities. Represent temperature as a grid‑based field visualized with a heatmap gradient (blue = cold, red = hot), where heat naturally spreads and fades into realistic thermal patterns under configurable boundary conditions such as insulated edges or constant‑temperature borders. Let the user add heat sources by clicking, cool regions via keyboard input, and adjust parameters like conductivity, diffusion speed, resolution, and optionally convection strength. Ensure the update loop is efficient enough for real‑time interaction, and optionally support multiple heat sources, material presets, and GPU‑accelerated shaders to keep the simulation smooth at higher resolutions. Put everything in a standalone html file.**

| Model                 | Score    |
| --------------------- | -------- |
| **Gemini 3**          | **0/10** |
| **ChatGPT 5.1**       | **0/10** |
| **Grok 4.1**          | **0/10** |
| **Claude Opus 4.5**   | **0/10** |

---

### 2D Fluid‑flow animation
**Create a computer‑generated 2D fluid‑flow animation in p5.js that simulates fluid moving through a tube past an obstacle and clearly shows the formation of a von Kármán vortex street (alternating vortices shed behind the object). Represent the fluid on a grid or with particles and solve a simple Navier–Stokes–style or lattice‑Boltzmann approximation so the flow bends around the shape and vortices naturally appear in its wake. The obstacle should not be fixed: allow the user to move it with the mouse, change its size and shape (e.g., from circle to ellipse/rectangle), and rotate it freely through 360 degrees, with the flow and vortex pattern updating in real time as the object moves. Use color or velocity vectors to visualize the flow field and vorticity, while keeping the simulation efficient enough for smooth, interactive frame rates in the browser. Put everything in a standalone html file.**

| Model                 | Score    |
| --------------------- | -------- |
| **Gemini 3**          | **0/10** |
| **ChatGPT 5.1**       | **0/10** |
| **Grok 4.1**          | **0/10** |
| **Claude Opus 4.5**   | **0/10** |

---

### 2D Monte Carlo simulation
**Create a 2D Monte Carlo simulation in p5.js that models the evolution of an ecosystem on a grid, where each cell can contain different entities such as plants, herbivores, and predators. Use probabilistic rules for birth, death, movement, feeding, and mutation: at each time step, randomly select individuals and stochastically decide their actions based on parameters like energy, local population density, and resource availability. Allow traits (speed, vision range, reproduction rate, etc.) to mutate slightly during reproduction so that species can evolve over many generations, and visualize these traits with color or size variations. Let the user adjust parameters such as mutation rate, carrying capacity, initial populations, and interaction strengths via sliders or keys, and display simple statistics (population curves, average traits) alongside the main view. Keep the update loop efficient so large grids and many agents can run in real time, illustrating emergent patterns like extinction events, predator–prey cycles, and adaptation. Put everything in a standalone html file.**

| Model                 | Score    |
| --------------------- | -------- |
| **Gemini 3**          | **0/10** |
| **ChatGPT 5.1**       | **0/10** |
| **Grok 4.1**          | **0/10** |
| **Claude Opus 4.5**   | **0/10** |

---

### Tesseract animation
**Create an interactive 4D tesseract animation in p5.js: render a wireframe projection of a rotating tesseract onto 2D, using a 4D → 3D → 2D projection pipeline (homogeneous coordinates or rotation matrices in 4D space). Animate continuous rotation around multiple 4D axes so the shape constantly morphs between cube‑within‑cube and other characteristic projections, with smooth interpolation and adjustable rotation speed. Let the user control parameters via mouse/keyboard: pause/resume rotation, change which 4D planes are rotating, adjust projection distance, and toggle between orthographic and perspective‑style projection. Use clean lines, subtle shading, and optional color gradients to distinguish inner and outer edges, keeping the frame rate high for a fluid, educational visualization of a tesseract. Put everything in a standalone html file.**

| Model                 | Score    |
| --------------------- | -------- |
| **Gemini 3**          | **0/10** |
| **ChatGPT 5.1**       | **0/10** |
| **Grok 4.1**          | **0/10** |
| **Claude Opus 4.5**   | **0/10** |

---

### Equal Earth projection
**Create a single‑file interactive world map using SVG.js that renders the Earth in the Equal Earth projection and supports full coordinate ↔ screen conversion. The app should draw a clean vector world map in Equal Earth, with zoom and pan (mouse wheel + drag) that keep the projection mathematically correct at any scale. Implement forward projection: given geographic coordinates (latitude, longitude in degrees), convert them to projected x,y in the Equal Earth projection and plot a small SVG circle/marker at the correct location on the map. Implement inverse projection as well: when the user clicks on any point of the map (taking into account current zoom and pan), compute the corresponding latitude and longitude for that position and display them in a small overlay or console readout. All logic (HTML, CSS, JavaScript, SVG.js setup, projection formulas, zoom/pan handling, marker drawing and coordinate display) must be contained in a single self‑contained HTML file that runs directly in the browser.**

| Model                 | Score    |
| --------------------- | -------- |
| **Gemini 3**          | **0/10** |
| **ChatGPT 5.1**       | **0/10** |
| **Grok 4.1**          | **0/10** |
| **Claude Opus 4.5**   | **0/10** |

---

### 2D Gas simulation
**Create a single‑file 2D gas simulation in p5.js that illustrates ideas from statistical mechanics as accurately as possible while still running in real time. Represent gas molecules as many small disks moving in a rectangular box with perfectly elastic collisions between particles and with the walls; conserve momentum and kinetic energy in each collision, and support adjustable particle mass and radius. Allow the user to change key parameters via on‑screen controls or keyboard: number of particles, initial temperature (speed distribution), box size, particle mass ratio (for mixture of species), and whether collisions are enabled/disabled. Continuously compute and display macroscopic quantities derived from the microscopic motion – e.g., kinetic‑energy‑based temperature, pressure on the walls (force per unit length or area), and simple histograms of speed distribution approaching a Maxwell–Boltzmann‑like curve. Everything (HTML, CSS, JavaScript, p5.js setup, UI, physics update and visualization) must be contained in a single self‑contained file that can be opened directly in the browser.**

| Model                 | Score    |
| --------------------- | -------- |
| **Gemini 3**          | **0/10** |
| **ChatGPT 5.1**       | **0/10** |
| **Grok 4.1**          | **0/10** |
| **Claude Opus 4.5**   | **0/10** |

---

### Strandbeest legs
**Create a single‑file 3D demo in Babylon.js that uses a genetic algorithm to evolve walking Strandbeest‑style leg mechanisms. Represent each creature as a simple body with two or more multi‑segment legs in a plane, where each leg is defined by a genome encoding joint lengths, pivot positions, and possibly phase offsets for the leg cycle; decode the genome into a Babylon.js rig made of boxes/cylinders connected by rotating joints. Simulate a walking cycle on a flat ground plane using basic forward kinematics and simple physics or kinematic constraints, then evaluate each individual’s fitness by how far its body moves forward in a fixed time while remaining stable. Implement a full GA loop in JavaScript (selection, crossover, mutation, generation stepping), with controls to start/pause evolution, adjust population size, mutation rate, and cycle duration, and the option to highlight or replay the current best individual in the Babylon.js scene. All HTML, CSS, JavaScript, Babylon.js setup, GA logic, and visualization should live in one standalone .html file that runs directly in the browser.**

| Model                 | Score    |
| --------------------- | -------- |
| **Gemini 3**          | **0/10** |
| **ChatGPT 5.1**       | **0/10** |
| **Grok 4.1**          | **0/10** |
| **Claude Opus 4.5**   | **0/10** |
