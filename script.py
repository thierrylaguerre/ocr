from paddleocr import PaddleOCR, draw_ocr
from matplotlib import pyplot as plt
import os
from PIL import Image, ImageDraw, ImageFont

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
scores = [line[1][1] for line in result[0]]  # Correction ici pour obtenir les scores en float

# Utilisation de la police Arial ou une autre police disponible sur votre système
font_path = "C:\\Windows\\Fonts\\arial.ttf"  # Changez ce chemin si nécessaire

# Chargement de l'image
image = Image.open(img_path).convert('RGB')

# Création d'un objet de dessin pour l'image
draw = ImageDraw.Draw(image)
font = ImageFont.truetype(font_path, 16)

# Annotation de l'image avec les boîtes, textes et scores
for box, text, score in zip(boxes, texts, scores):
    # S'assurer que les coordonnées sont sous forme de tuples
    box = [(int(point[0]), int(point[1])) for point in box]
    print(f"Box Coordinates: {box}")  # Pour déboguer
    draw.polygon(box, outline='red')
    text_annotation = f"{text} ({score:.2f})"
    draw.text((box[0][0], box[0][1] - 20), text_annotation, fill='white', font=font)

# Affichage de l'image annotée
plt.figure(figsize=(12, 12))
plt.imshow(image)
plt.axis('off')
plt.show()

# Affichage des textes avec leurs scores de confiance
for text, score in zip(texts, scores):
    print(f"Text: {text}, score de confiance: {score:.2f}")
