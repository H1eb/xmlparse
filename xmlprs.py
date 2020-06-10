from tkinter import *
import xml.etree.ElementTree as ET
from tkinter import messagebox
import re

def click_button():
    for i in range(height):  # Rows
        for j in range(width):  # Columns
            if i == 0:
                b = Entry(root, text="")
                b.grid(row=i, column=j)
                if j == 0:
                    b.insert(i, 'title')
                if j == 1:
                    b.insert(i, 'author')
                if j == 2:
                    b.insert(i, 'binding')
                if j == 3:
                    b.insert(i, 'pages')
                if j == 4:
                    b.insert(i, '$')
                if j == 5:
                    b.insert(i, 'rub')
            else:
                b = Entry(root, text="")
                b.grid(row=i, column=j)
                if j < 4:
                    b.insert(i, xml[i - 1][j].text)
                if j == 4:
                    x1 = re.sub(r"\W", r'', xml[i - 1][j].text)
                    b.insert(i, re.sub(r"\W", r'', x1))
                if j == 5:
                    b.insert(i, round(int(x1)*68.67, 2))

def edit_click():
    messagebox.showinfo("About", "Работу выполнили Сергеев, Матюшин, Шнабская")

def click_exit():
    sys.exit()

tree = ET.parse('/1.xml')
xml = tree.getroot()
root = Tk()
root.title("XML parse")
height = len(xml) + 1
width = 6
root.resizable(False, False)

for i in range(height):  # Rows
    for j in range(width):  # Columns
        b = Entry(root, text="")
        b.grid(row=i, column=j)

main_menu = Menu()

file_menu = Menu()
file_menu.add_command(label="Open", command=click_button)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=click_exit)

main_menu.add_cascade(label="File", menu=file_menu)
main_menu.add_cascade(label="About", command=edit_click)

root.config(menu=main_menu)

root.mainloop()