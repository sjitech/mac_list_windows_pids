#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from dataclasses import dataclass
from typing import Tuple, Iterable

import Quartz


@dataclass
class WindowInfo:
    pid: int
    win_id: int

    rect: Tuple[int, int, int, int]
    """
    rect: (x, y, width, height)
    """

    title: str
    subtitle: str


def list_window_infos() -> Iterable[WindowInfo]:
    return (
        WindowInfo(
            pid=int(w.valueForKey_('kCGWindowOwnerPID')),
            win_id=int(w.valueForKey_('kCGWindowNumber')),
            rect=(
                int(w.valueForKey_('kCGWindowBounds').valueForKey_('X')),
                int(w.valueForKey_('kCGWindowBounds').valueForKey_('Y')),
                int(w.valueForKey_('kCGWindowBounds').valueForKey_('Width')),
                int(w.valueForKey_('kCGWindowBounds').valueForKey_('Height')),
            ),
            title=str(w.valueForKey_('kCGWindowOwnerName') or ''),
            subtitle=str(w.valueForKey_('kCGWindowName') or '')
        )
        for w in Quartz.CGWindowListCopyWindowInfo(Quartz.kCGWindowListOptionAll, Quartz.kCGNullWindowID)
    )


def print_window_infos(win_list: Iterable[WindowInfo]):
    # print head
    print('    PID  WinID  (x, y, w, h)              [Title] SubTitle')
    print('-------  -----  ------------------------  --------------------------------------')
    # print items
    for w in win_list:
        title_info = f"[{w.title or ''}]{'' if not w.subtitle else ' ' + w.subtitle}"
        print(f"{w.pid: >7}  {w.win_id: >5}  {w.rect!r: <24}  {title_info}")


if __name__ == '__main__':
    print_window_infos(sorted(
        list_window_infos(),
        key=lambda k: (k.pid, k.win_id))
    )
