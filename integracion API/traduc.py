from api import take_info
from googletrans import Translator

translator = Translator()
def traduc_info():
    texto = take_info()
    traduccion = translator.translate(texto, src="en", dest = "es")
    return traduccion.text
