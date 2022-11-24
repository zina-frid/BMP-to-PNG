import os
from PIL import Image


class Converter:

    def __init__(self, path_link, answer):
        self.path_link = path_link
        self.answer = answer

    def convert(self):
        if self.answer == 'y':
            img = Image.open(self.path_link)
            new_dir = self.path_link[:self.path_link.rfind('.')]
            img.save(new_dir + ".png")
            print("Изображение сохранено!")
        else:
            images_list = list(filter(lambda x: x.endswith('.bmp'), os.listdir(self.path_link)))
            new_dir = self.path_link + "/converted/"
            if not os.path.exists(new_dir):
                os.mkdir(new_dir)

            for image in images_list:
                img = Image.open(self.path_link + "/" + image)
                img.save(new_dir + image[:image.find('.')] + ".png")
            print("Изображения сохранены в папке converted!")
