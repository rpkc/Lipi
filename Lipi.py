from KeyBoard import KeyBoard
import tkinter


class Lipi():
    def __init__(self):
        self.root=tkinter.Tk()
        self.menu=tkinter.Menu(self.root)
        self.frame=tkinter.Frame(self.root)
        self.button=tkinter.Button(self.frame,command=self.__toogle,text="ENGLISH",cursor="hand2")
        self.label=tkinter.Label(self.root,text="Made by Rupak",bg="#ccc")
        self.start=False
        self.kb=KeyBoard()
    
    def __toogle(self):
        # to start or stop keyboard
        self.start=not self.start
        if self.start:
            # when start make text bengali
            self.kb.start()
            self.button['text']="বাংলা"
        else:
            # when start make text Default
            self.kb.stop()
            self.button['text']="ENGLISH"


    def mainloop(self):
        self.root.geometry("200x100")
        self.root.resizable(0,0)
        self.root.iconbitmap("image/icon.ico")
        self.root.title("লিপি")
        self.frame.pack(expand=True,fill=tkinter.BOTH,padx=10,pady=10)
        self.button.pack(expand=True,fill=tkinter.BOTH)
        self.label.pack(expand=True,fill=tkinter.BOTH) 
        self.root.mainloop()

a=Lipi()
a.mainloop()
