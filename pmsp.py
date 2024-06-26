#!/usr/bin/python
###############################################################################
# Python Module Search Path (PMSP)
#
# SPDX-FileCopyrightText: Karel Zimmer <info@karelzimmer.nl>
# SPDX-License-Identifier: CC0-1.0
###############################################################################

import sys

for path in sys.path:
    print(path)

# Bovenstaande opdrachten in Python shell:
# /usr/lib/python38.zip
# /usr/lib/python3.8
# /usr/lib/python3.8/lib-dynload
# /home/karel/.local/lib/python3.8/site-packages
# /usr/local/lib/python3.8/dist-packages
# /usr/lib/python3/dist-packages

# Dit script vanaf Linux command line, python pmsp.py:
# /home/karel/python_work <== ontbreekt in de shell !
# /usr/lib/python38.zip
# /usr/lib/python3.8
# /usr/lib/python3.8/lib-dynload
# /home/karel/.local/lib/python3.8/site-packages
# /usr/local/lib/python3.8/dist-packages
# /usr/lib/python3/dist-packages
