import os
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

GUIpieTryOut = Tk()
GUIpieTryOut.title('Warsaw Wireless')
GUIpieTryOut.resizable(False, False)
GUIpieTryOut.geometry('800x600')
GUIpieTryOut.grid_propagate(False)

for x in range(20):
  Grid.columnconfigure(GUIpieTryOut, x, weight=1, uniform='row')
for y in range(15):
  Grid.rowconfigure(GUIpieTryOut, y, weight=1, uniform='row')
for x in range(20):
  for y in range(15):
    Label(GUIpieTryOut, width = 1, bg = '#000000').grid(row = y, column = x, sticky = N+S+E+W)

init = True
GUIpieTryOut.welcome = Label(GUIpieTryOut, text = "Welcome to Warsaw Wireless ", font = ('Arial', 16), width = 1, height = 1, fg = '#FFFFFF', bg = '#E77F00')
GUIpieTryOut.welcome.grid(row = 1, column = 4, columnspan = 12, rowspan = 2, sticky = N+S+E+W)
 v   
def runnewSale(argument):
  if not(__name__ == '__main__'):
    from main0 import newSale
    newSale(argument)

def runshowSale(argument):
  if not(__name__ == '__main__'):
    from main0 import showSale
    showSale(argument)

def runaddProduct(argument):
  if not(__name__ == '__main__'):
    from main0 import addProduct
    addProduct(argument)

def runshowProducts(argument):
  if not(__name__ == '__main__'):
    from main0 import showProducts
    showProducts(argument)

def runshowGoals(argument):
  if not(__name__ == '__main__'):
    from main0 import showGoals
    showGoals(argument)

def rundestroy(argument):
  if not(__name__ == '__main__'):
    from main0 import destroy
    destroy(argument)

GUIpieTryOut.Sale = Button(GUIpieTryOut, text = "New Sale", font = ('Arial', 16), width = 1, height = 1, fg = '#FFFFFF', command = lambda: runnewSale("Sale"), bg = '#E77F00')
GUIpieTryOut.Sale.grid(row = 3, column = 16, columnspan = 3, rowspan = 1, sticky = N+S+E+W)
GUIpieTryOut.showSale = Button(GUIpieTryOut, text = "View Sales", font = ('Arial', 16), width = 1, height = 1, fg = '#FFFFFF', command = lambda: runshowSale("showSale"), bg = '#E77F00')
GUIpieTryOut.showSale.grid(row = 5, column = 16, columnspan = 3, rowspan = 1, sticky = N+S+E+W)
GUIpieTryOut.addProduct = Button(GUIpieTryOut, text = "New Product", font = ('Arial', 16), width = 1, height = 1, fg = '#ffffff', command = lambda: runaddProduct("addProduct"), bg = '#E77F00')
GUIpieTryOut.addProduct.grid(row = 7, column = 16, columnspan = 3, rowspan = 1, sticky = N+S+E+W)
GUIpieTryOut.productList = Button(GUIpieTryOut, text = "Product List", font = ('Arial', 16), width = 1, height = 1, fg = '#ffffff', command = lambda: runshowProducts("productList"), bg = '#E77F00')
GUIpieTryOut.productList.grid(row = 9, column = 16, columnspan = 3, rowspan = 1, sticky = N+S+E+W)
GUIpieTryOut.goals = Button(GUIpieTryOut, text = "View Goals", font = ('Arial', 16), width = 1, height = 1, fg = '#ffffff', command = lambda: runshowGoals("goals"), bg = '#E77F00')
GUIpieTryOut.goals.grid(row = 11, column = 16, columnspan = 3, rowspan = 1, sticky = N+S+E+W)
GUIpieTryOut.exit = Button(GUIpieTryOut, text = "Exit", font = ('Arial', 16), width = 1, height = 1, fg = '#E77F00', command = lambda: rundestroy("exit"), bg = '#ffffff')
GUIpieTryOut.exit.grid(row = 13, column = 16, columnspan = 3, rowspan = 1, sticky = N+S+E+W)
GUIpieTryOut.Image1Original = Image.open(r'B:/Python/WarsawApp/logo0.jpg')
GUIpieTryOut.Image1Image = ImageTk.PhotoImage(GUIpieTryOut.Image1Original.resize((160, 120), Image.ANTIALIAS))
GUIpieTryOut.Image1 = Label(GUIpieTryOut, image = GUIpieTryOut.Image1Image, width = 1, height = 1, bg = '#000000')
GUIpieTryOut.Image1.grid(row = 0, column = 0, columnspan = 4, rowspan = 3, sticky = N+S+E+W)
GUIpieTryOut.Image2Original = Image.open(r'B:/Python/WarsawApp/logo0.jpg')
GUIpieTryOut.Image2Image = ImageTk.PhotoImage(GUIpieTryOut.Image2Original.resize((160, 120), Image.ANTIALIAS))
GUIpieTryOut.Image2 = Label(GUIpieTryOut, image = GUIpieTryOut.Image2Image, width = 1, height = 1, bg = '#000000')
GUIpieTryOut.Image2.grid(row = 0, column = 16, columnspan = 4, rowspan = 3, sticky = N+S+E+W)

def initModules():
  from main0 import newSale
  from main0 import showSale
  from main0 import addProduct
  from main0 import showProducts
  from main0 import showGoals
  from main0 import destroy

GUIpieTryOut.initModules = initModules

def hide():
  GUIpieTryOut.withdraw()

def show():
  GUIpieTryOut.deiconify()

def run():
  global init
  GUIpieTryOut.update()
  GUIpieTryOut.update_idletasks()
  if init:
    GUIpieTryOut.welcome.config(wraplength = GUIpieTryOut.welcome.winfo_width() + 2)
    GUIpieTryOut.Sale.config(wraplength = GUIpieTryOut.Sale.winfo_width() + 2)
    GUIpieTryOut.showSale.config(wraplength = GUIpieTryOut.showSale.winfo_width() + 2)
    GUIpieTryOut.addProduct.config(wraplength = GUIpieTryOut.addProduct.winfo_width() + 2)
    GUIpieTryOut.productList.config(wraplength = GUIpieTryOut.productList.winfo_width() + 2)
    GUIpieTryOut.goals.config(wraplength = GUIpieTryOut.goals.winfo_width() + 2)
    GUIpieTryOut.exit.config(wraplength = GUIpieTryOut.exit.winfo_width() + 2)
    init = False
    
GUIpieTryOut.run = run
GUIpieTryOut.hide = hide
GUIpieTryOut.show = show

if __name__ == "__main__":
  while True:
    GUIpieTryOut.run()
