# -*- coding: utf-8 -*-
__author__ = "FTest"

'''
8-5  城市 ：编写一个名为 describe_city() 的函数，它接受一座城市的名字以及该城市所属的国家。
这个函数应打印一个简单的句子，如 Reykjavik is in Iceland 。
给用于存储国家的形参指定默认值。为三座不同的城市调用这个函数，且其中至少有一座城市不属于默认国家。
'''
def describe_city(city,country="China"):
    print(city+ " is in " + country)
    pass
describe_city("Taiwan")

describe_city("Beijing")

describe_city("London","England")