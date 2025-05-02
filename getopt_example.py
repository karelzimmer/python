#!/usr/bin/env python3
###############################################################################
# SPDX-FileComment: Vervang argparse door getopt in Python scripts /
#                   Replace argparse with getopt in Python scripts
# Vervang: https://docs.python.org/3/library/argparse.html
#    door: https://docs.python.org/3/library/getopt.html
#
#          getopt - C-style parser for command line options
#
# # SPDX-FileCopyrightText: Karel Zimmer <info@karelzimmer.nl>
# SPDX-License-Identifier: CC0-1.0
###############################################################################


###############################################################################
# Imports
###############################################################################

import getopt
import sys


###############################################################################
# Constants
###############################################################################

PROGRAM_NAME: str = 'getopt_example.py'
PROGRAM_DESC: str = 'Vervang argparse door getopt in Python scripts'

OPTIONS_SHORT: str = 'hmuv'
OPTIONS_SHORT += 'g'
OPTIONS_SHORT += 'f:'       # option -f requires argument
OPTIONS_LONG: list = ['help', 'manual', 'usage', 'version']
OPTIONS_LONG += ['gui']     # Combineren alg. opties met spec. opties is mog.
OPTIONS_LONG += ['file=']   # option --file requires argument

###############################################################################
# Globals
###############################################################################


###############################################################################
# Main
###############################################################################

args: list = []
err: str = ''
opt: str = ''
opts: list = []

print(f'# Inhoud OPTIONS_SHORT: {OPTIONS_SHORT}')
print(f'# Inhoud OPTIONS_LONG : {OPTIONS_LONG}\n')

try:
    opts, args = getopt.gnu_getopt(sys.argv[1:], OPTIONS_SHORT, OPTIONS_LONG)
except getopt.error as err:
    print(f'{PROGRAM_NAME}: {err}')
    sys.exit(1)

for opt, arg in opts:
    if opt in ('-h', '--help'):
        print(f'{PROGRAM_NAME}: optie {opt} opgegeven')
    elif opt in ('-m', '--manual'):
        print(f'{PROGRAM_NAME}: optie {opt} opgegeven')
    elif opt in ('-u', '--usage'):
        print(f'{PROGRAM_NAME}: optie {opt} opgegeven')
    elif opt in ('-v', '--version'):
        print(f'{PROGRAM_NAME}: optie {opt} opgegeven')
    elif opt in ('-f', '--file'):
        print(f'{PROGRAM_NAME}: optie {opt} opgegeven')
        print(f'{PROGRAM_NAME}: > argument {arg} opgegeven')
    else:
        # Zou niet voor moeten komen als OPTIONS_SHORT/_SHORT 1:1 met if's. 
        print(f'{PROGRAM_NAME}: {opt}: niet-afgehandelde optie')

print(f'\n# Opgegeven argumenten: {args}')
