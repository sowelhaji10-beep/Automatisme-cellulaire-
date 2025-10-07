# Adji Faty DIENG 
# Elhadji SOW 

import random
from grid_manager import *



def create_langton_grid(rows, cols):
    """Retourne une grille de 'rows' lignes et 'cols' colonnes
    initialisée à 0 avec une fourmi de Langton placée au centre."""
    grid = create_grid_lc(rows, cols, 0)
    ant_pos = (rows // 2, cols // 2)
    grid[ant_pos[0]][ant_pos[1]] = 1  # Marquer la position initiale de la fourmi
    return grid, ant_pos, 'N'  # La direction initiale est vers le Nord

def tourne_G(direction):
    """Tourne la direction vers la gauche."""
    if direction == 'N':
        return 'W'
    elif direction == 'W':
        return 'S'
    elif direction == 'S':
        return 'E'
    elif direction == 'E':
        return 'N'

def tourne_D(direction):
    """Tourne la direction vers la droite."""
    if direction == 'N':
        return 'E'
    elif direction == 'E':
        return 'S'
    elif direction == 'S':
        return 'W'
    elif direction == 'W':
        return 'N'

def deplacer(position, direction):
    """Déplace la fourmi d'une case dans la direction donnée."""
    row, col = position
    if direction == 'N':
        return row - 1, col
    elif direction == 'E':
        return row, col + 1
    elif direction == 'S':
        return row + 1, col
    elif direction == 'W':
        return row, col - 1

def langton_etape(grid, ant_pos, ant_dir):
    """Effectue une étape du jeu de Langton."""
    current_cell = grid[ant_pos[0]][ant_pos[1]]

    # Inverser la couleur de la cellule actuelle
    grid[ant_pos[0]][ant_pos[1]] = 1 - current_cell

    # Tourner la fourmi
    if current_cell == 0:  # Cellule blanche
        ant_dir = tourne_D(ant_dir)
    else:  # Cellule noire
        ant_dir = tourne_D(ant_dir)

    # Déplacer la fourmi
    ant_pos = deplacer(ant_pos, ant_dir)

    return grid, ant_pos, ant_dir

if __name__ == "__main__":
    # Définitions des variables de test
    rows, cols = 5, 5
    langton_grid, ant_pos, ant_dir = create_langton_grid(rows, cols)

    # Afficher l'état initial
    print(grid2str(langton_grid))

    # Effectuer quelques étapes du jeu de Langton
    for _ in range(10):
        langton_grid, ant_pos, ant_direction = langton_etape(langton_grid, ant_pos, ant_dir)
        print(grid2str(langton_grid))
