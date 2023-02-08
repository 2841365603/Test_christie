# coding=utf-8
import pytest
import json
import allure
import random
import yaml
from common.request_utill import RequestTools
from common.test_read_Url import ReadIP , ReadAuthorization , ReadSN
from common.test_read_Intelligent_url import Read_Intelligent_url
from common.test_read_countdown_id import Read_countdown_id


class Test_06_modify_Countdown_info:
    @allure.feature('【需求点】：D006-修改指定倒计时')
    @allure.story('【正常获取】')
    @allure.severity('normal')
    def test_06_modify_Countdown_info(self) :
        ip = ReadIP().Read()
        countdown_id = Read_countdown_id().Read()
        urls = Read_Intelligent_url().Read()
        url1 = urls['url06']['url']
        url = ip + url1 + countdown_id
        auth = ReadAuthorization().Read()
        countdown_name = "修改倒计时"
        countdown_number = random.randint(200000 , 999999)
        countdown_name = countdown_name + str(countdown_number)
        data = {
            "name" : countdown_name ,
            "conditionsRelation" : "and" ,
            "condition" : [
                {
                    "type" : "countdown" ,
                    "params" : {
                        "countdownTime" : 36000
                    }
                }
            ]
        }
        headers = {
            'Authorization' : auth ,
        }
        method = 'patch'
        # 发送请求
        res = RequestTools().send_requests(method=method,url=url,header=headers,data=data)
        message = res['message']
        assert "Success" == message