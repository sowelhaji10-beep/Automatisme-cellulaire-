# Adji Faty DIENG 
# Elhadji SOW 


from tkinter import *
from grid_manager import *


# Dictionnaires des paramètres de forme d'une grille
COLORS = {'bg': 'white', 'fg': 'red', 'outline': 'black', 'text_val': 'black'}
FONT = {'text_val': 'Arial'}


def grid_canvas(master, grid, size_cell, margin=10, gutter=5, show_vals=True, outline=True):
    """Retourne un 'Canvas' placé dans la fenêtre 'master'. Celui-ci est construit à partir de la grille 'grid'
    en s'appuyant sur les modules 'grid_manager' et 'tkinter' ainsi que sur les dictionnaires des paramètres de forme.
    La largeur et la hauteur du Canvas sont calculés en considérant la taille 'size_cell' d'une cellule, la valeur de
    marge 'margin' autour de la grille et d'une taille de gouttière 'gutter' entre les lignes et les colonnes.
    Chaque cellule affichera en son centre le texte correspondant à son contenu si 'show_vals' est à la valeur 'True'.
    Les bordures des cellules ne s'afficheront que si 'outline' est à la valeur 'True'.
    Chaque cellule sera taguée par la chaine 'c_lin_col' et leur texte par la chaine 't_lin_col'.
    De plus, les deux seront taguées en plus par la chaine 'lin_col'."""
    hauteur = nb_lines(grid) * size_cell + 2*margin + \
        gutter * (nb_lines(grid)-1)
    largeur = nb_columns(grid) * size_cell + 2*margin + \
        gutter * (nb_columns(grid)-1)
    can = Canvas(master, bg=COLORS['bg'], width=largeur, height=hauteur)
    for i in range(nb_lines(grid)):
        for j in range(nb_columns(grid)):
            y = i * size_cell + margin + i * gutter
            x = j * size_cell + margin + j * gutter
            can.create_rectangle(x, y, x+size_cell,
                                 y+size_cell, tags=('c_'+str(i)+'_'+str(j), str(i)+'_'+str(j)))
            can.create_text((x+size_cell/2, y+size_cell/2), text=str(
                grid[i][j]), font=FONT['text_val'], fill=COLORS['text_val'], state=HIDDEN, tags=('t_'+str(i)+'_'+str(j), str(i)+'_'+str(j)))
            if show_vals:
                can.itemconfigure('t_'+str(i)+'_'+str(j), state=NORMAL)
            if outline:
                can.itemconfigure('c_'+str(i)+'_'+str(j),
                                  outline=COLORS['outline'])
    return can


def get_lines_columns(can):
    """Retourne le nombre de lignes et de colonnes de la grille représentée par le Canvas 'can'."""
    lin, col = can.gettags(can.find_all()[-1])[1].split('_')
    return (int(lin)+1, int(col)+1)


def get_grid(can):
    """Retourne la grille représentée par le Canvas 'can'."""
    list = [int(can.itemcget(k, "text")) for k in can.find_all() if k % 2 == 0]
    (lin, col) = get_lines_columns(can)
    return [[list[i*col+j] for j in range(col)] for i in range(lin)]


def get_color_cell(can, i, j):
    """Retourne la couleur de la cellule ('i', 'j') de la grille représentée par le Canvas 'can'."""
    return can.itemcget('c_'+str(i)+'_'+str(j), 'fill')


def set_color_cell(can, i, j, color, outline=True):
    """Rempli la cellule ('i', 'j') de la grille représentée par le Canvas 'can' par la couleur 'color'.
    Dessine ses bordures avec la couleur 'color' si 'outline' a la valeur 'False'."""
    can.itemconfigure('c_'+str(i)+'_'+str(j), fill=color)
    if not outline:
        can.itemconfigure('c_'+str(i)+'_'+str(j), outline=color)


def get_color_text(can, i, j):
    """Retourne la couleur du texte de la cellule ('i', 'j') de la grille représentée par le Canvas 'can'."""
    return can.itemcget('t_'+str(i)+'_'+str(j), 'fill')


def set_color_text(can, i, j, color):
    """Rempli le texte de la cellule ('i', 'j') de la grille représentée par le Canvas 'can' par la couleur 'color'."""
    can.itemconfigure('t_'+str(i)+'_'+str(j), fill=color)


def get_cell_text(can, i, j):
    item_id = can.find_withtag(f"cell_{i}_{j}")
    if item_id:
        text = can.itemcget(item_id, "text")
        return int(text) if text and text.isdigit() else 0  # Convertit en entier si le texte est un nombre, sinon retourne 0 par défaut
    else:
        return 0  # Si la cellule n'existe pas, retourne 0 par défaut



def set_cell_text(can, i, j, val):
    """Change la valeur du texte de la cellule ('i', 'j') du Canvas 'can' avec la valeur 'val'"""
    return can.itemconfigure('t_'+str(i)+'_'+str(j), text=val)


def set_cell(can, grid, i, j, val, color_cell, show_vals=True, outline=True, color_text=COLORS['text_val']):
    """Modifie la grille 'grid' et le Canvas 'can' en affectant la valeur 'val' à la cellule ('i', 'j').
    Change la couleur de fond par 'color_cell'.
    Change la couleur du texte par 'color_text' et la valeur par 'val' si 'show_vals' a la valeur 'True'.
    Dessine les bordures de la cellule selon la valeur booléenne de 'outline'."""
    grid[i][j] = val
    set_color_cell(can, i, j, color_cell, outline)
    if show_vals:
        set_color_text(can, i, j, color_text)
        set_cell_text(can, i, j, str(val))
        can.itemconfigure('t_'+str(i)+'_'+str(j), state=NORMAL)
    if outline:
        can.itemconfigure('c_'+str(i)+'_'+str(j), outline=COLORS['outline'])


if __name__ == "__main__":
    """Définitions des variables de test et des tests de chaque fonction"""
    fen = Tk()
    grid = create_random_grid_lc(4, 6, range(2))
    can = grid_canvas(fen, grid, 40)
    can.pack()
    print(get_lines_columns(can))
    print(grid)
    print(get_grid(can))
    # set_color_cell(can, 2, 2, 'blue', False)
    # print(get_color_cell(can, 2, 2))
    # set_color_text(can, 1, 1, 'blue')
    # print(get_color_text(can, 1, 1))
    # set_cell_text(can, 0, 0, '3')
    # print(get_cell_text(can, 0, 0))
    set_cell(can, grid, 2, 3, 5, 'green',
             outline=False)
    print(grid)
    fen.mainloop()
