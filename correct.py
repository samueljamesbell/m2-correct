import argparse


def apply_corrections(sentence, corrections):
    """Return a new sentence with corrections applied.

    Sentence should be a whitespace-separated tokenised string. Corrections
    should be a list of corrections.
    """
    tokens = sentence.split(' ')

    for c in corrections:
        tokens = _apply_correction(tokens, c)

    return ' '.join(tokens)


def _apply_correction(tokens, correction):
    """Apply a single correction to a list of tokens."""
    start_token_offset, end_token_offset, _, to_insert = correction
    return tokens[:start_token_offset] + to_insert + tokens[end_token_offset:]


def _parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('path', help='Path to text annotated with corrections')
    return parser.parse_args()


def _main():
    args = _parse_args()
    print(args)


if __name__ == '__main__':
    _main()
