import time
import os
import random
# random.randint(0, 1)
def read():
    number = []
    with open("./archivos/Words.txt","r",encoding="utf-8") as f:
        for line in f:
            number.append(line)
    word = random.choice(number)
    

    return word

def hangman(word):
    longitud = int(len(word))
    res = "_" * longitud
    
    a = 0
    b = ""
    letra_ingresada=''
    while a != 1:
        




        
        os.system("cls")

        print("""SELECCIONE UNA LETRA: \n""",res,b,letra_ingresada,word)
        letra_ingresada = input("Ingrese una letra:")
        letra_ingresada = letra_ingresada.strip()
        print(letra_ingresada,)
        for index, value in enumerate(word):
        # res = [list(map(lambda letter: letter == letra_ingresada, res))]
        # [worker["name"] for worker in DATA if worker ["organization"] == "Platzi"]
            if letra_ingresada == value:
                rplc = word[index]
                res = res. replace(rplc,letra_ingresada)
                b = ":)"
            else:
                b = ":("
        

def run():
    os.system("cls")
    ramdom_word = read() # Read random word
    new_word = ramdom_word.maketrans('áéíóú', 'aeiou')
    word = ramdom_word.translate(new_word)
    hangman(word)
    print(word)
    # hangman(ramdom_word)

if __name__ == '__main__':
    run()