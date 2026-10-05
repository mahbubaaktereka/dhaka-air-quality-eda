import csv

empty = 0
examples = []
with open("data/raw/pm25_sensor_24434.csv") as f:
    for line_number, row in enumerate(csv.DictReader(f), start=2):
        if row["value"] == "":
            empty += 1
            if len(examples) < 3:
                examples.append((line_number, row))

print("Rows with an empty value:", empty)
for line_number, row in examples:
    print("File line", line_number, row)