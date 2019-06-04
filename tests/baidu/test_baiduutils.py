from unittest import TestCase
from zwb_ocr.baidu import baiduutils


class BaiduUtilsTest(TestCase):

    def test_init(self):
        pass

    def test_get_access_token(self):
        token = baiduutils.get_access_token("oNQOtegx1gbSA77SrS9a4kFM", "z5nBPshSwZ8PeXEsXl1nbnmOH6hlFjGh")
        print(token)
