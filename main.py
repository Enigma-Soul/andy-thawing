from PIL import Image
from datetime import datetime
from library.Counting import GetCountingPhoto


class GetIce:
    def __init__(self,img_path):
        self.spring_festival = (2026, 3, 17)
        self.img_path = img_path

        self.top = 10 #顶部预留像素
        self.bottom = 15 #底部预留像素
    def get_percent(self):
        spring_festival = datetime(self.spring_festival[0], self.spring_festival[1], self.spring_festival[2])
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

        ice = Image.open(self.img_path+"/ice.png")
        ldh = Image.open(self.img_path+"/ldh.png")
        img = Image.new("RGBA", (ldh.width, ldh.height), (255, 255, 255,0))
        img.paste(ldh, (0, 0), ldh)
        if percent > 0:
            t = ice.height - int((ice.height - self.top - self.bottom) * percent + self.bottom + self.bottom)
            cutted = ice.crop((0, t, ice.width, ice.height))
            img.paste(cutted, (0,t), cutted)
        return img





def main():
    weight = 1000
    height = 600

    counting = GetCountingPhoto(r"fonts")
    counting.spring_festival = (2026, 2, 17)
    light_counting, dark_counting = counting.get_photo()

    t = GetIce("./img")
    t.spring_festival = (2026, 2, 17)
    ldh = t.get_img()

    dark = Image.new("RGBA", (weight, height), (0, 0, 0, 0))
    light = Image.new("RGBA", (weight, height), (255, 255, 255, 0))

    dark.paste(ldh, (0, 50), ldh)
    light.paste(ldh, (0, 50), ldh)

    dark.paste(dark_counting,(500,400), dark_counting)
    light.paste(light_counting, (500, 400), light_counting)

    dark.save("dark.png")
    light.save("light.png")

if __name__ == '__main__':
    main()