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
    res = ["_" for i in range(1, longitud)]
    a = 0
    while a != 1:
        os.system("cls")
        print("""SELECCIONE UNA LETRA: \n""",res)
        
        letra_ingresada = input("Ingrese una letra:")
        for index, value in enumerate(word):
            if letra_ingresada == value:
                res[index]=letra_ingresada
            else:
                res[index]="_"

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