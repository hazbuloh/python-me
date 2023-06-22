from tkinter import*
from PIL import ImageTk,Image

root = Tk()
root.title("PictureShow")
root.geometry("300x300")
root.iconbitmap('logo.ico')

my_img = ImageTk.PhotoImage(Image.open("logo.ico"))
my_lb = Label(text=my_img)
my_lb.pack()


root.mainloop()