# coding=utf-8
# import pytest
import json
import allure
import random
import yaml
from common.request_utill import RequestTools
from common.test_read_Url import ReadIP, ReadAuthorization, ReadSN
from common.test_read_Scene_url import Read_Scene_url


class Test_02_Add_Group:
    @allure.feature('【需求点】：C002新建场景')
    @allure.story('【正常获取】')
    @allure.severity('normal')
    def test_02_Add_Scene(self):
        ip = ReadIP().Read()
        # device_sn = ReadSN().Read()
        urls = Read_Scene_url().Read()
        url1 = urls['url02']['url']
        url = ip + url1
        auth = ReadAuthorization().Read()
        Scene_name = "新建场景"
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
        method = 'post'
        # 发送请求
        res = RequestTools().send_requests(method=method, url=url, header=headers, data=data)
        assert "id" in res
        with open(r"E:\Christie\V10\Test_christie\Testdata\Scene_id.yaml", "w" , encoding='utf-8') as f :
            data = {
                "name":res['id']
            }
            # allow_unicode=True，解决存储时unicode编码问题。
            # sort_keys=False，解决写入yaml的数据则不会排序后写入。
            f.write(yaml.dump(data,allow_unicode=True,sort_keys=False))




