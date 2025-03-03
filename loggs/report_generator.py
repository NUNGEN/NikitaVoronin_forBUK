def generate_report(data)
    ip_count = data[0]
    error_counts = data[1]
#    print(data[0])
#   print(data[1])
    with open("report.txt","w") as file:
        file.write("Log analizis report \n")
        file.write("Most active ip was: \n")
        for ip,count in ip_count.items():
            file.write(f"{ip}: {count} count \n")