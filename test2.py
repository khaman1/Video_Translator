from google_trans_new import google_translator
import cv2 
import pytesseract
from time import sleep


translator = google_translator()
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

cap = cv2.VideoCapture(r'input/video 1.mp4')

for i in range(0,25*3):
    ret, frame = cap.read()
        
img = frame[900:1100, 200:1700]
cv2.imshow('Video', img)
