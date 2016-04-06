print("Importando")
from SimpleCV import Camera, Display, Image
print("usando Camera()")
webcam=Camera()
print("Usando getImage")
foto=webcam.getImage()
print("Salvando Foto")
foto.save("ohmy.jpg")
