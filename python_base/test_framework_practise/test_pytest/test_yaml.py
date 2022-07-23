# -*- coding: utf-8 -*-
# @Author : Brandon
import yaml

with open('./yaml1.yaml') as f:
    data1 = yaml.safe_load(f)
    print(data1)
