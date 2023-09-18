#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from dataclasses import dataclass
from itertools import tee
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
    s_pid = 'PID'
    s_win_id = 'WinID'

    i_pid, i_win_id, i_rect = tee(win_list, 3)

    max_pid_chars = max(map(lambda w: len(str(w.pid)), i_pid))
    max_pid_chars = max(max_pid_chars, len(s_pid))

    max_wid_chars = max(map(lambda w: len(str(w.win_id)), i_win_id))
    max_wid_chars = max(max_wid_chars, len(s_win_id))

    max_rect_chars = max(map(lambda w: len(repr(w.rect)), i_rect))

    # print head
    print(f"{s_pid : >{max_pid_chars}}  {s_win_id : >{max_wid_chars}}"
          f"  {'(x, y, w, h)': <{max_rect_chars}}  [Title] SubTitle")
    print(f"{'-' * max_pid_chars}  {'-' * max_wid_chars}  {'-' * max_rect_chars}"
          f"  {'-' * (80 - max_pid_chars - max_wid_chars - max_rect_chars - 6)}")
    # print items
    for win in win_list:
        title_info = f"[{win.title}]{'' if not win.subtitle else ' ' + win.subtitle}"
        print(f"{win.pid: >{max_pid_chars}}  {win.win_id: >{max_wid_chars}}"
              f"  {win.rect!r: <{max_rect_chars}}  {title_info}")


if __name__ == '__main__':
    print_window_infos(sorted(
        list_window_infos(),
        key=lambda w: (w.pid, w.win_id)
    ))
