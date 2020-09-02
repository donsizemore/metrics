#!/usr/bin/env python

import argparse
import pandas as pd
import matplotlib.pyplot as plt
import sys

parser = argparse.ArgumentParser(description='generate a scatter plot from a given CSV')
parser.add_argument('-c','--csv',help='CSV file to parse.')
args = parser.parse_args()

if args.csv is None:
  print('Please provide a CSV file for input.')
  sys.exit(1)

csv = args.csv

df = pd.read_csv(csv)
df.plot(kind='scatter',x='hits',y='space')

of = csv + '.png'
plt.savefig(of)
