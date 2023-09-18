#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import Quartz

# win_list = Quartz.CGWindowListCopyWindowInfo( Quartz.kCGWindowListOptionOnScreenOnly | Quartz.kCGWindowListExcludeDesktopElements, Quartz.kCGNullWindowID)
win_list = Quartz.CGWindowListCopyWindowInfo(Quartz.kCGWindowListOptionAll, Quartz.kCGNullWindowID)
win_list = sorted(win_list, key=lambda k: k.valueForKey_('kCGWindowOwnerPID'))

# print head
print('    PID  WinID  (x, y, w, h)              [Title] SubTitle')
print('-------  -----  ------------------------  -------------------------------------------')

# print items
for w in win_list:
    win_rect = (
        f"("
        f"{int(w.valueForKey_('kCGWindowBounds').valueForKey_('X'))},"
        f" {int(w.valueForKey_('kCGWindowBounds').valueForKey_('Y'))},"
        f" {int(w.valueForKey_('kCGWindowBounds').valueForKey_('Width'))},"
        f" {int(w.valueForKey_('kCGWindowBounds').valueForKey_('Height'))}"
        f")"
    )
    subtitle = w.valueForKey_('kCGWindowName')
    title_info = (
        f"[{w.valueForKey_('kCGWindowOwnerName') or ''}]"
        f"{'' if not subtitle else ' ' + subtitle}"
    )

    print(
        f"{w.valueForKey_('kCGWindowOwnerPID') or '?': >7}"
        f"  {w.valueForKey_('kCGWindowNumber') or '?': >5}"
        f"  {win_rect: <24}  {title_info}"
    )
