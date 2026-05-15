from PIL import Image

from .config import IMAGE_WIDTH, IMAGE_HEIGHT
from .counting import GetCountingPhoto
from .ice import GetIce


def main():
    width = IMAGE_WIDTH
    height = IMAGE_HEIGHT

    counting = GetCountingPhoto()
    light_counting, dark_counting = counting.get_photo()

    ice = GetIce()
    ldh = ice.get_img()

    dark = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    light = Image.new("RGBA", (width, height), (255, 255, 255, 0))

    dark.paste(ldh, (0, 50), ldh)
    light.paste(ldh, (0, 50), ldh)

    dark.paste(dark_counting, (500, 400), dark_counting)
    light.paste(light_counting, (500, 400), light_counting)

    dark.save("dark.png")
    light.save("light.png")


if __name__ == "__main__":
    main()
