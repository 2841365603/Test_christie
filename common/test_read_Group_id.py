# coding=utf-8
import os
import yaml
yaml.warnings({'YAMLLoadWarning': False})
# 读取文件时相对路径一直报错，因此采取绝对路径
#  读取yaml文件url
class Read_Group_id:
    def Read(self):
        f = open(r"E:\Christie\V10\Test_christie\Testdata\Group_id.yaml", 'r', encoding='gbk')
        group_id = f.read()
        group_id = yaml.load(group_id)
        group_id = group_id['name']
        return group_id