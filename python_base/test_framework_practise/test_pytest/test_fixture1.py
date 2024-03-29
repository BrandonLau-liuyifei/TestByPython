# import pytest
#
#
# @pytest.fixture(scope="session")
# def order():
#     return []
#
#
# @pytest.fixture
# def func(order):
#     order.append("function")
#
#
# @pytest.fixture(scope="class")
# def cls(order):
#     order.append("class")
#
#
# @pytest.fixture(scope="module")
# def mod(order):
#     order.append("module")
#
#
# @pytest.fixture(scope="package")
# def pack(order):
#     order.append("package")
#
#
# @pytest.fixture(scope="session")
# def sess(order):
#     order.append("session")
#
#
# class TestClass:
#     def test_order(self, func, cls, mod, pack, sess, order):
#         assert order == ["session", "package", "module", "class", "function"]

# import pytest
#
#
# @pytest.fixture
# def order():
#     return []
#
#
# @pytest.fixture
# def a(order):
#     order.append("a")
#
#
# @pytest.fixture
# def b(a, order):
#     order.append("b")
#
#
# @pytest.fixture
# def c(a, b, order):
#     order.append("c")
#
#
# @pytest.fixture
# def d(c, b, order):
#     order.append("d")
#
#
# @pytest.fixture
# def e(d, b, order):
#     order.append("e")
#
#
# @pytest.fixture
# def f(e, order):
#     order.append("f")
#
#
# @pytest.fixture
# def g(f, c, order):
#     order.append("g")
#
#
# def test_order(g, order):
#     assert order == ["a", "b", "c", "d", "e", "f", "g"]

