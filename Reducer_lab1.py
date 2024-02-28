#!/usr/bin/python
from operator import itemgetter
import sys

# dict_ip_count = {}

# for line in sys.stdin:
#     line = line.strip()
#     ip, num = line.split('\t')
#     try:
#         num = int(num)
#         dict_ip_count[ip] = dict_ip_count.get(ip, 0) + num

#     except ValueError:
#         pass


# sorted_dict_ip_count = sorted(dict_ip_count.items(), key=itemgetter(0))
# for ip, count in sorted_dict_ip_count:
#     print '%s\t%s' % (ip, count)

for hour, counts in sys.stdin.items():
    top3 = sorted([(count, ip) for (h, ip), count in hashmap.items() if h == hour], reverse=True)[:3]
    for count, ip in top3:
        print '%s\t%s\t%s' % (hour, ip, count)