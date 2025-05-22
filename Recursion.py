# stack = []
# 
# for i in range (1,11):
#     stack.append(f"{i} element")
#     print(f"{i} element apended")
#     for i in stack:
#         print(i, end=" ")
        
# def helloPrinter(userInt, n):
#     if n <= 10:
#         n += 1
#         print("hello world")
#         helloPrinter(n)
#     else:
#         return False
# helloPrinter(0)
# def helloPrinter(userInt, n):
#     if n <= 10:
#         print("Hello"*n)
# helloPrinter(int,0)
# if helloPrinter()

# def exclamation_mark_killer_method():
#     exclamation_mark_killer = input("exclamation_mark")
#     input("exclamation mark deleter")
#     userInt = exclamation_mark_killer.replace("!", " ")
#         if userInt == True:
#             print(userInt)
#         else:
#             print("there is no any exclamation marks")
            
            
# def delit(words, n):
#      n += 1
#      if words[n] == "!"
#         words[n] == ""
#         delit(words, n += 1)
#     elif len(words) <= n:
#         print()
#         len
#     else:
#         return  words[n] + delit(words, n + 1)

# def up_or_down(words, n):
#     word = words[n]
#     
#     if word.isupper(): #up_or_down.isupper(words[n])
#         print(n)
# 
#     else:
#         n += 1
#         check (words, n)
#       
# words = up_or_down(input("write down any text with UPPER letters:"),0)

# def new_stroke(words, n):
#     print(words[n])
#         print(words[n])
#         n += 1
#         if n >= len(words):
#             pass
#         else:
#         check (words, n)
#       
# words = new_stroke(input("write down any text with UPPER letters:"),0)

def text_without_numbers(text):
    if text == "":
        return
    if text[n].isdigit(): 
        text[n]= "":
        n += 1
    else:
        n += 1
    return text_without_numbers(text, n)

        