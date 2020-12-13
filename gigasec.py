#Gigaseconds

print ('Using 30 days for a month and 365 days for a year (even for the dacade calculations)\nFor a more pricise value use days conversion or at most weeks')
time = input('Enter time (with unit and space between): ')

l_time =time.split()

if l_time[1].lower() == 's' or 'sec' or 'secs' or 'second' or 'seconds':
    g_time = float(l_time[0]) / 10**9

if l_time[1].lower() == 'm' or 'min' or 'mins' or 'minute' or 'minutes':
    g_time = (float(l_time[0]) * 60) / 10**9

if l_time[1].lower() == 'h' or 'hr' or 'hrs' or 'hour' or 'hours':
    g_time = (float(l_time[0]) * 3600) / 10**9

if l_time[1].lower() == 'd' or 'dy' or 'dys' or 'day' or 'days':
    g_time = (float(l_time[0]) * (24 * 3600)) / 10**9

if l_time[1].lower() == 'w' or 'wk' or 'wks' or 'week' or 'weeks':
    g_time = (float(l_time[0]) * (7 * 24 * 3600)) / 10**9

if l_time[1].lower() == 'm' or 'mth' or 'mo' or 'mths' or 'mos' or 'month' or 'months':
    g_time = (float(l_time[0]) * (30 * 24 * 3600)) / 10**9

if l_time[1].lower() == 'y' or 'yr' or 'yrs' or 'years' or 'years':
    g_time = (float(l_time[0]) * (365 * 24 * 3600)) / 10**9

if l_time[1].lower() == 'dec' or 'decs' or 'decade' or 'decades':
    g_time = (float(l_time[0]) * (3650 * 24 * 3600)) / 10**9

if g_time == 1:
    print (time, 'is', g_time, 'gigasecond')
else:
    print (time, 'is', g_time, 'gigaseconds')