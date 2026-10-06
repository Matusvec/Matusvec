<p align="center">
  <a href="https://matusvec.github.io">
    <img src="assets/banner.svg" width="100%" alt="Matus Vecera. Computer science and physics at Notre Dame, class of 2029. Gaussian splatting, reinforcement learning, C++ and low-level systems. The artwork is Mars drawn as a cloud of Gaussian splats.">
  </a>
</p>

<p align="center">
  <a href="https://matusvec.github.io"><img src="https://img.shields.io/badge/Portfolio-matusvec.github.io-5eead4?style=for-the-badge&labelColor=0b1020" alt="Portfolio: matusvec.github.io"></a>
  <a href="https://linkedin.com/in/mvecera"><img src="https://img.shields.io/badge/LinkedIn-in%2Fmvecera-818cf8?style=for-the-badge&labelColor=0b1020" alt="LinkedIn: in/mvecera"></a>
  <a href="mailto:mvecera@nd.edu"><img src="https://img.shields.io/badge/Email-mvecera%40nd.edu-f8fafc?style=for-the-badge&labelColor=0b1020" alt="Email: mvecera@nd.edu"></a>
</p>

I study computer science and physics at Notre Dame, class of 2029. Most of my work right now is in three places: **3D Gaussian splatting** (I've rebuilt a patch of Mars from rover photos and whole rooms from a phone), **reinforcement learning**, and **C++ close to the hardware**. Before that I spent a summer building production software at NASA Headquarters.

<p align="center">
  <a href="#nasa">NASA</a> ·
  <a href="#gaussian-splatting">Gaussian splatting</a> ·
  <a href="#machine-learning">Machine learning</a> ·
  <a href="#systems">Systems, graphics, and low-level</a> ·
  <a href="#hardware">Hardware</a> ·
  <a href="#more">More</a>
</p>

<table>
  <tr><th colspan="4" align="left">Gaussian splatting and machine learning</th></tr>
  <tr>
    <td width="25%" valign="top"><a href="#planetary-scene-studio"><img src="assets/planetary-concept.jpg" width="100%" alt="Planetary Scene Studio"></a><br><b><a href="#planetary-scene-studio">Planetary Scene Studio</a></b><br><sub>🥇 Winner, SpaceXAI track, MHacks 2026</sub><br><sub>Mars rebuilt from rover photos as a Gaussian splat you can plan a base on.</sub></td>
    <td width="25%" valign="top"><a href="#spatialmind"><img src="assets/spatialmind-scene.jpg" width="100%" alt="SpatialMind Gaussian splat scene"></a><br><b><a href="#spatialmind">SpatialMind</a></b><br><sub>🥈 2nd place, JacHacks 2026</sub><br><sub>Ask a 3D scene a question in plain language and it points to the answer.</sub></td>
    <td width="25%" valign="top"><a href="#sharks--minnows"><img src="assets/sharks-frame.jpg" width="100%" alt="Sharks and Minnows: minnows crossing the field while the shark chases the decoy"></a><br><b><a href="#sharks--minnows">Sharks &amp; Minnows</a></b><br><sub>Multi-agent reinforcement learning</sub><br><sub>A transformer policy that taught itself to use a decoy.</sub></td>
    <td width="25%" valign="top"><a href="#volana"><img src="assets/volana-surface.jpg" width="100%" alt="Volana dashboard"></a><br><b><a href="#volana">Volana</a></b><br><sub>🥇 1st place, WildHacks 2026</sub><br><sub>Arbitrage-free neural volatility surface, built solo in 24 hours.</sub></td>
  </tr>
  <tr><th colspan="4" align="left">Systems, graphics, and low-level</th></tr>
  <tr>
    <td width="25%" valign="top"><a href="#vecengine"><img src="assets/vecengine-1.jpg" width="100%" alt="vecEngine flight over procedural terrain"></a><br><b><a href="#vecengine">vecEngine</a></b><br><sub>C++17 and OpenGL 3.3, from scratch</sub><br><sub>A 3D engine and flight simulator with no engine underneath.</sub></td>
    <td width="25%" valign="top"><a href="#ember"><img src="assets/ember-landmarks.jpg" width="100%" alt="Ember facial landmark tracking"></a><br><b><a href="#ember">Ember</a></b><br><sub>🥇 1st place overall, Hesburgh Hackathon 2026</sub><br><sub>Run Linux with your face: webcam input injected at the kernel level.</sub></td>
    <td width="25%" valign="top"><a href="#8-bit-cpu-and-hardware-divider"><img src="assets/cpu-register-file.jpg" width="100%" alt="Register file schematic of the 8-bit CPU"></a><br><b><a href="#8-bit-cpu-and-hardware-divider">8-bit CPU</a></b><br><sub>Digital logic, from gates</sub><br><sub>A full CPU and a hardware divider wired by hand.</sub></td>
    <td width="25%" valign="top"><a href="#sentinel"><img src="assets/sentinel.jpg" width="100%" alt="Sentinel hardware"></a><br><b><a href="#sentinel">Sentinel</a></b><br><sub>🏅 Best Use of MongoDB, RocketHacks 2026</sub><br><sub>A ~$150 vision station that tracks people with a PID gimbal.</sub></td>
  </tr>
</table>

<a name="nasa"></a>
<p align="center"><img src="assets/h-nasa.svg" width="100%" alt="NASA Headquarters"></p>

**Summer 2026, Washington, DC**

I worked on EDAQ in close collaboration with colleagues across NASA. It is an analytics system now used by analysts at every NASA center: it answers plain-language questions over agency workforce data with grounded, cited results. I cut end-to-end latency by 41% and took the system through an independent security audit before rollout. Along the way I was flown from the Ames supercomputer to the Hubble control room at Goddard.

<p>
  <img src="assets/nasa-administrator.jpg" width="32.5%" alt="Matus with NASA Administrator Jared Isaacman">
  <img src="assets/nasa-sign.jpg" width="32.5%" alt="Matus in front of the NASA sign at Headquarters">
  <img src="assets/nasa-cohort.jpg" width="32.5%" alt="The NASA Headquarters intern cohort on stage">
</p>

<a name="gaussian-splatting"></a>
<p align="center"><img src="assets/h-splatting.svg" width="100%" alt="3D Gaussian splatting"></p>

Two of my projects are built on 3D Gaussian splatting: turning ordinary photos into a scene made of millions of oriented, coloured Gaussians that renders in real time. In both, the Gaussians carry more than colour. Semantic features from CLIP and SAM are lifted onto them, so the scene can be searched, labelled, and edited in plain language.

| | [Planetary Scene Studio](#planetary-scene-studio) | [SpatialMind](#spatialmind) |
|:--|:--|:--|
| **Scene** | Cheyava Falls, Jezero Crater, Mars | Real indoor rooms |
| **Gaussians** | 972,047 | 5.2 million |
| **Input** | 241 Perseverance rover photos | Phone capture |
| **Camera poses** | JPL camera models and rover telemetry, no structure-from-motion | COLMAP |
| **Training** | gsplat (MCMC) | 3D Gaussian Splatting with LangSplat |
| **Semantics** | SegFormer terrain classes, SAM + CLIP text search | CLIP features at three scales from SAM masks |
| **Result** | 🥇 Winner, SpaceXAI track, MHacks 2026 | 🥈 2nd place, Agentic AI track, JacHacks 2026 |

### Planetary Scene Studio

**🥇 Winner, SpaceXAI track, MHacks 2026** · [Source](https://github.com/Matusvec/spaceX-Mhacks-Challenge) · [Live](https://planetary-scene-studio.vercel.app)

Plan a base on Mars or the Moon on the real ground, together. From orbit, the sharpest pictures of Mars are 25 cm per pixel, so a 30 cm rock is a single pixel, and a rock that size decides whether a wheel or a landing leg works. Rovers have photographed some places at millimetres per pixel. Planetary Scene Studio puts a photoreal, metric ground site built from those rover photos onto real orbital terrain, then lets a mission team plan on it in one shared session. Built with two teammates.

<p align="center">
  <img src="assets/planetary-hero.jpg" width="100%" alt="The live site: swiping between the real 3D Mars scene and a concept render of a domed base painted onto the same terrain and camera angle">
</p>

- **A splat from rover photos.** 972,047 Gaussians trained with gsplat from 241 Perseverance photos of Cheyava Falls in Jezero Crater. There is no structure-from-motion: images are undistorted with JPL's camera models, posed from rover telemetry, and three rover stops are registered to within 2 pixels.
- **On real orbital terrain.** The splat sits on 2 km of HiRISE terrain in the same metric frame. Inside the 18 m site, orbit has about 4,000 photo pixels; the splat has nearly a million Gaussians.
- **Semantic layers on every Gaussian.** A SegFormer model trained on AI4Mars labels terrain class, and SAM regions embedded with CLIP power text search like "sand ripples".
- **Plan and drive.** A suitability map grades the terrain, placed habitats get a scorecard, and a six-wheel rocker-bogie rover follows the ground at Perseverance's real top speed of 4.2 cm/s.
- **The Moon too.** Sunlight and Earth visibility at Malapert Massif near the lunar south pole, computed from LOLA terrain and JPL ephemerides.
- **Live multiplayer.** Cursors, pins, modules, rover drives, and team chat sync through SpacetimeDB, with chat, voice, and concept renders through Grok.

`Python` `PyTorch` `gsplat` `SegFormer` `CLIP` `TypeScript` `React` `three.js` `SpacetimeDB`

<p>
  <img src="assets/planetary-orbit-vs-ground.jpg" width="32.5%" alt="The same 18 metre patch of Mars from orbit at half a metre per pixel and from the ground as a Gaussian splat">
  <img src="assets/planetary-rover.jpg" width="32.5%" alt="A six-wheel rover driving across the reconstructed Mars terrain">
  <img src="assets/planetary-text-search.jpg" width="32.5%" alt="Text search for sand ripples highlighting matching Gaussians in blue">
</p>
<p>
  <img src="assets/planetary-splat.jpg" width="32.5%" alt="Close view of the Gaussian splat of Cheyava Falls from rover eye height">
  <img src="assets/planetary-terrain-class.jpg" width="32.5%" alt="Terrain class layer colouring the splat by soil, bedrock, sand, and big rock">
  <img src="assets/planetary-moon.jpg" width="32.5%" alt="Illumination map of Malapert Massif near the lunar south pole">
</p>

### SpatialMind

**🥈 2nd place, Agentic AI track, JacHacks 2026 at Michigan** · [Source](https://github.com/Matusvec/spatialMind)

Real rooms rebuilt as 5.2 million semantic Gaussians, then queried in plain language: ask for the chair by the window and the scene points to it. Built and presented against 70+ teams.

<p>
  <img src="assets/spatialmind-scene.jpg" width="32.5%" alt="Semantic Gaussian splat scene of a desk with monitors">
  <img src="assets/spatialmind-recon.jpg" width="32.5%" alt="A 5.2 million Gaussian reconstruction of a person sitting on a couch">
  <img src="assets/spatialmind-present.jpg" width="32.5%" alt="Presenting the SpatialMind pipeline in a lecture hall">
</p>

- **Reconstruction.** Scenes are captured on a phone, posed with COLMAP, and trained as 3D Gaussian splats.
- **Semantics on every Gaussian.** LangSplat embeds CLIP features at three scales from SAM masks: whole objects, parts, and fine subparts.
- **The query pipeline.** Text becomes a 512-d CLIP vector, is scored against every Gaussian with LERF-style relevancy, and DBSCAN groups the hits into object instances that light up in the 3D viewport.
- **Edit and explore.** "Turn the couch blue" recolors the Gaussians live. An exploration walker catalogs objects and builds a spatial knowledge graph (left of, above, behind, near).
- **An agent on top.** Questions like "what furniture is near the window?" route to a tool-calling agent that composes several scene lookups.

`PyTorch` `OpenCLIP` `SAM` `COLMAP` `LangSplat` `FastAPI` `React` `Three.js`

<a name="machine-learning"></a>
<p align="center"><img src="assets/h-ml.svg" width="100%" alt="Machine learning"></p>

### Sharks & Minnows

**Multi-agent reinforcement learning** · [Source](https://github.com/Matusvec/sharks-and-minnows-rl)

One policy controls a team of ten minnows that have to cross a field past a shark that is faster than nine of them. The slow minnows cannot outrun it, so the only way to save everyone is to coordinate.

<p align="center">
  <img src="assets/sharks-and-minnows.gif" width="80%" alt="The learned policy saving all ten minnows: the fast minnow draws the shark to one sideline while the slow minnows cross the other way">
</p>

- **Decoy behaviour emerged on its own.** No reward term tells the fast minnow to act as a decoy. The policy learned it: the fast minnow runs to one sideline, the shark follows, and the nine slow minnows cross on the far side.
- **The policy** is a centralized, permutation-equivariant transformer. Each minnow is a token, with 2 self-attention layers, 4 heads, 64-d embeddings, and two critics (team value and per-minnow value).
- **Training** is PPO with GAE, KL early stopping, and rollback when validation collapses, on a curriculum that slows the minnows only after the policy passes a performance gate.
- **The simulator** is fully vectorized in PyTorch and steps 512 games at once on a laptop RTX 5070.
- **Results.** A perfect 10/10 game in 98.1% of 1,024 fixed-seed validation games at the starting difficulty, and 78.5% at the hardest speed solved. Below that, training settles on a "sacrifice one" local optimum that saves nine of ten. The repo documents every attempt to break it.

`PyTorch` `PPO` `Transformer policy` `Curriculum learning`

<p>
  <img src="assets/sharks-perfect-rate.jpg" width="49%" alt="Perfect-game rate against difficulty for two training runs, with the nine-of-ten plateau marked">
  <img src="assets/sharks-training.jpg" width="49%" alt="Training curves: average minnows saved, survival by speed, actor loss, and critic losses per PPO update">
</p>

### Volana

**🥇 1st place, Anthropic Claude track, WildHacks 2026 at Northwestern** · [Source](https://github.com/Matusvec/volpath)

Draw where you think a stock is going and see what your option is worth at every point along the path, including the moment volatility crushes on earnings day. Built and presented alone in 24 hours against full teams.

<p align="center">
  <img src="assets/volana-dashboard.jpg" width="100%" alt="Volana dashboard: the learned 3D volatility surface on the left, a hand-drawn price path with an earnings line in the middle, and the option's profit and loss curve along that path">
</p>

- **A neural volatility surface.** A physics-informed network (four hidden layers of 128 units, about 50,000 parameters) learns implied volatility as a continuous function of strike and maturity from about 1,000 live SPY option quotes.
- **No-arbitrage enforced in the loss.** The butterfly and calendar conditions are computed with `torch.autograd` and penalized during training. The final surface has zero butterfly and calendar violations.
- **Measured against SABR,** the 30-year industry standard: 93% lower error across every fold.
- **A scenario engine.** Every point on the drawn path is repriced with a sticky-moneyness vol lookup, a path-dependent vol regime, an earnings vol crush, and Black-Scholes, fast enough to update while you draw.
- **A live data pipeline.** Quotes are pulled from the market, inverted to implied vol with Brent root-finding, and cleaned of outliers per expiry before training.

`PyTorch` `autograd` `SciPy` `FastAPI` `Three.js`

<p>
  <img src="assets/volana-surface-fit.jpg" width="32.5%" alt="The fitted SPY implied volatility surface over strike and maturity, with 1,018 market quotes">
  <img src="assets/volana-present.jpg" width="32.5%" alt="Presenting Volana solo in a lecture hall">
  <img src="assets/volana-winner.jpg" width="32.5%" alt="Matus with an organizer after winning the track">
</p>

<a name="systems"></a>
<p align="center"><img src="assets/h-systems.svg" width="100%" alt="Systems, graphics, and low-level"></p>

### vecEngine

**C++17 and OpenGL 3.3, from scratch** · [Source](https://github.com/Matusvec/vecEngine)

A single-binary 3D engine and flight simulator on raw OpenGL, with no engine, scene graph, or asset library underneath: just GLFW, GLAD, and GLM. Lift, drag, thrust, and gravity are integrated every frame from aircraft state, so the aircraft flies because the physics says so. It holds 60+ FPS on a single thread.

<p align="center">
  <img src="assets/vecengine-flight.gif" width="100%" alt="Gameplay capture of vecEngine: an aircraft flying low over green hills toward alpine peaks, then banking along a steep mountainside in rain and fog">
</p>

- **Procedural terrain.** Value-noise FBM, ridged multifractal peaks, and domain warping, with biomes that blend by altitude from sand to snow.
- **Chunk streaming.** A fixed ring of chunks with modular slot indexing, so crossing a chunk boundary regenerates only one row or column.
- **Culling.** Frustum and fog-distance culling with bounding spheres, using Gribb–Hartmann plane extraction.
- **Lighting.** Phong shading and a 2048² shadow map with 3×3 PCF. The shadow camera is texel-snapped to stop shimmering.
- **GPU instancing.** Grass and shrubs are instanced, with wind animated in the vertex shader.
- **A game on top.** A ring course, balloons to shoot down, missiles that blow craters in the terrain, water, rain, and a procedural sky.
- **BLACKBOX.** A second app on the same engine: an airfield with a ground model, takeoff roll, stall and landing, 5 Hz UDP telemetry, and an injectable aileron actuator failure.
- **Tested headless.** Unit tests run with no GL context.

`C++17` `OpenGL 3.3` `GLSL` `GLFW` `GLM` `CMake`

<p>
  <img src="assets/vecengine-1.jpg" width="32.5%" alt="Aircraft low over grass and shrubs with ridged peaks fading into fog ahead">
  <img src="assets/vecengine-2.jpg" width="32.5%" alt="Aircraft banking over a lake with sand shorelines blending into grass">
  <img src="assets/vecengine-3.jpg" width="32.5%" alt="Aircraft passing a fresh missile crater on a hillside beside the lake">
</p>
<p>
  <img src="assets/vecengine-4.jpg" width="32.5%" alt="The ring course: the active ring directly ahead with two more beyond it">
  <img src="assets/vecengine-blackbox.jpg" width="32.5%" alt="The BLACKBOX airfield app: an aircraft just after takeoff over the runway centreline">
  <img src="assets/vecengine-fps.jpg" width="32.5%" alt="Aircraft banking over mountains in vecEngine">
</p>

### Ember

**🥇 1st place overall, Hesburgh Hackathon 2026** · [Source](https://github.com/Matusvec/ember)

A userspace input driver for people who can't use a mouse or keyboard. A standard webcam decodes facial expressions, head motion, and finger movements, and the driver injects them into the Linux kernel as real input events, so the whole OS and any application work hands-free. Built with a team of four.

<p>
  <img src="assets/ember-landmarks.jpg" width="32.5%" alt="Live facial landmark overlay from Ember on a webcam feed">
  <img src="assets/ember-present.jpg" width="32.5%" alt="Presenting Ember to the hackathon judges">
  <img src="assets/ember-award.jpg" width="32.5%" alt="Hackathon results slide: first place, $3,000, Ember">
</p>

- **Kernel-level input.** Events go through `/dev/uinput` as a virtual mouse and keyboard, so nothing needs to know Ember exists.
- **A tight loop.** Perception to action runs at 30 FPS inside a 33 ms frame budget.
- **Per-user profiles.** Onboarding maps whatever movements someone can reliably make to actions. Profiles hot-reload, so a changed binding takes effect on the next frame.
- **A voice agent.** A wake word opens a conversational agent that can launch apps, search the web, type, and click. Half-duplex audio keeps it from answering its own speech.
- **A dwell keyboard.** An on-screen keyboard types after 600 ms of cursor dwell through a second `uinput` device, so focus stays in the target app.

`Python` `MediaPipe` `OpenCV` `Linux uinput` `evdev` `FastAPI`

### 8-bit CPU and hardware divider

**Digital logic, from gates**

A complete 8-bit CPU and a hardware divider designed from raw gates in Logisim: ALUs, register files, datapaths, and FSM controllers, wired by hand. I'm porting the CPU to Verilog for FPGA.

<p>
  <img src="assets/cpu-register-file.jpg" width="49%" alt="Register file of the 8-bit CPU in Logisim">
  <img src="assets/cpu-divider-controller.jpg" width="49%" alt="Controller logic for the hardware divider">
</p>

<a name="hardware"></a>
<p align="center"><img src="assets/h-hardware.svg" width="100%" alt="Hardware"></p>

<p>
  <img src="assets/sentinel.jpg" width="32.5%" alt="Sentinel breadboard with Arduino, camera, and sensors">
  <img src="assets/audio-amp.jpg" width="32.5%" alt="Amplifier on the workbench">
  <img src="assets/subwoofer.jpg" width="32.5%" alt="Self-built subwoofer enclosure">
</p>

### Sentinel

**🏅 Best Use of MongoDB, RocketHacks 2026** · [Source](https://github.com/Matusvec/baseSentinel)

A ~$150 Python and Arduino perception station. Vision models drive PID-controlled pan/tilt tracking, fused with ultrasonic and IR sensors. It detects people and falls, recognizes known faces, and takes plain-English missions that reconfigure the perception pipeline.

### Audio chain

A SigmaDSP active crossover driving an amplifier stack and a subwoofer I built.

<a name="more"></a>
<p align="center"><img src="assets/h-more.svg" width="100%" alt="More"></p>

- [Label Check](https://github.com/Matusvec/ttb-label-verifier): checks alcohol label images against their application data and sorts each one into approved, rejected, or needs review. [Live demo](https://ttb-label-verifier-two.vercel.app)
- [aunalyticsNLSQL](https://github.com/Matusvec/aunalyticsNLSQL): turns plain-English questions into validated, read-only SQL, with a local LLM first and a cloud fallback.
- [Liberation Trader](https://liberationtraders.com): an AI research desk for self-directed investors.

<p align="center">
  <a href="https://matusvec.github.io">Portfolio</a> · <a href="https://linkedin.com/in/mvecera">LinkedIn</a> · <a href="mailto:mvecera@nd.edu">mvecera@nd.edu</a>
</p>
