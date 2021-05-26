#! /usr/bin/env bash

python3 -m pip install -r requirement.txt

shell=$(cut -d/ -f3 <<< "${SHELL}")
echo "If you want to use it everywhere on your computer, add this line to your $shell.rc:"
echo '--> export PATH=$PATH'":$PWD"

