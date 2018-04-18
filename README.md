# m2-correct
Tool to apply text error correction annotations in m2 format.

See the [MaxMatch Scorer](https://github.com/nusnlp/m2scorer/) for details on
file format.

## Dependencies
* Python 3.6
* pipenv

## Setup
```
pipenv install
```

## Usage
To apply m2-format corrections, run:
```
pipenv run python correct.py foo.m2
```
where `foo.m2` is your m2 file. This will print all sentences, with their
correction annotations applied, to stdout.

## License
See `LICENSE`.

The code in `parser.py` is taken from the [MaxMatch Scorer](https://github.com/nusnlp/m2scorer/), which is GNU GPL v2.0 licensed.
