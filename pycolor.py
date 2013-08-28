#!/usr/bin/env python
#-*- coding:utf-8 -*-

# Copyright (C) 
# 
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program; If not, see <http://www.gnu.org/licenses/>.
# 
# 2013 - Long Changjin <admin@longchangjin.cn>

#ntensity   0       1     2       3          4       5         6        7
#Normal     Black   Red   Green   Yellow     Blue    Magenta   Cyan     White
#Bright     Black   Red   Green   Yellow     Blue    Magenta   Cyan     White

NORMAL_BLACK = 0
NORMAL_RED = 1
NORMAL_GREEN = 2
NORMAL_YELLOW = 3
NORMAL_BLUE = 4
NORMAL_MAGENTA = 5
NORMAL_CYAN = 6
NORMAL_WHITE = 7
BRIGHT_BLACK = 8
BRIGHT_RED = 9
BRIGHT_GREEN = 10
BRIGHT_YELLOW = 11
BRIGHT_BLUE = 12
BRIGHT_MAGENTA = 13
BRIGHT_CYAN = 14
BRIGHT_WHITE = 15

COLOR_MIN = 0
COLOR_MAX = 15
COLOR_COUNT = 16

BG_ESCAPE = "\x1b[48;5;%dm"
FG_ESCAPE = "\x1b[38;5;%dm"
END_ESCAPE = "\x1b[0m"


def color_context(text, bgcolor=None, fgcolor=None):
    if fgcolor is not None and COLOR_MIN <= fgcolor <= COLOR_MAX:
        text = "%s%s%s" % (FG_ESCAPE % fgcolor, text, END_ESCAPE)
    if bgcolor is not None and COLOR_MIN <= bgcolor <= COLOR_MAX:
        text = "%s%s%s" % (BG_ESCAPE % bgcolor, text, END_ESCAPE)
    return text

if __name__ == '__main__':
    i = NORMAL_BLACK
    while i < COLOR_COUNT:
        print color_context(" t ", i, NORMAL_YELLOW),
        i += 1
    print
