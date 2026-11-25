# Linear Transformations: A Geometric Perspective (3Blue1Brown Style)

A ~4-minute animated educational video created with **Manim Community**, explaining the geometric intuition behind linear transformations, matrix-vector multiplication, eigenvectors, determinants, orientation, and dimension collapse.

---

## 🎥 Watch the Video

* **Full HD Master (1080p @ 60 FPS, Git LFS):** [Download / View `linear_transformations_final.mp4`](./linear_transformations_final.mp4)

<!-- Drag and drop linear_transformations_preview.mp4 here in GitHub's web editor for an inline video player! -->

---

## 📁 Project Architecture

```text
maths/
├── linear_transformations_final.mp4   # The 1 Final Master Video (1080p60 with Voiceover)
├── linear_transformations.py          # Complete Manim Animation Source Code
├── README.md                          # Project Documentation & Architecture
└── assets/
    └── voiceover.m4a                  # Raw Recorded Voiceover Audio
```

---

## 🎬 Master Video Details

* **File**: `linear_transformations_final.mp4`
* **Resolution**: 1920 × 1080 (Full HD)
* **Framerate**: 60 FPS
* **Duration**: **04:03** (243.3 Seconds)
* **Audio**: AAC 48 kHz, High-Quality 192 kbps Voiceover
* **Visual Style**: Dark theme `#0e1117` with color-coded basis vectors $\hat{i}$ (Green) and $\hat{j}$ (Red), inspired by Grant Sanderson's *Essence of Linear Algebra*.

---

## 🧠 Educational Chapters Covered

1. **Chapter 1: The Three Rules of Linearity** (`00:00 – 00:48`)
   * Origin $(0, 0)$ remains anchored.
   * Grid lines remain straight (no bending or curves).
   * Parallel grid lines remain parallel and evenly spaced.
   * Basis vectors $\hat{i} = [1, 0]^T$ and $\hat{j} = [0, 1]^T$.

2. **Chapter 2: The Matrix as a Coordinate Map & Grid Deformation** (`00:48 – 01:27`)
   * Columns of matrix $A = \begin{bmatrix} 2.0 & 1.0 \\ 0.5 & 1.5 \end{bmatrix}$ are where $\hat{i}$ and $\hat{j}$ land.
   * Smooth 8.5-second continuous grid deformation.
   * Vector transformation tracking: $\vec{u} = \begin{bmatrix} 3 \\ -2 \end{bmatrix} \to \begin{bmatrix} 4.0 \\ -1.5 \end{bmatrix}$.

3. **Chapter 3: Lengths, Directions & Both Eigenvectors** (`01:27 – 02:04`)
   * Vectors stretch and rotate ($\|\vec{v}\| = 1.80 \to 4.59$).
   * **Eigenvector 1**: $\vec{e}_1 = [2, 1]^T$ ($\lambda_1 = 2.5$) — does not rotate, scales along its own line.
   * **Eigenvector 2**: $\vec{e}_2 = [-1, 1]^T$ ($\lambda_2 = 1.0$) — invariant direction where points do not move.

4. **Chapter 4: Area Scaling and The Determinant** (`02:04 – 02:32`)
   * Unit square deforms into a parallelogram of Area = $\det(A) = ad - bc = 2.5$.
   * All 2D shapes expand area by $2.5\times$ (circle to ellipse demonstration).

5. **Chapter 5: Orientation Inversion and Negative Determinants** (`02:32 – 03:02`)
   * Counter-clockwise handedness ($\hat{i} \to \hat{j}$).
   * Reflection matrix $B = \begin{bmatrix} -1 & 0 \\ 0 & 1 \end{bmatrix}$ with $\det(B) = -1.0$.
   * Space flipped over like a sheet of paper (chirality reversed).

6. **Chapter 6: Zero Determinant & Dimension Collapse** (`03:02 – 03:39`)
   * Matrix $C = \begin{bmatrix} 1 & 2 \\ 0.5 & 1 \end{bmatrix}$ with $\det(C) = 0$.
   * Space squishes onto a 1D line ($y = 0.5x$).
   * Rank drops from 2 to 1 (singular, non-invertible matrix).

7. **Chapter 7: Master Summary & Outro** (`03:39 – 04:03`)
   * 6-point geometric summary table.
   * Closing quote: *"Think with geometry, compute with matrices."*

---

## 🛠️ How to Re-render (Reproducibility)

```bash
# Render video only in 1080p60
manim -qh linear_transformations.py LinearTransformationSceneComplete

# Mux with voiceover
ffmpeg -y -i media/videos/linear_transformations/1080p60/LinearTransformationSceneComplete.mp4 \
       -i assets/voiceover.m4a -c:v copy -c:a aac -b:a 192k linear_transformations_final.mp4
```
