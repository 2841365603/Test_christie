# coding=utf-8
import os
import yaml
yaml.warnings({'YAMLLoadWarning': False})
# 读取文件时相对路径一直报错，因此采取绝对路径
#  读取yaml文件url
class Read_countdown_id:
    def Read(self):
        f = open(r"E:\Christie\V10\Test_christie\Testdata\countdown_id.yaml", 'r', encoding='gbk')
        res = f.read()
        countdown_id = yaml.load(res)
        countdown_id = countdown_id['name']
        return countdown_id