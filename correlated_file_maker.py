from random import randint , getrandbits
import codecs

vocales = "aeiou"#AEIOUÀÁÉÈÍÌÒÓÚÙ
consonantes = "bcdfghjklmnpqrstvwxyz" #$€Ç
vocales_map = {
    "a" : ["A"],#,str(0xC1),str(0xC0)],
    "e" : ["E"],#,str(0xC8),str(0xC9)],
    "i" : ["I"],#,str(0xCC),str(0xCD)],
    "o" : ["O"],#,str(0xD3),str(0xD2)],
    "u" : ["U"]#,str(0xDA),str(0xD9)]
}

def render_matrix(matrix):
    string = ""
    for lista in matrix:
        string += '\n'
        for palabras in lista:
            string += palabras + " "
    return string

def gen_sufix(bananas,word):
    if bananas > 1:
        suffixed = word
        for i in range(0,bananas):
            suffixed = get_randomSilaba(suffixed)
        return suffixed
    else:
        return get_randomWord()

def get_randomWord():
    formacion = ""
    for silabas in range(0,randint(1,4)): 
        formacion = get_randomSilaba(formacion)
    return formacion
    
def randomize_vocals(word):
    result_word = ""
    for letter in word:
        choose = randint(0,1)
        
        if letter in vocales_map:
            if choose == 0:
                result_word += letter
            else:
                result_word += vocales_map[letter][choose-1]
        else:
            result_word += letter
    return result_word


def get_randomSilaba(composition):
    silabaSimple = getrandbits(1)
    index = randint(0,len(consonantes)-1)
    index2 = randint(0,len(vocales)-1)
    composition += consonantes[index] + vocales[index2]
    if not bool(silabaSimple):
        index = randint(0,len(consonantes)-1)
        composition += consonantes[index]
    return composition

def genApostrofes(lines):
    matriz = []
    for lineas in range(0, lines):
        lista = []
        for palabras in range(0,randint(1,5)): 
            lista.append(get_randomWord())
        matriz.append(lista)
    return matriz

def addsuffix(matrix):
    matrix2 = []
    count = 0
    for lista in matrix:
        list2 = []
        flag_count = False
        for word in lista:
            bananas = randint(0,1)
            if bananas == 0:
                bananas = randint(1,3)

            choosed_word = lista[randint(0,len(lista)-1)]
            new_word = gen_sufix( bananas, choosed_word )
            if choosed_word in new_word:
                new_word = randomize_vocals(new_word)
                flag_count = True
            list2.append( new_word )
        matrix2.append(list2)
        if flag_count:
            count+=1 

    print(str(count)+" Total lines with match")
    return matrix2, count

def main():
    print("Culion")
    total_lines = 512
    matrix= genApostrofes(total_lines)
    listaA = render_matrix(matrix)
    #listaB = getrand(total_lines, "Lista B")
    with open("lista_correlated.txt","wb") as file:
        file_meta = codecs.open("lista_meta.txt","w","utf-8-sig")
        file.write("Lista A".encode('ascii'))
        file.write((listaA + "\n").encode('ascii'))
        matrix2, count = addsuffix(matrix)
        listaB = render_matrix(matrix2)
        file_meta.write(str(count)+" Total lines with match")
        file.write("Lista B".encode('ascii'))
        file.write(listaB.encode('ascii'))

if __name__ == "__main__":
    main()