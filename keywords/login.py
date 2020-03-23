import json
import logging
from BearSki.CommonData import SkiGlobalData
from driver import d_requests

logger=logging.getLogger("kw.login")
BASE_URL=SkiGlobalData().get_global_data('BASE_URL')

# 提供通过用户名获取jwt的接口信息方法，获取后的认证字符串放在 SkiGlobalData 全局变量中
def login(body_data):
    url = BASE_URL+'/auth/login/'
    headers = {'Content-Type': 'application/json'}
    logger.info('in login！body_data is {0}'.format(body_data))
    logger.info('ask url is {0}'.format(url))
    login_user=body_data
    r = d_requests.post(url=url,headers=headers,json=login_user)    # 最基本的GET请求
    logger.info("response is : {0}".format(r))
    logger.info("response is : {0}".format(r.text))
    result=json.loads(r.text)
    # global jwt_access
    # jwt_access[login_user['username']]=result['data']['access']
    SkiGlobalData().add_global_data({"jwt_access":{login_user['username']:result['detail']['token']}})
    return r

def web_login(user_data):
  pass




  