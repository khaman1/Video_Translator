from google_trans_new import google_translator
import pytesseract
from .chinese import Chinese_Translator

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

class Image:
    def __init__(self, img=''):
        self.img = img

        self.translator = google_translator()
        

    def toString(self, lang_src='chi_sim', lang_dest='vi', custom_config=r'--oem 3 --psm 6'):
        text = pytesseract.image_to_string(self.img, config=custom_config, lang=lang_src).strip()
        return self.translator.translate(text, lang_tgt=lang_dest), text


    def toChinese_version2(self, lang_src='chi_sim', lang_dest='vi', custom_config=r'--oem 3 --psm 6'):
        text = pytesseract.image_to_string(self.img, config=custom_config, lang=lang_src).strip()
        
        #try:
        Englishtext = Chinese_Translator().translate(text=text), text
        #print('Englishtext: ' + Englishtext)
        
        result = self.translator.translate(Englishtext, lang_tgt=lang_dest)
        #print(result)
        #result = result.split('"')[0]#.split("'")[0].strip()#.replace("'","").replace('(','')

        print(result)
        
        
        return result, text
        #except:
        #    print("ERROR")
        #    return '',''
