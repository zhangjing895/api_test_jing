'''用户登录测试'''
import json
import requests
import unittest
import sys
sys.path.append("..")  # 提升包搜索路径到项目路径
from config import config as cf
from lib.read_excel import read_excel

class TestUserLogin(unittest.TestCase):
    def test_user_login_normal(self):
        case_data = get_case_data("test_user_data.xlsx","TestUserLogin",'test_user_login_normal')
        url = case_data[1]
        data=case_data[3]
        expect_res = case_data[4]
        data_dict = json.loads(data)
        res = requests.post(url=url,data=data_dict)
        self.assertEqual(expect_res,res.text)