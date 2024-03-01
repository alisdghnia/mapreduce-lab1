#!/usr/bin/python
import sys

dict_hour_ip_count = {}

counter = 0
for line in sys.stdin:
    line = line.strip()
    hour_ip, count = line.split('\t', 1)
    
    if '\t' in hour_ip:
        hour, ip = hour_ip.split('\t')
        print('%s\t%s\t%s' % (hour, ip, count))
    else:
        hour = hour_ip
        ip = ""
        print('%s%s\t%s' % (hour, ip, count))

