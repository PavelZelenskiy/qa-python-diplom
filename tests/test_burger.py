from ..praktikum.burger import Burger
from unittest.mock import Mock

class TestBurger:

    def test_set_buns(bun):
        burger = Burger()
        burger.set_buns(bun)
        assert burger.bun == bun


    def test_add_ingredient(ingredient):
        burger = Burger()
        burger.add_ingredient(ingredient)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == ingredient


    def test_remove_ingredient(self, prepared_burger):
        initial_count = len(prepared_burger.ingredients)
        prepared_burger.remove_ingredient(0)
        assert len(prepared_burger.ingredients) == initial_count - 1


    def test_move_ingredient(self, bun):
        burger = Burger()
        
        # Создаем два разных ингредиента
        ing1 = Mock()
        ing1.get_name.return_value = "ing1"
        ing2 = Mock()
        ing2.get_name.return_value = "ing2"
        
        burger.set_buns(bun)
        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)
        
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] == ing2
        assert burger.ingredients[1] == ing1


    def test_get_price(self, prepared_burger, bun, ingredient):
        expected_price = bun.get_price() * 2 + ingredient.get_price()
        assert prepared_burger.get_price() == expected_price


    def test_get_receipt(self, prepared_burger, bun, ingredient):
        receipt = prepared_burger.get_receipt()
        expected_receipt = [
        f'(==== {bun.get_name()} ====)',
        f'= {ingredient.get_type().lower()} {ingredient.get_name()} =',
        f'(==== {bun.get_name()} ====)',
        '',
        f'Price: {prepared_burger.get_price()}'
        ]
        assert receipt == '\n'.join(expected_receipt)


