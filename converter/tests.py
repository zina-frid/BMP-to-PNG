import unittest
import main
from converter import Converter
import requests
from PIL import Image


class ConverterTestCase(unittest.TestCase):
    def test_resize_smaller(self):
        link = "https://www.meme-arsenal.com/memes/45ce59fd730bafa6ed37b54f8ea7e705.jpg"
        re_value = 40
        conv = Converter('u', link, 'y', re_value, "jpg", "bmp")
        img_1 = Image.open(requests.get(link, stream=True).raw)
        height_1, width_1 = img_1.size
        height_1, width_1 = int(height_1 * re_value / 100), int(width_1 * re_value / 100)
        img_2 = conv.resize_image(img_1)
        height_2, width_2 = img_2.size
        self.assertTupleEqual((height_1, width_1), (height_2, width_2))

    def test_resize_bigger(self):
        link = "https://www.meme-arsenal.com/memes/ea8a7c37f66285b5639ae77f046c90e8.jpg"
        re_value = 200
        conv = Converter('u', link, 'y', re_value, "jpg", "png")
        img_3 = Image.open(requests.get(link, stream=True).raw)
        height_3, width_3 = img_3.size
        height_3, width_3 = int(height_3 * re_value / 100), int(width_3 * re_value / 100)
        img_4 = conv.resize_image(img_3)
        height_4, width_4 = img_4.size
        self.assertTupleEqual((height_3, width_3), (height_4, width_4))

    def test_check_url_path(self):
        self.assertTrue(main.check_url_path('u'))
        self.assertTrue(main.check_url_path('t'))
        self.assertFalse(main.check_url_path('ok'))
        self.assertFalse(main.check_url_path('5'))
        self.assertFalse(main.check_url_path('bmp'))

    def test_check_amount_answer(self):
        self.assertTrue(main.check_amount_answer('y'))
        self.assertTrue(main.check_amount_answer('n'))
        self.assertFalse(main.check_amount_answer('ok'))
        self.assertFalse(main.check_amount_answer(''))
        self.assertFalse(main.check_amount_answer('-'))

    def test_check_format(self):
        self.assertTrue(main.check_format("bmp", "png"))
        self.assertTrue(main.check_format("jpg", "bmp"))
        self.assertTrue(main.check_format("png", "jpg"))
        self.assertFalse(main.check_format("", ""))
        self.assertFalse(main.check_format("", "png"))
        self.assertFalse(main.check_format("jpg", ""))
        self.assertFalse(main.check_format("8", "10"))


if __name__ == '__main__':
    unittest.main()
