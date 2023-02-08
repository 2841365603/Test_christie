# coding=utf-8
import os
import yaml
yaml.warnings({'YAMLLoadWarning': False})
# 读取文件时相对路径一直报错，因此采取绝对路径
#  读取yaml文件url
class Read_Scene_url:
    def Read(self):
        f = open(r"E:\Christie\V10\Test_christie\Testdata\Scene_url.yaml", 'r', encoding='gbk')
        mes = f.read()
        urls = yaml.load(mes)
        return urls
