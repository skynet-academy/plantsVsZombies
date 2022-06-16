def lawn_x(x):
    if(250 < x < 326):
        column = 1
        center_x = 283
    elif(326 < x < 400):
        column = 2
        center_x = 360
    elif(400 < x < 485):
        column = 3
        center_x = 440
    elif(485 < x < 560):
        column = 4
        center_x = 520
    elif(560 < x < 640):
        column = 5
        center_x = 600
    elif(640 < x < 715):
        column = 6
        center_x = 675
    elif(715 < x < 785):
        column = 7
        center_x = 750
    elif(785 < x < 870):
        column = 8
        center_x = 830
    elif(870 < x < 960):
        column = 9
        center_x = 915
    return center_x, column
   

def lawn_y(y):
    if(29 < y <= 130):
        line = 1 
        center_y = 80
    elif(130 < y <= 220):
        line = 2
        center_y = 170
    elif(220 < y <= 323):
        line = 3
        center_y = 270
    elif(323 < y <= 424):
        line = 4
        center_y = 370
    elif(424 < y <= 527):
        line = 5
        center_y = 470
    return center_y , line
