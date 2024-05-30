from paddleocr import PaddleOCR, draw_ocr
from matplotlib import pyplot as plt
import os
from PIL import Image

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

# Dessin des résultats OCR sur l'image
im_show = draw_ocr(image, boxes, texts, scores, font_path=font_path)

# Conversion de l'image pour l'affichage avec matplotlib
im_show = Image.fromarray(im_show)

# Affichage de l'image annotée
plt.figure(figsize=(10, 10))
plt.imshow(im_show)
plt.axis('off')
plt.show()
