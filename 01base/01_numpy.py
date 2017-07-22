#!/usr/bin/python
# -*- coding=utf-8 -*-

"""
@author：     柳汝滕
@email:       fingthinking@qq.com
@time：       2017年07月22日} 下午8:29
@version:     v0.1
"""
import numpy as np

# 创建3*4矩阵，0~1之间
rd = np.random.rand(3,4)
print rd
mt = np.mat(rd)
print mt

print mt.I

print mt*mt.I