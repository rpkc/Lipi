from pyavrophonetic import avro
import keyboard


class KeyBoard():
    def __init__(self):
        self.state=keyboard._State()
        self.state.current:str=""
        self.halt:bool=False
 
    def keyboardHandeler(self,event):
        triggered_hoykey:bool=event.name=='space' or event.name=='enter'
        if self.halt:
            return        
        if triggered_hoykey and self.state.current!="":
            # print(self.state.current)
            replacement:str='\b'*(len(self.state.current)+1) + avro.parse(self.state.current)+" "
            self.state.current=""
            # print(replacement)
            keyboard.write(replacement)

        elif len(event.name)>1:
            if event.name == 'backspace':
                if len(self.state.current)>0:
                    self.state.current=self.state.current[:-1]            
        else:
            self.state.current+=event.name


    def __yesHalt(self,event):
        self.halt=True
    def __noHalt(self,event):
        self.halt=False

    def start(self):
        keyboard.on_press_key('ctrl',self.__yesHalt)
        keyboard.on_release_key('ctrl',self.__noHalt)
        keyboard.on_press(self.keyboardHandeler)

    def stop(self):
        keyboard.unhook_all() 
