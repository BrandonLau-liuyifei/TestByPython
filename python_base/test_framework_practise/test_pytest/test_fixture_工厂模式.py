# -*- coding: utf-8 -*-
# @Author : Brandon

import pytest


@pytest.fixture
def make_customer_record():
    def _make_customer_record(name):
        return {"name": name, "orders": []}

    return _make_customer_record


def test_customer_records(make_customer_record):
    customer1 = make_customer_record("lisa")
    customer2 = make_customer_record("Mike")
    customer3 = make_customer_record("meredith")
