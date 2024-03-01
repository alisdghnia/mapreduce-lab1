#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import sys
from operator import itemgetter

pattern = re.compile('(?P<ip>\d+\.\d+\.\d+\.\d+).*?\d{4}:(?P<hour>\d{2}):\d{2}.*?')

hour_ip_count = {}

for line in sys.stdin:
    match = pattern.search(line)
    if match:
        hour = '[' + match.group('hour') + ':00]'
        ip = match.group('ip')

        if hour not in hour_ip_count:
            hour_ip_count[hour] = {}

        if ip in hour_ip_count[hour]:
            hour_ip_count[hour][ip] += 1
        else:
            hour_ip_count[hour][ip] = 1


for hour, ips in hour_ip_count.items():
    sorted_ips = sorted(ips.items(), key= itemgetter(1), reverse=True)[:3]
    for ip, count in sorted_ips:
        print('%s\t%s\t%s' % (hour, ip, count))
