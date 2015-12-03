# mac_list_windows_pids
Mac OS X:  list all windows title and their owner process ids

##Usage:

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
	    267  3269 {0,0,16,609           }	[Terminal]
	    267  3246 {0,0,16,609           }	[Terminal]
	    267  2450 {345,178,650,542      }	[Terminal] エンコーディング
	    267   643 {100,100,1,1          }	[Terminal] Focus Proxy
	    267   183 {0,0,16,16            }	[Terminal]
	    267   182 {0,0,1280,22          }	[Terminal]
	    267   181 {0,0,1280,22          }	[Terminal]
	    267    91 {0,0,16,16            }	[Terminal]
	    267    30 {73,103,1179,632      }	[Terminal] mytest — Python — 167×43
	    267    29 {20,45,1165,632       }	[Terminal] mac_list_windows_pids — Python — 165×43
	    272  1515 {0,0,1280,22          }	[Dictionary]
	    272  1514 {0,0,1280,22          }	[Dictionary]
	    272    83 {541,110,690,650      }	[Dictionary] 辞書
	    274   454 {0,0,1280,22          }	[Activity Monitor]
	    274   453 {0,0,1280,22          }	[Activity Monitor]
	    274    84 {125,51,1084,711      }	[Activity Monitor] アクティビティモニタ (すべてのプロセス)
	    274    71 {0,660,53,140         }	[Activity Monitor] 
	    275   172 {100,100,1,1          }	[DeltaWalker] Focus Proxy
	    275   138 {0,0,1280,22          }	[DeltaWalker]
	    275   137 {0,0,1280,22          }	[DeltaWalker]
	    275   131 {0,0,0,0              }	[DeltaWalker] 
	    275   130 {0,23,1276,777        }	[DeltaWalker] Deltopia DeltaWalker
	    277    87 {0,0,276,300          }	[Microsoft Excel]
	    277    86 {1101,63,552,42       }	[Microsoft Excel]  
	    277    85 {-32000,-32000,194,219}	[Microsoft Excel] 書式パレット
	    277    82 {0,0,16,570           }	[Microsoft Excel]
	    277    68 {146,66,984,690       }	[Microsoft Excel] Excel ブック ギャラリー
	    277    66 {-1,-51,199,19        }	[Microsoft Excel] 
	    277    65 {639,402,2,40         }	[Microsoft Excel] 
	    277    64 {-1,0,3,3             }	[Microsoft Excel] 
	    277    63 {-1,0,2,3             }	[Microsoft Excel] 
	    277    62 {0,0,1,1              }	[Microsoft Excel] 
	    277    58 {0,23,400,377         }	[Microsoft Excel] 
	    277    57 {0,23,1276,777        }	[Microsoft Excel] Desktop
	    277    56 {0,0,1280,22          }	[Microsoft Excel]
	    277    55 {0,0,1280,22          }	[Microsoft Excel]
	    279  1957 {0,0,1280,800         }	[Dock] Desktop Picture - DefaultDesktop.jpg
	    279   397 {0,0,1280,800         }	[Dock] Desktop Picture - DefaultDesktop.jpg
	    279   128 {0,0,1280,800         }	[Dock]
	    279    40 {0,0,1280,800         }	[Dock] Dock
	    279    39 {0,0,1280,800         }	[Dock]
	    279    38 {0,0,1280,800         }	[Dock]
	    279    25 {0,0,1280,800         }	[Dock] Desktop Picture - DefaultDesktop.jpg
	    279    24 {0,0,1280,800         }	[Dock] Desktop Picture - DefaultDesktop.jpg
	    279    23 {1234,754,36,36       }	[Dock]
	    279    22 {50,755,36,36         }	[Dock]
	    279    21 {10,755,36,36         }	[Dock]
	    279    20 {504,199,284,166      }	[Dock] /Library/Widgets/Weather.wdgt/
	    279    19 {475,411,333,163      }	[Dock] /Library/Widgets/Calendar.wdgt/
	    279    18 {265,248,172,248      }	[Dock] /Library/Widgets/Calculator.wdgt/
	    279    17 {847,275,172,172      }	[Dock] /Library/Widgets/World Clock.wdgt/
	    280    49 {0,0,1280,22          }	[SystemUIServer]
	    280    46 {879,0,319,22         }	[SystemUIServer] 
	    280    44 {1234,0,46,22         }	[SystemUIServer] 
	    281   221 {0,0,16,16            }	[Finder]
	    281   220 {221,113,770,405      }	[Finder] Ricoh_PS_Printers_Vol3_DOM_LIO_2.6.0.0
	    281   199 {411,235,269,17       }	[Finder] 
	    281   122 {0,0,16,498           }	[Finder]
	    281   121 {201,72,933,621       }	[Finder] mac_list_windows_pids
	    281   120 {0,0,16,16            }	[Finder]
	    281   118 {850,0,29,22          }	[Finder] 
	    281   115 {201,93,933,600       }	[Finder] mac_list_windows_pids
	    281   113 {0,0,1280,22          }	[Finder]
	    281   112 {0,0,1280,22          }	[Finder]
	    281    52 {0,0,1280,800         }	[Finder] 
	    330   171 {300,160,680,56       }	[Spotlight] Spotlight
	    330    53 {1198,0,36,22         }	[Spotlight] 
	    340  3300 {0,733,196,67         }	[日本語入力プログラム] 
	    340  3299 {242,169,179,110      }	[日本語入力プログラム] 
	    340  3206 {0,733,196,67         }	[日本語入力プログラム] 
	    340  3205 {147,542,179,110      }	[日本語入力プログラム] 
	    340   710 {0,733,196,67         }	[日本語入力プログラム] 
	    340   709 {271,68,179,110       }	[日本語入力プログラム] 
	    495   106 {900,0,380,800        }	[通知センター] Banners and Alerts
	    495   105 {440,0,840,800        }	[通知センター] NotificationTableWindow
	    508   107 {820,0,30,22          }	[Google Photos Backup] 
	    510   132 {0,0,15,527           }	[Google ドライブ]
	    510   127 {140,105,995,612      }	[Google ドライブ] Google ドライブにログイン
	    510   126 {219,143,320,149      }	[Google ドライブ] 
	    510   123 {794,0,26,22          }	[Google ドライブ] 
	    667   191 {0,0,1280,22          }	[VirtualBox]
	    667   190 {0,0,1280,22          }	[VirtualBox]
	    667   189 {339,88,884,603       }	[VirtualBox] Oracle VM VirtualBox マネージャー
	   1320   768 {0,0,16,180           }	[コンソール]
	   1320   764 {0,23,1276,777        }	[コンソール] すべてのメッセージ
	   1320   760 {0,0,1280,22          }	[コンソール]
	   1320   759 {0,0,1280,22          }	[コンソール]
	   1502   918 {375,40,668,598       }	[システム環境設定] システム環境設定
	   1502   917 {0,0,1280,22          }	[システム環境設定]
	   1502   916 {0,0,1280,22          }	[システム環境設定]
	   2413  3081 {0,0,1280,22          }	[計算機]
	   2413  3080 {0,0,1280,22          }	[計算機]
	   2413  3079 {875,252,398,475      }	[計算機] 




