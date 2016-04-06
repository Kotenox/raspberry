Python 2.7.9 (default, Mar  8 2015, 00:52:26) 
[GCC 4.9.2] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> from SimpleCV import Camera, Display, Image
>>> time.sleep(10)
>>> webcam = Camera()
>>> time.sleep(10)
>>> foto = webcam.getImage()
>>> time.sleep(10)
>>> foto.save("myfirst.png")
