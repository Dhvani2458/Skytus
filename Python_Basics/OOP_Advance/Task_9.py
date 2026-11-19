# Create a MusicPlayer class and subclass Spotify to override play method. 
print("\nCreate a MusicPlayer class and subclass Spotify to override play method.")
class MusicPlayer:
    def play(self):
        print("Playing music")


class Spotify(MusicPlayer):
    def play(self):
        print("Playing music from Spotify")


choice = input("Enter player (music/spotify): ").lower()

if choice == "music":
    player = MusicPlayer()
    player.play()

elif choice == "spotify":
    player = Spotify()
    player.play()

else:
    print("Invalid player")
