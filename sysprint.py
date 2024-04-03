#!/usr/bin/python
"""
Print System Information.
"""
###############################################################################
# Print System Information.
#
# SPDX-FileCopyrightText: Karel Zimmer <info@karelzimmer.nl>
# SPDX-License-Identifier: CC0-1.0
###############################################################################

import sys

print("Name of script:",  sys.argv[0])
print("Number of args:",  len(sys.argv))
print("The argum. are:", str(sys.argv))
