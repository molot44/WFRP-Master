import tkinter as tk
from tkinter import ttk
from .utils import copy_prompt

def create_location_gui(root, return_to_menu):
    """Tworzy GUI generatora lokacji."""
    frame = tk.Frame(root, bg="#2c2c2c")

    # Nagłówek
    tk.Label(frame, text="Generator Lokacji", font=("Arial", 20), bg="#2c2c2c", fg="white").pack(pady=10)

    # Zmienne
    loc_type_var = tk.StringVar()
    size_var = tk.StringVar()
    mood_var = tk.StringVar()
    time_var = tk.StringVar()
    season_var = tk.StringVar()
    special_var = tk.StringVar()
    purpose_var = tk.StringVar()

    # Pola formularza
    fields = [
        ("Rodzaj lokacji:", loc_type_var, ["Las", "Miasto", "Opuszczona wioska", "Świątynia"]),
        ("Rozmiar i znaczenie:", size_var, ["Mały", "Średni", "Wielki"]),
        ("Klimat i nastrój:", mood_var, ["Ponury", "Tajemniczy", "Zniszczony", "Przyjazny", "Tłoczny"]),
        ("Pora dnia:", time_var, ["W południe", "O zmierzchu", "W nocy", "Środek dnia"]),
        ("Pora roku:", season_var, ["Wiosna", "Lato", "Jesień", "Zima"]),
        ("Przeznaczenie lokacji:", purpose_var, ["Miejsce odpoczynku", "Kryjówka wroga", "Miejsce handlu"]),
        ("Elementy szczególne:", special_var, None),
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
    prompt_text = tk.Text(
        frame,
        height=10,
        width=70,
        wrap="word",
        bg="#1e1e1e",
        fg="white",
        font=("Arial", 12)
    )
    prompt_text.pack(pady=10)

    # Funkcja generowania promptu
    def generate_prompt():
        prompt = f"""Proszę wygenerować szczegółowy, klimatyczny opis lokacji w lore Warhammer Fantasy w stylu Sapkowskiego:
        - Rodzaj lokacji: {loc_type_var.get()}
        - Rozmiar i znaczenie: {size_var.get()}
        - Klimat i nastrój: {mood_var.get()}
        - Czas akcji: {time_var.get()}
        - Pora roku: {season_var.get()}
        - Elementy szczególne: {special_var.get()}
        - Przeznaczenie lokacji: {purpose_var.get()}
        Uwzględnij:
        - Wrażenia zmysłowe (co gracze widzą, słyszą, czują, węszą).
        - Elementy interaktywne, np. podejrzani NPC, ślady w błocie, zagadkowe odgłosy.
        - Skieruj opis bezpośrednio do graczy, używając drugiej osoby liczby mnogiej.
        - Dodaj subtelne wskazówki fabularne, które zachęcą graczy do eksploracji lub zadawania pytań.
        - Pod opisem lokacji proszę napisz prompt dla ChatGPT, który po ewentualnym wysłaniu wygeneruje grafikę przedstawiającą tę lokację. Niech grafika odzwierciedla klimat, szczegóły i atmosferę opisanej scenerii. Uwzględnij elementy takie jak [elementy szczególne, np. martwe szczury, mgła, zimowy krajobraz] oraz nastrój [np. zniszczony, tajemniczy, ponury]. Grafika powinna być wizualizacją tego, co gracze mogą zobaczyć, czując w pełni klimat Warhammer Fantasy.
        """
        prompt_text.delete("1.0", tk.END)
        prompt_text.insert(tk.END, prompt)

    # Ramka na przyciski
    button_frame = tk.Frame(frame, bg="#2c2c2c")
    button_frame.pack(pady=10)

    # Przyciski
    tk.Button(
        button_frame,
        text="Generuj Prompt",
        command=generate_prompt,
        font=("Arial", 12),
        bg="#444444",
        fg="white"
    ).grid(row=0, column=0, padx=5)

    tk.Button(
        button_frame,
        text="Kopiuj Prompt",
        command=lambda: copy_prompt(prompt_text),
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
