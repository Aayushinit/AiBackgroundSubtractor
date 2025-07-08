# 🧠 AI Background Subtractor

A real-time background subtraction web application built using **Python**, **OpenCV**, and **Flask**. It features dynamic foreground detection using classic computer vision algorithms — **KNN** and **MOG2** — with a smooth, modern UI.

---

## 🚀 Features

- 📸 Live Webcam Feed  
- ✂️ Real-time Background Subtraction  
- 🧠 Toggle Between KNN and MOG2 Algorithms  
- 🌈 Colored Foreground & Shadow Detection (Green = Foreground, Red = Shadows)  
- 🖼️ Side-by-Side Original vs Processed Display  
- 🧪 Algorithm Selection UI  
- 🎨 Stylish Tailwind CSS Interface  
- ✅ Fully Local Python-Flask App (No external API needed)

---

## 📂 Folder Structure

```
AiBackgroundSubtractor/
├── templates/
│   └── index.html           # Web UI
└── app.py                   # Flask backend with OpenCV logic
```

---

## ⚙️ Technologies Used

| Technology      | Purpose                                  |
|-----------------|------------------------------------------|
| **Python**      | Backend logic and OpenCV processing      |
| **OpenCV**      | Video capture and background subtraction |
| **Flask**       | Local web server and API routes          |
| **Tailwind CSS**| Modern, responsive UI styling            |
| **HTML / JS**   | Frontend structure and interactivity     |

---

## 🎯 How It Works

- Your webcam provides a live video stream via **OpenCV**.  
- Each frame is processed by a **background subtractor**:
  - `KNN`: K-Nearest Neighbors method.
  - `MOG2`: Gaussian Mixture Model approach.
- Foreground and shadows are highlighted using color masks:
  - 🟩 Foreground → Green
  - 🟥 Shadows → Red
- The processed output is streamed in real-time alongside the raw feed.

---

## 🛠️ How to Run Locally

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Aayushinit/AiBackgroundSubtractor.git
   cd AiBackgroundSubtractor
   ```

2. **Install dependencies**:
   ```bash
   pip install flask opencv-python
   ```

3. **Run the app**:
   ```bash
   python app.py
   ```

4. **View in browser**:  
   Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

> 📸 Make sure your webcam is connected and not being used by another app.

---

## 📌 Use Cases

- Motion detection and surveillance  
- Human-computer interaction projects  
- Educational demos for Computer Vision  
- Lightweight vision system for robotics  

---

## 📃 License

This project is licensed under the [MIT License](LICENSE).

---

## 👨‍💻 Author

**Aayush Kadam**  
Final Year AI & Robotics Enthusiast  
GitHub: [github.com/your-username](https://github.com/Aayushinit)

---

---

> ⭐ If you found this project useful, give it a star and share it!
