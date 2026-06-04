def create_report(name, area, issue):
    report = {
        "name": name,
        "area": area,
        "issue": issue
    }
    return report

my_report = create_report("Assu", "Chennai", "Garbage")
print(my_report)
