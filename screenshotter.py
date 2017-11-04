from main import Main
from PIL import Image
import time
from skimage import color, transform, exposure

game = Main()


for i in range(9999999):
    _, test, _ = game.MainLoop()
    if i>400:

        gray = color.rgb2gray(test)
        resized_gray = transform.resize(gray,(80,80))
        result = Image.fromarray(test, 'RGB')
        result.show()
        result.save('screenshot.png')

        #We have the details of all pixels on a screen on this frame. next step is convert it to grayscale and resize it to 80x80

        result = Image.fromarray(gray*255)
        result.show()
        result.convert('RGB').save('grayscale.png')
        result = Image.fromarray(resized_gray*255)
        result.show()
        result.convert('RGB').save('downsized.png')

        import time
        time.sleep(99999)
