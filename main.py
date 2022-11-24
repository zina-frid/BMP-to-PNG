from converter import Converter


if __name__ == '__main__':
    print("Введите путь к изображению:")
    path_link = input()
    converter = Converter(path_link)
    converter.convert()
