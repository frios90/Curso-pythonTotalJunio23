import bs4
import requests
import base64

escuela = "https://www.escueladirecta.com/"
barby = "https://www.instagram.com/barbybox"
resultado = requests.get(escuela)

##Paso el contenido a un archivo
archivo = open("Dia11.webScraping/archivos/test001.html", "w")
archivo.write(resultado.text)
archivo.close()

sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

div = sopa.select("div")
h1 = sopa.select("h1")
parrafos = sopa.select("p")
img = sopa.select("img")

print(len(img))
for key, e in enumerate(img):

    print(e["src"])
    imagen = requests.get(e["src"])
    imagen = imagen.content
    archivo2 = open("Dia11.webScraping/imgs/img00"+str(key)+".jpg", "wb")
    archivo2.write(imagen)
    archivo2.close()

# archivo2 = open("Dia11.webScraping/archivos/test002.html", "w")
# archivo2.write(sopa.select("title")[0].text)
# archivo2.close()