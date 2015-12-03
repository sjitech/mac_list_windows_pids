#!/usr/bin/env python

import Quartz

#wl = Quartz.CGWindowListCopyWindowInfo( Quartz.kCGWindowListOptionOnScreenOnly | Quartz.kCGWindowListExcludeDesktopElements, Quartz.kCGNullWindowID)
wl = Quartz.CGWindowListCopyWindowInfo( Quartz.kCGWindowListOptionAll, Quartz.kCGNullWindowID)

wl = sorted(wl, key=lambda k: k.valueForKey_('kCGWindowOwnerPID'))

#print wl

print 'PID'.rjust(7) + ' ' + 'WinID'.rjust(5) + '  ' + 'x,y,w,h'.ljust(21) + ' ' + '\t[Title] SubTitle'
print '-'.rjust(7,'-') + ' ' + '-'.rjust(5,'-') + '  ' + '-'.ljust(21,'-') + ' ' + '\t-------------------------------------------'

for v in wl:
	print ( \
		str(v.valueForKey_('kCGWindowOwnerPID') or '?').rjust(7) + \
		' ' + str(v.valueForKey_('kCGWindowNumber') or '?').rjust(5) + \
		' {' + ('' if v.valueForKey_('kCGWindowBounds') is None else \
		 	( \
			 	str(int(v.valueForKey_('kCGWindowBounds').valueForKey_('X')))     + ',' + \
			 	str(int(v.valueForKey_('kCGWindowBounds').valueForKey_('Y')))     + ',' + \
			 	str(int(v.valueForKey_('kCGWindowBounds').valueForKey_('Width'))) + ',' + \
			 	str(int(v.valueForKey_('kCGWindowBounds').valueForKey_('Height'))) \
		 	) \
		 	).ljust(21) + \
		'}' + \
		'\t[' + ((v.valueForKey_('kCGWindowOwnerName') or '') + ']') + \
		('' if v.valueForKey_('kCGWindowName') is None else (' ' + v.valueForKey_('kCGWindowName') or '')) \
	).encode('utf8')
