from datetime import datetime

from PIL import Image, ImageDraw, ImageFont

from .config import SPRING_FESTIVAL
from .ew2_count import EW2Count
from .resources import font_path


class GetCountingPhoto:
    def __init__(self):
        self.red = (231, 27, 2)
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)

        self.time_unit = ""
        self.left_time = 0

    def get_counting(self):
        spring_festival = datetime(*SPRING_FESTIVAL)
        now = datetime.now()
        left = spring_festival - now

        if left.days <= 0:
            self.time_unit = "a"
            self.left_time = -1
            return None

        months = left.days // 30
        days = left.days
        hours = left.seconds // 3600
        minutes = (left.seconds // 60) % 60

        self.time_unit = ""
        self.left_time = 0

        if months == 0:
            if days == 0:
                if hours == 0:
                    self.time_unit = "min"
                    self.left_time = minutes
                else:
                    self.time_unit = "h"
                    self.left_time = hours
            else:
                self.time_unit = "d"
                self.left_time = days
        else:
            self.time_unit = "m"
            self.left_time = months
        return None

    def get_unit_text(self):
        cn = ""
        en = ""
        if self.time_unit == "m":
            cn = "月"
            en = "MONTHS"
        elif self.time_unit == "d":
            cn = "天"
            en = "DAYS"
        elif self.time_unit == "h":
            cn = "时"
            en = "HOURS"
        elif self.time_unit == "min":
            cn = "分"
            en = "MINUTES"
        else:
            cn = "已解冻"
            en = "THAWED"

        return cn, en

    def get_photo(self):
        self.get_counting()

        if self.time_unit == "a":
            img = Image.new("RGBA", (420, 60), (255, 255, 255, 0))
            font = ImageFont.truetype(str(font_path("text.ttf")), 60)
            draw = ImageDraw.Draw(img)
            draw.text((0, 0), "刘德华已解冻!!", font=font, fill=self.red)
            return img, img

        cn, en = self.get_unit_text()
        ew2 = EW2Count()
        ew2.set_fonts(str(font_path("text.ttf")), str(font_path("number.otf")), str(font_path("number.otf")), 50)
        ew2.set_text(("距刘德华解冻", "还剩"), ("ANDY LAU WILL THAW", f"IN {self.left_time} {en}"), self.left_time, cn)

        # 浅色版
        ew2.set_color(self.red, self.black)
        light = ew2.draw()
        # 深色版
        ew2.set_color(self.red, self.white)
        dark = ew2.draw()

        return light, dark
