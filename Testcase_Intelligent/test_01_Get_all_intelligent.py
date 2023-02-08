#coding=utf-8
import json
import allure
from common.request_utill_modify import RequestTools1
from common.test_read_Url import ReadIP,ReadAuthorization
from common.test_read_Intelligent_url import Read_Intelligent_url

class Test_01_Get_all_intelligent:

    @allure.feature('【需求点】：D001-获取所有智能信息')
    @allure.story('【正常获取】')
    @allure.severity('normal')
    def test_Get_all_intelligent(self):
        ip = ReadIP().Read()
        urls = Read_Intelligent_url().Read()
        url1 = urls['url01']['url']
        url = ip + url1
        auth = ReadAuthorization().Read()
        headers = {
            'Authorization': auth,
        }
        method = 'get'
        # 发送请求
        res = RequestTools1().send_requests1(method=method, url=url, header=headers)
        # 断言name存在于列表中
        assert "name" in res[0]




