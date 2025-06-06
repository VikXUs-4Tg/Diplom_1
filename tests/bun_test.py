from data import const
from helpers import TestTools
from praktikum.bun import Bun


class TestBun:

    def test_bun_get_name_return_name(self):
        bun = Bun(name=const['TESTS_DATA_BUN'][0], price=const['TESTS_DATA_BUN'][1])
        TestTools.check_unit_test_result(expected_value=const['TESTS_DATA_BUN'][0], actually_value=bun.get_name())

    def test_bun_get_price_return_price(self):
        bun = Bun(name=const['TESTS_DATA_BUN'][0], price=const['TESTS_DATA_BUN'][1])
        TestTools.check_unit_test_result(expected_value=const['TESTS_DATA_BUN'][1], actually_value=bun.get_price())
