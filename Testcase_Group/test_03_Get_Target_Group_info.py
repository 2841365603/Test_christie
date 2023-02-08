# coding=utf-8
# import pytest
import json
import allure
import random
from common.request_utill import RequestTools
from common.test_read_Url import ReadIP, ReadAuthorization, ReadSN
from common.test_read_Group_url import Read_Group_url
from common.test_read_Group_id import Read_Group_id


class Test_03_Get_Target_Group_info:
    @allure.feature('【需求点】：B003-查询指定id分组')
    @allure.story('【正常获取】')
    @allure.severity('normal')
    def test_031_Get_Target_Group_info(self):
        group_id = Read_Group_id().Read()
        print("---------------------------")
        print(group_id)
        ip = ReadIP().Read()
        urls = Read_Group_url().Read()
        url1 = urls['url03']['url']
        url = ip + url1 + group_id
        auth = ReadAuthorization().Read()
        headers = {
            'Authorization': auth,
        }
        method = 'get'
        # 发送请求
        res = RequestTools().send_requests(method=method,url=url,header=headers)
        assert res['devices']


