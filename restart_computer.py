#!/usr/bin/python
"""
Restart Computer.
"""
###############################################################################
# Restart Computer.
#
# SPDX-FileCopyrightText: Karel Zimmer <info@karelzimmer.nl>
# SPDX-License-Identifier: CC0-1.0
###############################################################################

import os

restart = input("Do you wish to restart your computer ? (yes / no): ")

if restart == 'no':
    exit()
else:
    os.system("shutdown -r -t 1")
