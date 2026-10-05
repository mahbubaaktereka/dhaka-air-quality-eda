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

counts = defaultdict(lambda: [0, 0])

slot = first
while slot <= last:
    counts[(slot.year, slot.month)][1] += 1
    if hours.get(slot) is not None:
        counts[(slot.year, slot.month)][0] += 1
    slot += timedelta(hours=1)

print("year " + " ".join(f"{m:>4}" for m in range(1, 13)))
for year in range(2016, 2026):
    cells = []
    for month in range(1, 13):
        if (year, month) in counts:
            n, total = counts[(year, month)]
            cells.append(f"{round(100 * n / total):>4}")
        else:
            cells.append("  --")
    print(year, " ".join(cells))