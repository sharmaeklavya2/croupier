#!/bin/bash

set -e
set -x

tests/test_guess.sh
flake8
