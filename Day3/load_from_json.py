import json

with open("report.json", "r") as file:
    report = json.load(file)

print(report)
