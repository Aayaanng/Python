import streamlit as st
from PIL import Image
import os

# Display image from URL
st.image('https://icon-icons.com/icon/python-logo/168886',
         caption='Python Logo', width=200)

# Display local image file
#img = Image.open('car.png')
#st.image(img, caption='My Photo', use_column_width=True)
IMAGE_FOLDER = r"C:\Users\aayaa\OneDrive\Desktop\rancholabs\streamlit"
IMAGE_NAME = "car.png"
full_path = os.path.join(IMAGE_FOLDER, IMAGE_NAME)
if os.path.exists(full_path):
    st.image(full_path, caption="Your Car Image", use_container_width=True)
# Display multiple images in a row using columns
col1, col2, col3 = st.columns(3)
with col1:
    st.image('image1.jpg', caption='Photo 1')
with col2:
    st.image('image2.jpg', caption='Photo 2')
with col3:
    st.image('image3.jpg', caption='Photo 3')
#videos and images
import streamlit as st

# Embed a YouTube video
st.video('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
# Play a local video file
# video_file = open('my_video.mp4', 'rb')
# st.video(video_file)

# Play audio
# audio_file = open('song.mp3', 'rb')
# st.audio(audio_file, format='audio/mp3')