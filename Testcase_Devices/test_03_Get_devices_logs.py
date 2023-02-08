#coding=utf-8
# import pytest
import json
import allure
from common.request_utill import RequestTools
from common.test_read_Url import ReadIP,ReadAuthorization,ReadURL


class Test_03_Get_devices_logs:

    @allure.feature('【需求点】：A003-获取设备log日志')
    @allure.story('【正常获取】')
    @allure.severity('normal')
    def test_Get_devices_logs(self):
        ip = ReadIP().Read()
        urls = ReadURL().Read()
        url1 = urls['url03']['url']
        url = ip + url1
        auth = ReadAuthorization().Read()
        headers = {
            'Authorization': auth,
        }
        method = 'get'
        # 发送请求
        res = RequestTools().send_requests(method=method, url=url, header=headers)
        assert res[0]['id']
