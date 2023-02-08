# coding=utf-8
# import pytest
import json
import allure
import random
from common.request_utill import RequestTools
from common.test_read_Url import ReadIP,ReadAuthorization,ReadSN
from common.test_read_Scene_url import Read_Scene_url
from common.test_read_Scene_id import Read_Scene_id


class Test_04_modify_Target_Scene:
    @allure.feature('【需求点】：C004修改指定场景')
    @allure.story('【正常获取】')
    @allure.severity('normal')
    def test_04_modify_Target_Scene(self):
        scene_id = Read_Scene_id().Read()
        scene_id = str(scene_id)
        ip = ReadIP().Read()
        urls = Read_Scene_url().Read()
        url1 = urls['url04']['url']
        url = ip + url1 + scene_id
        auth = ReadAuthorization().Read()
        Scene_name = "修改场景名称"
        Scene_number = random.randint(200000,999999)
        Scene_name = Scene_name + str(Scene_number)
        picture_list = [
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            12,
            13,
            14,
            15,
            16,
            17,
            19
        ]
        picture = random.choice(picture_list)
        picture = str(picture)
        icon_number = "/scenes/imgs/x.png"
        icon_number = icon_number.replace('x',picture)
        data = {
            "name":Scene_name,
            "icon":icon_number
        }
        headers = {
            'Authorization': auth,
        }
        method = 'patch'
        # 发送请求
        res = RequestTools().send_requests(method=method, url=url, header=headers, data=data)
        # 断言返回message为success
        assert res['message'] == 'Success'