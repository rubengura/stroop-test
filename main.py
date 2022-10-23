import tkinter as tk
from random import choice

COLORS = ["Amarillo", "Azul", "Rojo", "Verde"]
WORD_COLORS = ["yellow", "blue", "red", "green"]

COLOR_DICT = {"Amarillo": "yellow",
              "Azul": "blue",
              "Rojo": "red",
              "Verde": "green"}

STROOP_BG = "black"

# Create Object (GUI)
window = tk.Tk()

# Insert the title 
window.title("Bienvenida al Test")

# Set window dimensions
window.geometry("800x200")


def choose_fg_color(color):
    word_color = choice(WORD_COLORS)

    while COLOR_DICT[color] == word_color:
        word_color = choice(WORD_COLORS)
    
    return word_color


# Open New Window
def launch_test():
    global second
    second = tk.Toplevel()
    second.configure(background=STROOP_BG)
    second.title("Test de Stroop")
    second.geometry("1800x900")

    color = choice(COLORS)
    fg_color = choose_fg_color(color)

    tk.Label(second, text=color, fg=fg_color, bg=STROOP_BG, font="14").pack()
    tk.Button(second, text="Amarillo").pack(side="left", padx=(350,0), pady=(450,0))
    tk.Button(second, text="Azul").pack(side="left", padx=(200,0), pady=(450,0))
    tk.Button(second, text="Verde").pack(side="left", padx=(200,0), pady=(450,0))
    tk.Button(second, text="Rojo").pack(side="left", padx=(200,0), pady=(450,0))



# Show the window
def show():
    second.deiconify()

# Hide the window
def hide():
    second.withdraw()

# Adding some text to the window
tk.Label(window, text="Bienvenido al Test de Stroop", font='Helvetica 18 bold').pack()
tk.Label(window, text= """A continuación verás un conjunto de palabras escritas en un determinado color.\n 
                          El objetivo es identificar el color en que están escritas las palabras lo más rápido posible.\n
                          Para ello, selecciona la tecla adecuada (Flecha izda: Verde, Flecha dcha: Azul, Flecha sup: Rojo, Flecha inf: Amarillo)\n
                          Selecciona el botón "Empezar test" cuando estés preparado.""").pack()

# Add Buttons
tk.Button(window, text="Empezar test", command=launch_test).pack(pady=10)
# tk.Button(window, text="Show", command=show).pack(pady=10)
# tk.Button(window, text="Hide", command=hide).pack(pady=10)

# Execute Tkinter
window.mainloop()




