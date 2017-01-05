# Croupier

This program connects `stdout` of program A with `stdin` of program B
and `stdout` of program B to `stdin` of program A.
It also prints the outputs from both programs so that they can be inspected.

This program was originally made for testing solutions to
[interactive problems on codeforces](http://codeforces.com/blog/entry/45307).

This program is compatible with both python 2 and python 3.

Run `python croupier.py --help` for information on how to use this program.

## Examples

`python croupier.py "bash samples/hello/hello.sh" "python samples/hello/hello.py"`:

```
A: I'm bash.
B: I'm python.
B: Nice to meet you, bash.
A: Nice to meet you, python.
```

You can also change program labels.

`python croupier.py --name1=bash "bash samples/hello/hello.sh" --name2=python "python samples/hello/hello.py"`:

```
bash: I'm bash.
python: I'm python.
python: Nice to meet you, bash.
bash: Nice to meet you, python.
```

## Tests

Run `tests/test_guess.sh` for automated testing.

`flake8` is used for linting python code.

Travis CI has been set up to run `tests/test_guess.sh` and `flake8`.

## License

This program is licensed under the [MIT License](http://www.opensource.org/licenses/MIT).
