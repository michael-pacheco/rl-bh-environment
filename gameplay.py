import sys, os
from main import Main
from keras.models import Sequential
from keras.layers.core import Dense, Flatten
from keras.layers import Conv2D
game = Main()

model = Sequential()
while True:
    game.MainLoop(3)
