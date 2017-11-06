import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__))+"/game")
#sys.path.append(os.path.dirname(os.path.abspath(__file__))+'/game/images')

from main import Main
from keras.models import Sequential
from keras.layers.core import Dense, Flatten
from keras.layers import Conv2D
game = Main()

model = Sequential()
while True:
    game.MainLoop(3)
