import json

report = {
    "name": "Assu",
    "area": "Coimbatore",
    "issue": "Road Damage"
}

with open("report.json", "w") as file:
    json.dump(report, file)

print("JSON file saved")
