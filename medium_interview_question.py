import string


def get_key_to_letters():
    characters = string.ascii_lowercase
    digits = string.digits
    placeholder = {}
    index_point = 0
    for key in digits:
        if key == "0":
            placeholder[key] = " "
        elif key == "1":
            placeholder[key] = ""
        else:
            num_letter = 3
            if key in {"7", "9"}:
                num_letter = 4
            letters = characters[index_point: index_point + num_letter]
            placeholder[key] = letters
            index_point += num_letter
    return placeholder


KEY_TO_LETTER = get_key_to_letters()


def keypad_string(keys):
    '''
    Given a string consisting of 0-9,
    find the string that is created using
    a standard phone keypad
    | 1        | 2 (abc) | 3 (def)  |
    | 4 (ghi)  | 5 (jkl) | 6 (mno)  |
    | 7 (pqrs) | 8 (tuv) | 9 (wxyz) |
    |     *    | 0 ( )   |     #    |
    yYou can ignore 1, and 0 corresponds to space
    >>> keypad_string("12345")
    'adgj'
    >>> keypad_string("4433555555666")
    'hello'
    >>> keypad_string("2022")
    'a b'
    >>> keypad_string("")
    ''
    >>> keypad_string("111")
    ''
    '''
    # build the map from keys to letters
    # loop through the keys add the corresponding letter (taking into account keys pressed multiple times)

    result = ""
    count = 0
    prev_key = curr_key = ""
    for curr_key in keys:
        if curr_key == "1":
            pass
        else:
            if not prev_key:
                prev_key = curr_key
                count = 1
            else:
                current_key_letter = KEY_TO_LETTER[curr_key]
                if prev_key == curr_key:
                    if count == len(current_key_letter):
                        result += current_key_letter[-1]
                        count = 1
                    else:
                        count += 1
                else:
                    prev_letter = KEY_TO_LETTER[prev_key]
                    result += prev_letter[count - 1]
                    prev_key = curr_key
                    count = 1
    if curr_key:
        current_key_letter = KEY_TO_LETTER[curr_key]
        if len(current_key_letter) > 0:
            result += current_key_letter[count - 1]
    return result