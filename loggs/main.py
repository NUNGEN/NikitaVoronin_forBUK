#file = open("test.txt","r/w/a",)
#file.read()
#file.read()
#file.read()
import log_parser as logs:
import report_generator as generate_report:

log_file = "logs.txt"

result = logs.analyze_log(log_file)
generate_report.generate_report(result)


#print(result)
#with open("file.txt","r",encoding="utf-8") as file: