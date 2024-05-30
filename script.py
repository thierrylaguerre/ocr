from paddleocr import PaddleOCR, draw_ocr
from matplotlib import pyplot as plt
import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

# Instanciation du modèle
ocr_model = PaddleOCR(lang='en', use_angle_cls=True, use_gpu=True)

# Définition du chemin de l'image
img_path = os.path.join('.', 'Genova.png')

# Vérification si le fichier existe
if not os.path.exists(img_path):
    raise FileNotFoundError(f"Le fichier {img_path} n'a pas été trouvé.")

# Exécution de la méthode OCR sur le modèle OCR
result = ocr_model.ocr(img_path)

#handling the Tuple and list of lists
inner_result = result[0]
inner_result
for res in inner_result:
    print(res[1][0])

# Extracting detected components
boxes = [res[0] for res in result] # 
texts = [res[1][0] for res in result]
scores = [res[1][1] for res in result]

font_path = os.path.join('PaddleOCR', 'doc', 'fonts', 'latin.ttf')