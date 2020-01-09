# coding=utf-8
import time
import unittest
from BearSki.base import Ski
import logging

class TestLogin(unittest.TestCase,Ski):

    def setUp(self):
        self.logger=logging.getLogger("TestLogin")
    def tearDown(self):
        pass
    @Ski.case()
    def test_login(self):
        self.logger.info("in login")
        res=self.step("login",{"username": "admin","password": "admin@1234"})
        self.assertEqual(200,res.result.status_code)
        self.logger.info("login res {0}".format(res))