import string

ALPHABET = string.ascii_lowercase


REFLECTOR_CONFIGS = {
    "B": "yruhqsldpxngokmiebfzcwvjat",
    "C": "fvpjiaoyedrzxwgctkuqsbnmhl",
}


class Reflector:
    """
    A reflector maps each letter to another letter, providing symmetry.
    """

    def __init__(self, wiring):
        """
        Initialize the reflector with a given wiring.

        :param wiring: A 26-letter string defining the reflector's mapping.
        """
        self.mapping = {k: v for k, v in zip(ALPHABET, wiring)}

    def reflect(self, letter):
        """
        Reflect a letter according to the reflector's wiring.

        :param letter: The letter to reflect.
        :return: The reflected letter.
        """
        return self.mapping[letter]