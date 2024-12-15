import argparse
from enigma import Enigma
from rotor import Rotor, ROTOR_CONFIGS
from reflector import Reflector, REFLECTOR_CONFIGS
from plugboard import Plugboard





def parse_args():
    """
    Parse command-line arguments for the Enigma machine emulator.

    Example:
        python enigma.py --rotors I II III --positions a b c --rings a a a --reflector B --plugboard ab cd ef --text "hello world"
    """
    parser = argparse.ArgumentParser(description="Enigma I Machine Emulator")
    parser.add_argument("--rotors", nargs=3, required=True,
                        help="Three rotors in order (I, II, III, IV, V). "
                             "Example: --rotors I II III")
    parser.add_argument("--positions", nargs=3, required=True,
                        help="Initial positions for each rotor (e.g., a b c)")
    parser.add_argument("--rings", nargs=3, required=True,
                        help="Ring settings for each rotor (e.g., a a a)")
    parser.add_argument("--reflector", choices=["B", "C"], required=True,
                        help="Reflector to use (B or C)")
    parser.add_argument("--plugboard", nargs="*", default=[],
                        help="Plugboard pairs (e.g., ab cd ef). "
                             "Each pair is two letters, e.g. 'ab'.")
    parser.add_argument("--text", required=True,
                        help="Text to encrypt/decrypt")

    return parser.parse_args()


def main():
    args = parse_args()

    # Create rotor objects based on provided args
    rotors = [
        Rotor(ROTOR_CONFIGS[rotor]["wiring"], ROTOR_CONFIGS[rotor]["notch"], position, ring)
        for rotor, position, ring in zip(args.rotors, args.positions, args.rings)
    ]

    # Create reflector and plugboard
    reflector = Reflector(REFLECTOR_CONFIGS[args.reflector])
    plugboard = Plugboard(args.plugboard)

    # Create and run the Enigma machine
    enigma = Enigma(rotors, reflector, plugboard)
    result = enigma.process(args.text.lower())
    print("Result:", result)


if __name__ == "__main__":
    main()

# --rotors I II III --positions a b c --rings a a a --reflector B --plugboard ab cd ef --text "Hello, world!"