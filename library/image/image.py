from google_trans_new import google_translator
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

class Image:
    def __init__(self, img=''):
        self.img = img

        self.translator = google_translator()
        

    def toString(self, lang_src='chi_sim', lang_dest='vi', custom_config=r'--oem 3 --psm 6'):
        text = pytesseract.image_to_string(self.img, config=custom_config, lang=lang_src).strip()
        return self.translator.translate(text, lang_tgt=lang_dest), text

    
