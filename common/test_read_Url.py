# coding=utf-8
import os
import yaml
yaml.warnings({'YAMLLoadWarning': False})
# 读取文件时相对路径一直报错，因此采取绝对路径
class ReadAuthorization:
    def Read(self):
        f = open(r"E:\Christie\V10\Test_christie\Testdata\Authorization.yaml", 'r', encoding='gbk')
        mes = f.read()
        mes = yaml.load(mes)
        Authorization = mes['test']['Authorization']
        return Authorization
# 读取yaml文件ip
class ReadIP:
    def Read(self):
        f = open(r"E:\Christie\V10\Test_christie\Testdata\IP.yaml", 'r', encoding='gbk')
        mes1 = f.read()
        mes1 = yaml.load(mes1)
        host = mes1['test']['IP']
        return host
#  读取yaml文件url
class ReadURL:
    def Read(self):
        f = open(r"E:\Christie\V10\Test_christie\Testdata\Url.yaml", 'r', encoding='gbk')
        mes2 = f.read()
        urls = yaml.load(mes2)
        return urls

#  读取yaml文件sn
class ReadSN:
    def Read(self):
        f = open(r"E:\Christie\V10\Test_christie\Testdata\SN.yaml", 'r', encoding='gbk')
        mes3 = f.read()
        mes3 = yaml.load(mes3)
        sn1 = mes3['test']['SN']
        # print(sn1)
        # print(type(sn1))
        return sn1
