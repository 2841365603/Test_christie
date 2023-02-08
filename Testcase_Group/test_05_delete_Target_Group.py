# coding=utf-8
import pytest
import json
import allure
import random
from common.request_utill import RequestTools
from common.test_read_Url import ReadIP, ReadAuthorization, ReadSN
from common.test_read_Group_url import Read_Group_url
from common.test_read_Group_id import Read_Group_id


class Test_05_Delete_Target_Group_info:

    @allure.feature('【需求点】：B005-删除指定分组')
    @allure.story('【正常获取】')
    @allure.severity('normal')
    def test_05_delete_Target_Group(self):
        group_id = Read_Group_id().Read()
        ip = ReadIP().Read()
        urls = Read_Group_url().Read()
        url = urls['url05']['url']
        url = ip + url + group_id
        auth = ReadAuthorization().Read()
        headers = {
            'Authorization': auth,
        }
        method = 'delete'
        # 发送请求
        res = RequestTools().send_requests(method=method, url=url, header=headers)
        # 断言返回message为Success
        assert res['message'] == "Success"
























