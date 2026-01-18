# NeuroBlink-An-Intelligent-Eye-Blink-Based-Morse-Code-Communication-System
NeuroBlink is an intelligent eye-blink based communication system that uses real-time computer vision to detect blink patterns and translate them into Morse code. It enables hands-free text generation, offering an accessible and offline communication solution for assistive and human-computer interaction use cases.

# 🧠 NeuroBlink  
### An Intelligent Eye-Blink Based Morse Code Communication System

[![GitHub stars](https://img.shields.io/github/stars/Alexrohith/NeuroBlink-An-Intelligent-Eye-Blink-Based-Morse-Code-Communication-System?style=social)](https://github.com/Alexrohith/NeuroBlink-An-Intelligent-Eye-Blink-Based-Morse-Code-Communication-System)


<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue.svg"/>
  <img src="https://img.shields.io/badge/Computer%20Vision-OpenCV-green"/>
  <img src="https://img.shields.io/badge/AI-Assistive%20Tech-purple"/>
  <img src="https://img.shields.io/badge/License-MIT-yellow"/>
</p>

---

## 🚀 Overview

**NeuroBlink** is an AI-powered assistive communication system that enables hands-free text generation using eye blink patterns. By leveraging real-time computer vision and intelligent blink analysis, the system translates eye blinks into Morse code and converts them into readable text.

This project is designed to support **accessibility, human-computer interaction**, and **assistive technology**, offering an alternative communication method for individuals with speech or motor impairments.

---

## 🧠 How It Works

1. Captures real-time video input using a standard camera  
2. Detects eye landmarks and calculates Eye Aspect Ratio (EAR)  
3. Identifies intentional blink patterns  
4. Maps blink durations to Morse code (dot, dash, pause)  
5. Decodes Morse signals into text output  

---

## ✨ Key Features

- 👁️ Real-time eye blink detection  
- 📹 Computer vision-based processing  
- 🔤 Morse code translation to text  
- 👐 Hands-free communication  
- ⚡ Lightweight & offline execution  
- ♿ Assistive and accessibility-focused design  

---

## 🛠 Tech Stack

- **Programming Language:** Python  
- **Computer Vision:** OpenCV  
- **Facial Landmark Detection:** dlib / MediaPipe  
- **Logic Layer:** Morse code parsing & buffering  
- **Environment:** Virtual Environment (venv)

---

## 📂 Project Structure

```text
NeuroBlink/
│
├── src/                # Core application logic
├── vision/             # Eye detection & blink analysis
├── logic/              # Morse code encoding/decoding
├── utils/              # Helper functions
├── requirements.txt    # Dependencies
└── README.md


⚙️ Installation & Setup

# Clone the repository
git clone https://github.com/Alexrohith/NeuroBlink-An-Intelligent-Eye-Blink-Based-Morse-Code-Communication-System.git

# Navigate to project directory
cd NeuroBlink

# Create virtual environment
python -m venv venv

# Activate environment
# Windows
venv\Scripts\activate
# Linux / macOS
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

▶️ Run the Project
python src/main.py
## ⭐ Support the Project

If you find **NeuroBlink** useful or inspiring, please consider giving it a ⭐ on GitHub.  
Your support helps improve visibility and motivates further development!
