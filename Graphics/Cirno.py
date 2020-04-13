# подключение библиотеки под синонимом gr
import graphics as gr

# Инициализация окна с названием "Russian game" и размером 100х100 пикселей
window = gr.GraphWin("Jenkslex and Ganzz project", 400, 400)



dress = gr.Polygon(gr.Point(100, 300), gr.Point(300, 300), gr.Point(200, 100))
dress.setFill('blue')
dress.setOutline('black')

dress1 = gr.Polygon(gr.Point(100, 300), gr.Point(150, 300), gr.Point(125, 275))
dress1.setFill('white')
dress1.setOutline('black')

dress2 = gr.Polygon(gr.Point(150, 300), gr.Point(200, 300), gr.Point(175, 275))
dress2.setFill('white')
dress2.setOutline('black')

dress3 = gr.Polygon(gr.Point(200, 300), gr.Point(250, 300), gr.Point(225, 275))
dress3.setFill('white')
dress3.setOutline('black')

dress4 = gr.Polygon(gr.Point(250, 300), gr.Point(300, 300), gr.Point(275, 275))
dress4.setFill('white')
dress4.setOutline('black')

wing1 = gr.Polygon(gr.Point(225, 200), gr.Point(285, 225), gr.Point(345, 200), gr.Point(285, 175))
wing1.setFill(gr.color_rgb(166,228,255))
wing1.setOutline('black')

wing2 = gr.Polygon(gr.Point(220, 170), gr.Point(280, 170), gr.Point(320, 130), gr.Point(260, 130))
wing2.setFill(gr.color_rgb(166,228,255))
wing2.setOutline('black')

wing3 = gr.Polygon(gr.Point(230, 230), gr.Point(290, 230), gr.Point(330, 270), gr.Point(270, 270))
wing3.setFill(gr.color_rgb(166,228,255))
wing3.setOutline('black')

wing4 = gr.Polygon(gr.Point(175, 200), gr.Point(115, 225), gr.Point(55, 200), gr.Point(115, 175))
wing4.setFill(gr.color_rgb(166,228,255))
wing4.setOutline('black')

wing5 = gr.Polygon(gr.Point(180, 170), gr.Point(120, 170), gr.Point(80, 130), gr.Point(140, 130))
wing5.setFill(gr.color_rgb(166,228,255))
wing5.setOutline('black')

wing6 = gr.Polygon(gr.Point(170, 230), gr.Point(110, 230), gr.Point(70, 270), gr.Point(130, 270))
wing6.setFill(gr.color_rgb(166,228,255))
wing6.setOutline('black')

bant = gr.Polygon(gr.Point(110, 50), gr.Point(200, 70), gr.Point(290, 50), gr.Point(280, 85), gr.Point(290, 120), gr.Point(200, 110), gr.Point(110, 120), gr.Point(120, 85))
bant.setFill(gr.color_rgb(0,162,232))
bant.setOutline('black')

hair = gr.Polygon(gr.Point(139, 90), gr.Point(140, 70), gr.Point(160, 40), gr.Point(200, 35), gr.Point(240, 40), gr.Point(260, 70), gr.Point(261, 90))
hair.setFill(gr.color_rgb(21,185,255))
hair.setOutline('black')

face = gr.Circle(gr.Point(200, 100), 60)
face.setFill('yellow')


wing1.draw(window)
wing2.draw(window)
wing3.draw(window)
wing4.draw(window)
wing5.draw(window)
wing6.draw(window)
dress.draw(window)
dress1.draw(window)
dress2.draw(window)
dress3.draw(window)
dress4.draw(window)
bant.draw(window)
face.draw(window)
hair.draw(window)



window.getMouse()

window.close()