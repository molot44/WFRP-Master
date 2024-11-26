import tkinter as tk
from PIL import Image, ImageTk
import subprocess

from modules.lokacje import create_location_gui
from modules.wypowiedzi import create_npc_gui
from modules.random_npc import create_random_npc_gui
from modules.taverns import create_taverns_gui
from modules.combat import create_combat_gui


def open_notion():
    try:
        subprocess.Popen([r"C:\Users\marci\AppData\Local\Programs\Notion\Notion.exe"])
    except Exception as e:
        print(f"Nie udało się otworzyć Notion: {e}")


def open_discord():
    try:
        subprocess.Popen([r"C:\Users\marci\AppData\Local\Discord\app-1.0.9171\Discord.exe"])
    except Exception as e:
        print(f"Nie udało się otworzyć Discorda: {e}")


def open_gimp():
    try:
        subprocess.Popen([r"C:\Program Files\GIMP 2\bin\gimp-2.10.exe"])
    except Exception as e:
        print(f"Nie udało się otworzyć GIMP: {e}")


def open_molten():
    import webbrowser
    webbrowser.open("https://molot.moltenhosting.com/")

def open_url(url):
    """Otwiera podany URL w domyślnej przeglądarce."""
    import webbrowser
    webbrowser.open(url)


def load_image(path):
    """Ładuje obraz z pliku."""
    try:
        return Image.open(path)
    except Exception as e:
        print(f"Nie udało się załadować obrazu {path}: {e}")
        return None


def main():
    root = tk.Tk()
    root.title("WFRP Master")
    root.geometry("800x850")
    root.resizable(False, False)

    # Zmienna kontrolna dla checkboxa
    always_on_top_var = tk.BooleanVar(value=False)

    # Funkcja do ustawiania "Zawsze na wierzchu"
    def toggle_always_on_top():
        root.attributes("-topmost", always_on_top_var.get())

    def create_always_on_top_button():
        """Tworzy przycisk 'Zawsze na wierzchu'."""
        always_on_top_button = tk.Checkbutton(
            root,
            text="Zawsze na wierzchu",
            variable=always_on_top_var,
            command=toggle_always_on_top,
            bg="#2c2c2c",
            fg="white",
            font=("Arial", 10),
            activebackground="#444444",
            activeforeground="white",
            selectcolor="#666666"
        )
        always_on_top_button.place(relx=0.01, rely=0.98, anchor="sw")

    # Ustawienie tła
    background_image = load_image("assets/background.jpg")
    if background_image:
        bg_photo = ImageTk.PhotoImage(background_image.resize((800, 850), Image.Resampling.LANCZOS))
        bg_label = tk.Label(root, image=bg_photo)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Główna ramka aplikacji z wymuszoną szerokością i paddingiem
    main_frame = tk.Frame(root, bg="#2c2c2c")
    main_frame.place(relx=0.5, rely=0.5, anchor="center")
    main_frame.config(width=500, height=700)

    # Ładowanie logo
    logo_image = load_image("assets/logo.png")
    if logo_image:
        logo_photo = ImageTk.PhotoImage(logo_image.resize((200, 120), Image.Resampling.LANCZOS))
        logo_label = tk.Label(main_frame, image=logo_photo, bg="#2c2c2c")
        logo_label.image = logo_photo
        logo_label.pack(pady=20)

    # Dodanie pustych ramek wypełniających po bokach
    tk.Frame(main_frame, bg="#2c2c2c", width=50).pack(side="left", fill="y")
    content_frame = tk.Frame(main_frame, bg="#2c2c2c")
    content_frame.pack(side="left", fill="both", expand=True)
    tk.Frame(main_frame, bg="#2c2c2c", width=50).pack(side="left", fill="y")

    # Funkcja powrotu do menu
    def return_to_menu():
        for widget in root.winfo_children():
            widget.place_forget()
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        main_frame.place(relx=0.5, rely=0.5, anchor="center")
        create_always_on_top_button()
        create_bottom_links(root)

    # Funkcje otwierające moduły
    def open_location():
        main_frame.place_forget()
        location_frame = create_location_gui(root, return_to_menu)
        location_frame.pack(fill="both", expand=True)

    def open_wypowiedzi():
        main_frame.place_forget()
        wypowiedzi_frame = create_npc_gui(root, return_to_menu)
        wypowiedzi_frame.pack(fill="both", expand=True)

    def open_npc():
        main_frame.place_forget()
        npc_frame = create_random_npc_gui(root, return_to_menu)
        npc_frame.pack(fill="both", expand=True)

    def open_taverns():
        main_frame.place_forget()
        taverns_frame = create_taverns_gui(root, return_to_menu)
        taverns_frame.pack(fill="both", expand=True)

    def open_combat():
        main_frame.place_forget()
        combat_frame = create_combat_gui(root, return_to_menu)
        combat_frame.pack(fill="both", expand=True)

    def create_bottom_links(root):
        """Tworzy ramkę w dolnym prawym rogu z ikonami."""
        link_frame = tk.Frame(root, bg="#2c2c2c", height=40)
        link_frame.place(relx=0.99, rely=0.98, anchor="se")

        icons = [
            ("assets/foundry_icon.png", "https://foundryvtt.com/packages/modules"),
            ("assets/reddit_icon.png", "https://www.reddit.com/r/FoundryVTT/"),
            ("assets/youtube_icon.png", "https://www.youtube.com/results?search_query=foundry+vtt+module&sp=CAI%253D"),
        ]

        for icon_path, url in icons:
            icon_image = load_image(icon_path)
            if icon_image:
                icon_photo = ImageTk.PhotoImage(icon_image.resize((40, 40), Image.Resampling.LANCZOS))
                icon_button = tk.Button(
                    link_frame,
                    image=icon_photo,
                    command=lambda u=url: open_url(u),
                    bg="#2c2c2c",
                    activebackground="#444444",
                    bd=0
                )
                icon_button.image = icon_photo  # Zachowaj referencję do obrazka
                icon_button.pack(side="right", padx=10)



    # Lista przycisków z obsługą kliknięć i podświetleniem
    buttons = [
        ("Lokacje (prompt)", open_location),
        ("Wypowiedzi (prompt)", open_wypowiedzi),
        ("Generator NPC", open_npc),
        ("Generator Tawern", open_taverns),
        ("Walka", open_combat),
    ]

    def on_hover(event):
        event.widget.config(bg="#666666")

    def on_leave(event):
        event.widget.config(bg="#444444")

    for text, command in buttons:
        button = tk.Button(
            content_frame,
            text=text,
            command=command,
            font=("Arial", 14),
            bg="#444444",
            fg="white",
            activebackground="#666666",
            activeforeground="white",
            width=20,
            height=2
        )
        button.bind("<Enter>", on_hover)
        button.bind("<Leave>", on_leave)
        button.pack(pady=15)

    # Ramka na ikony
    icon_frame = tk.Frame(content_frame, bg="#2c2c2c")
    icon_frame.pack(pady=10)

    # Przyciski z ikonami
    notion_icon = load_image("assets/notion_icon.png")
    discord_icon = load_image("assets/discord_icon.png")
    gimp_icon = load_image("assets/gimp_icon.png")
    molten_icon = load_image("assets/molten_icon.png")  # Nowa ikona
    if notion_icon and discord_icon:
        notion_photo = ImageTk.PhotoImage(notion_icon.resize((40, 40), Image.Resampling.LANCZOS))
        discord_photo = ImageTk.PhotoImage(discord_icon.resize((45, 45), Image.Resampling.LANCZOS))
        gimp_photo = ImageTk.PhotoImage(gimp_icon.resize((40, 40), Image.Resampling.LANCZOS))
        molten_photo = ImageTk.PhotoImage(molten_icon.resize((40, 40), Image.Resampling.LANCZOS))

        notion_button = tk.Button(
            icon_frame,
            image=notion_photo,
            command=open_notion,
            bg="#2c2c2c",
            activebackground="#444444",
            bd=0
        )
        discord_button = tk.Button(
            icon_frame,
            image=discord_photo,
            command=open_discord,
            bg="#2c2c2c",
            activebackground="#444444",
            bd=0
        )
        gimp_button = tk.Button(
            icon_frame,
            image=gimp_photo,
            command=open_gimp,
            bg="#2c2c2c",
            activebackground="#444444",
            bd=0
        )
        molten_button = tk.Button(
            icon_frame,
            image=molten_photo,
            command=open_molten,
            bg="#2c2c2c",
            activebackground="#444444",
            bd=0
        )

        notion_button.grid(row=0, column=0, padx=5)
        discord_button.grid(row=0, column=1, padx=4)
        gimp_button.grid(row=0, column=2, padx=4)
        molten_button.grid(row=0, column=3, padx=4)  # Nowa ikona

    create_always_on_top_button()
    create_bottom_links(root)


    root.mainloop()


if __name__ == "__main__":
    main()
