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

# Usage Example 1:
# test = BruteForce(3)
# while test.step(): print(test.generator())

# Usage Example 2:
# for x in range(1,9):
#     test = BruteForce(x)
#     while test.step(): print(test.generator())

import random

class BruteForce():
        mapy_num = ('0','1','2','3','4','5','6','7','8','9')
        mapy_low_alpha  = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
        mapy_high_alpha = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
        mapy_special_common = ('!', '@', '#', '$', '%', '^', '&', '*', '.', ',', '+', '=', '_', '-', '?')

        def __init__(self, length, mapy=None, randomize=True):
                if mapy == None:
                        self.mapy = list(BruteForce.mapy_num + BruteForce.mapy_low_alpha + BruteForce.mapy_high_alpha)
                else:
                        self.mapy = list(mapy)
                self.pos = {x:0 for x in range(0, length)}
                self.length = length
                self.nomore = True
                self.ret = None
                if randomize == True:
                    random.shuffle(self.mapy)

        def get_map(self):
            return tuple(self.mapy)

        def step(self):
                self.pos[0] = self.pos[0] + 1
                for x in range(0, self.length):
                        if self.pos[x] == len(self.mapy):
                                        self.pos[x] = 0
                                        if x+1 == self.length:
                                            self.nomore = False
                                        else:
                                            self.pos[x+1] = self.pos[x+1] + 1
                return self.nomore

        def generator(self):
            ret = ''.join((self.mapy[self.pos[x]] for x in range(0, self.length)))
            return ret
