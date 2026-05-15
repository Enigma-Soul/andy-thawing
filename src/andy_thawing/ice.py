from datetime import datetime

from PIL import Image

from andy_thawing.config import SPRING_FESTIVAL, ICE_TOP_MARGIN, ICE_BOTTOM_MARGIN
from andy_thawing.resources import img_path


class GetIce:
    def get_percent(self):
        spring_festival = datetime(*SPRING_FESTIVAL)
        now = datetime.now()
        left = spring_festival - now
        percent = left.total_seconds() / (60 * 60 * 24 * 365)
        if percent < 0:
            percent = 0
        if percent > 1:
            percent = 1
        percent = float(format(percent, '.5f'))
        return percent

    def get_img(self):
        percent = self.get_percent()

        ice = Image.open(img_path("ice.png"))
        bg_ice = Image.open(img_path("bg_ice.png"))
        ldh = Image.open(img_path("ldh.png"))
        img = Image.new("RGBA", (ldh.width, ldh.height), (255, 255, 255, 0))

        if percent > 0:
            h = ice.height - int((ice.height - ICE_TOP_MARGIN - ICE_BOTTOM_MARGIN) * percent + ICE_BOTTOM_MARGIN + ICE_BOTTOM_MARGIN)
            t = bg_ice.crop((0, h, bg_ice.width, bg_ice.height))
            img.paste(t, (0, h), t)
            img.paste(ldh, (0, 0), ldh)
            t = ice.crop((0, h, ice.width, ice.height))
            img.paste(t, (0, h), t)
        else:
            img.paste(ldh, (0, 0), ldh)
        return img
