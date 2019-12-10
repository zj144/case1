import unittest

import requests

from api.api_login import ApiLogin


class TestLogin(unittest.TestCase):
    session = None
    @classmethod
    def setUp(self):
        self.session = requests.session()
        # 获取apilogin对象
        self.apilogin = ApiLogin(self.session)
    @classmethod
    def tearDownClass(cls):
        cls.session.close()
    def test01_login(self):
        pass
