from itertools import product

def table_de_verite():
    n = 3
    X1 = "A"
    X2 = "B"
    X3 = "C"
    X4 = "!B"
    X5 = "!C"
    X6 = "AB"
    X7 = "!BC"
    X8 = "A!C"
    X9 = "AB + !BC + A!C"
    results_list, results_list_two = [], []
    variables = [X1,X2,X3,X4,X5,X6,X7,X8]
    #print("Variables:", variables)
    print("Table de Vérité: f(A,B,C) = AB + !BC + A!C")
    print("+" + "-"*(16*n) + "+-------+")
    print("| " + " | ".join(variables) + f" | | {X9}|")
    print("+" + "-"*(16*n) + "+-------+")

    for values in product([0, 1], repeat=n):
        outputnB = nB(values)
        outputnC = nC(values)
        outputAB = AB(values)
        outputnBC = nBC(values)
        outputAnC = AnC(values)
        outputFinal = res(values)
        if outputFinal == 1 :
            form1 = canonical_first_forms(values)
            results_list.append(form1)
        concatened_result = " + ".join(results_list)

        if outputFinal == 0 :
            form2 = canonical_second_forms(values)
            results_list_two.append(form2)
        concatened_result_two = " ". join(results_list_two) 
        
        print("| " + " | ".join(str(v) for v in values) + f" | {outputnB}  |" + f"  {outputnC} |" + f"  {outputAB}" + f" |  {outputnBC}  |"+f"  {outputAnC}  |" + " | "+ " "*(4)+  f"  {outputFinal}  "+ " "*(5) +"|")

    print("+" + "-"*(16*n) + "+-------+")


    print("Première forme canonique : ", concatened_result)
    print("Deuxième forme canonique : ", concatened_result_two)
 
#Fonction qui retourne les valeurs de !B 
def nB(input_values):
    for v in input_values[1:2]:
        if v == 0 :
            return 1
        else :
            return 0

#Fonction qui donne les valeurs de AB
def AB(input_values):
    x = 0
    for v in input_values[:2]:
        if v == 1 :
            x += 1
        else :
            continue
    if x > 1 :
        return 1
    else : 
        return 0
    
#Foncion qui retourne les valeurs de !BC
def nBC(input_values):
    x = 0
    nb = nB(input_values)
    for v in input_values[2:3]:
        if (v == 1) & (nb == 1) :
            return 1
        else :
            return 0

#Fonction qui retourne les valeurs de !C
def nC(input_values):
    for v in input_values[2:3]:
        if v == 0 :
            return 1
        else :
            return 0

#Fonction qui retourne les valeurs de A!C      
def AnC(input_values):
    x = 0
    nc = nC(input_values)
    for v in input_values[0:1]:
        if (v == 1) & (nc == 1) :
            return 1
        else :
            return 0

#Fonction qui retourne les valeurs en sortie (AB + !BC + A!C )
def res(input_values):
    x = 0
    anc = AnC(input_values)
    ab = AB(input_values)
    nbc = nBC(input_values)
    for v in input_values:
        if (ab == 1) | (anc == 1) | (nbc == 1) :
            return 1
        else :
            return 0

def canonical_first_forms(input_values):
    a, b, c = "", "", ""
    resultat, resultatfinal = "", ""
    x = 0

    for v in input_values:
        if x == 0 :  
            a = "(A" if (v == 1)  else "(!A"
            x += 1
        elif x == 1 :
            b = "B" if (v == 1) else "!B"
            x += 1
        elif x == 2 :
            c = "C) " if (v == 1) else "!C)"
        #resultat = [a, b, c]
    resultat += a + " " + b + " " + c
    return resultat
    #return form1, form2

def canonical_second_forms(input_values):
    a, b, c = "", "", ""
    resultat, resultatfinal = "", ""
    x = 0

    for v in input_values:
        if x == 0 :  
            a = "(A" if (v == 0)  else "(!A"
            x += 1
        elif x == 1 :
            b = "B" if (v == 0) else "!B"
            x += 1
        elif x == 2 :
            c = "C) " if (v == 0) else "!C)"

    resultat += a  + " + " + b + " + " + c
    return resultat

    

def main():
    table_de_verite()

if __name__ == "__main__":
    main()
