# coding=utf-8
import pytest
import json
import allure
import random
from common.request_utill import RequestTools
from common.test_read_Url import ReadIP, ReadAuthorization, ReadSN
from common.test_read_Group_url import Read_Group_url
from common.test_read_Group_id import Read_Group_id


class Test_04_modify_Target_Group_info:
    @allure.feature('【需求点】：B004-修改指定分组')
    @allure.story('【正常获取】')
    @allure.severity('normal')
    def test_04_modify_Target_Group(self):
        group_id = Read_Group_id().Read()
        ip = ReadIP().Read()
        urls = Read_Group_url().Read()
        url1 = urls['url04']['url']
        url = ip + url1 + group_id
        auth = ReadAuthorization().Read()
        group_name = "修改测试分组"
        group_number1 = random.randint(100000 , 999999)
        group_name = group_name + str(group_number1)
        picture_list = [
            0 ,
            1 ,
            2 ,
            7 ,
            15
        ]
        picture = random.choice(picture_list)
        picture = str(picture)
        icon_number = "/groups/imgs/x.png"
        icon_number = icon_number.replace('x' , picture)
        data = {
            "name" : group_name ,
            "icon" : icon_number
        }
        headers = {
            'Authorization' : auth ,
        }
        method1 = 'PATCH'
        # 发送请求
        res = RequestTools().send_requests(method=method1 , url=url , header=headers , data=data)
        # 断言返回message为Success
        assert res['message'] == "Success"






