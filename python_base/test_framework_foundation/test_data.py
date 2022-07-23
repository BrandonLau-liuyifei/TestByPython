# ！/usr/bin/env python
# -*- coding：utf-8 -*-
import yaml

import pytest


class TestData:
    # 使用string
    @pytest.mark.parametrize('a,b', [(10, 20), (10, 30)])
    def test_param1(self, a, b):
        print(a + b)

    # 使用list
    @pytest.mark.parametrize(['a', 'b'], [(10, 20), (10, 30)])
    def test_param2(self, a, b):
        print(a + b)

    # 使用tuple
    @pytest.mark.parametrize(('a', 'b'), [(10, 20), (10, 30)])
    def test_param3(self, a, b):
        print(a + b)

    # 使用yaml参数化
    @pytest.mark.parametrize(["a", "b"], yaml.safe_load(open("yaml_0708.yaml")))
    def test_param4(self, a, b):
        print(a + b)
