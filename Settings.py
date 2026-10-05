# size
APP_SIZE = (400,600)
MAIN_ROWS = 7
MAIN_COLUMNS = 4


#Test
FONT = 'Helvetica'
OUTPUT_FONT_SIZE = 70
NORMAL_FONT_SIZE = 32


STYLING = {
    'gap': 4,
    'corner-radius': 50
}

NUM_POSITIONS ={
    '.':{'col':2, 'row':6,'span':1},
    0:{'col':1, 'row':6,'span':1},
    1:{'col':0, 'row':5,'span':1},
    2:{'col':1, 'row':5,'span':1},
    3:{'col':2, 'row':5,'span':1},
    4:{'col':0, 'row':4,'span':1},
    5:{'col':1, 'row':4,'span':1},
    6:{'col':2, 'row':4,'span':1},
    7:{'col':0, 'row':3,'span':1},
    8:{'col':1, 'row':3,'span':1},
    9:{'col':2, 'row':3,'span':1},
    '00':{'col':0, 'row':6,'span':1},
}

MAIN_POSITIONS ={
    '/':{'col':3, 'row':2,'character': ' ', 'image path':  {"light" :'asset/divide-solid_dark.png','dark':'asset/divide-solid.png' }},
    '*':{'col':3, 'row':3,'character': 'x', 'image path': None},
    '-':{'col':3, 'row':4,'character': '-', 'image path': None},
    '=':{'col':3, 'row':6,'character': '=', 'image path': None},
    '+':{'col':3, 'row':5,'character': '+', 'image path': None},
}


OPERATORS = {
    'clear':{'col':0, 'row':2,'text':'AC', 'image path': None},
    'back_space':{'col':2, 'row':2,'text':'', 'image path': {"light" :'asset/delete-left-solid_dark.png','dark':'asset/delete-left-solid.png' }},
    'percert':{'col':1, 'row':2,'text':'%', 'image path': None},
}


COLORS ={
    'light-grey':{'fg': ('#E8ECF3', '#151925'), 'hover': ('#DDE3ED', '#1B2030'), 'text': ("#484C51", '#F5F7FF')},
    'dark-grey':{'fg': ("#BEC4CD", '#202638'), 'hover': ("#B6BCC6", '#252E48'), 'text': ('#374151', '#F5F7FF')},
    'blue':{'fg': ("#4478C7", "#3D79D3"), 'hover': ('#5289F5', "#2357A4"), 'text': ("#19191A", '#FFFFFF')},
    'purple-highlight':{'fg': ("#7761A4", "#5C31B0"), 'hover': ("#7A54CB", "#6A4CA7"), 'text': ("#1C1C1C", '#FFFFFF')},
}

TITLE_BAR_COLORS = {
    'dark':  0x00251915 ,
    'light': 0x00E8DCD5
}

BLACK =  '#151925'
WHITE = '#D5DCE8'

