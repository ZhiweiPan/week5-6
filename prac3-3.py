from tkinter import *
root = Tk()

language = ['C','python','php','html','SQL','java']
movie = ['CSS','jQuery','Bootstrap']

list1 = Listbox(root)
list2 = Listbox(root)

for item in language:
    list1.insert(0,item)
for item in movie:
    list2.insert(0,item)

list1.pack()
list2.pack()
root.mainloop()