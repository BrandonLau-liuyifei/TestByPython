# ！/usr/bin/env python
# -*- coding：utf-8 -*-

import test

import pytest


def test_success():
    """this is succeeds"""
    assert True


def test_failure():
    """this is fail"""
    assert False


def test_skip():
    """this is sikkiped"""
    pytest.skip("for a reason")


def test_broken():
    raise Exception("oops")
