import streamlit as st
import os
from pydub import AudioSegment
import io

# Function to compress audio
def compress_audio(input_file, bitrate='64k'):
    audio = AudioSegment.from_file(input_file)
    compressed_audio = audio.set_frame_rate(44100).set_channels(1)
    output_buffer = io.BytesIO()
    compressed_audio.export(output_buffer, format='mp3', bitrate=bitrate)
    return output_buffer.getvalue()


page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
background-color: rgba(255,244,218,1);
background-size: cover
}
</style>
"""

# Define page for audio compression
def audio_compression():

    st.title("AUDIO CILIK")

    st.write("""
    ### Bitrate
    """)
    audio_bitrate = st.selectbox("Pilih bitrate", ["64k", "128k", "192k", "256k", "320k"])
    
    
    # File upload - audio
    audio_file = st.file_uploader("Pilih file", type=["mp3", "wav"])
    
    if audio_file is not None:
        st.audio(audio_file, format='audio/mp3', start_time=0)
        st.write("Uploaded Audio File Details:")
        audio_details = {"Filename":audio_file.name,"FileType":audio_file.type,"FileSize":audio_file.size}
        st.write(audio_details)
        
        # Compress audio button
        if st.button("Mulai Kompres"):
            st.write("Sedang mengompres...")
            compressed_audio = compress_audio(audio_file, bitrate=audio_bitrate)
            st.success("Kompres Berhasil!")
            
            # Download button for compressed audio
            st.write("### Unduh Hasil Kompres")
            audio_download_button_str = f"Unduh Hasil Kompres ({os.path.splitext(audio_file.name)[0]}_compressed.mp3)"
            st.download_button(label=audio_download_button_str, data=compressed_audio, file_name=f"{os.path.splitext(audio_file.name)[0]}_compressed.mp3", mime="audio/mpeg", key=None)
    

# Run the app
if __name__ == '__main__':
    audio_compression()
    st.markdown(page_bg_img, unsafe_allow_html=True)
    st.write("Created by Handal Khomsyat - 121705061")
