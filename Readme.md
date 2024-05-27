# OCR avec Tesseract et OpenCV

Ce projet démontre comment effectuer la reconnaissance optique de caractères (OCR) sur des images en utilisant Tesseract et OpenCV en Python. Le script lit une image, la traite pour extraire le texte et met en surbrillance le texte détecté sur l'image.

## Prérequis

- Python 3.x
- OpenCV
- pytesseract
- Pillow

### Installation

1. **Python**: Assurez-vous que Python est installé sur votre système. Vous pouvez le télécharger sur [python.org](https://www.python.org/downloads/).

2. **Installer les dépendances**: Installez les paquets Python requis en utilisant `pip` :
   ```sh
   pip install -r requirements.txt
3. **Assurez-vous que Tesseract est installé sur votre système.** 
    Vous pouvez l'installer en utilisant :
        - Pour Windows : [Téléchargez ici](https://github.com/UB-Mannheim/tesseract/wiki)
        - Pour macOS : `brew install tesseract`
        - Pour Linux : Utilisez votre gestionnaire de paquets, par exemple, `sudo apt-get install tesseract-ocr`

### Utilisation

1. **Préparez l'image** Assurez vous d'avoir une image dans le meme répertoire que votre script

2. **Exécuter le script** Exécutez le script python en ouvrant un terminal et en tapant cette ligne de code : python script.py

3. **Résultat** Le script affiche l'image avec des rectangles déssisnés autour du texte détecté et le texte superposé sur l'image.