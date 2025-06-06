from data import const
from helpers import TestTools
from praktikum.ingredient import Ingredient


class TestIngredient:

    def test_ingredient_get_type_return_type(self):
        ingredient = Ingredient(ingredient_type=const['TESTS_DATA_INGREDIENT'][0], name=const['TESTS_DATA_INGREDIENT'][1], price=const['TESTS_DATA_INGREDIENT'][2])
        TestTools.check_unit_test_result(expected_value=const['TESTS_DATA_INGREDIENT'][0], actually_value=ingredient.get_type())

    def test_ingredient_get_name_return_name(self):
        ingredient = Ingredient(ingredient_type=const['TESTS_DATA_INGREDIENT'][0], name=const['TESTS_DATA_INGREDIENT'][1], price=const['TESTS_DATA_INGREDIENT'][2])
        TestTools.check_unit_test_result(expected_value=const['TESTS_DATA_INGREDIENT'][1], actually_value=ingredient.get_name())

    def test_ingredient_get_price_return_price(self):
        ingredient = Ingredient(ingredient_type=const['TESTS_DATA_INGREDIENT'][0], name=const['TESTS_DATA_INGREDIENT'][1], price=const['TESTS_DATA_INGREDIENT'][2])
        TestTools.check_unit_test_result(expected_value=const['TESTS_DATA_INGREDIENT'][2], actually_value=ingredient.get_price())
