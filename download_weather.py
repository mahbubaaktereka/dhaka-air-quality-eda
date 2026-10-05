import csv, json, urllib.request

url = ("https://archive-api.open-meteo.com/v1/archive?latitude=23.796374&longitude=90.424614"
       "&start_date=2016-11-09&end_date=2025-03-25"
       "&hourly=temperature_2m,rain,wind_speed_10m&timezone=Asia/Dhaka&models=era5")
with urllib.request.urlopen(url) as resp:
    data = json.load(resp)

h = data["hourly"]
print("grid cell:", data["latitude"], data["longitude"], "elevation:", data["elevation"])
print("hours:", len(h["time"]))
print("first:", h["time"][0], "last:", h["time"][-1])
for k in ("temperature_2m", "rain", "wind_speed_10m"):
    print(k, "missing:", sum(v is None for v in h[k]))

with open("data/raw/weather_era5_dhaka.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["time_local", "temperature_2m", "rain", "wind_speed_10m"])
    for row in zip(h["time"], h["temperature_2m"], h["rain"], h["wind_speed_10m"]):
        w.writerow(row)
