import os
import requests
from converter import Converter

type_way, one_many, path_link, conv_from, conv_to, re_value = "", "", "", "", "", -1


def url_path():
    global type_way
    print("Если вы хотите выбрать изображение с компьютера, напишите t, если хотите использовать URL, то напишите u. "
          "[t/u]")
    while 1:
        type_way = input().lower()
        if type_way == 't' or type_way == 'u':
            break
        else:
            print("Некорректный ввод! Введите t или u.")


def check_amount_answer():
    global one_many
    print("Вы хотите конвертировать одно изображение? [y/n]")
    while 1:
        one_many = input().lower()
        if one_many == 'y' or one_many == 'n':
            break
        else:
            print("Ошибка ввода! Введите y или n.")


def check_format_path():
    global conv_to, conv_from
    print("Через пробел напишиите два формата: из которого хотите конвертировать и в какой хотите конвертировать. "
          "\nДоступные форматы: bmp, png, jpg")
    while 1:
        try:
            conv_from, conv_to = input().lower().split(" ")
            if (conv_from == "bmp" or conv_from == "png" or conv_from == "jpg") and \
                    (conv_to == "bmp" or conv_to == "png" or conv_to == "jpg"):
                break
            else:
                print("Выберите из доступных форматов. \nДоступные форматы: bmp, png, jpg")
        except Exception:
            print("Введите два формата через пробел. \nДоступные форматы: bmp, png, jpg")


def check_format_link():
    global conv_to
    print("В каком формате хотите сохранить избражение? \nДоступные форматы: bmp, png, jpg")
    while 1:
        conv_to = input().lower()
        if conv_to == "bmp" or conv_to == "png" or conv_to == "jpg":
            break
        else:
            print("Выберите из доступных форматов. \nДоступные форматы: bmp, png, jpg")


def take_and_ckeck_path():
    global path_link
    if type_way == 't':
        if one_many == 'y':
            print("Введите полный путь к изображению, включая его название и расширение:")
            while 1:
                path_link = input()
                if os.path.exists(path_link):
                    if os.path.isfile(path_link):
                        end = os.path.splitext(path_link)[1]
                        if end == "." + conv_from:
                            break
                        else:
                            print("Файл не ссответствует выбранному формату")
                    else:
                        print("Включите в путь название изображения и расширение:")
                else:
                    print("Путь не найден! Введите существующий путь:")

        if one_many == 'n':
            print("Введите полный путь к папке с изображениями:")
            while 1:
                path_link = input()
                if os.path.exists(path_link):
                    if os.path.isdir(path_link):
                        i = 0
                        for file in os.listdir(path_link):
                            if file.endswith("." + conv_from):
                                i += 1
                        if i == 0:
                            print("Файлов с выбранным расширением в заданной папке нет. \nВведите другой путь:")
                        else:
                            break
                    else:
                        print("Укажите путь только до папки:")
                else:
                    print("Путь не найден! Введите существующий путь:")
    if type_way == 'u':
        print("Введите ссылку на изображение:")
        while 1:
            path_link = input()
            try:
                check = requests.head(path_link)
                if str(check) == "<Response [200]>":
                    break
                else:
                    print("Введите корректную ссылку")
            except Exception:
                print("Введите корректную ссылку")


def check_resize():
    global re_value
    print("Хотите изменить размер изображения? [y/n]")
    while 1:
        resize = input()
        if resize == 'y':
            print("Введите желаемый процент сжатия/расширения > 0. Например, 50 или 200")
            while 1:
                try:
                    re_value = int(input())
                    if re_value < 0:
                        print("Введите число > 0")
                    else:
                        break
                except Exception:
                    print("Введите число > 0")
            break
        elif resize == 'n':
            break
        else:
            print("Ошибка ввода! Введите y или n.")


if __name__ == '__main__':
    url_path()
    if type_way == 't':
        check_amount_answer()
        check_format_path()
    else:
        check_format_link()
    take_and_ckeck_path()
    check_resize()

    converter = Converter(type_way, path_link, one_many, re_value, conv_from, conv_to)
    converter.convert()
