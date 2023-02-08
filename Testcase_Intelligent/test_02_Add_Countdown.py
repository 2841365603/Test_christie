# coding=utf-8
import pytest
import json
import allure
import random
import yaml
from common.request_utill import RequestTools
from common.test_read_Url import ReadIP , ReadAuthorization , ReadSN
from common.test_read_Intelligent_url import Read_Intelligent_url


class Test_02_Add_Countdown :
    @allure.feature('【需求点】：D002-新建倒计时')
    @allure.story('【正常获取】')
    @allure.severity('normal')
    def test_02_Add_Countdown(self) :
        ip = ReadIP().Read()
        urls = Read_Intelligent_url().Read()
        url1 = urls['url02']['url']
        url = ip + url1
        auth = ReadAuthorization().Read()
        countdown_name = "新建倒计时"
        countdown_number = random.randint(200000 , 999999)
        countdown_name = countdown_name + str(countdown_number)
        data = {
            "name" : countdown_name ,
            "conditionsRelation" : "and" ,
            "condition" : [
                {
                    "type" : "countdown" ,
                    "params" : {
                        "countdownTime" : 3600
                    }
                }
            ]
        }
        headers = {
            'Authorization' : auth ,
        }
        method = 'post'
        # 发送请求
        res = RequestTools().send_requests(method=method,url=url,header=headers,data=data)
        assert "id" in res
        with open(r"E:\Christie\V10\Test_christie\Testdata\countdown_id.yaml", "w" , encoding='utf-8') as f :
            data = {
                "name":res['id']
            }
            # allow_unicode=True，解决存储时unicode编码问题。
            # sort_keys=False，解决写入yaml的数据则不会排序后写入。
            f.write(yaml.dump(data,allow_unicode=True,sort_keys=False))
