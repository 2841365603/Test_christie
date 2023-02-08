# coding=utf-8
# import pytest
import json
import allure
import random
from common.request_utill import RequestTools
from common.test_read_Url import ReadIP,ReadAuthorization,ReadSN
from common.test_read_Intelligent_url import Read_Intelligent_url
from common.test_read_Intelligent_id import Read_intelligent_id


class Test_09_delete_target_intelligent:
    @allure.feature('【需求点】：D009-删除指定定时')
    @allure.story('【正常获取】')
    @allure.severity('normal')
    def test_09_delete_target_intelligent(self):
        intelligent = Read_intelligent_id().Read()
        intelligent = str(intelligent)
        ip = ReadIP().Read()
        urls = Read_Intelligent_url().Read()
        url1 = urls['url09']['url']
        url = ip + url1 + intelligent
        auth = ReadAuthorization().Read()
        headers = {
            'Authorization': auth,
        }
        method = 'delete'
        # 发送请求
        res = RequestTools().send_requests(method=method, url=url, header=headers)
        # 断言返回message为success
        assert res['message'] == 'Success'