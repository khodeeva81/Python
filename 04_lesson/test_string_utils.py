import pytest
from string_utils import StringUtils

@pytest.fixture
def utils():
    return StringUtils()


def test_capitalize_basic(utils):
    assert utils.capitalize("skypro") == "Skypro"

def test_capitalize_empty_string(utils):
    assert utils.capitalize("") == ""

def test_capitalize_already_capitalized(utils):
    assert utils.capitalize("Skypro") == "Skypro"

def test_capitalize_single_char(utils):
    assert utils.capitalize("a") == "A"


def test_trim_leading_spaces(utils):
    assert utils.trim("   skypro") == "skypro"

def test_trim_no_spaces(utils):
    assert utils.trim("skypro") == "skypro"

def test_trim_only_spaces(utils):
    assert utils.trim("       ") == ""

def test_trim_inside_spaces_not_removed(utils):

    assert utils.trim("  a  ") == "  a  "

def test_trim_empty_string(utils):
    assert utils.trim("") == ""


@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "S", True),
    ("SkyPro", "o", True),
    ("SkyPro", "U", False),
    ("", "a", False),
    ("abc", "a", True),
    ("abc", "z", False)
])
def test_contains_various_cases(utils, string, symbol, expected):
    assert utils.contains(string, symbol) == expected


def test_delete_symbol_single_occurrence(utils):
    assert utils.delete_symbol("SkyPro", "k") == "SyPro"

def test_delete_symbol_substring_pro(utils):
    assert utils.delete_symbol("SkyPro", "Pro") == "Sky"

def test_delete_symbol_char_not_found(utils):
    assert utils.delete_symbol("SkyPro", "x") == "SkyPro"

def test_delete_symbol_all_chars(utils):
    assert utils.delete_symbol("aaaaa", "a") == ""

def test_delete_symbol_empty_string(utils):
    assert utils.delete_symbol("", "a") == ""

def test_delete_symbol_empty_symbol(utils):

    assert utils.delete_symbol("abc", "") == "abc"