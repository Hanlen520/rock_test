# coding=utf-8
import time
import unittest
from BearSki.core import Ski
from BearSki.core import DT
import logging

class TestLogin(unittest.TestCase,Ski):

    def setUp(self):
        self.logger=logging.getLogger("TestLogin")
    def tearDown(self):
        pass

    @Ski.case()
    def test_login(self):
        self.logger.info("in login")
        self.logger.info(DT.excel("login.admin"))
        res=self.step("login",DT.excel("login.admin")['detail'])
        self.assertEqual(200,res.result.status_code)
        self.logger.info("login res {0}".format(res))