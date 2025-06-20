# 🗣️ English Text-to-Speech Web App with Accents

This Streamlit application allows users to input English text and convert it into speech using Google's Text-to-Speech engine (`gTTS`). The app supports multiple English accents including Indian, British, American, Australian, and more.

---

## 🚀 Features

- ✅ Text-to-Speech conversion using **Google Text-to-Speech (gTTS)**
- ✅ Supports **8 English accents** from different regions
- ✅ **Audio playback** and **MP3 download** functionality
- ✅ Custom **UI styling** with a responsive layout
- ✅ **Offline check** to notify if internet is unavailable
- ✅ Designed for internal creative/voice-over workflows

---

## 🧱 Tech Stack

- [Streamlit](https://streamlit.io/) — Web UI
- [gTTS (Google Text-to-Speech)](https://pypi.org/project/gTTS/) — Speech synthesis
- Python standard libraries (`os`, `socket`) — File handling and internet check

---

## 📁 Folder Structure

project/
│
├── app.py                # Main Streamlit app
├── requirements.txt      # Python dependencies
└── assets/
    └── logo.png          # Optional logo image


## 🖥️ How to Run Locally

### 1. Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/your-username/text-to-speech-app.git
cd text-to-speech-app
```
### 2. Create a Virtual Environment (Optional but Recommended)

It's good practice to use a virtual environment to manage your project's dependencies.

### 🖥️ For macOS/Linux:
```bash
python -m venv venv
source venv/bin/activate
```
### 3. Install Dependencies

After activating your virtual environment, install the required packages:

```bash
pip install -r requirements.txt
```
### 4. Run the App

Start the Streamlit application by running:

```bash
streamlit run app.py
```


## 🌐 Deployment

### Option 1: Streamlit Cloud

1. Push the app to a **public GitHub repository**.
2. Log in to [Streamlit Cloud](https://streamlit.io/cloud) using your GitHub account.
3. Click on **"New app"** and select your repository.
4. Set `app.py` as the **entry point** for your application.
5. Once deployed, your app will be accessible at a `.streamlit.app` URL.

> 💡 Make sure all required dependencies are listed in a `requirements.txt` file in your repository.

## 🌍 Supported Accents

| Country         | Accent Code (tld) |
|-----------------|-------------------|
| India           | co.in             |
| Australia       | com.au            |
| United Kingdom  | co.uk             |
| United States   | us                |
| Canada          | ca                |
| Ireland         | ie                |
| South Africa    | co.za             |
| Nigeria         | com.ng            |


## 📌 Notes

- An internet connection is required for the gTTS API to work.
- gTTS does **not** support true offline conversion.
- The `tld` option influences the accent via the regional Google endpoint.

## 📷 UI Preview (Optional)

_Add screenshots of the app in use here._

---

## 🙋‍♂️ Developed By

**Shashank H P**

*"Built to support the creative design team in voice-over editing."*

---

## 📜 License

This project is open-source. You may use and adapt it freely for personal or educational use. For commercial use, please review the gTTS and Google TTS API terms.
