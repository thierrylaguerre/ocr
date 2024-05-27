from paddleocr import PaddleOCR, draw_ocr
from matplotlib import pyplot as plt
import cv2
import os
import json

# Instanciation du modèle
ocr_model = PaddleOCR(lang='en', use_angle_cls=True, use_gpu=True)

# Définition du chemin de l'image
img_path = os.path.join('.', 'Genova.png')

# Vérification si le fichier existe
if not os.path.exists(img_path):
    raise FileNotFoundError(f"Le fichier {img_path} n'a pas été trouvé.")

# Exécution de la méthode OCR sur l'image
result = ocr_model.ocr(img_path)

# Traitement du tuple et des listes de listes
inner_result = result[0]

# Extraction des composants détectés
output = []
for res in inner_result:
    data = {
        'box': res[0],
        'text': res[1][0],
        'score': res[1][1]
    }
    output.append(data)

# Chemin du fichier de sortie JSON
output_path = os.path.join('.', 'ocr_results.json')

# Sauvegarde des résultats au format JSON
with open(output_path, 'w', encoding='utf-8') as json_file:
    json.dump(output, json_file, ensure_ascii=False, indent=4)

print(f"Les résultats OCR ont été sauvegardés dans {output_path}")

