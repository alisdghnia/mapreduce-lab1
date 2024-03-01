# import re
# import sys
# from operator import itemgetter

# def is_time_in_range(time_str, time_range):
#     start_hour, end_hour = map(int, time_range.split('-'))
#     return start_hour <= int(time_str) <= end_hour

# pattern = re.compile('(?P<ip>\d+\.\d+\.\d+\.\d+).*?\d{4}:(?P<hour>\d{2}):\d{2}.*?')

# # Input time range in the format "00-05"
# time_range = sys.argv[1]

# # Initialize a dictionary to store counts
# hour_ip_count = {}

# for line in sys.stdin:
#     match = pattern.search(line)
#     if match:
#         hour = '[' + match.group('hour') + ':00]'
#         ip = match.group('ip')

#         # Check if the hour is within the specified time range
#         if is_time_in_range(match.group('hour'), time_range):
#             # Initialize count for the hour and IP if not present
#             if hour not in hour_ip_count:
#                 hour_ip_count[hour] = {}

#             if ip in hour_ip_count[hour]:
#                 hour_ip_count[hour][ip] += 1
#             else:
#                 hour_ip_count[hour][ip] = 1

# # Emit the counts from the mapper
# for hour, ips in hour_ip_count.items():
#     sorted_ips = sorted(ips.items(), key=itemgetter(1), reverse=True)[:3]
#     for ip, count in sorted_ips:
#         print('%s\t%s\t%s' % (hour, ip, count))

import re
import sys
from operator import itemgetter

def is_time_in_range(time_str, time_range):
    start_hour, end_hour = map(int, time_range.split('-'))
    return start_hour <= int(time_str) < end_hour

pattern = re.compile('(?P<ip>\d+\.\d+\.\d+\.\d+).*?\d{4}:(?P<hour>\d{2}):\d{2}.*?')

# Input time range in the format "00-05"
time_range = sys.argv[1]

# Initialize a dictionary to store counts
ip_count = {}

for line in sys.stdin:
    match = pattern.search(line)
    if match:
        hour = match.group('hour')
        ip = match.group('ip')

        # Check if the hour is within the specified time range
        if is_time_in_range(hour, time_range):
            # Count occurrences of each IP
            if ip in ip_count:
                ip_count[ip] += 1
            else:
                ip_count[ip] = 1

# Emit the top 3 IP addresses for the time frame
sorted_ips = sorted(ip_count.items(), key=itemgetter(1), reverse=True)[:3]
for ip, count in sorted_ips:
    print('%s\t%s\t%s' % (time_range, ip, count))
