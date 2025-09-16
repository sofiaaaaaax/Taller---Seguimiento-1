import tkinter as tk
from tkinter import messagebox
from tkinter import Menu
 
class RecetasApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestor de Recetas")
        self.geometry("600x450")
 
        self.create_widgets()
        self.create_menu()
 
    def create_widgets(self):
        """Crea y organiza los elementos visuales de la interfaz."""
        main_frame = tk.Frame(self, padx=15, pady=15)
        main_frame.pack(fill=tk.BOTH, expand=True)
 
        # Sección para añadir recetas
        add_frame = tk.LabelFrame(main_frame, text="Añadir Nueva Receta", padx=10, pady=10)
        add_frame.pack(fill=tk.X, pady=(0, 20))
 
        tk.Label(add_frame, text="Nombre de la Receta:").pack(pady=(0, 5))
        self.entry_nombre = tk.Entry(add_frame, width=40)
        self.entry_nombre.pack()
 
        tk.Label(add_frame, text="Ingredientes:").pack(pady=(10, 5))
        self.entry_ingredientes = tk.Entry(add_frame, width=40)
        self.entry_ingredientes.pack()
       
        tk.Button(add_frame, text="Añadir Receta", command=self.add_receta).pack(pady=10)
 
        # Sección para visualizar y gestionar recetas
        view_frame = tk.LabelFrame(main_frame, text="Recetas Almacenadas", padx=10, pady=10)
        view_frame.pack(fill=tk.BOTH, expand=True)
 
        self.recetas_listbox = tk.Listbox(view_frame, width=50, height=10)
        self.recetas_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
       
        # Barra de desplazamiento para la lista
        scrollbar = tk.Scrollbar(view_frame, orient=tk.VERTICAL)
        scrollbar.config(command=self.recetas_listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.recetas_listbox.config(yscrollcommand=scrollbar.set)
       
        # Botón para eliminar
        tk.Button(main_frame, text="Eliminar Receta", command=self.delete_receta).pack(pady=10)
       
        self.recetas_listbox.bind('<<ListboxSelect>>', self.show_receta_details)
       
    def create_menu(self):
        """Crea la barra de menú con sus opciones."""
        menubar = Menu(self)
        self.config(menu=menubar)
 
        menu_archivo = Menu(menubar, tearoff=0)
        menu_archivo.add_command(label="Salir", command=self.quit)
        menubar.add_cascade(label="Archivo", menu=menu_archivo)
       
        menu_ayuda = Menu(menubar, tearoff=0)
        menu_ayuda.add_command(label="Acerca de", command=self.mostrar_info)
        menubar.add_cascade(label="Ayuda", menu=menu_ayuda)
 
    def add_receta(self):
        """Añade una nueva receta al diccionario y a la lista."""
        nombre = self.entry_nombre.get().strip()
        ingredientes = self.entry_ingredientes.get().strip()
       
        if not nombre or not ingredientes:
            messagebox.showerror("Error", "El nombre y los ingredientes no pueden estar vacíos.")
            return
 
        if nombre in self.recetas:
            messagebox.showwarning("Advertencia", f"La receta '{nombre}' ya existe. ¡Se actualizará!")
       
        self.recetas[nombre] = ingredientes
        self.update_recetas_listbox()
       
        messagebox.showinfo("Éxito", f"Receta '{nombre}' añadida correctamente.")
        self.entry_nombre.delete(0, tk.END)
        self.entry_ingredientes.delete(0, tk.END)
 
    def update_recetas_listbox(self):
        """Actualiza la lista visual de recetas."""
        self.recetas_listbox.delete(0, tk.END)
        for nombre in sorted(self.recetas.keys()):
            self.recetas_listbox.insert(tk.END, nombre)
 
    def delete_receta(self):
        """Elimina la receta seleccionada de la lista y del diccionario."""
        try:
            seleccion_index = self.recetas_listbox.curselection()[0]
            nombre_receta = self.recetas_listbox.get(seleccion_index)
 
            if messagebox.askyesno("Eliminar Receta", f"¿Estás seguro de que quieres eliminar '{nombre_receta}'?"):
                del self.recetas[nombre_receta]
                self.update_recetas_listbox()
                messagebox.showinfo("Éxito", "Receta eliminada correctamente.")
        except IndexError:
            messagebox.showerror("Error", "Por favor, selecciona una receta para eliminar.")
 
    def show_receta_details(self, event):
        """Muestra los ingredientes de la receta seleccionada en una ventana emergente."""
        try:
            seleccion_index = self.recetas_listbox.curselection()[0]
            nombre = self.recetas_listbox.get(seleccion_index)
            ingredientes = self.recetas.get(nombre)
            messagebox.showinfo(f"Ingredientes de {nombre}", ingredientes)
        except IndexError:
            pass 
 
    def mostrar_info(self):
        """Muestra una ventana de información de la aplicación."""
        messagebox.showinfo("Acerca de", "Gestor de Recetas v1.0\nCreao por sofia lopez holguin\nPermite guardar, visualizar y eliminar tus recetas favoritas.")
 
if __name__ == "__main__":
    app = RecetasApp()
    app.mainloop()

