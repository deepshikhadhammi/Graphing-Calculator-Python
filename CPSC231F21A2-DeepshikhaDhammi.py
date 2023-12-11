# COURSE CPSC 231 FALL 2021
# INSTRUCTOR: Jonathan Hudson
# Tutorial: TA Name
# ID: XXXXXXXX
# Date:
# Description:

#COURSE CPSC 231 FALL 2021
#INSTRUCTOR: Jonathon Hudson
# Tutorial : SARTHAK SHARAN(T08)
# ID: 30140157
# Date: October 22nd,2021
# Description: The below program consists of conversions between Cartesian coordinate systems and drawing the curve by
#               converting the points using calc_to_screen_coordinate into turtle screen coordinates.
#               Several other functions such as calculating starting and ending values of x axis and y axis, drawing
#               ticks and labelling the axis are also used. Furthermore, draw expression function is designed to draw
#               the curve based on the arithmetic expression entered by the user. y value is calculated for the
#               expression using calc() function. The program calculates different y values using delta value of 0.1
#               After drawing the curve it finds maxima and minima and draws a circle at the maxima and minima using
#               purple and orange colour respectively.

from math import *
import turtle

# Constants
BACKGROUND_COLOR = "white"
WIDTH = 800
HEIGHT = 600
AXIS_COLOR = "black"
DELTA=0.1
RADIUS=5

def get_color(equation_counter):
    """
    Get color for an equation based on counter of how many equations have been drawn (this is the xth equation)
    :param equation_counter: Number x, for xth equation being drawn
    :return: A string color for turtle to use
    """
    remainder=equation_counter%3  #calculates the remainder in order to determine colour based on this
    if(remainder==0):              #for first equation colour will be red
        color="red"
    elif(remainder==1):            #for second equation colour will be green
        color="green"
    else:                         #for every third equation colour will be blue
        color="blue"
    return color                  #returns colour


def calc_to_screen_coord(x, y, x_origin, y_origin, ratio):
    """
    Convert a calculator (x,y) to a pixel (screen_x, screen_y) based on origin location and ratio
    :param x: Calculator x
    :param y: Calculator y
    :param x_origin: Pixel x origin of pixel coordinate system
    :param y_origin: Pixel y origin of pixel coordinate system
    :param ratio: Ratio of pixel coordinate system (each 1 in calculator is worth ratio amount of pixels)
    :return: (screen_x, screen_y) pixel version of calculator (x,y)
    """
    screen_x=x_origin+ratio*x       #converting x coordinate into turtle screen coordinate
    screen_y=y_origin+ratio*y       #converting y coordinate into turtle screen coordinate
    return (screen_x,screen_y)      #returning  x and y screen coordinates


def calc_minmax_x(x_origin, ratio):
    """
    Calculate smallest and largest calculator INTEGER x value to draw for a 0->WIDTH of screen
    Smallest: Convert a pixel x=0 to a calculator value and return integer floor
    Largest : Convert a pixel x=WIDTH to a calculator value and return integer ceiling
    :param x_origin: Pixel x origin of pixel coordinate system
    :param ratio: Ratio of pixel coordinate system (each 1 in calculator is worth ratio amount of pixels)
    :return: (Smallest, Largest) x value to draw for a 0->WIDTH of screen
    """
    x=(0-x_origin)/ratio                 #converts x=0 into a calculator value
    x1=(WIDTH-x_origin)/ratio            #converts x=Height into a calculator value
    min_x=int(floor(x))                 #starting point of x axis
    max_x=int(ceil(x1))                 #ending point of x axis
    return min_x, max_x                 # returns starting and ending points of x axis


def calc_minmax_y(y_origin, ratio):
    """
    Calculate smallest and largest calculator INTEGER y value to draw for a 0->HEIGHT of screen
    Smallest: Convert a pixel y=0 to a calculator value and return integer floor
    Largest : Convert a pixel y=HEIGHT to a calculator value and return integer ceiling
    :param y_origin: Pixel y origin of pixel coordinate system
    :param ratio: Ratio of pixel coordinate system (each 1 in calculator is worth ratio amount of pixels)
    :return: (Smallest, Largest) y value to draw for a 0->HEIGHT of screen
    """
    y=(0-y_origin)/ratio            #convert 0 into a calculator value
    y1=(HEIGHT-y_origin)/ratio      # convert y=height into a calculator value
    min_y=int(floor(y))             #starting point of y axis
    max_y=int(ceil(y1))             #ending point of y axis
    return min_y, max_y             #returns starting and ending locations of y axis


def draw_line(pointer, screen_x1, screen_y1, screen_x2, screen_y2):
    """
    Draw a line between tow pixel coordinates (screen_x_1, screen_y_1) to (screen_x_2, screen_y_2)
    :param pointer: Turtle pointer to draw with
    :param screen_x1: The pixel x of line start
    :param screen_y1: The pixel y of line start
    :param screen_x2: The pixel x of line end
    :param screen_y2: The pixel y of line end
    :return: None (just draws in turtle)
    """

    pointer.goto(screen_x1,screen_y1) #starting point of line
    pointer.down()                    #draw line
    pointer.goto(screen_x2,screen_y2) #ending point of line

def draw_x_axis_tick(pointer, screen_x, screen_y):

        pointer.up()
        pointer.goto(screen_x,screen_y+5) #starting point of tick
        pointer.down()                    #draw tick
        pointer.goto(screen_x,screen_y-5) #ending point of tick
        pointer.up()

def draw_x_axis_label(pointer, screen_x, screen_y, label_text):
    """
    Draw an x-axis label for location (screen_x, screen_y), label is label_text
    :param pointer: Turtle pointer to draw with
    :param screen_x: The pixel x of tick location on axis
    :param screen_y: The pixel y of tick location on axis
    :param label_text: The string label to draw
    :return: None (just draws in turtle)
    """
    pointer.up()
    pointer.goto(screen_x-5,screen_y-20) #going to desired location write label
    pointer.write(str(label_text))       #writing labels



def draw_y_axis_tick(pointer, screen_x, screen_y):
    """
    Draw an y-axis tick for location (screen_x, screen_y)
    :param pointer: Turtle pointer to draw with
    :param screen_x: The pixel x of tick location on axis
    :param screen_y: The pixel y of tick location on axis
    :return: None (just draws in turtle)
    """
    pointer.up()
    pointer.goto(screen_x+5,screen_y) #going to the starting location to draw ticks
    pointer.down()      #drawing tick
    pointer.goto(screen_x-5,screen_y)  #ending point of tick
    pointer.up()
    pass


def draw_y_axis_label(pointer, screen_x, screen_y, label_text):
    """
    Draw an y-axis label for location (screen_x, screen_y), label is label_text
    :param pointer: Turtle pointer to draw with
    :param screen_x: The pixel x of tick location on axis
    :param screen_y: The pixel y of tick location on axis
    :param label_text: The string label to draw
    :return: None (just draws in turtle)
    """
    pointer.up()
    pointer.goto(screen_x-20,screen_y-5) #going to the desired location to write labels
    pointer.write(str(label_text))     #function to write labels on y axis

def draw_x_axis(pointer, x_origin, y_origin, ratio):
    """
    Draw an x-axis centred on given origin, with given ratio
    :param pointer: Turtle pointer to draw with
    :param x_origin: Pixel x origin of pixel coordinate system
    :param y_origin: Pixel y origin of pixel coordinate system
    :param ratio: Ratio of pixel coordinate system (each 1 in calculator is worth ratio amount of pixels)
    :return: None (just draws in turtle)
    """

    xmin,xmax= calc_minmax_x(x_origin,ratio) #calculating the starting and ending points of yaxis
    xtick=xmin                               #initialising the first tick value with minx value
    while(xtick>=xmin and xtick<=xmax):      #looping through starting and ending values of x axis
          xpixel,ypixel=calc_to_screen_coord(xtick,0,x_origin,y_origin,ratio) # converting the location of tick into screen coordinates
          draw_x_axis_tick(pointer,xpixel,ypixel) #drawing ticks on x axis
          xwrite=str(xtick)                       #converting tick into string type
          draw_x_axis_label(pointer,xpixel,ypixel,xwrite) #writing labels on x axis
          xtick=xtick+1                            #incrementing value of tick by 1
    xminpoint,yminpoint=calc_to_screen_coord(xmin,0,x_origin,y_origin,ratio) # converting the point xmin into screen coordinates
    xmaxpoint,ymaxpoint=calc_to_screen_coord(xmax,0,x_origin,y_origin,ratio) #converting the point xmax into screen coordinates
    draw_line(pointer,xminpoint,yminpoint,xmaxpoint,ymaxpoint)         #drawing the line between starting and ending point of x axis
    pointer.up()

def draw_y_axis(pointer, x_origin, y_origin, ratio):
    """
    Draw an y-axis centred on given origin, with given ratio
    :param pointer: Turtle pointer to draw with
    :param x_origin: Pixel x origin of pixel coordinate system
    :param y_origin: Pixel y origin of pixel coordinate system
    :param ratio: Ratio of pixel coordinate system (each 1 in calculator is worth ratio amount of pixels)
    :return: None (just draws in turtle)
    """
    ymin,ymax= calc_minmax_y(y_origin,ratio)   #converting the minimum and maximum starting point of y axis into screen coordinates
    ytick=ymin                                 #initialising the first tick value with minimum start value of y

    while(ytick>=ymin and ytick<=ymax):       #looping through starting and ending point of ticks
        xpixel,ypixel=calc_to_screen_coord(0,ytick,x_origin,y_origin,ratio) #converting the tick location into screen coordinates
        draw_y_axis_tick(pointer,xpixel,ypixel)      #drawing ticks on y axis
        ywrite=str(ytick)                            # converting tick value into string type
        draw_y_axis_label(pointer,xpixel,ypixel,ywrite) # drawing the labels of y axis
        ytick=ytick+1                                   # incrementing the value of tick by one
    x_min_point,y_min_point=calc_to_screen_coord(0,ymin,x_origin,y_origin,ratio)  # converting the point of ymin into screen coordinates
    x_max_point,y_maxpoint=calc_to_screen_coord(0,ymax,x_origin,y_origin,ratio) # converting the point of ymax into coordinate
    draw_line(pointer,x_min_point,y_min_point,x_max_point,y_maxpoint)   #drawing line between starting and ending points of y
    pointer.up()

def draw_expression(pointer, expr, colour, x_origin, y_origin, ratio):
    """
    Draw expression centred on given origin, with given ratio
    :param pointer: Turtle pointer to draw with
    :param expr: The string expression to draw
    :param colour: The colour to draw the expression
    :param x_origin: Pixel x origin of pixel coordinate system
    :param y_origin: Pixel y origin of pixel coordinate system
    :param ratio: Ratio of pixel coordinate system (each 1 in calculator is worth ratio amount of pixels)
    :return: None (just draws in turtle)
    """

    xmin,xmax=calc_minmax_x(x_origin,ratio)  #converting start and end location of xaxis into screen coordinates
    ymin,ymax=calc_minmax_y(y_origin,ratio)  #converting start and end location of y axis into screen coordinates
    x=xmin                                   # assigning starting value of x axis to x
    x_start,y_start=calc_to_screen_coord(xmin,ymin,x_origin,y_origin,ratio) #converting starting and ending location of x axis into screen coordinates
    x_end,y_end=calc_to_screen_coord(xmax,ymax,x_origin,y_origin,ratio)  # converting starting and ending location of y axis into screen coordinates
    maximum_x=0
    maximum_y=0
    minimum_x=0
    minimum_y=0
    value=True
    value1=True
    while(x>=xmin and x<=xmax):    #using the loop to calculate different values of using x from xminimum to x maximum

        y=calc(expr,x)             # calculating y calue by calling function calc and passing expression and x value
        if(y>=ymin and y<=ymax):   # drawing within the given screen
         xpixel,ypixel=calc_to_screen_coord(x,y,x_origin,y_origin,ratio) #converting x and y value into screen coordinates
         y_delta=calc(expr,(x+DELTA)) # calculating new y value when delta is added to x.
          #converting x+Delta and y=calc(expr,x+DELTA) into screen coordinates
         delta_x_pixels,delta_y_pixels=calc_to_screen_coord((x+DELTA),y_delta,x_origin,y_origin,ratio)
        #converting x-DELTA and y=calc(expr,x-DELTA)into screen coordinates
         pre_delta_x,pre_delta_y=calc_to_screen_coord(x-DELTA,calc(expr,x-DELTA),x_origin,y_origin,ratio)
         #converting x+DELTA+DELTA and y=calc(expr,x+DELTA+DELTA) into screen coordinates
         next_delta_x,next_delta_y=calc_to_screen_coord((x+DELTA+DELTA),calc(expr,x+DELTA+DELTA),x_origin,y_origin,ratio)

         pointer.color(colour) #changing colour of pointer to draw maximum and minimum

         if(delta_y_pixels>=y_start and delta_y_pixels<=y_end and delta_x_pixels>=x_start and delta_x_pixels<=x_end):
             #to check if delta values lies within the range of xmin,xmax and ymin,ymax
            draw_line(pointer,xpixel,ypixel,delta_x_pixels,delta_y_pixels) #draw curve between points
            pointer.up()
         if(pre_delta_y>=y_start and next_delta_y<=y_end and pre_delta_x>x_start and next_delta_x<=x_end) :
             # condition to check previous x value with delta subtracted lies within the range of xstart and x end and next delta value also less than end of x

           if(ypixel-pre_delta_y>0 and ypixel-delta_y_pixels<0 and next_delta_y-delta_y_pixels<0):
               #checking slope (derivative) whether increasing or decreasing. This condition is for maxima.

             pointer.up()
             pointer.color("purple")  # changing colour of turtle

             diffx=(delta_x_pixels-pre_delta_x)/2  # finding distance between two x values between which maxima lies
             diffy=(delta_y_pixels-pre_delta_y)/2  # finding difference between two y values between which maxima lies

             x_new_point=pre_delta_x+diffx     #finding x point of local maximum
             y_new_point=pre_delta_y+diffy     #finding y point of local maximum

             pointer.goto(x_new_point,y_new_point-RADIUS) #going to the point of maximum
             pointer.down()
             pointer.circle(RADIUS)                      #drawing the circle at point of local maximum
             pointer.up()

             local_maxima_x_point=(x_new_point-x_origin)/ratio #converting x local maximum point from screen coordinates to mathematical form
             local_maxima_y_point=(y_new_point-y_origin)/ratio # converting y local maximum point from screen coordinates to mathematical form
             if(value==True):
                maximum_x=local_maxima_x_point
                maximum_y=local_maxima_y_point
                value=False
             if( local_maxima_y_point>maximum_y): #finding largest local maximum
                      maximum_x=local_maxima_x_point
                      maximum_y=local_maxima_y_point

           elif(ypixel-pre_delta_y<0 and ypixel-delta_y_pixels>0 and next_delta_y-delta_y_pixels>0): #condition to find local minimum from slope
               diffx=(delta_x_pixels-pre_delta_x)/2    #finding distance between two x values between which minima lies
               diffy=(delta_y_pixels-pre_delta_y)/2    #finding distance between two y values between which maxima lies
               x_new_point=pre_delta_x+diffx           #finding x point of local minimum
               y_new_point=pre_delta_y+diffy           #finding y point of local minimum
               pointer.up()
               pointer.color("orange")                 #changing colour of the pointer
               pointer.goto(x_new_point,y_new_point-RADIUS) #going to local minimum location
               pointer.down()
               pointer.circle(RADIUS)                        #drawing circle at minimum location
               pointer.up()
               local_minima_xpoint=(x_new_point-x_origin)/ratio #converting screen coordinate into mathematical form
               local_minima_ypoint=(y_new_point-y_origin)/ratio
               if(value1==True):
                   minimum_x=local_minima_xpoint
                   minimum_y=local_minima_ypoint
                   value1=False
               if(local_minima_ypoint<minimum_y):   #finding lowest local minimum
                   minimum_x=local_minima_xpoint
                   minimum_y=local_minima_ypoint


        x=x+DELTA  #updating the value of x by delta
    print ("Expression global maximum (",maximum_x,",",maximum_y,")")
    print("Expression global minimum (",minimum_x,",",minimum_y,")")


def calc(expr, x):
    """
    Return y for y = expr(x)
    Example if x = 10, and expr = x**2, then y = 10**2 = 100.
    :param expr: The string expression to evaluate where x is the only variable
    :param x: The value to evaluate the expression at
    :return: y = expr(x)

    """

    return eval(expr)






def setup():
    """
    Sets the window up in turtle
    :return: None
    """
    turtle.bgcolor(BACKGROUND_COLOR)          #sets background colour of the turtle
    turtle.setup(WIDTH, HEIGHT, 0, 0)
    screen = turtle.getscreen()                #setting up turtle screen
    screen.screensize(WIDTH, HEIGHT)
    screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)
    screen.delay(delay=0)
    pointer = turtle
    pointer.hideturtle()
    pointer.speed(0)
    pointer.up()
    return pointer


def main():
    """
    Main loop of calculator
    Gets the pixel origin location in the window and a ratio
    Loops a prompt getting expressions from user and drawing them
    :return: None
    """
    # Setup
    pointer = setup()
    # turtle.tracer(0)
    # Get configuration
    x_origin, y_origin = eval(input("Enter pixel coordinates of chart origin (x,y): "))
    ratio = int(input("Enter ratio of pixels per step: "))
    # Draw axis
    pointer.color(AXIS_COLOR)
    draw_x_axis(pointer, x_origin, y_origin, ratio)
    draw_y_axis(pointer, x_origin, y_origin, ratio)
    # turtle.update()
    # Get expressions
    expr = input("Enter an arithmetic expression: ")
    equation_counter = 0
    while (expr != ""):
      # Get colour and draw expression
      colour = get_color(equation_counter)
      draw_expression(pointer, expr,colour, x_origin, y_origin, ratio)
      turtle.update()
      expr = input("Enter an arithmetic expression: ")
      equation_counter += 1


main()
turtle.exitonclick()
