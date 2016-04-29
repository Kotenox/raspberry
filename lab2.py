print("Importando")
import matplotlib.pyplot as plt
from SimpleCV import Camera, Image, time

print("Usando Camera")
webcam=Camera()
print("Usando getImage")
time.sleep(5)
foto=webcam.getImage()
print("Salvando Foto Original")
foto.save("Foto.jpg")

print("Salvando Foto en escala de Grises")
fotogris=foto.grayscale()
fotogris.save("Foto_Gris.jpg")
print("Salvando Foto Binaria")
fotobinaria=foto.binarize()
fotobinaria.save("Foto_Binaria.jpg")
print("Salvando Foto dividida en canales")
(rojo,verde,azul)=foto.splitChannels()
rojo.save("Foto_rojo.jpg")
verde.save("Foto_verde.jpg")
azul.save("Foto_azul.jpg")

print("Generando Histogramas")
histgris=fotogris.histogram(255)
histrojo=rojo.histogram(255)
histverde=verde.histogram(255)
histazul=azul.histogram(255)

plt.plot(histgris)
plt.plot(histrojo)
plt.plot(histverde)
plt.plot(histazul)

print("Listo!")
