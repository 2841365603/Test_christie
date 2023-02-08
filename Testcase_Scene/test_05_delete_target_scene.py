# coding=utf-8
# import pytest
import json
import allure
import random
from common.request_utill import RequestTools
from common.test_read_Url import ReadIP,ReadAuthorization,ReadSN
from common.test_read_Scene_url import Read_Scene_url
from common.test_read_Scene_id import Read_Scene_id


class Test_05_delete_Target_Scene:
    @allure.feature('【需求点】：C005删除指定场景')
    @allure.story('【正常获取】')
    @allure.severity('normal')
    def test_05_delete_Target_Scene(self):
        scene_id = Read_Scene_id().Read()
        scene_id = str(scene_id)
        ip = ReadIP().Read()
        urls = Read_Scene_url().Read()
        url1 = urls['url05']['url']
        url = ip + url1 + scene_id
        auth = ReadAuthorization().Read()
        headers = {
            'Authorization': auth,
        }
        method = 'delete'
        # 发送请求
        res = RequestTools().send_requests(method=method, url=url, header=headers)
        # 断言返回message为success
        assert res['message'] == 'Success'