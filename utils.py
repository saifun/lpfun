A_APOSTROPHE_UNICODE = '\u00e0'
ALEF = 'א'
HEBREW_ALPHABET_SIZE = 28


def convert_manufacturer_to_hebrew(manufacturer_name):
    return ''.join((translate_letter(letter) for letter in manufacturer_name))


def translate_letter(letter):
    if 0 <= ord(letter) - ord(A_APOSTROPHE_UNICODE) <= HEBREW_ALPHABET_SIZE:
        return chr(ord(ALEF) + ord(letter) - ord(A_APOSTROPHE_UNICODE))
    return letter
