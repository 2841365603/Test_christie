#coding=utf-8
# import pytest
import json
import allure
from common.request_utill import RequestTools
from common.test_read_Url import ReadIP,ReadAuthorization,ReadURL,ReadSN


class Test_04_Get_target_device_info:

    @allure.feature('【需求点】：A004-获取固定SN设备的信息')
    @allure.story('【正常获取】')
    @allure.severity('normal')
    def test_Get_target_device_info(self):
        ip = ReadIP().Read()
        urls = ReadURL().Read()
        device_sn = ReadSN().Read()
        url1 = urls['url04']['url']
        url = ip + url1
        url = url.replace('sn',device_sn)
        auth = ReadAuthorization().Read()
        headers = {
            'Authorization': auth,
        }
        method = 'get'
        # 发送请求
        res = RequestTools().send_requests(method=method,url=url,header=headers)
        assert res['type'] == "light"
