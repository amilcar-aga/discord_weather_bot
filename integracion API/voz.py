import pyttsx3



def sintesis_voz(texto):

    engine = pyttsx3.init()

    #configuraciones iniciales 
    engine.setProperty("rate",150)
    engine.setProperty("volume", 1.0)

    voces = engine.getProperty("voices")

    engine.setProperty("voice", voces[3].id)


    #hablar del texto
    engine.say(texto)
    engine.runAndWait()