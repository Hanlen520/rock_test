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
    def test_user_basecase(self):

        self.logger.info("开始测试 test_user_basecase")
        role_user={'name':'admin'}
        user_data=DT("users.oneuser").json()
        self.logger.info("获取待替新增用户数据: {0}".format(user_data))

        self.logger.info("Step1: 新建用户")
        step1_res=self.step("getCreateUser",role_user,user_data)
        self.assertEqual(201,step1_res.result.status_code)
        print(step1_res)
        user_id=json.loads(step1_res.result.text)['detail']['id']

        self.logger.info("Step2: 查询新建用户信息")
        step2_res=self.step("getOneUser",role_user,user_id)
        self.assertEqual(200,step2_res.result.status_code)

        update_name="test987"
        user_data['detail']['name']=update_name
        self.logger.info("Step3: 修改用户 修改信息{0}".format(user_data))

        step3_res=self.step("getUpdataUser",role_user,user_id,user_data)
        self.assertEqual(200,step3_res.result.status_code)

        self.logger.info("Step4: 查询修改用户信息")
        step4_res=self.step("getOneUser",role_user,user_id)
        self.assertEqual(200,step4_res.result.status_code)
        read_name=json.loads(step4_res.result.text)['name']
        self.assertEqual(read_name,update_name)

        self.logger.info("Step5: 删除用户")
        step5_res=self.step("getDeleteUser",role_user,user_id)
        self.assertEqual(204,step5_res.result.status_code)

        self.logger.info("Step6: 查询删除用户信息")
        step6_res=self.step("getOneUser",role_user,user_id)
        self.assertEqual(404,step6_res.result.status_code)
       
   
