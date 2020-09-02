#!/usr/bin/env python

from datetime import datetime
import os
import subprocess

# vars
base_dir = '/internal/manage/metrics'
distro_dir = '/public/distributions'
distro_list = []
today = datetime.today().strftime('%Y%m%d')
output = base_dir + '/distro_space.' + today + '.csv'

# read directory, populate list
def read_dir(distro_dir):
  global distro_list
  dir_list = os.listdir(path=distro_dir)
  for entry in dir_list:
    dir = distro_dir + '/' + entry
    if os.path.isdir(dir):
      distro_list.append(dir)

# calculate sizes
def du_dir(distro_list):
  for dir in distro_list:
    size = subprocess.check_output(['du','-sm', dir]).split()[0].decode('utf-8')
    distro = dir.split('/')[3]
    of.write(distro + ',' + size + '\n')

# do work
read_dir(distro_dir)
of = open(output,'w+')
of.write('distro,size\n')
du_dir(distro_list)
of.close()  
