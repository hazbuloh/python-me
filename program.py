from tkinter import*

root = Tk()
root.title("MyGui")
root.geometry("300x300")

menuItem = Menu()
menuItem.add_command(label = "new windows")
menuItem.add_command(label = "test2")


myMenu = Menu()
root.config(menu = myMenu)

myMenu.add_cascade(label = "File",menu=menuItem)
myMenu.add_cascade(label = "Edit")
myMenu.add_cascade(label = "View")





root.mainloop()