# ！/usr/bin/env python
# -*- coding：utf-8 -*-
import pytest
import yaml


class TestDemo:

    def test_yaml(self):
        print(yaml.safe_load(open("yaml_0709.yaml")))

    @pytest.mark.parametrize("env", yaml.safe_load(open("yaml_0709.yaml")))
    def test_demo(self, env):
        if "test" in env:
            print("this is a test env,IP:", env["test"])
        elif "dev" in env:
            print("this is a dev env,IP:", env["dev"])


if __name__ == '__main__':
    case = TestDemo()
    case.test_demo()
