#coding=utf-8
# import pytest
import json
import allure
import requests

from common.request_utill import RequestTools
from common.test_read_Url import ReadIP,ReadAuthorization,ReadURL


class Test_Get_devices_info:

    @allure.feature('【需求点】：A001-获取设备信息')
    @allure.story('【正常获取】')
    @allure.severity('normal')
    def test_Get_devices_info(self):
        ip = ReadIP().Read()
        urls = ReadURL().Read()
        url1 = urls['url01']['url']
        url = ip + url1
        auth = ReadAuthorization().Read()

        headers = {
            'Authorization': auth,
        }
        method = 'get'
        # 发送请求
        res = RequestTools().send_requests(method=method, url=url, header=headers)
        # 断言返回的结果中包含light
        res = res[0]['type']
        assert res == "light"
        print(res)