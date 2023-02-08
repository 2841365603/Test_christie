# coding=utf-8
# import pytest
import json
import allure
import random
from common.request_utill_modify import RequestTools1
from common.test_read_Url import ReadIP,ReadAuthorization,ReadSN
from common.test_read_Intelligent_url import Read_Intelligent_url
from common.test_read_Intelligent_id import Read_intelligent_id


class Test_05_Get_target_intelligent_info:
    @allure.feature('【需求点】：D005-查询指定定时')
    @allure.story('【正常获取】')
    @allure.severity('normal')
    def test_05_Get_target_intelligent_info(self):
        intelligent_id = Read_intelligent_id().Read()
        intelligent_id = str(intelligent_id)
        ip = ReadIP().Read()
        urls = Read_Intelligent_url().Read()
        url1 = urls['url05']['url']
        url = ip + url1 + intelligent_id
        auth = ReadAuthorization().Read()
        headers = {
            'Authorization': auth,
        }
        method = 'get'
        res = RequestTools1().send_requests1(method=method,url=url,header=headers)
        res = res['condition']
        res = res[0]['type']
        assert res == "timing"