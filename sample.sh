#!/usr/bin/env bash

echo "I'm bash."
read line
name="${line:4:(-1)}"
echo "Nice to meet you, $name."
