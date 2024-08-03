import ffmpeg
from pathlib import Path
import os
def adjust_playback_speed(input_audio, output_audio, speed=1.25):
    """
    Adjusts the playback speed of an audio file using ffmpeg.

    Args:
    - input_audio: Path to the input audio file.
    - output_audio: Path to the output audio file.
    - speed: Playback speed adjustment factor.
    """
    # Construct ffmpeg command for adjusting playback speed
    (
        ffmpeg
        .input(os.path.join(input_audio))
        .filter('atempo', speed)
        .output(output_audio, acodec='libmp3lame', audio_bitrate='192k')  # Use MP3 codec with a high bitrate
        .run(overwrite_output=True)
    )
    print(f'Playback speed adjusted to {speed}x and saved to "{output_audio}"')

    # Clean up temporary file
    
    os.remove(input_audio)

number = 1

adjust_playback_speed(f"mp3/output_{number:03}.mp3, mp3/outputLOL.mp3", 1.25)