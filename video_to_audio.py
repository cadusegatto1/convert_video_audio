# pip install
import moviepy.editor

# 🎥 Read video file
video = moviepy.editor.VideoFileClip('video1.mp4')

# 🔄 Convert video data to audio
audio = video.audio

# 💾 Save audio file
audio.write_audiofile('audio_name.mp3')
