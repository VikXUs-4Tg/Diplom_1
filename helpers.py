import random
import copy

class Generators:

    @staticmethod
    def random_number():
        return random.randint(1, 10000)

class TestTools:

    @staticmethod
    def check_unit_test_result (expected_value, actually_value):
        assert expected_value == actually_value, f'\nОжидаемое значение:\n"{expected_value}"\nФактическое значение:\n"{actually_value}"'

    @staticmethod
    def make_copy_of_ingredient(class_ingredient, new_ingredients=None):
        new_class_ingredient = copy.deepcopy(class_ingredient)
        if new_ingredients:
            new_class_ingredient.type = new_ingredients[0]
            new_class_ingredient.name = new_ingredients[1]
            new_class_ingredient.price = new_ingredients[2]
        return new_class_ingredient

    @staticmethod
    def get_list_of_buns_from_class_buns(buns):
        list_of_buns = []
        for element in buns:
            list_of_buns.append((element.name, element.price))
        return list_of_buns

    @staticmethod
    def get_list_of_ingredients_from_class_ingredients(ingredients):
        list_of_ingredients = []
        for element in ingredients:
            list_of_ingredients.append((element.type, element.name, element.price))
        return list_of_ingredients
