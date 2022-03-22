#Bridge design pattern .
# The bridge design pattern devides de logic of a very big class into 2 hierarchies of smaller classes 
# that can be developed independently.
# The bridge patter is specially usefull to deal with multiplatform apps.

from devices import WebCam,Camera
from Streaming import Youtube,Discord

# create devices 

camera = Camera()
webcam = WebCam()

# create streaming 

youtube = Youtube(webcam)
discord  = Discord(webcam)

# start serices 
youtube.fill_buffer()
youtube.start_stream()
discord.fill_buffer()
discord.start_stream()