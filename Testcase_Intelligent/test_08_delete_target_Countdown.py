# coding=utf-8
# import pytest
import json
import allure
import random
from common.request_utill import RequestTools
from common.test_read_Url import ReadIP,ReadAuthorization,ReadSN
from common.test_read_Intelligent_url import Read_Intelligent_url
from common.test_read_countdown_id import Read_countdown_id


class Test_08_delete_Target_Countdown:
    @allure.feature('【需求点】：D008-删除指定倒计时')
    @allure.story('【正常获取】')
    @allure.severity('normal')
    def test_08_delete_Target_Countdown(self):
        countdown_id = Read_countdown_id().Read()
        countdown_id = str(countdown_id)
        ip = ReadIP().Read()
        urls = Read_Intelligent_url().Read()
        url1 = urls['url08']['url']
        url = ip + url1 + countdown_id
        auth = ReadAuthorization().Read()
        headers = {
            'Authorization': auth,
        }
        method = 'delete'
        # 发送请求
        res = RequestTools().send_requests(method=method, url=url, header=headers)
        # 断言返回message为success
        assert res['message'] == 'Success'