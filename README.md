# mac_list_windows_pids
Mac OS X:  list all windows title and their owner process ids

##Usage:  

Tested on OS X Yosemite 10.10.5, Python 2.7

*Note* if you run into error `No module named Quartz`, then run `pip install pyobjc-framework-Quartz` to install it.

	$ python lswin.py

	    PID WinID  x,y,w,h               	[Title] SubTitle
	------- -----  --------------------- 	-------------------------------------------
	    169  1956 {0,-38,1280,25        }	[Window Server] Backstop Menubar
	    169  1955 {0,-60,1280,22        }	[Window Server] Menubar
	    169   396 {0,-38,1280,25        }	[Window Server] Backstop Menubar
	    169   395 {0,-60,1280,22        }	[Window Server] Menubar
	    169     6 {0,0,0,0              }	[Window Server] Cursor
	    169     4 {0,22,1280,25         }	[Window Server] Backstop Menubar
	    169     3 {0,0,1280,22          }	[Window Server] Menubar
	    169     2 {0,0,1280,800         }	[Window Server] Desktop
	    262   404 {0,-38,1280,38        }	[Google Chrome] 
	    262   393 {0,0,1280,800         }	[Google Chrome] 
	    262   380 {100,100,1,1          }	[Google Chrome] Focus Proxy
	    262   351 {1189,45,46,18        }	[Google Chrome] 
	    262    51 {0,0,1280,800         }	[Google Chrome] sjitech/mac_list_windows_pids
	    262    50 {0,755,1,1            }	[Google Chrome] 
	    262    43 {0,0,1280,22          }	[Google Chrome]
	    262    42 {0,0,1280,22          }	[Google Chrome]
	    266  3294 {0,23,1276,777        }	[Sublime Text] README.md — mac_list_windows_pids
	    266  1954 {0,-38,1280,38        }	[Sublime Text] 
	    266  1953 {0,0,1280,800         }	[Sublime Text] 
	    266  1952 {0,0,1280,800         }	[Sublime Text] 
	    266   345 {529,83,116,56        }	[Sublime Text] 
	    266   188 {100,100,1,1          }	[Sublime Text] Focus Proxy
	    266   186 {0,0,1280,22          }	[Sublime Text]
	    266   185 {0,0,1280,22          }	[Sublime Text]
	    266    93 {0,0,1280,800         }	[Sublime Text] lswin
	    ... ...


##Known problems

Processes created by Safari browser will be displayed as same PID as main Safari process.

https://github.com/sjitech/mac_list_windows_pids/issues/1


