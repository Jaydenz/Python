import tkinter

window = tkinter.Tk()
window.title('Aria2 GUI')
window.geometry("1000x600")
var = tkinter.StringVar()


L = tkinter.Label(window,
                  text = 'Aria2 GUI',
                  font = ('微软雅黑', 12),
                  width = 20, height = 1
                  )
L.pack()


window.mainloop()

