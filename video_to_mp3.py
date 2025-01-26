# Video to mp3
import moviepy.editor as mp
import sys
import whisper

# extract first parameter from command line
if len(sys.argv) < 2:
    print("Usage: python video_to_mp3.py <video_path>")
    print("Acceptable formats: .mp4, .mov")
    sys.exit(1)

video_path = sys.argv[1]
if not (video_path.endswith('.mp4') or video_path.endswith('.mov')):
    print("Error: Unsupported file format. Acceptable formats: .mp4, .mov")
    sys.exit(1)

# convert video to mp3
print("Converting video to mp3")
video = mp.VideoFileClip(video_path)
audio = video.audio
audio.write_audiofile("audio.mp3")
print("Video converted to mp3")

# Convert mp3 to text using whisper and show progress
print("Converting mp3 to text")
model = whisper.load_model("base") # tiny, small, medium, large
result = model.transcribe("audio.mp3", verbose=True)
print("Mp3 converted to text")

print("Saving text to file")
# Save the text to a file with the same name as the video file
with open(video_path.replace(".mp4", ".txt"), "w") as f:
    f.write(result["text"])
print("Text saved to file")
print(" ")
print("This is the text:")
print(result["text"])
