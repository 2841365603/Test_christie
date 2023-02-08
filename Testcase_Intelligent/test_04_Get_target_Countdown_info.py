# coding=utf-8
# import pytest
import json
import allure
import random
from common.request_utill_modify import RequestTools1
from common.test_read_Url import ReadIP,ReadAuthorization,ReadSN
from common.test_read_Intelligent_url import Read_Intelligent_url
from common.test_read_countdown_id import Read_countdown_id


class Test_04_Get_target_Countdown_info:
    @allure.feature('【需求点】：D004-查询指定倒计时')
    @allure.story('【正常获取】')
    @allure.severity('normal')
    def test_04_Get_target_Countdown_info(self):
        Countdown_id = Read_countdown_id().Read()
        Countdown_id = str(Countdown_id)
        ip = ReadIP().Read()
        urls = Read_Intelligent_url().Read()
        url1 = urls['url04']['url']
        url = ip + url1 + Countdown_id
        auth = ReadAuthorization().Read()
        headers = {
            'Authorization': auth,
        }
        method = 'get'
        res = RequestTools1().send_requests1(method=method,url=url,header=headers)
        res = res['condition']
        res = res[0]['type']
        assert res == "countdown"