>>> from SimpleCV import Camera, Display, Image
>>> time.sleep(5)
>>> webcam = Camera()
>>> foto = webcam.getImage()
>>> time.sleep(20)
>>> foto.save("myfirst.png")
