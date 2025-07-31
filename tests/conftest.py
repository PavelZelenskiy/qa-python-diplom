import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from tests.data import BUN_PARAMS, INGREDIENT_PARAMS

#Подготовка булочки 
@pytest.fixture(params=BUN_PARAMS)
def bun(request):
    name, price = request.param
    mock_bun = Mock()
    mock_bun.get_price.return_value = price
    mock_bun.get_name.return_value = name
    return mock_bun

#подготовка ингридиента
@pytest.fixture(params=INGREDIENT_PARAMS)
def ingredient(request):
    ingredient_type, name, price = request.param
    mock_ingredient = Mock()
    mock_ingredient.get_price.return_value = price
    mock_ingredient.get_name.return_value = name
    mock_ingredient.get_type.return_value = ingredient_type
    return mock_ingredient

#подготовка бургера
@pytest.fixture
def prepared_burger(bun, ingredient):
    burger = Burger()
    burger.set_buns(bun)
    burger.add_ingredient(ingredient)
    return burger