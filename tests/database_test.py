from data import const
from helpers import TestTools
from praktikum.database import Database


class TestDatabase:

    def test_database_init_data_buns_is_valid(self):
        buns_from_database = TestTools.get_list_of_buns_from_class_buns(buns=Database().buns)
        TestTools.check_unit_test_result(expected_value=const['TESTS_DATA_DATABASE_INIT_BUNS'], actually_value=buns_from_database)

    def test_database_init_data_ingredients_is_valid(self):
        ingredients_from_database = TestTools.get_list_of_ingredients_from_class_ingredients(ingredients=Database().ingredients)
        TestTools.check_unit_test_result(expected_value=const['TESTS_DATA_DATABASE_INIT_INGREDIENTS'], actually_value=ingredients_from_database)

    def test_database_available_buns_return_available_buns(self):
        database = Database()
        buns_from_database = TestTools.get_list_of_buns_from_class_buns(buns=database.buns)
        buns_from_method = TestTools.get_list_of_buns_from_class_buns(buns=database.available_buns())
        TestTools.check_unit_test_result(expected_value=buns_from_database, actually_value=buns_from_method)

    def test_database_available_ingredients_return_available_ingredients(self):
        database = Database()
        ingredients_from_database = TestTools.get_list_of_ingredients_from_class_ingredients(ingredients=database.ingredients)
        ingredients_from_method = TestTools.get_list_of_ingredients_from_class_ingredients(ingredients=database.available_ingredients())
        TestTools.check_unit_test_result(expected_value=ingredients_from_database, actually_value=ingredients_from_method)
