import tkinter as tk
import json
import random


def load_data(file_name, subfolder="npc"):
    """Ładuje dane JSON z podanego pliku."""
    with open(f"data/{subfolder}/{file_name}", "r", encoding="utf-8") as f:
        return json.load(f)


def generate_npc(gender):
    """Generuje losowego NPC na podstawie wybranej płci."""
    if gender == "male":
        first_names = load_data("name_male.json", subfolder="npc")
        appearance = load_data("male_appearance.json", subfolder="npc")
        behavior = load_data("male_behavior.json", subfolder="npc")
    else:
        first_names = load_data("name_female.json", subfolder="npc")
        appearance = load_data("female_appearance.json", subfolder="npc")
        behavior = load_data("female_behavior.json", subfolder="npc")

    surnames = load_data("surname.json", subfolder="npc")
    characteristics = load_data("characteristics.json", subfolder="npc")
    speech = load_data("speech.json", subfolder="npc")

    name = f"{random.choice(first_names)} {random.choice(surnames)}"
    npc_appearance = random.choice(appearance)
    npc_behavior = random.choice(behavior)
    npc_characteristics = random.choice(characteristics)
    npc_speech = random.choice(speech)

    return {
        "Imię i nazwisko": name,
        "Wygląd": npc_appearance,
        "Zachowanie": npc_behavior,
        "Cechy charakterystyczne": npc_characteristics,
        "Styl mówienia": npc_speech
    }


def create_random_npc_gui(root, return_to_menu):
    """Tworzy interfejs generatora losowych NPC."""
    frame = tk.Frame(root, bg="#2c2c2c")
    frame.pack(fill="both", expand=True)

    # Nagłówek
    tk.Label(
        frame,
        text="Generator Losowych NPC",
        font=("Arial", 20, "bold"),
        bg="#2c2c2c",
        fg="#ffffff"
    ).pack(pady=10)

    # Funkcja generowania i wyświetlania NPC w tym samym oknie
    def display_npc(gender):
        npc_data = generate_npc(gender)

        # Czyszczenie pola tekstowego
        output_text.config(state="normal")
        output_text.delete("1.0", tk.END)

        # Wstawianie danych NPC do pola tekstowego
        for key, value in npc_data.items():
            output_text.insert("end", f"{key}:\n", "bold")
            output_text.insert("end", f"{value}\n\n")
        output_text.config(state="disabled")  # Tylko do odczytu

    # Przyciski wyboru płci NPC
    tk.Label(
        frame,
        text="Wybierz płeć NPC:",
        font=("Arial", 12),
        bg="#2c2c2c",
        fg="#ffffff"
    ).pack(pady=10)

    button_frame = tk.Frame(frame, bg="#2c2c2c")
    button_frame.pack(pady=10)

    tk.Button(
        button_frame,
        text="Mężczyzna",
        command=lambda: display_npc("male"),
        font=("Arial", 12),
        bg="#444444",
        fg="#ffffff",
        width=14
    ).pack(side="left", padx=5)

    tk.Button(
        button_frame,
        text="Kobieta",
        command=lambda: display_npc("female"),
        font=("Arial", 12),
        bg="#444444",
        fg="#ffffff",
        width=14
    ).pack(side="right", padx=5)

    # Pole tekstowe na wynik
    output_text = tk.Text(
        frame,
        wrap="word",
        bg="#1e1e1e",
        fg="#ffffff",
        font=("Arial", 12),
        height=15,
        bd=0,
        highlightthickness=0
    )
    output_text.pack(padx=20, pady=10, fill="both", expand=True)

    # Konfiguracja stylu bold
    output_text.tag_configure("bold", font=("Arial", 12, "bold"))
    output_text.config(state="disabled")  # Ustawione na tylko do odczytu

    # Przycisk powrotu do menu
    tk.Button(
        frame,
        text="Powrót do menu",
        command=lambda: [frame.destroy(), return_to_menu()],
        font=("Arial", 12),
        bg="#444444",
        fg="#ffffff",
        width=14
    ).pack(pady=20)

    return frame
