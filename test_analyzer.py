import pytest

from analyzer import count_words, count_chars, find_most_common_word

def test_count_words():
    assert count_words("Hello world") == 2
    assert count_words("") == 0
    assert count_words("One two three four five") == 5

def test_count_chars():
    assert count_chars("Hello") == 5
    assert count_chars("") == 0
    assert count_chars("1234567890") == 10

def test_find_most_common_word():
    assert find_most_common_word("apple banana apple orange banana apple") == "apple"
    assert find_most_common_word("one two three two one two") == "two"
    assert find_most_common_word("") == ""