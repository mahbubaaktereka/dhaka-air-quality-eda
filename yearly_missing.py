import csv
from collections import defaultdict
from datetime import datetime, timedelta

hours = {}
with open("data/raw/pm25_sensor_24434.csv") as f:
    for row in csv.DictReader(f):
        start = datetime.fromisoformat(row["from_local"])
        hours[start] = None if row["value"] == "" else float(row["value"])

first = min(hours)
last = max(hours)

tally = defaultdict(lambda: [0, 0, 0])

slot = first
while slot <= last:
    if slot not in hours:
        tally[slot.year][2] += 1
    elif hours[slot] is None:
        tally[slot.year][1] += 1
    else:
        tally[slot.year][0] += 1
    slot += timedelta(hours=1)

print("year with_number blank no_row total percent_with_number")
for year in sorted(tally):
    n, b, g = tally[year]
    total = n + b + g
    print(year, n, b, g, total, round(100 * n / total, 1))