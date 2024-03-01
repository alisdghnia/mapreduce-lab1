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

dict_hour_ip_count = {}


counter = 0
for line in sys.stdin:
    line = line.strip()
    hour_ip, count = line.split('\t', 1)
    hour = hour_ip[:7]
    ip = hour_ip[7:]
    print('%s%s\t%s' % (hour, ip, count))

    counter += 1
    if counter % 3 == 0:
        print()
