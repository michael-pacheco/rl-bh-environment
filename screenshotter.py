from main import Main
from PIL import Image
import time
from skimage import color, transform, exposure

game = Main()

from config import num_of_cols, num_of_rows

for i in range(9999999):
    _, test, _ = game.MainLoop(3)
    if i>200:

        gray = color.rgb2gray(test)
        resized_gray = transform.resize(gray,(num_of_cols,num_of_rows))
        result = Image.fromarray(test, 'RGB')
        result.show()
        result.save('screenshots/screenshot.png')

        #We have the details of all pixels on a screen on this frame. next step is convert it to grayscale and resize it to 80x80

        result = Image.fromarray(gray*255)
        result.show()
        result.convert('RGB').save('screenshots/grayscale.png')
        result = Image.fromarray(resized_gray*255)
        result.show()
        result.convert('RGB').save('screenshots/downsized.png')

        import time
        time.sleep(99999)
