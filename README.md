# 🚀 QR Generator Web App (Flask)

A sleek, lightweight web application built with Python and Flask that allows users to instantly generate high-quality QR codes from URLs.

## 🌟 Features
* **Instant Generation:** Creates QR codes in real-time as you type or submit.
* **Custom File Name:** Specify a custom filename before exporting for easier file organization and retrieval.
* **Downloadable Images:** Allows users to save the generated QR code directly to their device as a `.png` file.
* **Responsive Design:** Fully mobile-friendly interface built with clean CSS.

## 🛠️ Tech Stack
* **Backend:** Python, Flask
* **Frontend:** HTML, CSS
* **Libraries:** `qrcode` (Python library for generation)

## 📦 Installation & Setup

Follow these simple steps to run the application locally on your machine:

1. **Install Flask:**
   Open your terminal and run the following command to install the web framework:
   ```bash
   pip install flask
   ```

2. **Install the QR Code library:**
   Install the necessary generation and image processing packages:
   ```bash
   pip install qrcode[pil]
   ```

3. **Run the application:**
   Launch the local backend server using Python:
   ```bash
   py app.py
   ```

4. **Open in your browser:**
   Copy the local network link generated in your terminal (usually `http://127.0.0`) and paste it into your web browser.

5. **Generate QR Codes:**
   You can now use the website to generate scannable QR codes using any link or text. To stop the application and exit, press `Ctrl + C` inside your terminal window.
