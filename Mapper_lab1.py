#!/usr/bin/python
# --*-- coding:utf-8 --*--
import re
import sys

# pat = re.compile('(?P<ip>\d+.\d+.\d+.\d+).*?\d{4}:(?P<hour>\d{2}):\d{2}.*? ')
# for line in sys.stdin:
#     match = pat.search(line)
#     if match:
#         print '%s\t%s' % ('[' + match.group('hour') + ':00' + ']' + match.group('ip'), 1)


hashmap = {}
pat = re.compile('(?P<ip>\d+\.\d+\.\d+\.\d+).\[(?P<datetime>\d+/[a-zA-Z]+/\d+:(?P<hour>\d+):\d+:\d+).?"\w+ (?P<subdir>.*?)')
for line in sys.stdin:
    match = pat.search(line)
    if match:
        hashmap[(match.group('hour'), match.group('ip'))] = hashmap.get((match.group('hour'), match.group('ip')), 0) + 1

total_count = {}
for (hour, ip), count in hashmap.items():
    if hour in total_count:
        total_count[hour] += count

for hour, counts in total_count.items():
    top3 = sorted([(count, ip) for (h, ip), count in hashmap.items() if h == hour], reverse=True)[:3]
    for count, ip in top3:
        print '%s\t%s\t%s' % (hour, ip, count)