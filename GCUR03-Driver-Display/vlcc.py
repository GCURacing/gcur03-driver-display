import vlc
import time, os

script_dir = os.path.dirname(os.path.abspath(__file__))
video_path = os.path.join(script_dir, "media", "intro.mp4")
player = vlc.MediaPlayer(video_path)
player.play()
time.sleep(10)  # or wait for player.get_state()