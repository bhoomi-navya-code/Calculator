from customtkinter import CTkButton
from Settings import *

class Button(CTkButton):
    def __init__(self, parent, text , func,col,row, fonts,color = 'blue'):
        super().__init__( master= parent,
                         text= text ,
                         corner_radius= STYLING['corner-radius'],
                         font= fonts,
                         command= func,
                         fg_color= COLORS[color]['fg'],
                         hover_color= COLORS[color]['hover'],
                         text_color= COLORS[color]['text'],
                         cursor = 'hand2')
        self.grid(column = col ,row = row, sticky = 'NEWS',padx = 3, pady = 2)

class NumButton(Button):
    def __init__(self, parent, text, func, col, row, fonts, color='dark-grey'):
        super().__init__(parent = parent , 
                         text = text, 
                         func = lambda:func(text),
                         col = col , 
                         row = row , 
                         fonts = fonts, 
                         color = color)

class MathsButton(Button):
    def __init__(self, parent, text, operator,func, col, row, fonts, color='purple-highlight'):
        super().__init__(parent = parent , 
                         text = text, 
                         func = lambda:func(operator),
                         col = col , 
                         row = row , 
                         fonts = fonts, 
                         color = color)

class ImageButton(CTkButton):
    def __init__(self, parent, text , func,col,row, image ,color = 'blue'):
        super().__init__( master= parent,
                         text= text ,
                         corner_radius= STYLING['corner-radius'],
                         image= image,
                         command= func,
                         fg_color= COLORS[color]['fg'],
                         hover_color= COLORS[color]['hover'],
                         text_color= COLORS[color]['text'],
                         cursor = 'hand2')
        self.grid(column = col ,row = row, sticky = 'NEWS',padx = STYLING['gap'], pady=STYLING['gap'])


class MathsImageButton(ImageButton):
    def __init__(self, parent, func, col, operator,row, image, color='purple-highlight'):
        super().__init__(parent = parent , 
                         func = lambda:func(operator),
                         col = col , 
                         text='', 
                         row = row , 
                         image= image,
                         color = color)
                         