#!/usr/bin/env python

import argparse
from datetime import datetime
import os
import subprocess

# vars
base_dir = '/internal/manage/metrics'
distro_dir = '/public/distributions'
log_base = '/public/archive/logs/distro.ibiblio.org'
thismonth = datetime.today().strftime('%Y%m')
distro_list = []

# parse arguments
parser = argparse.ArgumentParser(description='Given a YYYYMM string, determine total number of hits including errors per TLD in /public/distributions.')
parser.add_argument('-m', '--month', help='month in YYYYMM. defaults to current month')

# determine month
args = parser.parse_args()
if args.month is None:
  monthstr = thismonth
else:
  monthstr = args.month

# outputfile
output = base_dir + '/distro_hits.' + monthstr + '.csv'

# get list of distros by TLD
def get_distros(distro_dir):
  global distro_list
  dir_list = os.listdir(path=distro_dir)
  for entry in dir_list:
    dir = distro_dir + '/' + entry
    if os.path.isdir(dir):
      distro_list.append(entry) 

# zgrep logfiles by distro for given month
def process_distro(distro_list):
  for distro in distro_list:
    year = monthstr[0:4]
    month = monthstr[4:6]
    log_dir = log_base + '/' + year + '/' + month
    logfiles = os.listdir(path=log_dir)
    total = 0
    for log in logfiles:
      logpath = log_dir + '/' + log
      result = subprocess.run(['/usr/bin/zgrep','-c',distro,logpath], stdout=subprocess.PIPE)
      count = result.stdout.decode('utf-8').strip()
      total = total + int(count)
    of.write(distro + ',' + str(total) + '\n')

# do work
get_distros(distro_dir)
of = open(output,'w+')
of.write('distro,hits\n')
process_distro(distro_list)
of.close()
