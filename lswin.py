#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from dataclasses import dataclass, fields
from itertools import tee
from optparse import OptionParser
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
    rect_index = {'x': 0, 'y': 1, 'width': 2, 'height': 3}
    supported_sort_keys = tuple(
        [f.name for f in fields(WindowInfo) if f.name != 'rect']
        + list(rect_index.keys())
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
    )
    option_parser.add_option(
        '--exclude-0-area', dest='exclude_0_area', default=False,
        action='store_true', help='exclude windows with 0 area')
    option_parser.add_option(
        '-k', '--sort-key', dest='sort_key', default=[], action='append',
        help=f"sort key, can be {sort_keys_str}; default sort key is (pid, win_id)")
    options, _ = option_parser.parse_args()

    illegal_sort_keys = tuple(filter(lambda k: k not in supported_sort_keys, options.sort_key))
    if illegal_sort_keys:
        print(f"Unsupported sort key: {', '.join(illegal_sort_keys)}!"
              f" supported sort keys: {sort_keys_str}", file=sys.stderr)
        exit(1)

    ############################################################
    # biz logic
    ############################################################

    windows = list_window_infos()
    if options.exclude_0_area:
        windows = filter(lambda w: w.rect[2] > 0 and w.rect[3] > 0, windows)


    def sort_key(w: WindowInfo):
        key = []
        for k in options.sort_key:
            if hasattr(w, k):
                key.append(getattr(w, k))
            else:
                key.append(w.rect[rect_index[k]])
        return key + [w.pid, w.win_id]


    print_window_infos(sorted(windows, key=sort_key))
