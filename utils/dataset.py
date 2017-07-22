#!/usr/bin/python
# -*- coding=utf-8 -*-

"""
@author：     柳汝滕
@email:       fingthinking@qq.com
@time：       2017年07月22日} 下午11:06
@version:     v0.1
"""
import requests
import gzip
import os.path as path


def knn():
    if not path.exists("digist.zip"):
        resp = requests.post("https://github.com/Haojen/hexo-theme-Anisina/blob/master/README.md")
        r = open("README.md","w")
        r.write(resp.content)

if __name__ == "__main__":
    knn()