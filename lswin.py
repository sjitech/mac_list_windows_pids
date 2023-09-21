#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from dataclasses import dataclass, fields
from itertools import tee
from optparse import OptionParser
from typing import Iterable

import Quartz


@dataclass
class Rect:
    x: int
    y: int
    width: int
    height: int

    def t(self):
        """
        tuple representation
        """
        return self.x, self.y, self.width, self.height

    def s(self):
        """
        tuple style string for output
        """
        return str(self.t())


@dataclass
class WindowInfo:
    pid: int
    win_id: int

    rect: Rect

    title: str
    subtitle: str


def list_window_infos() -> Iterable[WindowInfo]:
    return (
        WindowInfo(
            pid=int(w.valueForKey_('kCGWindowOwnerPID')),
            win_id=int(w.valueForKey_('kCGWindowNumber')),
            rect=Rect(
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

    max_pid_chars = max(len(str(w.pid)) for w in i_pid)
    max_pid_chars = max(max_pid_chars, len(s_pid))

    max_wid_chars = max(len(str(w.win_id)) for w in i_win_id)
    max_wid_chars = max(max_wid_chars, len(s_win_id))

    max_rect_chars = max(len(w.rect.s()) for w in i_rect)

    # print head
    print(f"{s_pid : >{max_pid_chars}}  {s_win_id : >{max_wid_chars}}"
          f"  {'(x, y, w, h)': <{max_rect_chars}}  [Title] SubTitle")
    print(f"{'-' * max_pid_chars}  {'-' * max_wid_chars}  {'-' * max_rect_chars}"
          f"  {'-' * (80 - max_pid_chars - max_wid_chars - max_rect_chars - 6)}")
    # print items
    for win in win_list:
        title_info = f"[{win.title}]{'' if not win.subtitle else ' ' + win.subtitle}"
        print(f"{win.pid: >{max_pid_chars}}  {win.win_id: >{max_wid_chars}}"
              f"  {win.rect.s(): <{max_rect_chars}}  {title_info}")


if __name__ == '__main__':
    supported_sort_keys = tuple(
        [f.name for f in fields(WindowInfo) if f.name != 'rect']
        + [f.name for f in fields(Rect)]
    )
    sort_keys_str = ', '.join(supported_sort_keys)

    ############################################################
    # parse options
    ############################################################

    option_parser = OptionParser(
        '%prog [OPTION]...'
        '\nlist all windows title and their owner process ids.'
        '\n\nExamples:'
        '\n  %prog'
        '\n  %prog --exclude-0-area'
        '\n  %prog --sort-key x --sort-key title'
        '\n  %prog --keep-one-for-same-pid-rect'
    )
    option_parser.add_option(
        '-Z', '--exclude-0-area', dest='exclude_0_area', default=False,
        action='store_true', help='exclude windows with 0 area')
    option_parser.add_option(
        '-o', '--keep-one-for-same-pid-rect', dest='keep_one_for_same_pid_rect',
        default=False, action='store_true', help='keep only one window for same (pid, rect)')
    option_parser.add_option(
        '-k', '--sort-key', dest='sort_keys', default=[], action='append', metavar='SORT_KEY',
        help=f"sort key, can be {sort_keys_str}; default sort key is (pid, win_id)")

    options, _ = option_parser.parse_args()

    illegal_sort_keys = tuple(k for k in options.sort_keys if k not in supported_sort_keys)
    if illegal_sort_keys:
        print(f"Unsupported sort key: {', '.join(illegal_sort_keys)}!"
              f" supported sort keys: {sort_keys_str}", file=sys.stderr)
        exit(1)

    ############################################################
    # biz logic
    ############################################################

    windows = list_window_infos()
    if options.exclude_0_area:
        windows = (w for w in windows if w.rect.width > 0 and w.rect.height > 0)
    if options.keep_one_for_same_pid_rect:
        windows = {(w.pid, w.rect.t()): w for w in windows}.values()

    print_window_infos(sorted(
        windows, key=lambda w: tuple(
            getattr(w, k) if hasattr(w, k) else getattr(w.rect, k)
            for k in options.sort_keys
        ) + (w.pid, w.win_id)
    ))
