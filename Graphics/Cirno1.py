import graphics as gr


window = gr.GraphWin("Strongest!", 400, 400)


def triangle(x, y, w, h, color='blue'):
    dress = gr.Polygon(gr.Point(x, y), gr.Point(x+w, y), gr.Point(x+w/2, y-h))
    dress.setFill(color)
    dress.setOutline('black')
    dress.draw(window)
    
def dress(x, y, w, h):
    triangle(x, y, w, h)
    for i in range(4):
        triangle(x+i*w/4, y, w/4, h/6, 'white')

def wings(x, y, w, h):
    def draw(wing):
        wing.setFill(gr.color_rgb(166,228,255))
        wing.setOutline('black')
        wing.draw(window)
    
    x2=x*0.98
    y2=y-h/2
    wing2 = gr.Polygon(gr.Point(x2, y2), gr.Point(x2+w*0.35, y2-h), gr.Point(x2+w*0.9, y2-h), gr.Point(x2+w*0.52, y2))
    draw(wing2)
    
    x3=x*1.02
    y3=y+h*1.5
    wing3 = gr.Polygon(gr.Point(x3, y3-h), gr.Point(x3+w*0.35, y3), gr.Point(x3+w*0.9, y3), gr.Point(x3+w*0.52, y3-h))
    draw(wing3)

    wing1 = gr.Polygon(gr.Point(x, y), gr.Point(x+w/2, y-h/2), gr.Point(x+w, y), gr.Point(x+w/2, y+h/2))
    draw(wing1)
    
def head(x, y, w):
    hair = gr.Polygon(gr.Point(139, 90), gr.Point(140, 70), gr.Point(160, 40), gr.Point(200, 35), gr.Point(240, 40), gr.Point(260, 70), gr.Point(261, 90))
    hair = gr.Polygon(gr.Point(x-w, y-w*0.2), gr.Point(x-w*0.99, y-w*0.5), gr.Point(x-w*0.6, y-w), gr.Point(x, y-w*1.1), gr.Point(x+w*0.6, y-w), gr.Point(x+w*0.99, y-w*0.5), gr.Point(x+w, y-w*0.2))
    hair.setFill(gr.color_rgb(21,185,255))
    hair.setOutline('black')

    face = gr.Circle(gr.Point(x, y), w)
    face.setFill('yellow')
    face.draw(window)
    hair.draw(window)
    


bant = gr.Polygon(gr.Point(110, 50), gr.Point(200, 70), gr.Point(290, 50), gr.Point(280, 85), gr.Point(290, 120), gr.Point(200, 110), gr.Point(110, 120), gr.Point(120, 85))
bant.setFill(gr.color_rgb(0,162,232))
bant.setOutline('black')




wings(225,200,130,50)
wings(175,200,-130,-50)
dress(100,300,200,200)
bant.draw(window)
head(200, 100, 60)



window.getMouse()

window.close()