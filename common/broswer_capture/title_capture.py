import pygetwindow
import pyautogui
from PIL import Image

def capture_window(title, path):
  window = pygetwindow.getWindowsWithTitle(title)[0]
  x1, y1 = window.topleft
  x2, y2 = window.bottomright

  pyautogui.screenshot(path)

  im = Image.open(path)
  im = im.crop((x1, y1, x2, y2))
  im.save(path)

def get_titles():
  print(pygetwindow.getAllTitles())


def show_img(path):
  im = Image.open(path)
  im.show(path)


# https://www.youtube.com/watch?v=hvy9UzMTXpg