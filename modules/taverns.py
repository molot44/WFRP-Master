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


def generate_tavern_data(richness, generate_name, custom_name):
    """Generuje dane dla tawerny."""
    base_path = os.path.join("data", "taverns")

    # Ładowanie plików JSON
    atmosphere_data = load_json(os.path.join(base_path, "tavern_atmosphere.json"))
    clientele_data = load_json(os.path.join(base_path, "tavern_clientele.json"))
    description_data = load_json(os.path.join(base_path, "tavern_description.json"))
    names_data = load_json(os.path.join(base_path, "tavern_names.json"))

    # Wybór danych na podstawie zamożności
    atmosphere = random.choice(atmosphere_data[richness])
    clientele = random.choice(clientele_data[richness])
    description = random.choice(description_data[richness])

    # Generowanie lub ustawianie nazwy tawerny
    if generate_name:
        name_entry = random.choice(names_data["zwyczajne"] if richness in ["biedne", "zwyczajne"] else names_data["bogate"])
        tavern_name = name_entry["nazwa"]
        tavern_geneza = name_entry["geneza"]
    elif custom_name.strip():
        tavern_name = custom_name
        tavern_geneza = "Brak genezy – nazwa wprowadzona ręcznie."
    else:
        raise ValueError("Brak nazwy tawerny! Wprowadź nazwę lub zaznacz generowanie automatyczne.")

    # Tworzenie końcowego opisu
    return {
        "name": tavern_name,
        "geneza": tavern_geneza,
        "atmosphere": atmosphere,
        "clientele": clientele,
        "description": description
    }

def generate_menu_item(richness):
    """Generuje pozycję menu na podstawie zamożności tawerny."""
    menu_data = load_json("data/taverns/tavern_menu.json")
    return random.choice(menu_data[richness])

def generate_tavern_hook(category, richness):
    """Generuje pojedynczy wpis z tavern_hooks.json."""
    tavern_hooks_data = load_json("data/taverns/tavern_hooks.json")
    hook_list = tavern_hooks_data[richness][category]
    content = random.choice(hook_list)
    return f"[{category.upper()}] {content}"  # Usunięto ['content']

def create_taverns_gui(root, return_to_menu):
    """Tworzy GUI generatora tawern."""
    frame = tk.Frame(root, bg="#2c2c2c")

    # Nagłówek
    tk.Label(frame, text="Generator Tawern", font=("Arial", 20), bg="#2c2c2c", fg="white").pack(pady=10)

    # Wybór zamożności tawerny
    tk.Label(frame, text="Wybierz zamożność tawerny:", font=("Arial", 12), bg="#2c2c2c", fg="white").pack(pady=5)
    richness_var = tk.StringVar(value="biedne")
    tk.Radiobutton(frame, text="Biedna", variable=richness_var, value="biedne", bg="#2c2c2c", fg="white", selectcolor="#444444").pack()
    tk.Radiobutton(frame, text="Zwyczajna", variable=richness_var, value="zwyczajne", bg="#2c2c2c", fg="white", selectcolor="#444444").pack()
    tk.Radiobutton(frame, text="Bogata", variable=richness_var, value="bogate", bg="#2c2c2c", fg="white", selectcolor="#444444").pack()

    # Checkbox do generowania nazwy
    generate_name_var = tk.BooleanVar(value=True)
    tk.Checkbutton(frame, text="Automatycznie wygeneruj nazwę", variable=generate_name_var, bg="#2c2c2c", fg="white", selectcolor="#444444").pack()

    # Pole do ręcznego wprowadzania nazwy
    custom_name_entry = tk.Entry(frame, width=30, font=("Arial", 12))
    custom_name_entry.pack(pady=5)

    # Pole tekstowe na wynik
    output_text = tk.Text(frame, height=20, width=70, font=("Arial", 12), wrap="word", state="disabled", bg="#2c2c2c", fg="white")
    output_text.pack(pady=10)

    # Zmienne do przechowywania stanu
    current_tavern = None
    current_menu_item = None
    current_hook = None

    def display_tavern():
        """Wyświetla dane tawerny w polu tekstowym."""
        output_text.config(state="normal")
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, f"Nazwa tawerny: {current_tavern['name']}\n", "bold")
        output_text.insert(tk.END, f"Geneza: {current_tavern['geneza']}\n\n", "normal")
        output_text.insert(tk.END, f"Opis: {current_tavern['description']}\n", "bold")
        output_text.insert(tk.END, f"Atmosfera: {current_tavern['atmosphere']}\n", "bold")
        output_text.insert(tk.END, f"Klientela: {current_tavern['clientele']}\n\n", "bold")
        output_text.insert(tk.END, f"Menu: {current_menu_item['nazwa']} - {current_menu_item['opis']}\n\n", "bold")
        output_text.insert(tk.END, f"Zdarzenie: {current_hook}\n", "bold")
        output_text.config(state="disabled")

    def generate_tavern():
        """Generuje dane tawerny oraz dodatkowe elementy."""
        nonlocal current_tavern, current_menu_item, current_hook
        richness = richness_var.get()
        generate_name = generate_name_var.get()
        custom_name = custom_name_entry.get()

        current_tavern = generate_tavern_data(richness, generate_name, custom_name)
        current_menu_item = generate_menu_item(richness)

        # Losowanie kategorii (plotki, klientela, wydarzenia)
        categories = ["plotki", "klientela", "wydarzenia"]
        selected_category = random.choice(categories)
        current_hook = generate_tavern_hook(selected_category, richness)

        display_tavern()

    def reroll_menu_item():
        """Przelosowuje pozycję menu."""
        nonlocal current_menu_item
        richness = richness_var.get()
        current_menu_item = generate_menu_item(richness)
        display_tavern()

    def reroll_hook():
        """Przelosowuje dodatkowy element."""
        nonlocal current_hook
        richness = richness_var.get()

        # Losowanie kategorii
        categories = ["plotki", "klientela", "wydarzenia"]
        selected_category = random.choice(categories)
        current_hook = generate_tavern_hook(selected_category, richness)

        display_tavern()

    # Przycisk generowania
    tk.Button(frame, text="Generuj Tawernę", command=generate_tavern, font=("Arial", 12), bg="#444444", fg="white").pack(pady=10)

    # Przycisk przelosowywania
    tk.Button(frame, text="Przelosuj Menu", command=reroll_menu_item, font=("Arial", 12), bg="#444444", fg="white").pack(pady=5)
    tk.Button(frame, text="Przelosuj Zdarzenie", command=reroll_hook, font=("Arial", 12), bg="#444444", fg="white").pack(pady=5)

    # Przycisk powrotu
    tk.Button(frame, text="Powrót do menu", command=lambda: [frame.pack_forget(), return_to_menu()], font=("Arial", 12), bg="#444444", fg="white").pack(pady=10)

    return frame