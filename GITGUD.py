# music_base =[
#     {"id": 1, "artist": "Eminem", "Title": "The Real Slim Shadies"},
#     {"id": 2, "artist": "DM Dokuro", "Title": "The Tale Of A Cruel World"},
#     {"id": 3, "artist": "Daisuke Ishivatari", "Title": "Destructive Goodwill"}
#     ]
# 
# print(music_base[0]["Title"])
# 
# def input_music(par):
#     result = []
#     for music in music_base:
#         if par in music["title"] or par in music["artist"]:
#             result.append(music)
#             
#             
#             
#     if result():
#         for muusika in result:
#             print(music["muusika"],music["title"])
#     return result
# 
# userInput = input_music(input("Choose your music"))
# print(userInput)
# 
# # for i in range (1,2):

grades = {
    "Mari": {
        "Math":[4, 5, 3],
        "Estonian":[5, 4],
        "Chemistry":[3],
    },
    "Jüri": {
        "Math":[2, 3],
        "Estonian":[3],
        "Chemistry":[4, 4, 5],
    },
    "Anatoliy": {
        "Math":[5, 5],
        "Estonian":[5],
        "Chemistry":[5, 5],  
    }
}
print(grades["Mari"]["Math"][-1]):
middle = 0
subject = 0
count = 0
for aine in grades["Mari"]:
    for grade in grades["Mari"][aine]
        subject = subject + grade
        count += 1
middle = subject / count
print("Mari:", middle)