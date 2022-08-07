import pytest

@pytest.fixture
def make_customer_record():
    def _make_customer_record(name):
        return {"name":name,"order":[]}
    return _make_customer_record

def test_customer_records(make_customer_record):
    customer_1 = make_customer_record("LIsa")
    customer_2 = make_customer_record("Mike")
    customer_3 = make_customer_record("Tom")
    print(customer_1, customer_2, customer_3)
