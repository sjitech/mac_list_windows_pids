# `mac_list_windows_pids`

MacOS:  list all windows title and their owner process ids.

## Usage

Tested on `MacOS 13.4`, Python `3.7 ~ 3.11`.

*Note* if you run into error `No module named Quartz`, then run `pip install pyobjc-framework-Quartz` to install it.

```sh
$ python lswin.py
  PID  WinID  (x, y, w, h)           [Title] SubTitle
-----  -----  ---------------------  -------------------------------------------
  163  30498  (0, -24, 1920, 24)     [Window Server] Menubar
  163    382  (3906, -44, 1920, 24)  [Window Server]
  163    355  (0, -68, 1920, 24)     [Window Server] Menubar
  163    169  (0, 0, 1920, 24)       [Window Server]
  163    168  (0, 0, 1920, 24)       [Window Server] Menubar
  163      4  (4, 4, 26, 35)         [Window Server]
  187   6516  (751, 246, 417, 173)   [loginwindow]
  187   1512  (0, -40, 1004, 30)     [loginwindow]
  482     67  (0, 0, 1920, 1080)     [AXVisualSupportAgent]
  482     68  (0, 0, 1920, 1080)     [AXVisualSupportAgent]
  541  36561  (1173, 101, 367, 62)   [Google Chrome.app]
  541  36554  (0, 25, 1920, 1055)    [Google Chrome.app]
  541  32762  (1238, 242, 270, 74)   [Google Chrome.app]
  541    307  (400, 204, 1120, 876)  [Google Chrome.app]
  541  24548  (360, 236, 1200, 844)  [Google Chrome.app]
 2522    474  (836, 473, 247, 160)   [TextInputSwitcher]
 2525    255  (100, 852, 100, 128)   [Alfred]
 2525    288  (634, 306, 652, 126)   [Alfred]
 2525  11681  (100, 100, 1, 1)       [Alfred]
    ......
```

## Known problems

Processes created by Safari browser will be displayed as same PID as main Safari process.

https://github.com/sjitech/mac_list_windows_pids/issues/1
