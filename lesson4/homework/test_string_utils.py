import pytest
from string_utils import StringUtils

string_utils = StringUtils()


@pytest.mark.positive_test
@pytest.mark.parametrize('input_string, expected_output', [
    ("google", "Google"),
    ("Google", "Google")])
def test_capitalize_text_positive(input_string, expected_output):
    string_utils = StringUtils()
    res = string_utils.capitilize(input_string)
    assert res == expected_output


@pytest.mark.negative_test
@pytest.mark.parametrize('input_string, expected_output', [
    ("", "")
])
def test_capitalize_text_negative(input_string, expected_output):
    string_utils = StringUtils()
    res = string_utils.capitilize(input_string)
    assert res == expected_output


@pytest.mark.positive_test
@pytest.mark.parametrize('input_string, expected_output', [
    ("      Google", "Google"),
    ("", ""),
    ("   ", "")])
def test_trim_whitespace_positive(input_string, expected_output):
    string_utils = StringUtils()
    res = string_utils.trim(input_string)
    assert res == expected_output


@pytest.mark.positive_test
@pytest.mark.parametrize('input_string, expected_output', [
    ("Строка,состоящая,из,пяти,слов",
     ["Строка", "состоящая", "из", "пяти", "слов"]),
    (",,,", ["", "", "", ""]),
    ("один", ["один"])
])
def test_to_list_positive(input_string, expected_output):
    string_utils = StringUtils()
    res = string_utils.to_list(input_string)
    assert res == expected_output


@pytest.mark.negative_test
@pytest.mark.parametrize('input_string, expected_output', [("", [])])
def test_to_list_negative(input_string, expected_output):
    string_utils = StringUtils()
    res = string_utils.to_list(input_string)
    assert res == expected_output


@pytest.mark.positive_test
@pytest.mark.parametrize('input_string, letter, result', [
    ("Google", "e", True),
    ("", "", True),
    ("123", "3", True),
    ("!@#%^&*", "#", True)
])
def test_contains_positive(input_string, letter, result):
    string_utils = StringUtils()
    res = string_utils.contains(input_string, letter)
    assert res == result


@pytest.mark.negative_test
@pytest.mark.parametrize('input_string, letter, result', [
    ("Google", "y", False),
    ("Google", "y", False),
    ("", "j", False)
])
def test_contains_negative(input_string, letter, result):
    string_utils = StringUtils()
    res = string_utils.contains(input_string, letter)
    assert res == result


@pytest.mark.positive_test
@pytest.mark.parametrize('input_string, symbol, result', [
    ("Google", "o", "Ggle"),
    (" ", " ", "")
])
def test_delete_symbol_positive(input_string, symbol, result):
    string_utils = StringUtils()
    res = string_utils.delete_symbol(input_string, symbol)
    assert res == result


@pytest.mark.negative_test
@pytest.mark.parametrize('input_string, symbol, result', [
    ("Google", "y", "Google"),
    ("", "o", "")
])
def test_delete_symbol_negative(input_string, symbol, result):
    string_utils = StringUtils()
    res = string_utils.delete_symbol(input_string, symbol)
    assert res == result


@pytest.mark.positive_test
@pytest.mark.parametrize('input_string, letter, result', [
    ("Google", "G", True),
    ("1Google", "1", True),
    (" Google", " ", True)
])
def test_start_with_positive(input_string, letter, result):
    string_utils = StringUtils()
    res = string_utils.starts_with(input_string, letter)
    assert res == result


@pytest.mark.negative_test
@pytest.mark.parametrize('input_string, letter, result', [
    ("Google", "o", False),
    ("", "G", False)
])
def test_start_with_negative(input_string, letter, result):
    string_utils = StringUtils()
    res = string_utils.starts_with(input_string, letter)
    assert res == result


@pytest.mark.positive_test
@pytest.mark.parametrize('input_string, letter, result', [
    ("Google", "e", True),
    ("Google2", "2", True),
    ("Google#", "#", True),
    ("Google", "", True)
])
def test_end_with_positive(input_string, letter, result):
    string_utils = StringUtils()
    res = string_utils.end_with(input_string, letter)
    assert res == result


@pytest.mark.negative_test
@pytest.mark.parametrize('input_string, letter, result', [
    ("Google", "d", False),
    ("", "d", False)
])
def test_end_with_negative(input_string, letter, result):
    string_utils = StringUtils()
    res = string_utils.end_with(input_string, letter)
    assert res == result


@pytest.mark.positive_test
@pytest.mark.parametrize('input_string, result', [
    ("Google", False),
    ("", True),
    ("    ", True)
])
def test_is_empty_positive(input_string, result):
    string_utils = StringUtils()
    res = string_utils.is_empty(input_string)
    assert res == result


@pytest.mark.negative_test
@pytest.mark.parametrize('input_string, result', [
    ("\t\t", True)
])
def test_is_empty_negative(input_string, result):
    string_utils = StringUtils()
    res = string_utils.is_empty(input_string)
    assert res == result


@pytest.mark.positive_test
@pytest.mark.parametrize('lst, joiner, result', [
    (["Google", "Chrome", 1], ",", "Google,Chrome,1"),
    ([], ",", ""),
    (["One"], ",", "One")
])
def test_list_to_string_positive(lst, joiner, result):
    string_utils = StringUtils()
    res = string_utils.list_to_string(lst, joiner)
    assert res == result
