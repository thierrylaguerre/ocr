from paddleocr import PaddleOCR, draw_ocr
from matplotlib import pyplot as plt
import os
from PIL import Image, ImageDraw, ImageFont
import json

# Autoriser les doublons de la bibliothèque OpenMP
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

# Instanciation du modèle OCR
ocr_model = PaddleOCR(lang='en', use_angle_cls=True, use_gpu=True)

# Définition du chemin de l'image
img_path = os.path.join('.', 'Genova.png')

# Vérification si le fichier existe
if not os.path.exists(img_path):
    raise FileNotFoundError(f"Le fichier {img_path} n'a pas été trouvé.")

# Exécution de la méthode OCR sur le modèle OCR
result = ocr_model.ocr(img_path)

# Extraction des boîtes, textes et scores détectés
boxes = [line[0] for line in result[0]]
texts = [line[1][0] for line in result[0]]
scores = [line[1][1] for line in result[0]]

# Utilisation de la police Arial ou une autre police disponible sur votre système
font_path = "C:\\Windows\\Fonts\\arial.ttf"  

# Chargement de l'image
image = Image.open(img_path).convert('RGB')

# Création d'un objet de dessin pour l'image
draw = ImageDraw.Draw(image)
font = ImageFont.truetype(font_path, 16)

# Préparation des données pour le fichier JSON
ocr_results = []
for box, text, score in zip(boxes, texts, scores):
    box = [(int(point[0]), int(point[1])) for point in box]
    print(f"Box Coordinates: {box}") 
    draw.polygon(box, outline='red')
    text_annotation = f"{text} ({score:.2f})"
    draw.text((box[0][0], box[0][1] - 20), text_annotation, fill='White', font=font)
    
    # Ajouter les résultats OCR dans la liste
    ocr_results.append({
        "box": box,
        "text": text,
        "score": score
    })

# Affichage de l'image annotée
plt.figure(figsize=(10, 10))
plt.imshow(image)
plt.axis('off')
plt.show()

# Sauvegarde des résultats dans un fichier JSON
output_json_path = os.path.join('.', 'ocr_results.json')
with open(output_json_path, 'w', encoding='utf-8') as json_file:
    json.dump(ocr_results, json_file, ensure_ascii=False, indent=4)

# Affichage des textes avec leurs scores de confiance
for text, score in zip(texts, scores):
    print(f"Text: {text}, Confidence Score: {score:.2f}")

