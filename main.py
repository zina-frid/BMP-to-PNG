from converter import Converter


if __name__ == '__main__':
    print("Вы хотите конвертировать одно изображение? [y/n]")
    answer = input()
    if answer == 'y':
        print("Введите полный путь к изображению, включая его название и расширение:")
    if answer == 'n':
        print("Введите полный путь к папке с изображениями:")
    path_link = input()

    converter = Converter(path_link, answer)
    converter.convert()
    