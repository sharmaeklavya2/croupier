# Croupier

This program connects `stdout` of program A with `stdin` of program B
and `stdout` of program B to `stdin` of program A.
It also prints the outputs from both programs so that they can be inspected.

This program was originally made for testing solutions to
[interactive problems on codeforces](http://codeforces.com/blog/entry/45307).

Run `python croupier.py --help` for information on how to use this program.

Run `python croupier.py "bash sample.sh" "python sample.py"` to see a demo.

This program is compatible with both python 2 and python 3.

## License

This program is licensed under the [MIT License](http://www.opensource.org/licenses/MIT).
