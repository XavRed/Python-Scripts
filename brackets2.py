#!/usr/bin/env python3

# Copyright (c) 2020 XavRed
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import sys
import json
from io import StringIO
import argparse

def proccess_file_2(f, o, add=None):
    line = f.readline()
    while line != "":
        if line == "{\n":
            with StringIO() as entry:
                entry.write(line)
                if add != None: entry.write(add)
                while line != "}\n":
                    line = f.readline()
                    entry.write(line)
                o.write(json.dumps(json.loads(entry.getvalue())) + "\n")
        line = f.readline()

parser = argparse.ArgumentParser(description='Clean up N00b data', epilog='You\'re a Terrible Person.')
parser.add_argument('files', help='Terrible json files, or stdin if not specified', nargs='+', type=argparse.FileType('r', encoding="utf-8"), default=sys.stdin)
parser.add_argument('--out', help='Cleaned up json, else stdout', type=argparse.FileType('w', encoding="utf-8"), default=sys.stdout)
parser.add_argument('--add', help='Add custom json to every entry', type=str, default=None)
args = parser.parse_args()

for f in args.files:
    proccess_file_2(f, args.out)
