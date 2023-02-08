#coding=utf-8
# import pytest
import json
import allure
from common.request_utill import RequestTools
from common.test_read_Url import ReadIP,ReadAuthorization
from common.test_read_Group_url import Read_Group_url

class Test_01_Get_Group_info:
    @allure.feature('【需求点】：B001-获取分组信息')
    @allure.story('【正常获取】')
    @allure.severity('normal')
    def test_Get_Group_info(self):
        ip = ReadIP().Read()
        urls = Read_Group_url().Read()
        url1 = urls['url01']['url']
        url = ip + url1
        auth = ReadAuthorization().Read()

        headers = {
            'Authorization': auth,
        }
        method = 'get'
        # 发送请求
        res = RequestTools().send_requests(method=method, url=url, header=headers)
        res = res[0]['name']
        assert res





