#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_paths',nargs='+',required=True)
parser.add_argument('-keys',nargs='+',required=True)
parser.add_argument('--output_path',required=True)
args = parser.parse_args()

# imports
import os
import json
import matplotlib.pyplot as plt
from collections import Counter,defaultdict
from datetime import datetime

# load each of the input paths
total = defaultdict(lambda: Counter())
for path in args.input_paths:
    with open(path) as f:
        tmp = json.load(f)
        date_str = path.split('.')[0].split('-')[1:]
        month, day = date_str
        date_obj = datetime(2020, int(month), int(day))
        for hashtag,counts in tmp.items():
            for lang, count, in counts.items():
                total[date_obj][hashtag] += tmp[hashtag][lang]

# write the output path
json_total = {d.isoformat(): dict(total[d]) for d in total}
with open(args.output_path, 'w') as f:
    json.dump(json_total, f)

# open the input path
with open(args.output_path) as f:
    counts = json.load(f)

#print the graph
dates = sorted([datetime.fromisoformat(d) for d in counts.keys()])
y = []
for hashtag in args.keys:
    y = [counts[d.isoformat()].get(hashtag, 0) for d in dates]
    plt.plot(dates,y, label=hashtag)

plt.xlabel('Date')
plt.ylabel('Count')
plt.legend()
plt.title(f'Hashtag Counts Over Time')
plt.savefig(f'plots/alternative_reduce.png')
