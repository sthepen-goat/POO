import tkinter as tk
from tkinter import ttk

class MenuInicial:
    def __init__(self, root, callback_iniciar):
        self.root = root
        self.callback = callback_iniciar
        self.frame = tk.Frame(root)
        self.frame.pack(pady=50)
        
        tk.Label(self.frame, text="Jogo de Cartas", font=("Arial", 24)).pack(pady=20)
        
        self.entries = []
        for i in range(4):
            frame = tk.Frame(self.frame)
            frame.pack(pady=5)
            tk.Label(frame, text=f"Jogador {i+1}:").pack(side=tk.LEFT)
            entry = tk.Entry(frame)
            entry.pack(side=tk.LEFT)
            entry.insert(0, f"Jogador {i+1}")
            self.entries.append(entry)
        
        tk.Button(
            self.frame, 
            text="Iniciar Jogo",
            command=self.iniciar,
            font=("Arial", 14)
        ).pack(pady=20)
    
    def iniciar(self):
        nomes = [entry.get() or f"Jogador {i+1}" 
                for i, entry in enumerate(self.entries)]
        self.frame.destroy()
        self.callback(nomes)