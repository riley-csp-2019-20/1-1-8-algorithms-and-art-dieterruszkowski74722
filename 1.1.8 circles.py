import turtle as trtl

ike = trtl.Turtle()
#ike.pencolor("random")
ike.penup()
for i in range(1, 500, 50):
    ike.right(90)    # Face South
    #ike.forward(i)   # Move one radius
    ike.right(270)   # Back to start heading
    ike.pendown()    # Put the pen back down
    ike.circle(i)    # Draw a circle
    ike.penup()      # Pen up while we go home
    
    


wn = trtl.Screen()
wn.mainloop()