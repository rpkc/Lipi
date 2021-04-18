# MIT License

# Copyright (c) 2021 Rupak Chowdhury

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from pyavrophonetic.avro import parse
from keyboard import on_press,on_press_key,is_pressed,write,unhook_all

CODE_DICT:dict={'space':' ','enter':'\n'}
 
class KeyBoard():
    def __init__(self):
        self.current:str=""
        self.replace:str=""

    def keyPressEvent(self,event):
        # if event is a single char and `ctrl` is not pressed
        if len(event.name)==1 and not is_pressed('ctrl'):
            # then add that word to current state
            self.current+=event.name   

        elif event.name=='backspace' and self.current!="":
            #when backspace is pressed, delete the last character of current string
            self.current=self.current[:-1]

    def onPressHotkey(self,event)->None:
        # when hotkey ('enter' or 'space') is pressed, this will parse the text 
        self.replace:str='\b'*(len(self.current)+1) + parse(self.current) + CODE_DICT[event.name]
        self.current=""
        write(self.replace)


    def start(self):
        on_press(self.keyPressEvent)
        on_press_key('enter',self.onPressHotkey)
        on_press_key('space',self.onPressHotkey)

    def stop(self):
        unhook_all()
