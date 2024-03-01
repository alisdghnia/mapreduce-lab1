import re
import sys
from operator import itemgetter

def is_time_in_range(time_str, time_range):
    start_hour, end_hour = map(int, time_range.split('-'))
    return start_hour <= int(time_str) < end_hour

pattern = re.compile('(?P<ip>\d+\.\d+\.\d+\.\d+).*?\d{4}:(?P<hour>\d{2}):\d{2}.*?')

# Input time range in the format "00-05"
time_range = sys.argv[1]

ip_count = {}
for line in sys.stdin:
    match = pattern.search(line)
    if match:
        hour = match.group('hour')
        ip = match.group('ip')
        
        if is_time_in_range(hour, time_range):            
            if ip in ip_count:
                ip_count[ip] += 1
            else:
                ip_count[ip] = 1

sorted_ips = sorted(ip_count.items(), key=itemgetter(1), reverse=True)[:3]
for ip, count in sorted_ips:
    print('%s\t%s\t%s' % (time_range, ip, count))
