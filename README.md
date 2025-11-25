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
**Make a clone of the Windows 11 desktop. Use the original wallpaper. On the desktop, there should be icons for MS Word, Paint, Calculator, and Chrome. Each program should work. Use working images. Put everything in a standalone html file**

| Model                 | Score    |
| --------------------- | -------- |
| **Gemini 3**        | **0/10** |
| **ChatGPT 5.1**       | **0/10** |
| **Grok 4.1**          | **0/10** |
| **Claude Sonnet 4.5** | **0/10** |

---

### Excel clone
**Create a functional clone of Microsoft Excel in a single standalone HTML file (no external dependencies except CSS/JS embedded or via CDN). The UI should resemble a modern spreadsheet app with a toolbar at the top, a formula bar, column headers (A, B, C, …), row numbers (1, 2, 3, …), and a scrollable grid of editable cells. Each cell must support entering values and formulas (starting with =), with basic formula support for arithmetic (+ - * /), cell references (e.g. =A1+B2), and simple functions like SUM, AVERAGE, MIN, MAX over ranges (e.g. =SUM(A1:A10)). While editing a formula in the formula bar, allow the user to click or drag-select cells/ranges so their addresses (e.g. A1, B2, A1:A10) are automatically inserted into the formula. Implement automatic recalculation of dependent cells whenever a referenced cell changes, and display the currently selected cell’s address and formula/value in the formula bar. Include basic features such as: selecting cells with mouse, dragging to select ranges, double-click to edit, keyboard navigation with arrow keys/Enter/Tab, resizing columns, and support for multiple sheets (with sheet tabs and the ability to add/rename/delete sheets). Add a minimal toolbar with actions like bold/italic text, background color for cells, clear contents, and a simple “Download as CSV” and “Upload CSV” for the active sheet. Make the design clean and responsive, visually inspired by Excel but without using any copyrighted assets, and ensure everything runs smoothly in the browser without a backend.**

| Model                 | Score    |
| --------------------- | -------- |
| [**Gemini 3**](https://vislupus.github.io/LLM-testing/Excel%20clone/gemini.html)          | **5/10** |
| [**ChatGPT 5.1**](https://vislupus.github.io/LLM-testing/Excel%20clone/chatgpt.html)       | **3/10** |
| **Grok 4.1**          | **0/10** |
| [**Claude Sonnet 4.5**](https://vislupus.github.io/LLM-testing/Excel%20clone/claude.html) | **5/10** |

---

### Photoshop clone
**Create a clone of photoshop with all the basic tools. Include brushes, layers, edit history, filters, blending options, and more. Put everything in a standalone html file**

| Model                 | Score    |
| --------------------- | -------- |
| **Gemini 3**          | **0/10** |
| **ChatGPT 5.1**       | **0/10** |
| **Grok 4.1**          | **0/10** |
| **Claude Sonnet 4.5** | **0/10** |

---

### Beehive simulation
**Make a visual simulation of a beehive construction, showing hexagonal cells forming, worker bee paths, and honey storage. Include sliders for colony size and resource availability. Put everything in a standalone html file**

| Model                 | Score    |
| --------------------- | -------- |
| **Gemini 3**          | **0/10** |
| **ChatGPT 5.1**       | **0/10** |
| **Grok 4.1**          | **0/10** |
| **Claude Sonnet 4.5** | **0/10** |

---

### Space shooter game
**Create a space shooter game where players pilot a ship through asteroid fields, dodging debris and firing lasers at alien invaders. Make it visually stunning with particle explosions. Use publicly available assets. Put everything in a standalone html file.**

| Model                 | Score    |
| --------------------- | -------- |
| **Gemini 3**          | **0/10** |
| **ChatGPT 5.1**       | **0/10** |
| **Grok 4.1**          | **0/10** |
| **Claude Sonnet 4.5** | **0/10** |

---

### 3D scene
**Code a beautiful 3D scene inspired by this image. Use Three.js in a single html file**

| Model                 | Score    |
| --------------------- | -------- |
| **Gemini 3**          | **0/10** |
| **ChatGPT 5.1**       | **0/10** |
| **Grok 4.1**          | **0/10** |
| **Claude Sonnet 4.5** | **0/10** |

---

### Ray tracing simulation
**Develop a real-time ray tracing simulation featuring 2 metallic spheres suspended above a street scene. Use any publicly available 3D street view environment, and allow adjustable parameters such as reflectivity, roughness, and other material properties of the sphere. Put everything in a standalone html file.**

| Model                 | Score    |
| --------------------- | -------- |
| **Gemini 3**          | **0/10** |
| **ChatGPT 5.1**       | **0/10** |
| **Grok 4.1**          | **0/10** |
| **Claude Sonnet 4.5** | **0/10** |

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
| [**Gemini 3**](https://vislupus.github.io/LLM-testing/Three-body%20problem/gemini.html)          | **3/10** |
| [**ChatGPT 5.1**](https://vislupus.github.io/LLM-testing/Three-body%20problem/chatgpt.html)       | **6/10** |
| [**Grok 4.1**](https://vislupus.github.io/LLM-testing/Three-body%20problem/grok.html)          | **2/10** |
| [**Claude Sonnet 4.5**](https://vislupus.github.io/LLM-testing/Three-body%20problem/claude.html) | **2/10** |

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
