from .managers import AudioManager, ImageManager

audioManager = AudioManager("resources/audio")
imageManager = ImageManager("resources/images", "fallback.png")

imageManager.add_resource("tile", "sprites/test-tile.png")