# Projet OCR

Ce projet utilise le modèle OCR de PaddleOCR pour détecter et reconnaître du texte dans une image.

## Installation

1. Assurez-vous d'avoir Python 3.11 installé sur votre système 

2. Installez les dépendances requises en exécutant les lignes de commande suivantes :
      python -m pip install paddlepaddle-gpu==2.6.1 -i https://mirror.baidu.com/pypi/simple
      python -m pip install paddlepaddle -i https://pypi.tuna.tsinghua.edu.cn/simple
      pip install -r requirements.txt 

## Utilisation

1. Placez votre image dans le dossier contenant script.py.
2. Exécutez le script `script.py` pour détecter et reconnaître le texte dans l'image.
3. Les résultats seront affichés dans la console et enregistrés dans un fichier JSON.

## Auteur

Ce projet a été développé par [Thierry LAGUERRE] <thierrylaguerre81@gmail.com>.
