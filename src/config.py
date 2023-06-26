"""This module introduces global variables"""

from pathlib import Path

word_type = ''
num_of_keys = 0

radios_word_type = []
radios_num_of_keys = []

buttons_with_translation = []

using_prefixes = False
using_suffixes = False
using_endings = False

language = 'eng'

FONT = ('Bitter', 12)
FONT_LRG = ('Bitter', 14)
FONT_INPUT = ('Bitter', 10)

COLOR_FONT = '#453E30'
COLOR_FONT_DARK = '#232218'
COLOR_BG = '#D3B890'
COLOR_FIELD = '#EDDECC'

images_path = f'{Path.cwd()}\\assets\\images'

default_output = '✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦'
