# 🍩 Console Donut Renderer

Welcome to the **Console Donut Renderer**! 🎉 This project is a mesmerizing experiment in math, ASCII art, and pure creativity. Watch a 3D donut come to life in your console, spinning hypnotically, and showcasing the beauty of mathematical visualizations! ✨

---

## 🌟 About This Project

This project is a **recreation of the famous ASCII donut render by Andy Sloane**, which took the programming world by storm! However, this version introduces a **voxel-based approach**, which is a stark departure from Andy Sloane's original mathematical rendering method. The voxel method introduces its own quirks and challenges, making the donut spin in a unique and fascinating way! 🎲🍩

If you've ever been mesmerized by spinning ASCII art, you're in the right place!

---

## ✨ Features

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

## ⚠️ Important: Console Size Matters!

To fully enjoy the donut's hypnotic spin, **make sure your console window is large enough to fit the whole donut**.  
If your console is too small, you might see artifacts or leftover visuals. Resize your window, sit back, and enjoy the show! 🖥️

---

## 🌟 How It Works

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

## 🎬 Video Previews

Want to see the donut in action? Check out these previews! 👇

### 🍩 Depth-Based Shading  
![Depth-Based Shading](path-to-your-depth-based-shading.gif)

### 💡 Light-Based Shading  
![Light-Based Shading](path-to-your-light-based-shading.gif)

### 🌀 Hybrid Shading  
![Hybrid Shading](path-to-your-hybrid-shading.gif)

### 🎭 Custom ASCII Characters  
![Custom ASCII Characters](path-to-your-custom-ascii.gif)

### ⚡ Faster Rotation  
![Faster Rotation](path-to-your-faster-rotation.gif)

*(Replace `path-to-your-*.gif` with actual file paths or hosted URLs.)*

---

## 🛠️ Installation

Setting up the donut renderer is super simple! Let’s get started:  

1. **Clone the repository**:  
   ```bash
   git clone https://github.com/Akshat-Mishra-py/console-donut-renderer.git
   cd console-donut-renderer
   ```

2. **Install dependencies**:  
   ```bash
   pip install numpy
   ```

And that’s it! You’re ready to render some donuts! 🍩🎉

---

## 🚀 Usage

Let’s spin that donut! Run the script with:  
```bash
python donut.py
```

Sit back and enjoy the hypnotic rotations. You deserve it. 🌀✨

---

## 🎨 Customization

Make the donut your own! Here are some ways to tweak it:  

- **🛠️ Adjust Grid Size**:  
  Change the `GRID` variable (default is 40). Larger grids = more detail but slower performance.

- **💡 Lighting Options**:  
  Modify the `LIGHTING` variable to adjust the light ratio.  
  - `1`: Pure light-based shading.  
  - `0`: Depth-based shading.  
  - Any value in-between combines the two.

- **🎭 ASCII Characters**:  
  Change the `FILLER` characters to customize the shading style. Try:  
  - `' ', '.', '-', '=', '+', '*', '#', '@'`  
  - `(' ', '▏', '▎', '▍', '▌', '▉', '█')`

---

## 📦 Dependencies

- Python 3.x 🐍  
- NumPy 📊  

---

## 📜 License

This project is licensed under the [MIT License](LICENSE.txt). Feel free to use, modify, and share it! 🚀

---

## 💡 Contributing

We’d love your help in making this project even better! 💖  

- Found a bug? 🐛 Open an issue!  
- Have a cool new feature in mind? ✨ Submit a pull request!  

**Note:** This project uses a voxel-based approach that differs significantly from Andy Sloane's original method. The rotation matrix is also intentionally flawed. These quirky design choices create the unique spin effect that makes the donut so mesmerizing. If you'd like to "fix" it, feel free to contribute, but keep in mind this was done on purpose to add character! 🎲

---

## 🙌 Acknowledgments

This project is inspired by the **famous ASCII donut render by Andy Sloane**. His original work showcased the beauty of math and ASCII art in a way that captivated programmers worldwide. This version is a tribute with its own twist, using a voxel-based approach and intentionally flawed methods to add a unique spin effect. Thank you, Andy, for inspiring us all! 💖✨