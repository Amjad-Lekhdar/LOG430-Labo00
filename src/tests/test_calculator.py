"""
Calculator app tests
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""

from calculator import Calculator

def test_app():
    my_calculator = Calculator()
    welcome_message = my_calculator.get_hello_message()
    assert "== Calculatrice v1.0 ==" in welcome_message

# Test de l'addition
def test_addition():
    my_calculator = Calculator()
    assert my_calculator.addition(2, 3) == 5

# Test de la soustraction
def test_subtraction():
    my_calculator = Calculator()
    assert my_calculator.subtraction(5, 2) == 3


# Test fautif de l'addition pour la question 1
def test_addition_erreur():
    my_calculator = Calculator()
    assert my_calculator.addition(2, 3) == 6

