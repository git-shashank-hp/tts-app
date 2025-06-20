import streamlit as st
from gtts import gTTS
import socket
import os

# --- Config ---
st.set_page_config(layout="wide")

# --- Style ---
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Nunito+Sans&display=swap');
    html, body, [class*="css"] {
        font-family: 'Nunito Sans', sans-serif !important;
    }
    .block-container {
        padding-top: 3rem;
    }
    .custom-text-label {
        font-size: 28px;
        font-weight: bold;
        color: #000000;
        margin-bottom: 8px;
    }
    [data-testid="stTextArea"] textarea {
        font-weight: bold !important;
        color: white !important;
        background-color: #5378b3 !important;
        border-radius: 0px;
        padding: 25px;
        font-size: 18px;
    }
    div[data-baseweb="select"] > div {
        background-color: #5378b3 !important;
        border-radius: 10px !important;
        color: white !important;
        border: none !important;
    }
    div.stButton > button {
        background-color: #5378b3 !important;
        color: white !important;
        font-weight: bold !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 0.5rem 1.5rem !important;
        font-size: 16px !important;
        width: 100%;
        transition: background-color 0.3s ease;
    }
    div.stButton > button:hover {
        background-color: #405f91 !important;
        cursor: pointer;
    }
    div.stDownloadButton > button {
        background-color: #4CAF50 !important;
        color: white !important;
        font-weight: bold !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 0.5rem 1.5rem !important;
        font-size: 16px !important;
        width: 100%;
        margin-top: 10px;
        transition: background-color 0.3s ease;
    }
    div.stDownloadButton > button:hover {
        background-color: #388E3C !important;
        cursor: pointer;
    }
    .equal-row {
        display: flex;
        align-items: center;
        gap: 1rem;
    }
    .equal-row .st-audio {
        flex: 1;  /* make audio take available width */
    }
    .equal-row .stDownloadButton > button {
        height: 52px !important;  /* Match audio control height */
        min-width: 160px;
        background-color: #4CAF50 !important;
        color: white !important;
        font-weight: bold;
        border-radius: 10px;
        border: none;
        font-size: 16px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- Accent options ---
accent_options = {
    "India": "co.in",
    "Australia": "com.au",
    "United Kingdom": "co.uk",
    "United States": "us",
    "Canada": "ca",
    "Ireland": "ie",
    "South Africa": "co.za",
    "Nigeria": "com.ng",
}

# --- Utility Functions ---

def internet_available(host="8.8.8.8", port=53, timeout=3):
    """Check if internet connection is available."""
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except Exception:
        return False


@st.cache_data(show_spinner=False)
def generate_tts_audio(text: str, tld: str) -> bytes:
    """Generate speech audio bytes from text and accent."""
    tts = gTTS(text=text, lang="en", tld=tld, slow=False)
    audio_path = "output.mp3"
    tts.save(audio_path)
    with open(audio_path, "rb") as f:
        audio_bytes = f.read()
    # Clean up saved file (optional)
    try:
        os.remove(audio_path)
    except Exception:
        pass
    return audio_bytes

# --- Main App UI ---

def main():  
    with st.container():
        col_logo, col_title, col_accent = st.columns([1, 7, 2])

        with col_logo:
            logo_path = "assets/logo.png"
            if os.path.exists(logo_path):
                st.image(logo_path, width=150)
            else:
                st.warning("Logo not found at 'assets/logo.png'.")

        with col_title:
            st.title("English : Text to Speech with Accents")

        with col_accent:
            st.markdown('<div class="custom-text-label">Accent</div>', unsafe_allow_html=True)
            selected_accent = st.selectbox(
                "", options=list(accent_options.keys()), label_visibility="collapsed"
            )
            tld = accent_options[selected_accent]


    # Input text area
    st.markdown(
        '<div class="custom-text-label">Enter text to convert to speech:</div>',
        unsafe_allow_html=True,
    )
    default_text = (
        "Welcome to the Stramlit Audio Experience. "
        "Developed by Shashank to assist the creative design team in voice-over editing."
    )
    text = st.text_area(
        label="",
        value=default_text,
        height=250,
        label_visibility="collapsed",
    )

    # Convert button aligned right
    col1, col2 = st.columns([8, 2])
    with col2:
        convert_clicked = st.button("Convert to Speech")

    if convert_clicked:
        if not internet_available():
            st.error("Internet connection required for text-to-speech conversion.")
            return
        if text.strip() == "":
            st.error("Please enter some text.")
            return

        try:
            audio_bytes = generate_tts_audio(text, tld)
        except Exception as e:
            st.error(f"Failed to generate audio: {e}")
            return

        # Display audio player and download button side by side
        col_audio, col_button = st.columns([8, 2], gap="small", vertical_alignment="bottom")

        with col_audio:
            st.audio(audio_bytes, format="audio/mp3")

        with col_button:
            st.download_button(
                label="Download Audio",
                data=audio_bytes,
                file_name="output.mp3",
                mime="audio/mp3",
            )

    st.markdown("---")  # Horizontal separator

    # Footer with author and Streamlit link
    col_left, col_right = st.columns([8, 2])

    with col_left:
        st.markdown("**Built by Shashank H P**", unsafe_allow_html=True)

    with col_right:
        st.markdown(
            '<div style="text-align: right;">Powered by '
            '<a href="https://streamlit.io" target="_blank" '
            'style="color: #5378b3; font-weight: bold; text-decoration: none;">Streamlit</a></div>',
            unsafe_allow_html=True,
        )

if __name__ == "__main__":
    main()
