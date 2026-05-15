from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


class EW2Count:
    def __init__(self):
        self.cn_font = None
        self.en_font = None
        self.number_font = None

        self.red = None
        self.text = None
        self.bg = None

        self.cn_text = None
        self.en_text = None
        self.number = None

    def set_fonts(self, cn_font_path, en_font_path, number_font_path, font_size):
        font_size = abs(font_size)
        self.cn_font = ImageFont.truetype(cn_font_path, font_size)
        self.en_font = ImageFont.truetype(en_font_path, font_size / 2)
        self.number_font = ImageFont.truetype(number_font_path, font_size * 2.5)
        self.font_size = font_size

    def set_color(self, red, text, bg=(0, 0, 0, 0)):
        self.red = red
        self.text = text
        self.bg = bg

    def set_text(self, cn_text, en_text, number, unit):
        self.cn_text = cn_text
        self.en_text = en_text
        self.number = number
        self.unit = unit

    def draw(self):
        def get_size():
            t1 = len(self.cn_text[0]) + len(str(self.number)) * 1.25 + len(self.unit)
            t2 = len(self.cn_text[0]) - len(self.cn_text[1]) + (max(len(self.en_text[0]), len(self.en_text[1])) / 2)
            w = max(t1, t2) * self.font_size
            h = 3 * self.font_size
            return int(w), int(h)

        w, h = get_size()
        img = Image.new('RGBA', (int(w), int(h)), self.bg)
        draw = ImageDraw.Draw(img)
        # 第一行中文
        draw.text((0, 0), self.cn_text[0], self.text, font=self.cn_font)

        deviation = (len(self.cn_text[0]) - len(self.cn_text[1])) * self.font_size

        # 第二行中文
        draw.text((deviation, self.font_size), self.cn_text[1], self.text, font=self.cn_font)
        # 红色线
        draw.rectangle(((deviation * 0.93, self.font_size), (deviation * 0.95, self.font_size * 3)), fill=self.red)
        # 第一行英文
        draw.text((deviation, self.font_size * 2), self.en_text[0], self.text, font=self.en_font)
        # 第二行英文
        draw.text((deviation, self.font_size * 2.5), self.en_text[1], self.text, font=self.en_font)
        # 数字
        draw.text((len(self.cn_text[0]) * self.font_size, -(self.font_size / 2.5)), str(self.number), self.red, font=self.number_font)
        # 单位
        draw.text((len(self.cn_text[0]) * self.font_size + len(str(self.number)) * self.font_size * 1.2, self.font_size), self.unit, self.text, font=self.cn_font)
        return img
