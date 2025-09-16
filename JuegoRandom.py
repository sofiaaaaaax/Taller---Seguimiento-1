import tkinter as tk
from tkinter import messagebox
from tkinter import Menu
import random
 
RUTA_DEL_ICONO = "icono.ico"
 
# ----- juego -----
class AdivinaNumeroApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Adivina el Número")
        self.geometry("300x250")
       
        # Atributos de la clase
        self.secret_number = 0
        self.guesses = 0
        self.entry_guess = None
        self.feedback_label = None
 
        self.create_widgets()
        self.create_menu()
        self.start_new_game()
 
    def create_widgets(self):
        """Crea y organiza los elementos visuales de la interfaz."""
        main_frame = tk.Frame(self, padx=10, pady=10)
        main_frame.pack(expand=True, fill="both")
 
        tk.Label(main_frame, text="ingresa un número entre 1 y 100:", font=("Arial", 10)).pack(pady=10)
       
        self.entry_guess = tk.Entry(main_frame)
        self.entry_guess.pack()
       
        tk.Button(main_frame, text="Verificar", command=self.check_guess).pack(pady=5)
       
        tk.Button(main_frame, text="Reiniciar Juego", command=self.start_new_game).pack(pady=5)
 
        self.feedback_label = tk.Label(main_frame, text="", font=("Arial", 12, "bold"))
        self.feedback_label.pack(pady=10)
 
    def create_menu(self):
        """Crea la barra de menú con sus opciones."""
        menubar = Menu(self)
        self.config(menu=menubar)
 
        # Menú Juego
        menu_game = Menu(menubar, tearoff=0)
        menu_game.add_command(label="Reiniciar", command=self.start_new_game)
        menu_game.add_command(label="Salir", command=self.quit)
        menubar.add_cascade(label="Juego", menu=menu_game)
 
        # Menú Ayuda
        menu_ayuda = Menu(menubar, tearoff=0)
        menu_ayuda.add_command(label="Mostrar ayuda", command=self.mostrar_ayuda)
        menu_ayuda.add_command(label="Acerca de", command=self.mostrar_acerca_de)
        menubar.add_cascade(label="Ayuda", menu=menu_ayuda)
   
    def start_new_game(self):
        """Genera un nuevo número aleatorio y reinicia el juego."""
        self.secret_number = random.randint(1, 100)
        self.guesses = 0
        self.feedback_label.config(text="")
        self.entry_guess.delete(0, tk.END)
        self.entry_guess.config(state=tk.NORMAL)
        print(f"DEBUG: El número secreto es {self.secret_number}") # Para pruebas
 
    def check_guess(self):
        """Verifica la suposición del usuario y da retroalimentación."""
        try:
            user_guess = int(self.entry_guess.get())
            self.guesses += 1
           
            if user_guess < 1 or user_guess > 100:
                self.feedback_label.config(text="No esta dentro del 1 al 100. Intenta poniendo un numero entre estos dos valores.", fg="red")
            elif user_guess < self.secret_number:
                self.feedback_label.config(text="Demasiado bajo. Intenta de nuevo.", fg="purple")
            elif user_guess > self.secret_number:
                self.feedback_label.config(text="Demasiado alto. Intenta de nuevo.", fg="pink")
            else:
                self.feedback_label.config(text=f"¡Correcto! Lo adivinaste en {self.guesses} intentos.", fg="red")
                self.entry_guess.config(state=tk.DISABLED) # Deshabilita la entrada
                messagebox.showinfo("¡Ganaste!", f"¡Felicidades! Lo adivinaste en {self.guesses} intentos.")
 
            self.entry_guess.delete(0, tk.END) # Limpia la entrada
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa un número válido.")
            self.entry_guess.delete(0, tk.END)
 
    # Funciones de ayuda e información
    def mostrar_ayuda(self):
        messagebox.showinfo("Ayuda", "Ingresa un número y el programa te dirá si es el número secreto.")
 
    def mostrar_acerca_de(self):
        messagebox.showinfo("Acerca de", "Juego Adivina el Número\nCreador sofia lopez holguin >_<\n2025")
 
# ----- Iniciar la aplicación -----
if __name__ == "__main__":
    app = AdivinaNumeroApp()
    app.mainloop()