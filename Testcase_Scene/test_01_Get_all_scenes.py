#coding=utf-8
import json
import allure
from common.request_utill import RequestTools
from common.test_read_Url import ReadIP,ReadAuthorization
from common.test_read_Scene_url import Read_Scene_url

class Test_01_Get_all_scenes:

    @allure.feature('【需求点】：C001获取所有场景信息')
    @allure.story('【正常获取】')
    @allure.severity('normal')
    def test_Get_all_scenes(self):
        ip = ReadIP().Read()
        urls = Read_Scene_url().Read()
        url1 = urls['url01']['url']
        url = ip + url1
        auth = ReadAuthorization().Read()
        headers = {
            'Authorization': auth,
        }
        method = 'get'
        # 发送请求
        res = RequestTools().send_requests(method=method, url=url, header=headers)
        assert res[0]['name']





