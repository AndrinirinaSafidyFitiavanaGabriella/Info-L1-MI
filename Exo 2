def karnaugh_minimization():
    # Création de la table de Karnaugh
    k_map = [[0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]]

    # Remplissage de la table avec les valeurs de la fonction
    k_map[0][1] = 1  # ab
    k_map[1][2] = 1  # !bc
    k_map[2][0] = 1  # a!c

    # Affichage de la table de Karnaugh
    print("Table de Karnaugh:")
    for row in k_map:
        print(row)

    # Identification des groupes et termes communs
    groups = []
    for i in range(3):
        for j in range(4):
            if k_map[i][j] == 1:
                group = [(i, j)]
                k_map[i][j] = 0  # Marquer la case comme visitée
                # Regroupement des cases adjacentes
                if j < 3 and k_map[i][j+1] == 1:
                    group.append((i, j+1))
                    k_map[i][j+1] = 0
                if i < 2 and k_map[i+1][j] == 1:
                    group.append((i+1, j))
                    k_map[i+1][j] = 0
                groups.append(group)

    # Construction de l'expression minimisée
    minimized_expr = ""
    for group in groups:
        terms = []
        for cell in group:
            a = 'a' if cell[0] == 0 else '!a'
            b = 'b' if cell[1] == 0 or cell[1] == 1 else '!b'
            c = 'c' if cell[1] == 0 or cell[1] == 2 else '!c'
            terms.append(a + b + c)
        minimized_expr += "(" + " + ".join(terms) + ")"

    print("Expression minimisée:", minimized_expr)


# Appel de la fonction pour minimiser l'expression
karnaugh_minimization()
