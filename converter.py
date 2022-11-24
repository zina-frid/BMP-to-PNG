import os
from PIL import Image


class Converter:

    def __init__(self, path_link, one_many, re_value):
        self.path_link = path_link
        self.one_many = one_many
        self.re_value = re_value

    def convert(self):
        if self.one_many == 'y':
            self.convert_one()
        else:
            self.convert_many()

    def resize_image(self, img):
        height, width = img.size
        height, width = int(height * self.re_value / 100), int(width * self.re_value / 100)
        img = img.resize((height, width))
        return img

    def convert_one(self):
        img = Image.open(self.path_link)
        new_dir = self.path_link[:self.path_link.rfind('.')]
        if self.re_value != -1:
            img = self.resize_image(img)
        img.save(new_dir + ".png")
        print("Изображение сохранено!")

    def convert_many(self):
        images_list = list(filter(lambda x: x.endswith('.bmp'), os.listdir(self.path_link)))
        new_dir = self.path_link + "/converted/"
        if not os.path.exists(new_dir):
            os.mkdir(new_dir)
        for image in images_list:
            img = Image.open(self.path_link + "/" + image)
            if self.re_value != -1:
                img = self.resize_image(img)
            img.save(new_dir + image[:image.find('.')] + ".png")
        print("Изображения сохранены в папке converted!")