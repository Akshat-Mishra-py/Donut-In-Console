# 🍩 Console Donut Renderer

Welcome to the **Console Donut Renderer**! 🎉 This project is a mesmerizing experiment in math, ASCII art, and pure creativity. Watch a 3D donut come to life in your console, spinning hypnotically, and showcasing the beauty of mathematical visualizations! ✨

---
## Table of Contents

   - [About This Project](#about-this-project)
   - [Features](#features)
   - [Installation](#installation)
   - [Usage](#usage)
   - [Technical Details](#technical-details)
      - [Torus Geometry](#1-torus-geometry)
      - [Rotation Mechanics](#2-rotation-mechanics)
      - [Lighting and Normals](#3-lighting-and-normals)
      - [ASCII Shading](#4-ascii-shading)
      - [Rendering Process](#5-rendering-process)
      - [Performance Optimization](#6-performance-optimization)
      - [Customization](#7-customization)

   - [Dependencies](#dependencies)
   -  [License](#license)
   - [Contributing](#contributing)
   - [Acknowledgments](#acknowledgments)

---
## About This Project

This project is a **recreation of the famous ASCII donut render by Andy Sloane**, which took the programming world by storm! However, this version introduces a **voxel-based approach**, which is a stark departure from Andy Sloane's original mathematical rendering method. The voxel method introduces its own quirks and challenges, making the donut spin in a unique and fascinating way! 🎲🍩

If you've ever been mesmerized by spinning ASCII art, you're in the right place!

---

## Features

🍩 **Voxel-Based 3D Torus Geometry**:  
Generate a voxel-based 3D torus using mathematical equations that define its perfect donut shape.

🔄 **Smooth Rotation**:  
The donut rotates along an axis of your choice using a (flawed but fascinating 🤓) 3D rotation matrix.

💡 **Lighting and Shading**:  
Enjoy realistic lighting effects! Normals and light vectors combine to create stunning depth and brightness.

🎨 **Customizable ASCII Art**:  
Choose your own characters to represent brightness levels. The donut becomes your artistic canvas! 🎭

⚡ **Performance**:  
Runs at ~25 FPS for a smooth and satisfying experience right in your terminal.

---

## Important: Console Size Matters!

To fully enjoy the donut's hypnotic spin, **make sure your console window is large enough to fit the whole donut**.  
If your console is too small, you might see artifacts or leftover visuals. Resize your window, sit back, and enjoy the show! 🖥️

---

## How It Works

1. **🛠️ Voxel Grid**:  
   Unlike Andy Sloane's original method, this project uses a **voxel-based grid** to create the 3D torus. Each voxel represents a small 3D "block" in the donut's structure, giving it a distinct aesthetic.

2. **🔄 Rotation Magic**:  
   A 3D rotation matrix spins the torus around an axis of your choice. (P.S. The matrix is intentionally flawed for a fun, quirky spin effect! 🎲)

3. **💡 Lighting & Normals**:  
   Normals are calculated for every voxel, and lighting is added based on a customizable light direction.

4. **🎨 ASCII Shading**:  
   Brightness levels are represented by ASCII characters to produce a stunning visual effect.

5. **📽️ Rendering**:  
   The torus is rasterized onto a 2D buffer and rendered beautifully as ASCII art in your console.

---

## Video Previews

Want to see the donut in action? Check out the preview! 👇

<video src = "https://github.com/user-attachments/assets/1de9462b-f762-4e68-a978-b8419dd4b01b" width=300 controls></video>
<video src = "https://github.com/user-attachments/assets/4e73448f-c4c3-437d-98b8-4895fcdb661b"  width=300 controls></video>

<a href="https://youtube.com/shorts/PIdHU3gy6KI?feature=share">More Previews</a>

---

## Installation

Setting up the donut renderer is super simple! Let’s get started:  

1. **Clone the repository**:  
   ```bash
   git clone https://github.com/Akshat-Mishra-py/Donut-In-Console.git
   cd Donut-In-Console
   ```

2. **Install dependencies**:  
   ```bash
   pip install numpy
   ```

And that’s it! You’re ready to render some donuts! 🍩🎉

---

## Usage

Let’s spin that donut! Run the script with:  
```bash
python donut.py
```

Sit back and enjoy the hypnotic rotations. You deserve it. 🌀✨

---
## Technical Details

The Console Donut Renderer relies on a combination of **voxel-based geometry**, **matrix transformations**, and **ASCII art rendering** to create its mesmerizing effect. Here’s a detailed breakdown of its core mechanics:

---

### 1. **Torus Geometry**

- The donut is represented as a **voxel grid** in 3D space.
- The torus geometry is defined by two radii:
  - **Major Radius (R)**: Radius from the center of the torus to the midpoint of the tube.
  - **Minor Radius (r)**: Radius of the tube itself.
  
- The equation used to define the torus:
  ```
  ((R - sqrt(x² + y²))² + z²) <= r²
  ```
  - `(x, y, z)` are points in a 3D space.
  - Only the points satisfying this condition are part of the torus, and the rest are discarded.

---

### 2. **Rotation Mechanics**

- The torus rotates in 3D space using a **rotation matrix**. The axis of rotation is defined by a user-specified **rotation vector** which is normalized before use.
- The rotation matrix for an arbitrary axis `(ux, uy, uz)` and angle `θ` is:
  ```bash
  | cos(θ) + ux²(1-cos(θ))        uy*ux(1-cos(θ)) - uz*sin(θ)   uz*ux(1-cos(θ)) + uy*sin(θ) |
  | uy*ux(1-cos(θ)) + uz*sin(θ)   cos(θ) + uy²(1-cos(θ))        uz*uy(1-cos(θ)) - ux*sin(θ) |
  | uz*ux(1-cos(θ)) - uy*sin(θ)   uz*uy(1-cos(θ)) + ux*sin(θ)   cos(θ) + uz²(1-cos(θ))      | 
  ```

- Each voxel point in the torus is rotated around the specified axis using this matrix. The resulting coordinates are clipped and mapped back to the grid.

---

### 3. **Lighting and Normals**

- **Normal Vectors**:
  - For each voxel, a normal vector is calculated based on its position relative to the torus geometry.
  - The normal vector is determined by:
    ```
    nX = 2*X*(1 - R/Q)
    nY = 2*Y*(1 - R/Q)
    nZ = 2*Z
    ```
    where `Q = sqrt(x² + y²)`.

- **Lighting**:
  - A light vector is specified (e.g., `[-1, -1, 2]`) and normalized.
  - The brightness of each voxel is calculated as the **dot product** of the normal vector and the light vector:
    ```
    brightness = normal · light
    ```
  - This value is normalized and used to determine the shading.

---

### 4. **ASCII Shading**

- The renderer uses a customizable **ASCII character set** to represent different brightness levels. For example:
  - `(' ', '▏', '▎', '▍', '▌', '▋', '▊', '▉', '█')`
  - Lighter areas of the torus use characters like `' '` or `'▏'`.
  - Darker and brighter areas use progressively denser characters like `'▉'` or `'█'`.

- Brightness is mapped to the corresponding ASCII character by scaling it to the range of the character set.

---

### 5. **Rendering Process**

1. **Buffers**:
   - A **screen buffer** represents the 2D grid of the console.
   - A **z-buffer** tracks the depth of each voxel to handle occlusion.

2. **Rasterization**:
   - Each voxel is projected onto the 2D screen buffer.
   - The brightness and shading are calculated for the closest voxel at each screen position.

3. **Output**:
   - The ASCII representation of the donut is constructed line by line.
   - Each frame is then printed to the console with a slight delay to simulate smooth animation (~25 FPS).

---

### 6. **Performance Optimization**

- **NumPy**:
  - NumPy is used extensively for matrix operations and transformations, ensuring efficient computations.
- **Grid Size**:
  - The default grid size is `40x40x40`. A larger grid produces a more detailed torus but may reduce performance.
- **Frame Timing**:
  - The renderer dynamically adjusts to maintain a consistent frame rate of ~25 FPS.

---
### 7. **Customization**

Make the donut your own! Here are some ways to tweak it:  

- **🛠️ Adjust Grid Size**:  
  Change the `GRID` variable (default is 40). Larger grids = more detail but slower performance.

- **💡 Lighting Options**:  
  Modify the `LIGHTING` variable to adjust the light ratio.  
  - `1`: Pure light-based shading.  
  - `0`: Depth-based shading.  
  - Any value in-between combines the two.

- **🎭 ASCII Characters**:  
  Change the `ASCII_MODE` characters to customize the shading style. Try:  
   - `1` -> `(' ', '▏', '▎', '▍', '▌', '▉', '█')`  
   - `2` -> `(' ','⡀', '⡄', '⡆', '⡇', '⣇', '⣧', '⣷', '⣿')`
---


## Dependencies

- Python 3.x 🐍  
- NumPy 📊  

---

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and share it! 🚀

---

## Contributing

We’d love your help in making this project even better! 💖  

- Found a bug? 🐛 Open an issue!  
- Have a cool new feature in mind? ✨ Submit a pull request!  

**Note:** This project uses a voxel-based approach that differs significantly from Andy Sloane's original method. The rotation matrix is also intentionally flawed. These quirky design choices create the unique spin effect that makes the donut so mesmerizing. If you'd like to "fix" it, feel free to contribute, but keep in mind this was done on purpose to add character! 🎲

---

## Acknowledgments

This project is inspired by the **famous ASCII donut render by Andy Sloane**. His original work showcased the beauty of math and ASCII art in a way that captivated programmers worldwide. This version is a tribute with its own twist, using a voxel-based approach and intentionally flawed methods to add a unique spin effect. Thank you, Andy, for inspiring us all! 💖✨
