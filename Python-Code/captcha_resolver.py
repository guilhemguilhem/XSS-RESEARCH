#Build for a root-me challenge

import requests
from PIL import Image
import base64
from io import BytesIO
import pytesseract
import cv2
import numpy as np
from bs4 import BeautifulSoup
import time
import json


# URL de la page contenant l'image
url = "http://challenge01.root-me.org/programmation/ch8/"

# Récupérer le contenu HTML de la page
response = requests.get(url)
headers = response.headers
cookie = response.cookies


# Enregistrement des en-têtes dans un fichier headers.txt
with open("headers.txt", "w") as file:
    for header, value in headers.items():
        file.write(f"{header}: {value}\n")
        


html_content = response.text

# Trouver la balise <img> dans le contenu HTML
start_tag = "<img"
end_tag = ">"
start_index = html_content.find(start_tag)
end_index = html_content.find(end_tag, start_index)
img_tag = html_content[start_index:end_index + 1]

# Extraire le contenu en base64 de la balise <img>
start_base64 = img_tag.find("base64,") + 7
end_base64 = img_tag.find("\"", start_base64)
base64_content = img_tag[start_base64:end_base64]

# Décoder le contenu base64 en une image
image_data = base64.b64decode(base64_content)
image_tmp = Image.open(BytesIO(image_data))
#image.show()

# Enregistrer l'image en tant que fichier PNG
image_tmp.save("1.png", "PNG")

image = cv2.imread("1.png")



# Conversion de l'image en niveaux de gris
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Seuillage de l'image pour obtenir le fond en blanc
_, threshold = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

# Définir le kernel pour la morphologie
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))

# Fermeture morphologique pour remplir les petits trous
closed = cv2.morphologyEx(threshold, cv2.MORPH_CLOSE, kernel)

# Inversion des couleurs de l'image
inverted = cv2.bitwise_not(closed)

# Enregistrer l'image result_gray
cv2.imwrite("result_gray.jpg", inverted)

# Appliquer la reconnaissance optique de caractères (OCR) pour extraire le texte de l'image
text = pytesseract.image_to_string(inverted, config='--psm 6')
text = text.replace('\n', '')
text2 = str(text)

# Données à envoyer dans la requête POST
data = {
    "cametu": text2
}

# Lecture des en-têtes depuis le fichier headers.txt
with open("headers.txt", "r") as file:
    saved_headers = {}
    for line in file:
        header, value = line.strip().split(": ")
        saved_headers[header] = value

req = requests.post(url, data=data, cookies=cookie)

# Vérifier le code de statut de la réponse
if req.status_code == 200:
    content = req.content
    print(req.text)

    # Créer un objet BeautifulSoup pour le contenu HTML
    soup = BeautifulSoup(content, "html.parser")

    # Trouver toutes les balises <p> et imprimer leur contenu
    paragraphs = soup.find_all("p")
    for paragraph in paragraphs:
        print(paragraph.text)
        # Afficher le texte extrait
        print("Texte extrait de l'image :\n" + text2)
else:
    print("La requête a échoué avec le code", req.status_code)
