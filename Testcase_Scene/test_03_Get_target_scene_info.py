# coding=utf-8
# import pytest
import json
import allure
import random
from common.request_utill import RequestTools
from common.test_read_Url import ReadIP,ReadAuthorization,ReadSN
from common.test_read_Scene_url import Read_Scene_url
from common.test_read_Scene_id import Read_Scene_id


class Test_03_Get_Target_Scene_info:
    @allure.feature('【需求点】：C003查询指定场景')
    @allure.story('【正常获取】')
    @allure.severity('normal')
    def test_03_Get_Target_Scene_info(self):
        scene_id = Read_Scene_id().Read()
        scene_id = str(scene_id)
        ip = ReadIP().Read()
        urls = Read_Scene_url().Read()
        url1 = urls['url03']['url']
        url = ip + url1 + scene_id
        auth = ReadAuthorization().Read()
        headers = {
            'Authorization': auth,
        }
        method = 'get'
        res = RequestTools().send_requests(method=method,url=url,header=headers)
        assert "id" in res