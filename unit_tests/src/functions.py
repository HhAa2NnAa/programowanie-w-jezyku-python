import re
import math


def is_palindrome(text: str) -> bool:
    clean_text = text.replace(" ", "").lower()
    return clean_text == clean_text[::-1]


def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("n nie może być liczbą ujemną")
    if n == 0:
        return 0
    if n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def count_vowels(text: str) -> int:
    vowels = {'a', 'e', 'i', 'o', 'u', 'y', 'ą', 'ę', 'ó'}
    count = 0
    for char in text.lower():
        if char in vowels:
            count += 1
    return count


def calculate_discount(price: float, discount: float) -> float:
    if not (0 <= discount <= 1):
        raise ValueError("Obniżka musi zawierać się pomiędzy 0 a 1")

    return price * (1 - discount)


def flatten_list(nested_list: list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten_list(item))
        else:
            flat_list.append(item)
    return flat_list


def word_frequencies(text: str):
    if not text:
        return {}

    words = re.findall(r'\w+', text.lower())
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq


def is_prime(n: int):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
