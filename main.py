from PIL import Image
import turtle

im = Image.open('input.jpg')
pix = im.load()
rgb_pix = im.convert('RGB')
x, y = rgb_pix.size

turtle.colormode(255)
t = turtle.Turtle()
t.speed(10)
t.shape("turtle")

for i in range(y):
    for j in range(x):
        r,g,b = rgb_pix.getpixel((j,i))
        t.pencolor(r,g,b)
        t.forward(1)
    t.right(90)
    t.forward(1)
    t.right(90)
    t.forward(x)
    t.right(90)
    t.right(90)
    print(j,i)

turtle.mainloop()

