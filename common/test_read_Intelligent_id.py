# coding=utf-8
import os
import yaml
yaml.warnings({'YAMLLoadWarning': False})
# 读取文件时相对路径一直报错，因此采取绝对路径
#  读取yaml文件url
class Read_intelligent_id:
    def Read(self):
        f = open(r"E:\Christie\V10\Test_christie\Testdata\Intelligent_id.yaml", 'r', encoding='gbk')
        intelligent_id = f.read()
        intelligent_id = yaml.load(intelligent_id)
        intelligent_id = intelligent_id['name']
        return intelligent_id