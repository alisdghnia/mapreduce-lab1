# #!/usr/bin/python
# # --*-- coding:utf-8 --*--
# import re
# import sys

# # pat = re.compile('(?P<ip>\d+.\d+.\d+.\d+).*?\d{4}:(?P<hour>\d{2}):\d{2}.*? ')
# # for line in sys.stdin:
# #     match = pat.search(line)
# #     if match:
# #         print '%s\t%s' % ('[' + match.group('hour') + ':00' + ']' + match.group('ip'), 1)


# hashmap = {}
# pat = re.compile('(?P<ip>\d+\.\d+\.\d+\.\d+).\[(?P<datetime>\d+/[a-zA-Z]+/\d+:(?P<hour>\d+):\d+:\d+).?"\w+ (?P<subdir>.*?)')
# for line in sys.stdin:
#     match = pat.search(line)
#     if match:
#         hashmap[(match.group('hour'), match.group('ip'))] = hashmap.get((match.group('hour'), match.group('ip')), 0) + 1

# total_count = {}
# for (hour, ip), count in hashmap.items():
#     if hour in total_count:
#         total_count[hour] += count


# for hour, counts in total_count.items():
#     top3 = sorted([(count, ip) for (h, ip), count in hashmap.items() if h == hour], reverse=True)[:3]
#     for count, ip in top3:
#         print '%s\t%s\t%s' % (hour, ip, count)

#!/usr/bin/python
# ---- coding:utf-8 ----
import re
import sys

# Initialize a dictionary to hold the counts for each IP and hour
counts = {}

# Compile the regular expression pattern to extract IP, hour, and path
pat = re.compile('(?P<ip>\d+\.\d+\.\d+\.\d+).\[(?P<datetime>\d+/[a-zA-Z]+/\d+:(?P<hour>\d+):\d+:\d+).?"\w+ (?P<subdir>.*?) ')

for line in sys.stdin:
    match = pat.search(line)
    if match:
        ip = match.group('ip')
        hour = match.group('hour')
        key = (ip, hour)
        counts[key] = counts.get(key, 0) + 1

# After processing all lines, aggregate counts by hour and then select the top 3 IPs for each hour
final_counts = {}
for (ip, hour), count in counts.items():
    if hour not in final_counts:
        final_counts[hour] = []
    final_counts[hour].append((ip, count))

# Sort the IPs in each hour by count and select the top 3
for hour, ips_counts in final_counts.items():
    top_ips = sorted(ips_counts, key=lambda x: x[1], reverse=True)[:3]
    for ip, count in top_ips:
        print('%s %s\t%s' % (hour, ip, count))