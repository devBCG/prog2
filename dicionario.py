def concatena(d1, d2, d3):
     dic = {}
     list = []

     for i in d1:
        print(i)
    
    


def filtra(dic):
    dicio2 = {}
    for i in dic:
        if dic[i] > 170:
            dicio2[i] = dic[i] 
    return dicio2
def remove_none(d):
    dic2 = {}
    for i in d:
        if d[i] != None:
            dic2[i] = d[i] 
    return dic2

def cria_dicionario():
    dic = dict(ramon=20, alvaro=20, jhone=None, Hilal= 175, Carvalho = 180, Eleonora = 165, Cunha = 190)
    return dic


def main():
    
    a = ['S001', 'S002', 'S003', 'S004']
    b = ['Pedra da Cebola', 'Praça do Papa', 'Costa Pereira', 'Reserva Paulo Vinhas']
    c = [85, 98, 89, 92]
    

    tela = concatena(a,b,c)
    print(tela)

    # d={}
    # d=cria_dicionario()
    # print(d)

    # j = remove_none(d)
    # print(j)

    # h = filtra(j)
    # print(h)
    #--------------------------
    
    # dicio1 = dict(zip(d2, d3))
    # final_dictionare = dict(zip(d1, dicio1))
    # return final_dictionare
    
main()