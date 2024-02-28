#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 17:11:53 2024

@author: yanchiliu
"""
#!/usr/bin/python
import sys
from operator import itemgetter
from collections import defaultdict

# create a dictionary
dict_hour_ip_count = defaultdict(lambda: defaultdict(int))

# get output from Mapper
for line in sys.stdin:
    line = line.strip()
    hour_ip, count = line.split('\t', 1)
    try:
        count = int(count)
        dict_hour_ip_count[hour_ip[:5]][hour_ip[6:]] += count
    except ValueError:
        pass

# sort hour+ip, get top 3
for hour, ips in dict_hour_ip_count.items():
    sorted_ips = sorted(ips.items(), key=itemgetter(1), reverse=True)[:3]
    for ip, count in sorted_ips:
        print('%s\t%s\t%s' % (hour, ip, count))
