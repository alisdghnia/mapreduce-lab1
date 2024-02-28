#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 17:10:23 2024

@author: yanchiliu
"""
import re
import sys

pattern = re.compile('(?P<ip>\d+\.\d+\.\d+\.\d+).*?\d{4}:(?P<hour>\d{2}):\d{2}.*?')

for line in sys.stdin:
    match = pattern.search(line)
    if match:
        print('%s\t%s' % ('[' + match.group('hour') + ':00' + ']' + match.group('ip'), 1))
