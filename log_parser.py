# def minus(a,b):
#     return a-b
# def mySymm(a,b,func):
# #    result= a +b
# #   return result
#     result = func(a,b)
#     return result
# result1 = mySymm(5,5)
# print(result1)
# result2 = mySymm
# print(result2)
# result3 = minus
# print(result(1,2)re)
#
# logid = [
#     {"aeg": "2025-03-10", "tüüp": "Info", "sõnum": "Server käivitati"},
#     {"aeg": "2025-03-10", "tüüp": "Hoiatus", "sõnum": "Mälu kasutus ületas 80% piiri"},
#     {"aeg": "2025-03-10", "tüüp": "Viga", "sõnum": "Andmebaasi ühendus nurjus"},
#     {"aeg": "2025-03-10", "tüüp": "Info", "sõnum": "Kasutaja 'admin' sisselogimine õnnestus"},
#     {"aeg": "2025-03-10", "tüüp": "Viga", "sõnum": "Faili kirjutamine ebaõnnestus"},
#     {"aeg": "2025-03-10", "tüüp": "Hoiatus", "sõnum": "Ühendus andmebaasiga katkestatud"},
#     {"aeg": "2025-03-10", "tüüp": "Info", "sõnum": "Kohandatud seadistused rakendatud"},
#     {"aeg": "2025-03-10", "tüüp": "Viga", "sõnum": "HTTP päring ebaõnnestus: 404 Not Found"}
# ]
# 
# def errorCount(data):
#     infoCount = 0
# for elem in range(0,len(logid)):
#         print(log[elem]["tüpp"]):
# elif elem in logid:
#     if logid[elem]["tüüp"] == "Viga":
#         infoCount = infoCount + 1
#     return{"viga":infoCount}
# 
# def errorCount(data):
#     infoCount = 0
# for elem in range(0,len(logid)):
#         print(log[elem]["tüpp"]):
# elif elem in logid:
#     if logid[elem]["tüüp"] == "Hoiatus":
#         infoCount = infoCount + 1
#     return{"hoiatus":infoCount}
# 
# def errorCount(data):
#     infoCount = 0
# for elem in range(0,len(logid)):
#         print(log[elem]["tüpp"]):
# elif elem in logid:
#     if logid[elem]["tüüp"] == "Info":
#         infoCount = infoCount + 1
#     return{"info":infoCount}
# 
# myList = [errorCount(logid),warningCount(logid),infoCount(logid)]
# print(myList)

# try:
#     myList = [5,4,3]
#     print(myList[5])
# except IndexError:
#     print("Viga:vale pandnud indexid")
# print("text")

try:
    myList = [5,4,3]
    print(myList[2])
    x=10
    x/0
    e=3
    x*e-2
except IndexError:
    print("Viga: vale pandnud indexid")
except ZeroDivisionErrorError:
    print("Viga: ei või jagada nulliks")
except IndexError:
    print("Viga: vale pandnud indexid")
finally:
    print("Programmi lõpp")

paradox()
