import time
import keyboard
from os import system
system('clear')

while(1):
    print('Saida gerada...')
    if(keyboard.is_pressed('a')):
      break
    time.sleep(0.5)