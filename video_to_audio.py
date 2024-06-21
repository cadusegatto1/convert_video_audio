# pip install
import moviepy.editor

video = moviepy.editor.VideoFileClip('video1.mp4')

audio = video.audio
audio.write_audiofile('audio_name.mp3')
