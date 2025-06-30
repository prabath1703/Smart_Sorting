
# 🧠 Smart Sorting: AI-Powered Produce Quality Detection 🍎🥦

Smart Sorting is a deep learning-powered web application that classifies fruits and vegetables as **healthy** or **rotten** using a fine-tuned VGG16 model. Built using Python, Flask, and Keras, this tool simplifies visual food quality inspection with high accuracy and ease of use.

---

## 🚀 Features

- 🔍 Classifies fruits and vegetables into **Healthy** or **Rotten**
- 🧠 Uses Transfer Learning with **VGG16**
- 💻 Clean, user-friendly **web interface**
- ⚡ Fast predictions using `.h5` model
- 🔌 REST API support (`/predict`, `/api/predict`, `/health`)
- 📦 Easily deployable on local servers or cloud

---

## 📂 Project Structure

```
Smart_Sorting/
├── app.py                  # Flask server
├── healthy_vs_rotten.h5    # Trained deep learning model
├── requirements.txt
├── templates/
│   ├── index.html
│   ├── result.html
│   └── blog.html
├── static/
│   └── uploads/
└── README.md
```

---

## 🛠️ Installation & Running

### 1. Clone the repository
```bash
git clone https://github.com/prabath1703/Smart_Sorting.git
cd Smart_Sorting
```

### 2. Create a virtual environment
```bash
python -m venv venv
venv\Scripts\activate      # On Windows
# or
source venv/bin/activate   # On macOS/Linux
```

### 3. Install required packages
```bash
pip install -r requirements.txt
```

### 4. Add your model file
Ensure `healthy_vs_rotten.h5` is in the root directory (same level as `app.py`).

### 5. Run the Flask app
```bash
python app.py
```
Visit `http://127.0.0.1:5000/` in your browser.

---

## 🧪 Model Overview

- 📚 **Base model**: VGG16 (pretrained on ImageNet)
- 🧠 **Custom layers**: Dense, Dropout for final classification
- ⚙️ **Optimizer**: Adam
- 🎯 **Accuracy**: ~99% on validation set

---

## 📲 API Endpoints

| Method | Endpoint         | Description                  |
|--------|------------------|------------------------------|
| GET    | `/`              | Home page with upload form   |
| POST   | `/predict`       | Upload image via form        |
| POST   | `/api/predict`   | Upload image via base64 JSON |
| GET    | `/health`        | Health check (returns OK)    |

---

## 📸 Screenshot

## 📸 Screenshot

![Smart Sorting UI](static/Screenshot.png)


---

## 🔮 Future Improvements

- ✅ Add more fruit/veggie classes
- 🖼️ Add support for webcam/image streams
- 📱 Convert to mobile app or PWA
- 🐳 Dockerize the app for deployment
- 📁 Use Git LFS for `.h5` files >100MB

---

## 👤 Author

- **Damarla Saiprabath**  
- GitHub: [@prabath1703](https://github.com/prabath1703)

---

## 📄 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
