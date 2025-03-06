import emsine as emsineFail
import teine as teineFail

def turn_right():
    for _ in range(3):
        right()

def fill_room():
    row = 0
    steps_count = 0 

    while True:
        while not is_wall():
            if not is_painted():
                paint()
            step()
            steps_count += 1  

            if steps_count == 10:
                turn_right()
                steps_count = 0

        if not is_painted():
            paint()

        if row % 2 == 0:  
            right()
            if is_wall():
                break 
            step()
            right()
        else:  
            turn_right()
            if is_wall():
                break
            step()
            turn_right()

        row += 1  

    col = 0
    steps_count = 0

    while True:
        while not is_wall():
            if not is_painted():
                paint()
            step()
            steps_count += 1  

            if steps_count == 11:
                turn_right()
                steps_count = 0 

        if not is_painted():
            paint()

        if col % 2 == 0: 
            right()
            if is_wall():
                break
            step()
            right()
        else:  
            turn_right()
            if is_wall():
                break
            step()
            turn_right()

        col += 1

def move_to_next_room():
    while True:
        if is_wall():
            right()
        else:
            step()
        
        if not is_wall() and not is_painted(): 
            break

while True:
    fill_room()  
    move_to_next_room()
