import cv2
import pytesseract

# Defina o caminho do executável do Tesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

imagem1 = cv2.imread('imagem1.jpg')
imagem2 = cv2.imread('imagem2.jpg')

resultado1 = pytesseract.image_to_string(imagem1)
resultado2 = pytesseract.image_to_string(imagem2)

print(f'O texto na imagem 1: {resultado1}')
print(f'O texto na imagem 2: {resultado2}')