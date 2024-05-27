# OCR avec Tesseract et OpenCV

Ce projet démontre comment effectuer la reconnaissance optique de caractères (OCR) sur des images en utilisant Tesseract et OpenCV en Python. Le script lit une image, la traite pour extraire le texte et met en surbrillance le texte détecté sur l'image.

## Prérequis

- Python 3.6 ou supérieur
- PaddleOCR
- OpenCV
- Matplotlib

### Installation

1. **Python**: Assurez-vous que Python est installé sur votre système. Vous pouvez le télécharger sur [python.org](https://www.python.org/downloads/).

2. **Installer les dépendances**: Installez les paquets Python requis en utilisant `pip` :
   ```sh
   pip install -r requirements.txt

### Utilisation

1. **Préparez l'image** Assurez vous d'avoir une image dans le meme répertoire que votre script

2. **Exécuter le script** Le script exécutera l'OCR sur l'image et imprimera le texte détecté. De plus, il extraira les boîtes englobantes, le texte détecté et les scores de confiance.

3. **Résultat** Le script affichera le texte détecté dans la console. Si vous souhaitez visualiser les résultats, vous pouvez utiliser OpenCV et Matplotlib pour dessiner les boîtes englobantes et le texte détecté sur l'image.
