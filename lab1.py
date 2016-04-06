print("Importando")
from SimpleCV import Camera, Display, Image
import time
print("usando Camera()")
webcam=Camera()
print("Usando getImage")
time.sleep(5)
foto=webcam.getImage()
print("Salvando Foto")
foto.save("Foto.jpg")
