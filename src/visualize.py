#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_path',required=True)
parser.add_argument('--key',required=True)
parser.add_argument('--percent',action='store_true')
args = parser.parse_args()

# imports
import os
import json
import matplotlib.pyplot as plt
from collections import Counter,defaultdict

# open the input path
with open(args.input_path) as f:
    counts = json.load(f)

# normalize the counts by the total values
if args.percent:
    for k in counts[args.key]:
        counts[args.key][k] /= counts['_all'][k]

# print the count values
items = sorted(counts[args.key].items(), key=lambda item: (item[1],item[0]), reverse=True)
for k,v in items:
    print(k,':',v)

#print the graph
x = []
y = []
for i in range(10):
    if i == len(items):
        break
    x.append(items[i][0])
    y.append(items[i][1])

plt.bar(x,y)
plt.xlabel(args.key)
plt.ylabel('Values')
plt.title(f'Coronavirus Key Country Bar Graph')
plt.savefig(f'plots/{args.key}_country_bar_graph.png')
