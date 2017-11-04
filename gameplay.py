from main import Main
from keras.models import Sequential
from keras.layers.core import Dense, Flatten
from keras.layers import Conv2D
game = Main()

model = Sequential()
model.add(Dense(512, input_dim=512))
while True:
    game.MainLoop(3)
