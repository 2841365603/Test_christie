# coding=utf-8
import pytest
import json
import allure
import random
import yaml
from common.request_utill import RequestTools
from common.test_read_Url import ReadIP , ReadAuthorization , ReadSN
from common.test_read_Intelligent_url import Read_Intelligent_url
from common.test_read_Intelligent_id import Read_intelligent_id


class Test_07_modify_intelligent_info:
    @allure.feature('【需求点】：D007-修改指定定时')
    @allure.story('【正常获取】')
    @allure.severity('normal')
    def test_07_modify_intelligent_info(self):
        ip = ReadIP().Read()
        intelligent_id = Read_intelligent_id().Read()
        urls = Read_Intelligent_url().Read()
        url1 = urls['url07']['url']
        url = ip + url1 + intelligent_id
        auth = ReadAuthorization().Read()
        intelligent_name = "修改定时"
        intelligent_number = random.randint(200000 , 999999)
        intelligent_name = intelligent_name + str(intelligent_number)
        f = [0 , 1 , 2 , 3 , 4 , 5 , 6]
        num = random.randint(1, 7)
        week_list = random.sample(f , num)
        data = {
            "name" : intelligent_name ,
            "conditionsRelation" : "and" ,
            "condition" : [
                {
                    "type" : "timing" ,
                    "params" : {
                        "weekdays" : week_list ,
                        "time" : "08:33:00" ,
                        "timeZone" : "America/New_York"
                    }
                }
            ]
        }
        headers = {
            'Authorization' : auth ,
        }
        method = 'patch'
        # 发送请求
        res = RequestTools().send_requests(method=method , url=url , header=headers , data=data)
        message = res['message']
        assert "Success" == message