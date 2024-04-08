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
    variables = [X1,X2,X3,X4,X5,X6,X7,X8]
    print("Variables:", variables)
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
        print("| " + " | ".join(str(v) for v in values) + f" | {outputnB}  |" + f"  {outputnC} |" + f"  {outputAB}" + f" |  {outputnBC}  |"+f"  {outputAnC}  |" + " | "+ " "*(4)+  f"  {outputFinal}  "+ " "*(5) +"|")

    print("+" + "-"*(16*n) + "+-------+")
 
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

def canonical_forms():
    # Identifie les termes de la fonction logique
    terms = ["Ab", "!BC", "A!C"]
    
    # Première forme canonique (FCD)
    form1 = " OR ".join(f"({term})" for term in terms)
    
    # Deuxième forme canonique (FCC)
    form2 = " AND ".join(f"(NOT ({term}))" for term in terms)
    
    return form1, form2
    

def main():
    table_de_verite()
    form1, form2 = canonical_forms()
    print("Première forme canonique:", form1)
    print("Deuxième forme canonique:", form2)

if __name__ == "__main__":
    main()
