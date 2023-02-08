# coding=utf-8
# import pytest
import json
import allure
import random
import yaml
from common.request_utill import RequestTools
from common.test_read_Url import ReadIP, ReadAuthorization, ReadSN
from common.test_read_Group_url import Read_Group_url

class Test_02_Add_Group:

    @allure.feature('【需求点】：B002-新建分组')
    @allure.story('【正常获取】')
    @allure.severity('normal')
    def test_021_Add_Group(self):
        ip = ReadIP().Read()
        device_sn = ReadSN().Read()
        urls = Read_Group_url().Read()
        url1 = urls['url02']['url']
        url = ip + url1
        auth = ReadAuthorization().Read()
        group_name = "测试分组"
        group_number = random.randint(100000,999999)
        group_name = group_name + str(group_number)
        picture_list = [
            0,
            1,
            2,
            7,
            15
        ]
        picture = random.choice(picture_list)
        picture = str(picture)
        icon_number = "/groups/imgs/x.png"
        icon_number = icon_number.replace('x',picture)
        print(device_sn)
        data = {
            "name": group_name,
            "icon": icon_number,
            "devices": [
                device_sn
            ]
        }
        headers = {
            'Authorization': auth,
        }
        method = 'post'
        # 发送请求
        res = RequestTools().send_requests(method=method, url=url, header=headers, data=data)
        # print(type(res))
        # print(res['id'])
        with open(r"E:\Christie\V10\Test_christie\Testdata\Group_id.yaml", "w" , encoding='utf-8') as f :
            data = {
                "name":res['id']
            }
            f.write(yaml.dump(data,allow_unicode=True,sort_keys=False))
        assert res['devices']



