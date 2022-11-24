from PIL import Image


class Converter:

    def __init__(self, path_link):
        self.path_link = path_link

    def convert(self):
        img = Image.open(self.path_link)
        new_dir = self.path_link[:self.path_link.rfind('.')]
        img.save(new_dir + ".png")
        print("Изображение сохранено!")
