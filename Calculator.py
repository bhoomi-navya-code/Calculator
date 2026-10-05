from Settings import *
from buttons import Button, ImageButton, NumButton, MathsButton, MathsImageButton
import customtkinter as ctk
from PIL import Image
import darkdetect 
try:
   from  ctypes import windll, byref, sizeof , c_int
except:
    pass
    
class Calculator(ctk.CTk):

    def __init__(self, is_dark):
        super().__init__( fg_color= (WHITE,BLACK))
        #window
        self.geometry(f'{APP_SIZE[0]}x{APP_SIZE[1]}')
        self.resizable(False,False)
        self.title('')
        self.iconbitmap('asset/icon.ico')
        ctk.set_appearance_mode(f'{'dark' if is_dark else 'light'}')
        self.change_titlebar_color(is_dark)

        #layout
        self.rowconfigure(list(range(MAIN_ROWS)),weight = 1, uniform = 'a')
        self.columnconfigure(list(range(MAIN_COLUMNS)),weight = 1, uniform = 'a')

        #data
        self.result_string = ctk.StringVar(value= '0')
        self.formula_string = ctk.StringVar(value= '')
        self.display_nums = []
        self.full_opration = []
        
        #widgts
        self.create_widget()

        #run
        self.mainloop()

    def create_widget(self):
        #fonts
        main_font = ctk.CTkFont(family= FONT,size= NORMAL_FONT_SIZE)
        reslut_font = ctk.CTkFont(family= FONT,size= OUTPUT_FONT_SIZE)

        #OUTPUT
        OutPutLabel(self,0,'SE', main_font,self.formula_string)
        OutPutLabel(self,1,'E',reslut_font,self.result_string)

        #button AC
        Button(
            parent= self, 
            func= self.AC_clear, 
            text= OPERATORS['clear']['text'] , 
            col =OPERATORS['clear']['col'],
            row =OPERATORS['clear']['row'],
            fonts= main_font
        )

        #percert button
        Button(
            parent= self, 
            func= self.percert, 
            text= OPERATORS['percert']['text'] , 
            col =OPERATORS['percert']['col'],
            row =OPERATORS['percert']['row'],
            fonts= main_font
        )

        # backsace button
        back_space_img = ctk.CTkImage(light_image= Image.open(OPERATORS['back_space']['image path']['light']),
                                  dark_image=Image.open(OPERATORS['back_space']['image path']['dark']),
                                  size = (30,30))
        ImageButton(parent = self, 
                    text =OPERATORS['back_space']['text'], 
                    func =self.back_space ,
                    col=OPERATORS['back_space']['col'],
                    row=OPERATORS['back_space']['row'],
                    image= back_space_img,
                    )

        #number button
        for num ,data in NUM_POSITIONS.items():
            NumButton( parent = self, 
                      text = num, 
                      func= self.num_press,
                      col = data['col'],
                      row= data['row'], 
                     fonts = main_font, 
                    )

        for  operator,data in MAIN_POSITIONS.items():
            if data['image path']:
                divide_img = ctk.CTkImage(light_image= Image.open(data['image path']['light']),
                                            dark_image=Image.open(data['image path']['dark']),
                                            size = (30,30))
                MathsImageButton(parent = self, 
                    func =self.maths_press ,
                     operator = operator,
                    col = data['col'],
                    row= data['row'], 
                    image= divide_img,)
            else:
                MathsButton( parent = self, 
                        text = data['character'], 
                        operator = operator,
                        func=self.maths_press,
                        col = data['col'],
                        row= data['row'], 
                        fonts = main_font, 
                        )
        
   #work
    def num_press(self,value):
      self.display_nums.append(str(value))
      full_num = '' .join(self.display_nums)
      self.result_string.set(full_num)

    def maths_press(self,value):
      current_num = '' .join(self.display_nums)
      if current_num:
          self.full_opration.append(current_num)

          if value != '=' :
              #update data
              self.full_opration.append(value)
              self.display_nums.clear()


              #update output

              self.result_string.set('')
              self.formula_string.set(' '.join(self.full_opration))
          else :
              formula = ' '.join(self.full_opration)


              try:
                 result = eval(formula)
              except Exception:
                  self.result_string.set('Error')
                  return

              if isinstance(result,float):
                 if result.is_integer():
                     result = int(result)
                 else:
                     result = round(result,6)
              
              
              #update data
              self.full_opration.clear()
              self.display_nums = [str(result)]
              

              #update output
              self.result_string.set(result)
              self.formula_string.set(formula)

      elif value == '-':
           self.display_nums.append('-')
           self.result_string.set('-')    
      
    def AC_clear(self):
        #clear output
        self.result_string.set(0)
        self.formula_string.set('')

        #clear data
        self.display_nums.clear()
        self.full_opration.clear()

    def back_space(self):
       if self.display_nums:
         #remove 
         self.display_nums.pop()


         # update
         if self.display_nums:
             self.result_string.set(''.join(self.display_nums)) 
         else:
             self.result_string.set('0')
                    
    def percert(self):
           if self.display_nums:
                #get perc
                current_number = float(''.join(self.display_nums))
                perc_num = current_number/100
               

                #update
                self.display_nums = list(str(perc_num))
                self.result_string.set(''.join(self.display_nums))
                

    # you need to call this funtion
    def change_titlebar_color(self, is_dark):
        try: 
            HWND = windll.user32.GetParent(self.winfo_id()) 
            DWMWA_ATTRIBUTE = 35 
            COLOR = TITLE_BAR_COLORS['dark'] if is_dark else TITLE_BAR_COLORS['light'] 
            windll.dwmapi.DwmSetWindowAttribute( HWND, DWMWA_ATTRIBUTE, byref(c_int(COLOR)), sizeof(c_int) ) 
        except: 
            pass

class OutPutLabel(ctk.CTkLabel):
    def __init__(self, parent,row, anchor, font,string_var):
        super().__init__(master = parent ,font= font, textvariable = string_var)
        self.grid(column = 0, columnspan = 4, row = row, sticky = anchor, padx = 10)

if __name__ == '__main__':
    Calculator(darkdetect.isDark())