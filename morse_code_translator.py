"""Converts text to and from Morse code"""

def convert_english_to_morse(line: str) -> str:
    "Converts a single english letter/number into morse line"
    morse_vocabulary = {"a": ".-", "b": "-...", "c": "-.-.", "d": "-..", 
    "e": ".", "f": "..-.", "g": "--.", "h": "....", "i": "..", "j": ".---", 
    "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---", "p": ".--.", 
    "l": ".-..", "m": "--", "n": "-.", "o": "---", "p": ".--.", "q": "--.-",
    "r": ".-.", "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", 
    "x": "-..-", "y": "-.--", "z": "--..", "1": ".----", "2": "..---", "3": 
    "...--", "4": "....-", "5": ".....", "6": "-....", "7": "--...", "8": 
    "---..", "9": "----.", "0": "-----", ".": ".-.-.-", ",": "--..--", "?": 
    "..--..", "/": "-..-.", " ": "/"}

    morse_code = ""
    for character in line:
        if (character in morse_vocabulary.keys()):
            morse_code += morse_vocabulary[character] + " "
        else:
            morse_code += " X "
    return morse_code[:-1]

print(convert_english_to_morse("cat"))

