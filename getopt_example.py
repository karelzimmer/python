#!/usr/bin/env python3
###############################################################################
# Vervang argparse door getopt?
# vervang https://docs.python.org/3/library/argparse.html
#    door https://docs.python.org/3/library/getopt.html
###############################################################################

import getopt
import sys

OPTIONS_SHORT = 'hmuv'
OPTIONS_LONG = ["help", "manual", "usage"]
OPTIONS_LONG += ["version"]  # Is voor combineren alg. opties met spec. opties

print(OPTIONS_LONG)

try:
    opts, args = getopt.gnu_getopt(sys.argv[1:], OPTIONS_SHORT, OPTIONS_LONG)
except getopt.error as err:
    print('<program_name>:', err)
    sys.exit(1)

for opt, arg in opts:
    if opt in ("-h", "--help"):
        print('Help opgegeven')
    elif opt in ("-m", "--manual"):
        print('Manual opgegeven')
    elif opt in ("-u", "--usage"):
        print('Usage opgegeven')
    elif opt in ("-v", "--version"):
        print('Version opgegeven')
    else:
        assert False, "unhandled option"

print('args:', args)