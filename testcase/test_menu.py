import time
import unittest
from BearSki.base import Ski
import logging
from BearSki.base import DT
import json

class TestUsers(unittest.TestCase,Ski):

    def setUp(self):
        self.logger=logging.getLogger("TestUsers")
        self.step("login",{"username": "admin","password": "admin@1234"})

    def tearDown(self):
        pass
    @Ski.case()
    def test_getuserlist(self):
        res=self.step("getUserList",{'name':'admin'})
        self.assertEqual(200,res.result.status_code)


    @Ski.case()
    def test_menu_basecase(self):
        self.logger.info("开始测试 test_menu_basecase")
        role_user = {'name': 'admin'}
        user_data = DT("menus.onemenu").json()
        self.logger.info("获取待替新增菜单数据: {0}".format(user_data))

        self.logger.info("Step1: 新建菜单")
        step1_res=self.step("getCreateMenu",role_user,user_data)
        self.assertEqual(201,step1_res.result.status_code)
        mune_id = json.loads(step1_res.result.text)['id']

        self.logger.info("Step2: 查询新建菜单信息")
        step2_res=self.step("getOneMenu",role_user,mune_id)
        self.assertEqual(200,step2_res.result.status_code)

        update_name="test988"
        user_data['detail']['name']=update_name
        self.logger.info("Step3: 修改菜单 修改信息{0}".format(user_data))
        step3_res = self.step("getUpdataMenu", role_user, mune_id, user_data)
        self.assertEqual(200, step3_res.result.status_code)

        self.logger.info("Step4: 查询修改菜单信息")
        step4_res = self.step("getOneMenu", role_user, mune_id)
        self.assertEqual(200, step4_res.result.status_code)
        read_name = json.loads(step4_res.result.text)['name']
        self.assertEqual(read_name, update_name)

        self.logger.info("Step5: 菜单")
        step5_res = self.step("getDeleteMenu", role_user, mune_id)
        self.assertEqual(204, step5_res.result.status_code)

        self.logger.info("Step6: 查询删除菜单信息")
        step6_res = self.step("getOneUser", role_user, mune_id)
        self.assertEqual(404, step6_res.result.status_code)