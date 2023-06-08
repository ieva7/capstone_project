"""Testing the morse vocabulary with 'The quick brown fox 
jumps over lazy dog. 01234567890?,/'"""
from morse_code_translator import convert_english_to_morse


def test_word_the():
    assert convert_english_to_morse("the") == "- .... ."


def test_word_quick():
    assert convert_english_to_morse("quick") ==  "--.- ..- .. -.-. -.-"


def test_word_brown():
    assert convert_english_to_morse("brown") == "-... .-. --- .-- -."


def test_word_fox():
    assert convert_english_to_morse("fox") == "..-. --- -..-"


def test_word_jumps():
    assert convert_english_to_morse("jumps") == ".--- ..- -- .--. ..."


def test_word_over():
    assert convert_english_to_morse("over") == "--- ...- . .-."


def test_word_lazy():
    assert convert_english_to_morse("lazy") == ".-.. .- --.. -.--"


def test_word_dog():
    assert convert_english_to_morse("dog") == "-.. --- --."


def test_numbers_and_symbols():
    assert convert_english_to_morse(". 01234567890?,/") == ".-.-.- / ----- .---- ..--- ...-- ....- ..... -.... --... ---.. ----. ----- ..--.. --..-- -..-."