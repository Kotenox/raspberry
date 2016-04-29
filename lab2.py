print("Importando, espere...")
import matplotlib.pyplot as plt
from SimpleCV import Camera, Image, time

print("Usando Camera")
webcam=Camera()
print("Usando getImage")
time.sleep(5)
foto=webcam.getImage()
print("Salvando Foto Original")
foto.save("Original.jpg")

print("Salvando Foto en escala de Grises")
fotogris=foto.grayscale()
fotogris.save("Grises.jpg")

print("Salvando Foto dividida en canales")
(rojo,verde,azul)=foto.splitChannels()
rojo.save("Rojo.jpg")
verde.save("Verde.jpg")
azul.save("Azul.jpg")

print("Salvando Foto Binaria")
fotobinaria=foto.binarize()
fotobinaria.save("Binaria.jpg")

print("Generando Histogramas")
histgris=fotogris.histogram(255)
histrojo=rojo.histogram(255)
histverde=verde.histogram(255)
histazul=azul.histogram(255)

print("Salvando Histogramas")
fig=plt.figure()
plt.plot(histgris)
plt.title("Gris")
plt.show()
fig.savefig("Hist_Gris.png")

fig=plt.figure()
plt.plot(histrojo)
plt.title("Rojo")
plt.show()
fig.savefig("Hist_Rojo.png")

fig=plt.figure()
plt.plot(histverde)
plt.title("Verde")
plt.show()
fig.savefig("Hist_Verde.png")

fig=plt.figure()
plt.plot(histazul)
plt.title("Azul")
plt.show()
fig.savefig("Hist_Azul.png")

print("Listo!")
