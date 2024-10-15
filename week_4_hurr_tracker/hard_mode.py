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


def milton():
    """Animates the path of hurricane Irma
    """
    (t, wn, map_bg_img) = milton_setup()

    # opens / reads file into a list and strips unnecessary information
    # all that is needed is longitude, latitude, and windspeed
    with open('week_4_hurr_tracker/data/milton.csv', 'r') as oFile: 
        # change THIS path!
        lines = [line.strip() for line in oFile.readlines()]
        lines = lines[1:]
        lines = [line.split(',') for line in lines]
        lines = [line[2:5] for line in lines]

    #draw lines based on latitude & longitude

if __name__ == "__main__":
    milton()