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
from io import BytesIO
import argparse

def proccess_file(f, add=None):
    r = ""
    while f.read(1) != b'':
        f.seek(f.tell()-1)
        b = f.read(1)
        if b == b'{':
            bracket_counter = 1
            with BytesIO() as entry:
                entry.write(b)
                if add != None:
                    for x in add: entry.write(x.encode())
                while bracket_counter != 0:
                    b = f.read(1)
                    entry.write(b)
                    if   b == b'{': bracket_counter += 1
                    elif b == b'}': bracket_counter -= 1
                    else: pass
                r += json.dumps(json.loads(str(entry.getvalue(), 'utf-8'))) + "\n"
    return r

parser = argparse.ArgumentParser(description='Clean up N00b data', epilog='You\'re a Terrible Person.')
parser.add_argument('files', help='Terrible json files, or stdin if not specified', nargs='+', type=argparse.FileType('rb'), default=sys.stdin)
parser.add_argument('--out', help='Cleaned up json, else stdout', type=argparse.FileType('w'), default=sys.stdout)
parser.add_argument('--add', help='Add custom json to every entry', type=str, default=None)
args = parser.parse_args()

for f in args.files:
    args.out.write(proccess_file(f, args.add))
