import wikipedia
try:
    wikipedia.set_lang("es")
    result = wikipedia.summary("Apolo 11", sentences = "1")
    print(result)

except:
     print("error")

     #instalar con pip install wikipedia