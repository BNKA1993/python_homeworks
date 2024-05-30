import pytest
from string_utils import StringUtils

string_utils = StringUtils()

def test_capitalize_text():
    string_utils = StringUtils()
    res = string_utils.capitilize("google")
    assert res == "Google"

def test_capitalize_text_with_upper():
    string_utils = StringUtils()
    res = string_utils.capitilize("Google")
    assert res == "Google"
       
def test_capitalize_text_negative():
    string_utils = StringUtils()
    res = string_utils.capitilize("")
    assert res == ""
    
def test_trim_whitespace():
    string_utils = StringUtils()
    res = string_utils.trim("      Google")
    assert res == "Google"

def test_trim_whitespace():
    string_utils = StringUtils()
    res = string_utils.trim("")
    assert res == ""
    
def test_to_list():
    string_utils = StringUtils()
    res = string_utils.to_list("Строка,состоящая,из,пяти,слов")
    assert res == ["Строка", "состоящая", "из", "пяти", "слов"]
       
def test_to_list_empty_string_negative():
    string_utils = StringUtils()
    res = string_utils.to_list("")
    assert res == []    

def test_to_list_include_only_comma():
    string_utils = StringUtils()
    res = string_utils.to_list(",,,")
    assert res == ["", "", "", ""]

def test_include_symbol_contains_contains():
    string_utils = StringUtils()
    res = string_utils.contains("Google", "e")
    assert res == True

def test_not_include_symbol_contains():
    string_utils = StringUtils()
    res = string_utils.contains("Google", "y")
    assert res == False

def test_contains_empty_string():
    string_utils = StringUtils()
    res = string_utils.contains("", "y")
    assert res == False

def test_contains_empty_string_and_empty_symbol():
    string_utils = StringUtils()
    res = string_utils.contains("", "")
    assert res == True

def test_contains_numbers():
    string_utils = StringUtils()
    res = string_utils.contains("123", "3")
    assert res == True

def test_contains_include_special_symbol():
    string_utils = StringUtils()
    res = string_utils.contains("!@#%^&*", "#")
    assert res == True

def test_delete_symbol():
    string_utils = StringUtils()
    res = string_utils.delete_symbol("Google", "o")
    assert res == "Ggle"

def test_delete_symbol_empty_string():
    string_utils = StringUtils()
    res = string_utils.delete_symbol("", "o")
    assert res == ""

def test_delete_symbol_include_only_whitespace():
    string_utils = StringUtils()
    res = string_utils.delete_symbol("     ", " ")
    assert res == ""
    
def test_start_with():
    string_utils = StringUtils()
    res = string_utils.starts_with("Google", "G")
    assert res == True
     
def test_start_with():
    string_utils = StringUtils()
    res = string_utils.starts_with("Google", "o")
    assert res == False   

    
def test_start_with_numbers():
    string_utils = StringUtils()
    res = string_utils.starts_with("1Google", "1")
    assert res == True
    
    
def test_start_with_empty_string():
    string_utils = StringUtils()
    res = string_utils.starts_with("", "G")
    assert res == False

    
def test_start_with_whitespace():
    string_utils = StringUtils()
    res = string_utils.starts_with(" Google", " ")
    assert res == True
    
def test_end_with():
    string_utils = StringUtils()
    res = string_utils.end_with("Google", "e")
    assert res == True

def test_end_with():
    string_utils = StringUtils()
    res = string_utils.end_with("Google", "d")
    assert res == False

def test_end_with_number():
    string_utils = StringUtils()
    res = string_utils.end_with("Google2", "2")
    assert res == True

def test_end_with_special_symbol():
    string_utils = StringUtils()
    res = string_utils.end_with("Google#", "#")
    assert res == True

def test_end_with_empty_string():
    string_utils = StringUtils()
    res = string_utils.end_with("", "d")
    assert res == False
    
def test_end_with_empty_symbol():
    string_utils = StringUtils()
    res = string_utils.end_with("Google", "")
    assert res == True
    
def test_is_empty():
    string_utils = StringUtils()
    res = string_utils.is_empty("")
    assert res == True

def test_is_not_empty():
    string_utils = StringUtils()
    res = string_utils.is_empty("Google")
    assert res == False
    
def test_is_empty():
    string_utils = StringUtils()
    res = string_utils.is_empty("")
    assert res == True

def test_is_empty_with_whitespaces():
    string_utils = StringUtils()
    res = string_utils.is_empty("    ")
    assert res == True
 
def test_is_empty_with_tabulation():
    string_utils = StringUtils()
    res = string_utils.is_empty("\t\t")
    assert res == True
    
def test_list_to_string():
    string_utils = StringUtils()
    res = string_utils.list_to_string(["Google", "Chrome", 1])
    assert res == "Google, Chrome, 1"

def test_list_to_string_with_empty_lst():
    string_utils = StringUtils()
    res = string_utils.list_to_string([])
    assert res == ""

