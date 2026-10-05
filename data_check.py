import csv
from datetime import datetime

times = []
values = []
blank_values = 0
with open("data/raw/pm25_sensor_24434.csv") as f:
    for row in csv.DictReader(f):
        times.append(datetime.fromisoformat(row["from_utc"].replace("Z", "+00:00")))
        if row["value"] == "":
            blank_values += 1
        else:
            values.append(float(row["value"]))

unique = sorted(set(times))

print("Rows:", len(times))
print("Unique start times:", len(unique))
print("Rows with a blank value:", blank_values)
print("Rows with a number:", len(values))
print("First reading starts:", unique[0])
print("Last reading starts:", unique[-1])

expected = int((unique[-1] - unique[0]).total_seconds() // 3600) + 1
print("Hourly slots from first to last:", expected)

gaps = 0
missing_total = 0
for earlier, later in zip(unique, unique[1:]):
    hours = int((later - earlier).total_seconds() // 3600)
    if hours > 1:
        gaps += 1
        missing_total += hours - 1
print("Number of gaps:", gaps)
print("Total missing hours (no row at all):", missing_total)

print("Lowest value:", min(values))
print("Highest value:", max(values))
print("Negative values:", sum(1 for v in values if v < 0))
print("Values equal to -999:", sum(1 for v in values if v == -999))