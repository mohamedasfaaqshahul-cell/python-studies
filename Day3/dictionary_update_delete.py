report = {
    "your_name": "Assu",
    "your_area": "Bangalore",
    "issue_type": "Road Damage"
}

report["issue_type"] = "Water Leakage"
print(report)

del report["your_area"]
print(report)
