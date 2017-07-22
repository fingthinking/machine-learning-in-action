#!/usr/bin/python
# -*- coding=utf-8 -*-

"""
@author：     柳汝滕
@email:       fingthinking@qq.com
@time：       2017年07月22日} 下午9:00
@version:     v0.1
"""
import numpy as np


def create_data_set():
    """
    创建数据集
    :return:
    """
    group = np.array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    lable = ["A", "A", "B", "B"]
    return group, lable


def classify(in_x, data_set, labels, k):
    """
    进行分类
    :param in_x: 输入分量x
    :param data_set: 已知类别的数据集
    :param labels:  对应的数据集的label
    :param k: 迭代次数
    :return:
    """
    size = data_set.shape[0]  # 训练数据集的个数

    # np.title第二个参数是数组形式，
    # 其中第一个数字代表复制的次数，
    # 后面的数字代表在哪个维度上复制，
    # 如果只有一个值，则代表维度扩张复制

    # ======= 求距离 ========
    mat_dif = np.tile(in_x, (size, 1)) - data_set  # 2维， [[x1-x],[x2-x]]
    mat_pow = mat_dif ** 2
    dis = np.sqrt(mat_pow.sum(axis=1))  # axis是对哪一个维度求和运算, 无需开根号运算
    dis_arg = dis.argsort()
    # ======= 距离计算完成且有序 ===
    cls_count = {}
    for i in xrange(k):
        vote_label = labels[dis_arg[i]]  # 获得第i小的排序结果的分类
        cls_count[vote_label] = cls_count.get(vote_label, 0) + 1

    # 获取cls中值最大的key
    st = sorted(cls_count.iteritems(), key=lambda item: item[1], reverse=True)
    return st[0][0]


def auto_norm(data_set):
    """
    数据归一化
    :param data_set: 待归一化的数据集
    :return: 归一化后的数据集，每一列的取值范围，每一列的最小值
    """
    # 获取每一列最大值和最小值
    d_max, d_min = data_set.max(0), data_set.min(0)
    d_range = d_max - d_min

    mat_min = np.tile(d_min, (data_set.shape[0], 1))
    mat_range = np.tile(d_range, (data_set.shape[0], 1))

    mat_norm = (data_set - mat_min) / mat_range
    return mat_norm, d_range, d_min


if __name__ == "__main__":
    x = [2.0, 0.5]
    data, lab = create_data_set()
    print classify(x, data, lab, 3)

    rand_data = np.random.rand(5,6) * 100
    print rand_data
    print auto_norm(rand_data)[1]