from .manager import ImageManager

images = ImageManager("resources/images", "fallback.png")

sprites = images.sprites
ui = images.ui_components
