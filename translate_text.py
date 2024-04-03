#!/usr/bin/python
"""
Translate Text.
"""
###############################################################################
# Translate Text.
#
# SPDX-FileCopyrightText: Karel Zimmer <info@karelzimmer.nl>
# SPDX-License-Identifier: CC0-1.0
###############################################################################
from translate import Translator
# pip install translate

translator = Translator(from_lang='Spanish', to_lang='english')
result = translator.translate('Te amo')  # Enter text to translate
print(result)
