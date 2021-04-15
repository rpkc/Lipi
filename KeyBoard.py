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

from pyavrophonetic import avro
import keyboard



class KeyBoard():
    def __init__(self):
        self.state=keyboard._State()
        self.state.current:str=""
        self.halt:bool=False
 
    def keyboardHandeler(self,event):
        #it triggers when 'space' or 'enter' is presses
        triggered_hoykey:bool=event.name=='space' or event.name=='enter'
        # if halt happens, meaning Ctrl is pressed    
        if self.halt:
            return
        # when triggers
        if triggered_hoykey and self.state.current!="":
            # backspace all characters in buffer and
            # avro.parse() makes all stored characters bengali
            replacement:str='\b'*(len(self.state.current)+1) + avro.parse(self.state.current)+" "
            # make buffer empty
            self.state.current=""
            # print all chars 
            keyboard.write(replacement)
        # if keystroke is not a visible chaacter    
        elif len(event.name)>1:
            if event.name == 'backspace':
                if len(self.state.current)>0:
                    self.state.current=self.state.current[:-1]
        # add new char to main string           
        else:
            self.state.current+=event.name

# two functions to halt the process
    # start halt
    def __yesHalt(self,event):
        self.halt=True
    # stop halt    
    def __noHalt(self,event):
        self.halt=False

    def start(self):
        # when 'ctrl' will be pressed, do nothing
        keyboard.on_press_key('ctrl',self.__yesHalt)
        keyboard.on_release_key('ctrl',self.__noHalt)
        keyboard.on_press(self.keyboardHandeler)

    def stop(self):
        keyboard.unhook_all() 
