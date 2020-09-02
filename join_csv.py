#!/usr/bin/env python

import argparse
import pandas
import sys

# parse arguments
parser = argparse.ArgumentParser(description='merges two CSV files on index.')
parser.add_argument('-d', '--downloads', help='CSV file of monthly hits')
parser.add_argument('-o', '--output', help='target CSV filename')
parser.add_argument('-s', '--storage', help='CSV file of storage usage')

args = parser.parse_args()

# sanity checks
if args.downloads is None:
  print('Please provide CSV download file.')
  sys.exit(1)

if args.storage is None:
  print('Please provide CSV storage file.')
  sys.exit(1)

if args.output is None:
  print('Please provide output filename.')
  sys.exit(1)

hits_csv = args.downloads
storage_csv = args.storage
output = args.output

# read in files
hits_df = pandas.read_csv(hits_csv, index_col=[0])
storage_df = pandas.read_csv(storage_csv, index_col=[0])

output_df = storage_df.merge(hits_df, left_on='distro', right_on='distro')
output_df.to_csv(output)
