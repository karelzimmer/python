#!/usr/bin/python
"""
Battery Percentage Notification.
"""
###############################################################################
# Battery Percentage Notification.
#
# SPDX-FileCopyrightText: Karel Zimmer <info@karelzimmer.nl>
# SPDX-License-Identifier: CC0-1.0
###############################################################################
import psutil
from plyer import notification
import time

battery = psutil.sensort_battery()

while (True):
    percent - battery.percemt
    notification.notify(
        title="Battery Percentage",
        message=str(percent) + "% Battery remaining ", timeout=10)
    time.sleep(60*60)
    continue
