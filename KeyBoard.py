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
        self.current:str=""  # to store the current string
        self.bengali:str=""  # to store the bengali translated String
        self.previous:str="" # to store the previous value of `current` string

    def keyPressEvent(self,event):
        # if event is a single char and `ctrl` is not pressed
        if len(event.name)==1 and not is_pressed('ctrl'):
            # then add that word to current state
            self.current+=event.name   

    def onPressHotkey(self,event)->None:
        self.bengali=parse(self.current) #parsed value will be stored in
        
        # fire backspace to delete previous word
        # then place the bengali word followed by triggered key 
        replace:str='\b'*(len(self.current)+1) + self.bengali + CODE_DICT[event.name]
        
        self.previous=self.current # store the current value to previous for `smart backspace` 
        self.current="" 
        write(replace) # write the string

    def smartBackspace(self,event)->None:
        if self.current!="": # for normal backspace
            self.current=self.current[:-1] # omit the last char
        # ** smart Backspace model **
        # ---------------------------
        # if `shift` is pressed and `bengali` string is not empty    
        elif is_pressed('shift') and self.bengali!="":
            # fire backspace to delete previous word
            # and the place the `previous`    
            replace:str='\b'*(len(self.bengali))+self.previous
            # now set the the current to previous
            self.current=self.previous
            write(replace) # write the string   

    def start(self):
        on_press(self.keyPressEvent)
        on_press_key('enter',self.onPressHotkey)
        on_press_key('space',self.onPressHotkey)
        on_press_key('backspace',self.smartBackspace)
        self.current:str=""

    def stop(self):
        unhook_all()
