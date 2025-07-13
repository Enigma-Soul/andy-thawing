from datetime import datetime
from .EW2_Count import *


class GetCountingPhoto:
    def __init__(self,font_path):
        # 中文字体名为text.ttf
        # 英文和数字的字体名为number.otf

        self.red = (231, 27, 2)
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)

        self.time_unit = ""
        self.left_time = 0
        self.font_path = font_path

        self.spring_festival = (2026, 2, 17)

    def get_counting(self):
        spring_festival = datetime(self.spring_festival[0], self.spring_festival[1], self.spring_festival[2])
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
            # 不可能的 ^_^
            cn = "已解冻"
            en = "THAWED"

        return cn, en

    def get_photo(self):
        self.get_counting()

        if self.time_unit == "a":
            img = Image.new("RGBA",(420,60),(255,255,255,0))
            font = ImageFont.truetype(self.font_path+r"\text.ttf", 60)
            draw = ImageDraw.Draw(img)
            draw.text((0,0),"刘德华已解冻!!",font=font,fill=self.red)
            return img,img


        cn,en = self.get_unit_text()
        img = EW2_Count()
        img.set_fonts(self.font_path+r"\text.ttf",self.font_path+r"\number.otf",self.font_path+r"\number.otf",50)
        img.set_text(("距刘德华解冻", "还剩"), ("ANDY LAU WILL THAW", f"IN {self.left_time} {en}"), self.left_time, cn)

        # 浅色版
        img.set_color(self.red, self.black)
        light = img.draw()
        # 深色版
        img.set_color(self.red, self.white)
        dark = img.draw()

        return light,dark

if __name__ == '__main__':
    # 调用示例
    img = GetCountingPhoto(r"..\fonts")
    img.spring_festival = (2026, 2, 17)
    light, dark = img.get_photo()
    light.save("light.png")
    dark.save("dark.png")
