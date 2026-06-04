report = "Road damage reported in Coimbatore"

file = open("reports.txt", "w")
file.write(report)
file.close()

print("Report saved successfully")
