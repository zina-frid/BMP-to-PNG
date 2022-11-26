import os

import requests
from PIL import Image


class Converter:

    def __init__(self, type_way, path_link, one_many, re_value, conv_from, conv_to):
        self.type_way = type_way
        self.path_link = path_link
        self.one_many = one_many
        self.re_value = re_value
        self.conv_from = conv_from
        self.conv_to = conv_to

    def convert(self):
        if self.type_way == 'u':
            self.url_image()
        if self.type_way == 't':
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
        img.save(new_dir + "." + self.conv_to)
        print("Изображение сохранено!")

    def convert_many(self):
        images_list = list(filter(lambda x: x.endswith(self.conv_from), os.listdir(self.path_link)))
        new_dir = self.path_link + "/converted/"
        if not os.path.exists(new_dir):
            os.mkdir(new_dir)
        for image in images_list:
            img = Image.open(self.path_link + "/" + image)
            if self.re_value != -1:
                img = self.resize_image(img)
            img.save(new_dir + image[:image.find('.')] + "." + self.conv_to)
        print("Изображения сохранены в папке converted!")

    def url_image(self):
        re = requests.get(self.path_link, stream=True).raw
        img = Image.open(re)
        print("Введите путь к папке для сохранения:")
        new_dir = ""
        while 1:
            new_dir = input()
            if os.path.exists(new_dir):
                if os.path.isdir(new_dir):
                    break
                else:
                    print("Укажите путь только до папки:")
            else:
                print("Путь не найден! Введите существующий путь:")
        if self.re_value != -1:
            img = self.resize_image(img)
        img.save(new_dir + "/new." + self.conv_to)
        print(f"Изображение сохранено в выбранную папку c именем new.{self.conv_to}!")
