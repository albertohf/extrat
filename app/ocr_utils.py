from PIL import Image
import pytesseract
import numpy as np
import cv2
import io

# Caminho para o executável do Tesseract (ajuste para seu sistema)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def preprocess_image(image_bytes: bytes) -> Image.Image:
    # Abrir imagem
    pil_image = Image.open(io.BytesIO(image_bytes))
    cv_image = np.array(pil_image.convert("RGB"))

    # Cinza
    gray = cv2.cvtColor(cv_image, cv2.COLOR_RGB2GRAY)

    # Aumentar contraste e brilho
    contrast = cv2.convertScaleAbs(gray, alpha=1.5, beta=20)  # alpha: contraste, beta: brilho

    # Remover ruído com desfoque leve
    blurred = cv2.GaussianBlur(contrast, (3, 3), 0)

    # Binarização adaptativa
    thresh = cv2.adaptiveThreshold(
        blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2
    )

    # Sharpen (realce dos contornos)
    # kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 1))
    sharpened = cv2.filter2D(thresh, -1, kernel)

    # Redimensionar para facilitar OCR
    resized = cv2.resize(sharpened, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)

    return Image.fromarray(resized)

def extract_text_from_image(image_bytes: bytes, lang: str = "eng+por") -> str:
    # Pré-processar imagem
    processed_image = preprocess_image(image_bytes)
    custom_config = r'--oem 3 --psm 6'
    # Executar OCR com idioma (ex: "por" para português)
    text = pytesseract.image_to_string(processed_image, lang=lang, config=custom_config)
    return text
