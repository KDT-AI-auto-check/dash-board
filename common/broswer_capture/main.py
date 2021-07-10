from datetime import datetime
from title_capture import capture_window, get_titles, show_img

timestr = datetime.now().strftime('%m%d_%H%M%S')
title = 'Meet - k-digitalhackathon - Chrome'
path = f'./{title}_{timestr}.png'

# get_titles()
capture_window(title, path)
show_img(path)