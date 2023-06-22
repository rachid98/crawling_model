import requests
from bs4 import BeautifulSoup
import re

# URL de la page à crawler
url = "https://code.travail.gouv.fr/convention-collective/1486-bureaux-detudes-techniques-cabinets-dingenieurs-conseils-et-societes-de"

# Envoi de la requête HTTP et récupération du contenu de la page
response = requests.get(url)
content = response.content

# Vérifier si la requête a réussi
if response.status_code == 200:
    # Parser le contenu HTML de la page
    soup = BeautifulSoup(response.content, "html.parser")
    # with open("template_html.txt", "w", encoding="utf-8") as fichier:
    #     fichier.write(f"{soup.prettify()}",)
    test = soup.find_all(["div", "a"],class_ =["sc-dAlyuH jPBRFo", "sc-f36b7225-0 fPOxyW", "sc-bmzYkS cIuQvc sc-1a4a1107-0 ioZrZV no-after" ])
    with open("template_FAQ.txt", "w", encoding="utf-8") as fichier:
        for t in test :
            fichier.write(t.get_text() +"\n")