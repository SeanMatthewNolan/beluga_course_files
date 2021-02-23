# Define character to morse mappings here
lookup_dict = {
    'a': '.-',    'b': '-...',  'c': '-.-.',  'd': '-..',   'e': '.',
    'f': '..-.',  'g': '--.',   'h': '....',  'i': '..',    'j': '.---',
    'k': '-.-',   'l': '.-..',  'm': '--',    'n': '-.',    'o': '---',
    'p': '.--.',  'q': '--.-',  'r': '.-.',   's': '...',   't': '-',
    'u': '..-',   'v': '...-',  'w': '.--',   'x': '-..-',  'y': '-.--',
    'z': '--..',  '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '0': '-----', ' ': '|'
}


def text_to_morse(text):
    # Make text lowercase because case doen't matter for Morse code
    text = text.lower()

    # Intialize output string
    out = ''

    # Iterate through each character in the string
    for char in text:
        # If char is letter, number, or space
        if char in lookup_dict.keys():
            out += lookup_dict[char] + ' '

    return out


if __name__ == '__main__':

    # Test function
    test_strings = [
        'Hello World',
        'The quick brown fox jumps over the lazy dog',
        'In principio erat Verbum, et Verbum erat apud Deum, et Deus erat Verbum.'
    ]

    morse_results = [text_to_morse(test_string) for test_string in test_strings]

    for input_string, output_string in zip(test_strings, morse_results):
        print('{0}\n{1}\n\n'.format(input_string, output_string))
