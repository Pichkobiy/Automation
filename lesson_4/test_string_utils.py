
import pytest
from string_utils import StringUtils

utils = StringUtils()


@pytest.mark.parametrize("input_str, expected_result", [
    #позитивные
    ("frank", "Frank"), 
    ("вода", "Вода"),
    ("summer holiday", "Summer holiday"),
    ("coffe House", "Coffe house"),
    #негативные
    ("@#$", "@#$"),
    ("564", "564"),
    (" ", " "),
    ("", "")

])
def test_capitalize(input_str, expected_result):
    assert utils.capitalize(input_str) == expected_result



# trim

def test_trim():
    #позитивные
    assert utils.trim(" first") == "first"
    assert utils.trim("  Hi Where") == "Hi Where"
    assert utils.trim(" LOL ") == "LOL "
    # негативные
    assert utils.trim("569") == "569"
    assert utils.trim(" ") == ""

# to list

@pytest.mark.parametrize("string, delimeter, result", [
    ("coffee,tea,juice", ",", ["coffee", "tea", "juice"]),
    ("one,two,three", ",", ["one", "two", "three"]),
    ("1,2,3", ",", ["1", "2", "3"])
])

def test_to_list(string, delimeter, result):
    assert utils.to_list(string, delimeter) == result

#contains

@pytest.mark.parametrize("string, simbol, result",[
    ("tree", "r", True),
    ("Jary", "J", True),
    ("mark", "M", False),
    ("@info", "@", True),
    ("852", "5", True),
    #негативные
    ("art", "@", False),
    (" ", " ", True),
    ("", " ", False)
])
def test_contains(string, simbol, result):
     assert utils.contains(string, simbol) == result

#delete_symbol

@pytest.mark.parametrize("string, simbol, result", [
    ("pulse", "p", "ulse"),
    ("дом", "д", "ом"),
    ("1996", "9", "16"),
    ("$%&", "%", "$&"),
    #негативные
    ("tools", "p", "tools"),
    ("*&$", "@", "*&$"),
    (" ", "h", " "),
    ("", "", "")
])

def test_delete_symbol(string, simbol, result):
      assert utils.delete_symbol(string, simbol) == result

#starts_with

@pytest.mark.parametrize("string, simbol, result",[
    ("tree", "t", True),
    ("Jary", "J", True),
    ("mark", "M", False),
    ("@info", "@", True),
    ("852", "5", False),
    ("art", "@", False),
    (" ", " ", True),
    ("", " ", False),
    ("", "", True),
    (" root", " ", True)

])
def test_starts_with(string, simbol, result):
      assert utils.starts_with(string, simbol) == result

#end_with

@pytest.mark.parametrize("string, simbol, result",[
    ("tree", "e", True),
    ("Jary", "y", True),
    ("mark", "M", False),
    ("@info", "o", True),
    ("852", "2", True),
    ("art", "@", False),
    (" ", " ", True),
    ("", " ", False),
    ("", "", True),
    (" root ", " ", True)

])

def test_end_with(string, simbol, result):
   assert utils.end_with(string, simbol) == result

#is_empty

@pytest.mark.parametrize("string, result",[
    ("", True),
    ("mark",  False),
    (" ", True),
    ("", True)
])

def test_is_empty(string, result):
   assert utils.is_empty(string) == result

#list_to_string

@pytest.mark.parametrize("lst, joiner, result", [
    (["coffee", "juice"], " and ", "coffee and juice"),
    (["one", "two", "three"], "-", "one-two-three"),
    (["1","2","3"], ":", "1:2:3"),
    (["кот", "енот", "барсук"], " и ", "кот и енот и барсук"),
    (["l", "o", "l"], "@", "l@o@l"),
    (["u", "t", "a"], "1", "u1t1a")
])

def test_list_to_string(lst, joiner, result):
    assert utils.list_to_string(lst, joiner) == result
