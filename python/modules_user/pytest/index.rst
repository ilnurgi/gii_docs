.. title:: python pytest

.. meta::
    :description:
        Справочная информация по python модулю pytest.
    :keywords:
        python pytest

.. py:module:: pytest

pytest
======

.. code-blcok:: sh

    pip install pytest


.. code-block:: py

    # test.py

    def test():
        f = FizzBuzz()
        assert f.say(3) == 'Fizz'

.. code-block:: py

    # test.py

    @pytest.fixture
    def fizzbuzz():
        return FizzBuzz()

    def test(fizzbuzz):
        assert fizzbuzz.say(3) == 'Fizz'


.. code-block:: py

    # test.py

    @pytest.fixture
    def fizzbuzz():
        return FizzBuzz()

    @pytest.mark.parametrize('test_input, expected', [
        (3, 'Fizz'),
        (6, 'Fizz'),
        (5, 'Buzz'),
        (10, 'Buzz'),
        (15, 'FizzBuzz'),
        (30, 'FizzBuzz'),
        (2, 2),
        (7, 7),
    ])
    def test(fizzbuzz, test_input, expected):
        assert fizzbuzz.say(test_input) == expected
