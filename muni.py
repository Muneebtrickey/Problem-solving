def draw_line(tick_lenght, label=" "):
    line = "-" * tick_lenght
    if label:
        line += " " + label
    print(line)

def draw_interval(major_length):

    if major_length > 0:
        draw_interval(major_length-1)
        draw_line(major_length)
        draw_interval(major_length - 1)



def draw_ruler(nums_length, major_length):

    draw_line(major_length, label="0")

    for i in range(1 , nums_length +1):

        draw_interval(major_length - 1)

        draw_line(major_length , str(i))



draw_ruler(2,4)

