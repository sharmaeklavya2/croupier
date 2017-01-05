#!/bin/bash

set -e

python 'tests/gen_guess_output.py' 'tests/outputs2'
diff 'tests/outputs' 'tests/outputs2' > /dev/null
