from playsound import playsound
import os

class SoundManager:
    def __init__(self, board):
        self.sound_dir = os.path.join(os.path.dirname(__file__), "sounds")
        self.move_sound = os.path.join(self.sound_dir, "move.mp3")

    def play_move_sound(self):
        try:
            playsound(self.move_sound)
        except:
            # Silently fail if sound can't be played
            pass 