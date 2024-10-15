import turtle


def milton_setup(): # DO NOT CHANGE
    """Creates the Turtle and the Screen with the map background
       and coordinate system set to match latitude and longitude.

       :return: a tuple containing the Turtle and the Screen

       DO NOT CHANGE THE CODE IN THIS FUNCTION!
    """
    import tkinter
    turtle.setup(965, 600)  # set size of window to size of map

    wn = turtle.Screen()
    wn.title("Hurricane Milton")

    # kludge to get the map shown as a background image,
    # since wn.bgpic does not allow you to position the image
    canvas = wn.getcanvas()
    turtle.setworldcoordinates(-90, 0, -17.66, 45)

    map_bg_img = tkinter.PhotoImage(file="week_4_hurr_tracker/images/atlantic-basin.png") # change THIS path!

    # additional kludge for positioning the background image
    # when setworldcoordinates is used
    canvas.create_image(-1175, -580, anchor=tkinter.NW, image=map_bg_img)

    t = turtle.Turtle()
    wn.register_shape("week_4_hurr_tracker/images/hurricane.gif") # change THIS path!
    t.shape("week_4_hurr_tracker/images/hurricane.gif") # change THIS path!

    return (t, wn, map_bg_img)


def read_hurricane_data(filepath):
    """Reads hurricane data from a CSV file and returns a list of (longitude, latitude, wind speed)."""
    with open(filepath, 'r') as file:
        lines = [line.strip().split(',')[2:5] for line in file.readlines()[1:]]
    return [(float(line[1]), float(line[0]), int(line[2])) for line in lines]

def set_turtle_attributes(t, windspeed):
    """Sets the turtle's pen color and width based on wind speed category."""
    if windspeed < 74:
        #change pen width
        #change pen color
    elif 74 <= windspeed <= 95:
        #change pen width
        #change pen color
        #write 1 (for category 1 windspeed)
    elif 96 <= windspeed <= 110:
    
    #...

    elif windspeed >= 158:


def milton():
    """Animates the path of Hurricane Milton."""
    hurricane_turtle, wn, map_bg_img = milton_setup()
    
    #set data path to csv file

    hurricane_turtle.penup()
    hurricane_turtle.hideturtle()

    start = lines[0]
    # set first coordinate to first_longitude & first_latitude

    # go to first long & lat 

    hurricane_turtle.showturtle()

    # Animate the hurricane path
    for  #each longitude & latitude from csv:
        set_turtle_attributes(hurricane_turtle, windspeed)
        #move turtle to coordinates based on longitude & latitude

    wn.exitonclick()

if __name__ == "__main__":
    milton()
