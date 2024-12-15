import string

ALPHABET = string.ascii_lowercase


class Enigma:
    """
    The Enigma machine: a combination of rotors, a reflector, and a plugboard,
    providing a letter substitution cipher with moving parts.
    """

    def __init__(self, rotors, reflector, plugboard):
        """
        Initialize the Enigma machine.

        :param rotors: A list of three Rotor objects [left, middle, right].
        :param reflector: A Reflector object.
        :param plugboard: A Plugboard object.
        """
        self.rotors = rotors
        self.reflector = reflector
        self.plugboard = plugboard

    def step_rotors(self):
        """
        Implement the Enigma stepping mechanism (double-stepping):

        Rules:
        - The rightmost rotor steps on every key press.
        - If the rightmost rotor hits its notch, it causes the middle rotor to step on the next press.
        - The middle rotor hitting its notch also causes the left rotor to step simultaneously
          (the double-step).

        Procedure each key press:
          1. If the middle rotor is at notch, advance the left rotor as well (double-step).
          2. If the middle rotor is at notch OR the right rotor is at notch, advance the middle rotor.
          3. Always advance the right rotor.
        """
        left, middle, right = self.rotors

        middle_at_notch = (ALPHABET[middle.position] == middle.notch)
        right_at_notch = (ALPHABET[right.position] == right.notch)

        if middle_at_notch:
            left.rotate()

        if middle_at_notch or right_at_notch:
            middle.rotate()

        right.rotate()

    def process(self, text):
        """
        Encrypt or decrypt the given text using the Enigma machine.

        :param text: The input text to process (string).
        :return: The resulting encrypted or decrypted text.
        """
        output = []
        for letter in text:

            if letter not in ALPHABET:
                # Non-letter characters pass unchanged
                output.append(letter)
                continue

            # Step rotors before each letter is processed
            self.step_rotors()

            # Pass through plugboard
            letter = self.plugboard.swap(letter)

            # Pass forward through the rotors (right to left)
            for rotor in reversed(self.rotors):
                letter = rotor.encode_forward(letter)

            # Reflect
            letter = self.reflector.reflect(letter)

            # Pass backward through the rotors (left to right)
            for rotor in self.rotors:
                letter = rotor.encode_backward(letter)

            # Pass through plugboard again
            letter = self.plugboard.swap(letter)

            output.append(letter)

        return ''.join(output)