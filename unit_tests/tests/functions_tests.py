import pytest
from unit_tests.src.functions import (
    is_palindrome,
    fibonacci,
    count_vowels,
    calculate_discount,
    flatten_list,
    word_frequencies,
    is_prime
)


@pytest.mark.parametrize("text, expected", [
    ("kajak", True),
    ("Kobyła ma mały bok", True),
    ("python", False),
    ("", True),
    ("A", True)
])
def test_is_palindrome(text, expected):
    assert is_palindrome(text) == expected


@pytest.mark.parametrize("n, expected", [
    (0, 0),
    (1, 1),
    (5, 5),
    (10, 55)
])
def test_fibonacci(n, expected):
    assert fibonacci(n) == expected

def test_fibonacci_negative():
    with pytest.raises(ValueError):
        fibonacci(-1)


@pytest.mark.parametrize("text, expected", [
    ("Python", 2),
    ("AEIOUY", 6),
    ("bcd", 0),
    ("", 0),
    ("Próba żółwia", 5)
])
def test_count_vowels(text, expected):
    assert count_vowels(text) == expected


@pytest.mark.parametrize("price, discount, expected", [
    (100, 0.2, 80.0),
    (50, 0, 50.0),
    (200, 1, 0.0)
])
def test_calculate_discount(price, discount, expected):
    assert calculate_discount(price, discount) == pytest.approx(expected)


@pytest.mark.parametrize("discount", [-0.1, 1.5])
def test_calculate_discount_errors(discount):
    with pytest.raises(ValueError):
        calculate_discount(100, discount)


@pytest.mark.parametrize("nested_list, expected", [
    ([1, 2, 3], [1, 2, 3]),
    ([1, [2, 3], [4, [5]]], [1, 2, 3, 4, 5]),
    ([], []),
    ([[[1]]], [1]),
    ([1, [2, [3, [4]]]], [1, 2, 3, 4])
])
def test_flatten_list(nested_list, expected):
    assert flatten_list(nested_list) == expected


def test_word_frequencies_basic():
    text = "To be or not to be"
    expected = {"to": 2, "be": 2, "or": 1, "not": 1}
    assert word_frequencies(text) == expected

def test_word_frequencies_punctuation():
    text = "Hello, hello!"
    expected = {"hello": 2}
    assert word_frequencies(text) == expected

def test_word_frequencies_empty():
    assert word_frequencies("") == {}

def test_word_frequencies_case():
    text = "Python Python python"
    expected = {"python": 3}
    assert word_frequencies(text) == expected

def test_word_frequencies_complex_punctuation():

    text = "Ala ma kota, a kot ma Ale."
    result = word_frequencies(text)
    assert result["ala"] == 1
    assert result["kota"] == 1
    assert "kota," not in result


@pytest.mark.parametrize("n, expected", [
    (2, True),
    (3, True),
    (4, False),
    (0, False),
    (1, False),
    (5, True),
    (97, True)
])
def test_is_prime(n, expected):
    assert is_prime(n) == expected