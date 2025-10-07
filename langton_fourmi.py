# Adji Faty DIENG 
# Elhadji SOW 




from tkinter import *
from fichier1 import*
from grid_tk import*
import time
COLORS ={'bg':'white','fg':'red','outline':'black','text_val':'black','ant':'blue'}
FONT ={'text_val':'Arial'}

def langton_ant_step_gui(can, ant_pos, ant_dir):
    current_cell = int(get_cell_text(can, ant_pos[0], ant_pos[1]))

    set_cell(can, get_grid(can), ant_pos[0], ant_pos[1], 1 - current_cell, COLORS['ant'], show_vals=True, outline=True)

    if current_cell == 0:
        ant_dir = tourne_D(ant_dir)
    else:
        ant_dir = tourne_G(ant_dir)

    # Déplacer la fourmi uniquement si la cellule actuelle est 1
    if current_cell == 1:
        ant_pos = deplacer(ant_pos, ant_dir)

    return ant_pos, ant_dir
def langton_ant_step(grid, ant_pos, ant_dir):
    current_cell = grid[ant_pos[0]][ant_pos[1]]

    # Inversion de la couleur de la cellule actuelle
    grid[ant_pos[0]][ant_pos[1]] = 1 - current_cell

    # Tourner la fourmi à gauche si la cellule actuelle est blanche (0), sinon à droite
    ant_dir = tourne_G(ant_dir) if current_cell == 0 else tourne_D(ant_dir)

    # Déplacer la fourmi
    ant_pos = deplacer(ant_pos, ant_dir)

    return ant_pos, ant_dir

def draw_langton_ant(canvas, grid, ant_pos, size_cell, margin=10, gutter=5):
    canvas.delete("all")

    # Dessiner la grille
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            y = i * size_cell + margin + i * gutter
            x = j * size_cell + margin + j * gutter
            color = COLORS['bg'] if grid[i][j] == 0 else COLORS['fg']
            canvas.create_rectangle(x, y, x + size_cell, y + size_cell, fill=color, outline=COLORS['outline'])

    # Dessiner la fourmi
    ant_x, ant_y = ant_pos
    ant_x = ant_x * size_cell + margin + ant_x * gutter + size_cell // 2
    ant_y = ant_y * size_cell + margin + ant_y * gutter + size_cell // 2
    canvas.create_oval(ant_x - size_cell // 4, ant_y - size_cell // 4, ant_x + size_cell // 4, ant_y + size_cell // 4, fill=COLORS['fg'])

if __name__ == "__main__":
    fen = Tk()
    size_cell = 20
    rows, columns = 20, 30
    grid = create_grid_lc(rows, columns, 0)
    ant_pos = (rows // 2, columns // 2)  # Position initiale de la fourmi
    ant_dir = 'N'  # Direction initiale de la fourmi

    canvas = Canvas(fen, bg=COLORS['bg'], width=columns * size_cell + 2 * 10 + (columns - 1) * 5,
                    height=rows * size_cell + 2 * 10 + (rows - 1) * 5)
    canvas.pack()

    while True:
        time.sleep(0.5)
        ant_pos, ant_dir = langton_ant_step(grid, ant_pos, ant_dir)
        draw_langton_ant(canvas, grid, ant_pos, size_cell)
        fen.update()

    fen.mainloop()
