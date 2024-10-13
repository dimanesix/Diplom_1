from unittest.mock import Mock

from practicum.bun import Bun
from practicum.burger import Burger
from practicum.ingredient import Ingredient


class TestBurger:

    def test_burger_initialize(self, burger):
        # Проверяем начальную инициализацию объекта Burger
        assert burger.bun is None, "Поле bun должно быть равно None"
        assert isinstance(burger.ingredients, list) and len(burger.ingredients) == 0, ("Поле ingredients - пустой "
                                                                                           "массив из Ingredient")
        for ingredient in burger.ingredients:
            assert isinstance(ingredient, Ingredient), "Поле ingredients - пустой массив из Ingredient"

    def test_set_buns(self, burger):
        # Проверяем выбор булки для бургера
        bun = Bun("Имя", 100)
        burger.set_buns(bun)
        assert burger.bun == bun

    def test_add_ingredients(self, burger):
        # Проверяем добавление ингредиентов для бургера
        ingredient_one = Ingredient("Тип", "Имя", 100)
        ingredient_two = Ingredient("Тип", "Имя", 100)
        burger.add_ingredient(ingredient_one)
        assert burger.ingredients == [ingredient_one] and len(burger.ingredients) == 1
        burger.add_ingredient(ingredient_two)
        assert burger.ingredients == [ingredient_one, ingredient_two] and len(burger.ingredients) == 2
