import tkinter as tk
from tkinter import messagebox
import json
import random
import os

def load_json(file_path):
    """Ładuje dane JSON z pliku."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except Exception as e:
        raise ValueError(f"Błąd ładowania pliku JSON {file_path}: {e}")

def generate_combat_description(opponent_type):
    """Generuje opis walki na podstawie typu przeciwnika."""
    base_path = os.path.join("data", "combat")

    # Przypisanie odpowiednich plików na podstawie przeciwnika
    if opponent_type == "Człowiek":
        attack_file = os.path.join(base_path, "human_attack.json")
        attack_key = "human_attack"
    elif opponent_type == "Zwierzoczłowiek":
        attack_file = os.path.join(base_path, "beastman_attack.json")
        attack_key = "beastman_attack"
    else:
        raise ValueError(f"Nieznany typ przeciwnika: {opponent_type}")

    atmosphere_file = os.path.join(base_path, "combat_atmosphere.json")
    atmosphere_key = "combat_atmosphere"

    # Ładowanie danych
    attack_data = load_json(attack_file).get(attack_key, [])
    atmosphere_data = load_json(atmosphere_file).get(atmosphere_key, [])

    print(f"Załadowano dane ataku: {len(attack_data)} wpisów")
    print(f"Załadowano dane atmosfery: {len(atmosphere_data)} wpisów")

    if not attack_data:
        raise ValueError(f"Brak danych ataku dla {opponent_type}! Upewnij się, że plik JSON zawiera wpisy.")
    if not atmosphere_data:
        raise ValueError("Brak danych atmosfery walki! Upewnij się, że plik JSON zawiera wpisy.")

    # Losowanie wpisów
    attack = random.choice(attack_data)["description"]
    atmosphere = random.choice(atmosphere_data)["description"]

    # Tworzenie opisu walki
    return f"{attack}\n\n{atmosphere}"


def create_combat_gui(root, return_to_menu):
    """Tworzy GUI generatora walk."""
    frame = tk.Frame(root, bg="#2c2c2c")

    # Nagłówek
    tk.Label(frame, text="Generator Walki", font=("Arial", 20), bg="#2c2c2c", fg="white").pack(pady=10)

    # Wybór przeciwnika
    tk.Label(frame, text="Wybierz przeciwnika:", font=("Arial", 12), bg="#2c2c2c", fg="white").pack(pady=5)
    opponent_var = tk.StringVar(value="Człowiek")
    tk.Radiobutton(frame, text="Człowiek", variable=opponent_var, value="Człowiek", bg="#2c2c2c", fg="white", selectcolor="#444444").pack()
    tk.Radiobutton(frame, text="Zwierzoczłowiek", variable=opponent_var, value="Zwierzoczłowiek", bg="#2c2c2c", fg="white", selectcolor="#444444").pack()

    # Pole tekstowe na wynik
    output_text = tk.Text(frame, height=15, width=70, font=("Arial", 12), wrap="word", state="disabled", bg="#2c2c2c", fg="white")
    output_text.pack(pady=10)

    def generate_combat():
        try:
            opponent_type = opponent_var.get()
            print(f"Wybrany typ przeciwnika: {opponent_type}")
            description = generate_combat_description(opponent_type)

            # Wyświetlanie wyniku
            output_text.config(state="normal")
            output_text.delete("1.0", tk.END)
            output_text.insert(tk.END, description)
            output_text.config(state="disabled")
        except ValueError as e:
            messagebox.showerror("Błąd", str(e))

    # Przycisk generowania
    tk.Button(frame, text="Generuj Walkę", command=generate_combat, font=("Arial", 12), bg="#444444", fg="white").pack(pady=10)

    # Przycisk powrotu
    tk.Button(frame, text="Powrót do menu", command=lambda: [frame.pack_forget(), return_to_menu()], font=("Arial", 12), bg="#444444", fg="white").pack(pady=10)

    return frame
