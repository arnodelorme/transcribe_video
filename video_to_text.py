# Video/Audio to text converter
import moviepy.editor as mp
import sys
import whisper
import os

# extract first parameter from command line
if len(sys.argv) < 2:
    print("Usage: python video_to_text.py <file_path>")
    print("Acceptable formats: .mp4, .mov, .mp3, .wav")
    sys.exit(1)

file_path = sys.argv[1]
supported_video_formats = ['.mp4', '.mov']
supported_audio_formats = ['.mp3', '.wav']
file_extension = os.path.splitext(file_path)[1].lower()

if file_extension not in supported_video_formats + supported_audio_formats:
    print("Error: Unsupported file format.")
    print(f"Acceptable formats: {', '.join(supported_video_formats + supported_audio_formats)}")
    sys.exit(1)

# Convert video to mp3 if input is a video file with the same name as the input file    
audio_path = os.path.splitext(file_path)[0] + ".mp3"

# Convert video to mp3 if input is a video file
if file_extension in supported_video_formats:
    print("Converting video to mp3")
    video = mp.VideoFileClip(file_path)
    audio = video.audio
    audio.write_audiofile(audio_path)
    print("Video converted to mp3")
else:
    # If input is already an audio file, use it directly
    audio_path = file_path
    print("Using audio file directly")

# Convert audio to text using whisper and show progress
print("Converting audio to text")
model = whisper.load_model("base")  # tiny, small, medium, large
result = model.transcribe(audio_path, verbose=True)
print("Audio converted to text")

print("Saving text to file")
# Save the text to a file with the same name as the input file
output_path = os.path.splitext(file_path)[0] + ".txt"
with open(output_path, "w") as f:
    f.write(result["text"])
print("Text saved to file")
print(" ")
print("This is the text:")
print(result["text"])

