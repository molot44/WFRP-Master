import tkinter as tk
from tkinter import ttk
from .utils import copy_prompt

def create_npc_gui(root, return_to_menu):
    """Tworzy GUI generatora wypowiedzi NPC."""
    frame = tk.Frame(root, bg="#2c2c2c")

    # Nagłówek
    tk.Label(frame, text="Generator Wypowiedzi NPC", font=("Arial", 20), bg="#2c2c2c", fg="white").pack(pady=10)

    # Zmienne
    npc_name_var = tk.StringVar()
    npc_role_var = tk.StringVar()
    npc_character_var = tk.StringVar()
    npc_speech_style_var = tk.StringVar()
    npc_goal_var = tk.StringVar()
    player_emotion_var = tk.StringVar()
    short_count_var = tk.StringVar()
    long_count_var = tk.StringVar()

    # Pola formularza
    fields = [
        ("Imię i nazwisko:", npc_name_var, None),
        ("Rola NPC:", npc_role_var, ["Kupiec", "Karczmarz", "Strażnik", "Mieszczanin", "Chłop"]),
        ("Charakter:", npc_character_var, ["Uprzejmy", "Cyniczny", "Wrogi"]),
        ("Styl mowy:", npc_speech_style_var, ["Archaiczny", "Kolokwialny", "Wyniosły", "Uczony"]),
        ("Cel wypowiedzi:", npc_goal_var, ["Rozmowa", "Pytanie", "Propozycja", "Prowokacja"]),
        ("Jakie emocje ma wywołać:", player_emotion_var, ["Nieokreślone", "Ciekawość", "Zaniepokojenie"]),
        ("Liczba krótkich wypowiedzi:", short_count_var, ["1", "2", "3", "4", "5"]),
        ("Liczba długich wypowiedzi:", long_count_var, ["1", "2", "3", "4", "5"]),
    ]

    # Tworzenie pól formularza
    for label, var, options in fields:
        tk.Label(
            frame,
            text=label,
            font=("Arial", 12),
            bg="#2c2c2c",
            fg="white",
            anchor="w"
        ).pack(pady=5)
        if options:
            ttk.Combobox(frame, textvariable=var, values=options, width=40, state="normal").pack(pady=5)
        else:
            tk.Entry(frame, textvariable=var, width=40, bg="#1e1e1e", fg="white", font=("Arial", 12)).pack(pady=5)

    # Pole tekstowe na prompt
    output_text = tk.Text(
        frame,
        height=7,
        width=70,
        wrap="word",
        bg="#1e1e1e",
        fg="white",
        font=("Arial", 12)
    )
    output_text.pack(pady=10)

    # Funkcja generowania promptu
    def generate_npc_prompt():
        prompt = f"""Proszę wygenerować wypowiedzi NPC z uniwersum Warhammer Fantasy, posługując się stylem Sapkowskiego:
        Imię i nazwisko: {npc_name_var.get()}
        Rola: {npc_role_var.get()}
        Charakter: {npc_character_var.get()}
        Styl mowy: {npc_speech_style_var.get()}
        Cel wypowiedzi: {npc_goal_var.get()}
        Jakie emocje ma wywołać: {player_emotion_var.get()}
        Liczba krótkich wypowiedzi: {short_count_var.get()}
        Liczba długich wypowiedzi: {long_count_var.get()}
         Uwzględnij:
        - Różnorodność wypowiedzi: Twórz wypowiedzi emocjonalne, neutralne i konfliktowe, aby rozmowa była bardziej zróżnicowana i interesująca.
        - Gesty i zachowania NPC: Dodaj subtelne gesty, które postać może wykonywać w trakcie mówienia, np. bębnienie palcami, spoglądanie na bok czy poprawianie stroju.
        - Spójność z lore: Dopasuj wypowiedzi do uniwersum Warhammer Fantasy, uwzględniając styl wypowiedzi jak u Sapkowskiego.
        - Konkrety: Nie wprowadzaj w wypowiedzi wymyślonych, niewspomnianych postaci, skomplikowanych nowych wątków fabularnych oraz zadań dla odbiorcy wiadomości.
        - Ciekawy styl mowy: Użyj specyficznego języka lub słownictwa odpowiedniego dla postaci (np. archaizmy, kolokwializmy, poetycki język).
        """
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, prompt)

    # Ramka na przyciski
    button_frame = tk.Frame(frame, bg="#2c2c2c")
    button_frame.pack(pady=10)

    # Przyciski
    tk.Button(
        button_frame,
        text="Generuj Prompt",
        command=generate_npc_prompt,
        font=("Arial", 12),
        bg="#444444",
        fg="white"
    ).grid(row=0, column=0, padx=5)

    tk.Button(
        button_frame,
        text="Kopiuj Prompt",
        command=lambda: copy_prompt(output_text),
        font=("Arial", 12),
        bg="#444444",
        fg="white"
    ).grid(row=0, column=1, padx=5)

    # Przycisk powrotu do menu
    tk.Button(
        frame,
        text="Powrót do menu",
        command=lambda: [frame.destroy(), return_to_menu()],
        font=("Arial", 12),
        bg="#444444",
        fg="white"
    ).pack(pady=10)

    return frame
