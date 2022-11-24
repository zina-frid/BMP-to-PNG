from converter import Converter


if __name__ == '__main__':
    print("Вы хотите конвертировать одно изображение? [y/n]")
    one_many = input()
    if one_many == 'y':
        print("Введите полный путь к изображению, включая его название и расширение:")
    if one_many == 'n':
        print("Введите полный путь к папке с изображениями:")
    path_link = input()

    print("В какой формат вы хотите конвертировать: png или jpg? [png/jpg]")
    conv_to = input()

    re_value = -1
    print("Хотите изменить размер изображения? [y/n]")
    resize = input()
    if resize == 'y':
        print("Введите желаемый процент сжатия/расширения. Например, 50 или 200")
        re_value = int(input())

    converter = Converter(path_link, one_many, re_value, conv_to)
    converter.convert()
