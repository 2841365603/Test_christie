# coding=utf-8
import pytest
import json
import allure
import random
import yaml
from common.request_utill import RequestTools
from common.test_read_Url import ReadIP , ReadAuthorization , ReadSN
from common.test_read_Intelligent_url import Read_Intelligent_url


class Test_03_Add_intelligent :
    @allure.feature('【需求点】：D003-新建定时')
    @allure.story('【正常获取】')
    @allure.severity('normal')
    def test_03_Add_intelligent(self) :
        ip = ReadIP().Read()
        urls = Read_Intelligent_url().Read()
        url1 = urls['url03']['url']
        url = ip + url1
        auth = ReadAuthorization().Read()
        intelligent_name = "新建定时"
        intelligent_number = random.randint(200000,999999)
        intelligent_name = intelligent_name + str(intelligent_number)
        f = [0,1,2,3,4,5,6]
        num = random.randint(1,7)
        week_list =  random.sample(f,num)
        data = {
            "name" : intelligent_name ,
            "conditionsRelation" : "and" ,
            "condition" : [
                {
                    "type" : "timing" ,
                    "params" : {
                        "weekdays" : week_list,
                        "time" : "07:33:00" ,
                        "timeZone" : "America/New_York"
                    }
                }
            ]
        }
        headers = {
            'Authorization' : auth ,
        }
        method = 'post'
        # 发送请求
        res = RequestTools().send_requests(method=method , url=url , header=headers , data=data)
        assert "id" in res
        with open(r"E:\Christie\V10\Test_christie\Testdata\Intelligent_id.yaml" , "w" , encoding='utf-8') as f :
            data = {
                "name" : res['id']
            }
            # allow_unicode=True，解决存储时unicode编码问题。
            # sort_keys=False，解决写入yaml的数据则不会排序后写入。
            f.write(yaml.dump(data,allow_unicode=True,sort_keys=False))
