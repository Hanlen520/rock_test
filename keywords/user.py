import json
import logging
from BearSki.CommonData import SkiGlobalData
from driver import d_requests

logger=logging.getLogger("kw.user")
BASE_URL=SkiGlobalData().get_global_data('BASE_URL')

def getUserList(user_name):
  url = '/api/users/'
  headers = {'Content-Type': 'application/json','Authorization': 'Bearer '+SkiGlobalData().get_global_data('jwt_access')[user_name['name']]}
  logger.info('in getUserinfo heasers is :{0}'.format(headers))
  r = d_requests.get(url=BASE_URL+url,headers=headers)    # 最基本的GET请求
  logger.info("response is : {0}".format(r.text))
  return r

def add_user(user_name,body_data):
    url = '/api/users/'
    headers = {'Content-Type': 'application/json','Authorization': 'Bearer '+SkiGlobalData().get_global_data('jwt_access')[user_name['name']] }
    login_user=body_data['detail']
    r = d_requests.post(url=BASE_URL+url,headers=headers,json=login_user)    # 最基本的GET请求
    logger.info("response is : {0}".format(r.text))
    return r

def update_user(user_name,sid,body_data):
    url = '/api/users/{0}/'.format(str(sid))
    headers = {'Content-Type': 'application/json','Authorization': 'Bearer '+SkiGlobalData().get_global_data('jwt_access')[user_name['name']] }
    login_user=body_data['detail']
    r = d_requests.put(url=BASE_URL+url,headers=headers,json=login_user)    # 最基本的GET请求
    logger.info("response is : {0}".format(r.text))
    return r

def delete_user(user_name,sid):
    url = '/api/users/{0}/'.format(str(sid))
    headers = {'Content-Type': 'application/json','Authorization': 'Bearer '+SkiGlobalData().get_global_data('jwt_access')[user_name['name']] }
    r = d_requests.delete(url=BASE_URL+url,headers=headers)    # 最基本的GET请求
    logger.info("response is : {0}".format(r.text))
    return r

def read_user(user_name,sid):
    url = '/api/users/{0}/'.format(str(sid))
    headers = {'Content-Type': 'application/json','Authorization': 'Bearer '+SkiGlobalData().get_global_data('jwt_access')[user_name['name']]}
    r = d_requests.get(url=BASE_URL+url,headers=headers)    # 最基本的GET请求
    logger.info("response is : {0}".format(r.text))
    return r


