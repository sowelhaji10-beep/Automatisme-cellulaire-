# Adji Faty DIENG 
# Elhadji SOW 


import random


def create_grid_lc(lin, col, val):
    """Retourne une grille de 'lin' lignes et 'col' colonnes
    initialisées à 'val'"""
    return [[val for _ in range(col)] for _ in range(lin)]


def create_random_grid_lc(lin, col, vals):
    """Retourne une grille de 'lin' lignes et 'col' colonnes
    initialisés aléatoirement avec des valeurs de la liste 'vals'"""
    return [[random.choice(vals) for _ in range(col)] for _ in range(lin)]


def nb_lines(grid):
    """Retourne le nombre de lignes de la grille 'grid'"""
    return len(grid)


def nb_columns(grid):
    """Retourne le nombre de colonnes de la grille 'grid'"""
    if len(grid) == 0:
        return 0
    return len(grid[0])


def line2str(grid, num_line, sep='\t'):
    """Retourne la chaine de caractère correspondant à la concaténation des valeurs
    de la ligne numéro 'num_line' de la grille 'grid'. Les caractères sont séparés par le caractère 'sep'"""
    res = ""
    for i in grid[num_line]:
        res = res + str(i) + sep
    return res


def grid2str(grid, sep='\t'):
    """Retourne la chaine de caractère représentant la grille 'grid'.
    Les caractères de chaque ligne de 'grid' sont séparés par le caractère 'sep'.
    Les lignes sont séparées par le caractère de retour à la ligne \n"""
    res = ""
    for i in range(nb_lines(grid)):
        res = res + line2str(grid, i, sep) + '\n'
    return res


def neighbour(grid, lin, col, delta, tore=True):
    """Retourne le voisin de la cellule 'grid[lin][col]' selon le tuple 'delta' = (delta_lin, delta_col).
    Si 'tore' est à 'True' le voisin existe toujours en considérant 'grid' comme un tore.
    Si 'tore' est à 'False' retourne 'None' lorsque le voisin est hors de la grille 'grid'."""
    l = lin + delta[0]
    c = col + delta[1]
    if tore:
        return grid[l % nb_lines(grid)][c % nb_columns(grid)]
    if 0 <= l < nb_lines(grid) and 0 <= c < nb_columns(grid):
        return grid[l][c]
    return None


def neighborhood(grid, lin, col, deltas, tore=True):
    """Retourne pour la grille 'grid' la liste des N voisins de 'grid[lin][col]'
    correspondant aux N (delta_lin, delta_col) fournis par la liste 'deltas'.
    Si 'tore' est à 'True' le voisin existe toujours en considérant 'grid' comme un tore.
    Si 'tore' est à 'False' un voisin hors de la grille 'grid' n'est pas considéré."""
    return [neighbour(grid, lin, col, delta, tore) for delta in deltas if neighbour(grid, lin, col, delta, tore) != None]


if __name__ == "__main__":
    """Définitions des variables de test et des tests de chaque fonction"""
    # Tuple des déplacements (delta_lig, delta_col) pour repérer une cellule voisine dans une grille de Conway.
    # Les 8 directions possibles dans l'ordre sont : NO, N, NE, O, E, SO, S, SE.
    DELTAS_CONWAY = ((-1, -1), (-1, 0), (-1, 1), (0, -1),
                     (0, 1), (1, -1), (1, 0), (1, 1))

    print(create_grid_lc(3, 3, 1))
    # print(create_random_grid_lc(4,3,[0,1]))
    grid = create_random_grid_lc(4, 3, range(10))
    # print(nb_lines(grid))
    # print(nb_columns(grid))
    # print(line2str(grid, 2))
    print(grid2str(grid))
    # print(neighbour(grid, 3, 2, (1, 0)))
    print(neighborhood(grid, 0, 0, DELTAS_CONWAY, False))
