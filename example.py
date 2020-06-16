import streamlit as st

from webcam import webcam

st.title("Webcam capture component")

st.write("""
- Accesses the user's webcam and displays the video feed in the browser.
- Click the "Capture Frame" button to grab the current video frame and
return it to Streamlit.
""")
image = webcam(video=True, audio=False)
if image is None:
    st.write("Waiting for capture...")
else:
    st.write("Got an image from the webcam:")
    st.image(image)

