#coding=utf-8
import requests
import json

class RequestTools():
    '''
    功能：封装requests各种方法
    '''
    # get方法封装
    def get_method(self,url,data=None,header=None):
        if header is not None:
           res = requests.get(url,params=data,headers=header)
        else:
           res = requests.get(url,params=data)
        return res.json()

    # post方法封装
    def post_method(self, url, data=None, header=None):
        # global res
        if header is not None:
            res = requests.post(url, json=data, headers=header)
        else:
            res = requests.post(url, json=data)
        if str(res) == "":
            return res.json()
        else:
            return res.text

    # patch
    def patch_method(self,url,data=None,header=None):
         if header is not None:
            res = requests.patch(url,json=data,headers=header)
         else:
            res = requests.patch(url, json=data)
         return res.json()

    # put方法封装
    def put_method(self,url,data=None,header=None):
         if header is not None:
            res = requests.put(url,json=data,headers=header)
         else:
            res = requests.delete(url, json=data)
         return res.json()



   # delete方法封装
    def delete_method(self, url, data=None, header=None):
         if header is not None:
            res = requests.delete(url, json=data, headers=header)
         else:
            res = requests.delete(url, json=data)
         return res.json()

# 调用主方法
    def send_requests(self,method,url,data=None,header=None):
          if method == 'get' or method == 'GET':
             res = self.get_method(url,data,header)
          elif method == 'post' or method =='POST':
             res = self.post_method(url,data,header)
          elif method == 'patch' or method == 'PATCH':
             res = self.patch_method(url, data, header)
          elif method == 'delete' or method == 'DELETE':
             res = self.delete_method(url,data,header)
          elif method == 'put' or method == 'PUT':
             res = self.put_method(url,data,header)
          else:
             res = "请求方式有误！"
          res = json.loads(str(res).replace("'", "\""))
          return res




























# import requests
#
# class RequestTolls:
#
#     # def send_request(self,method,headers,url):
#     #     # method = str(method).lower()
#     #     # res = None
#     #     # if method == "get":
#     #     #     res = RequestUtill.send_request(self,method=method,url=url,headers=None)
#     #     # # elif method == "post":
#     #     # #     res = RequestUtill.request(method=method,url=url,headers=None,data=datas,verify=False,**kwargs)
#     #     # # elif method == "put":
#     #     # #     pass
#     #     # # elif method == "patch":
#     #     # #     pass
#     #     # # elif method == "delete":
#     #     # #     pass
#     #     # else:
#     #     #     pass
#     #     # # print(res)
#     #     # return res
