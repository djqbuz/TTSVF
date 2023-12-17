import tkinter as tk
from tkinter import scrolledtext, messagebox
from urllib import request
import json
import os
import sys
import types
import logika

class VirtualFriendApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Virtual Friend")
        self.root.geometry("600x400")

        # Dodaj motyw
        self.motyw = self.wczytaj_motyw()
        self.UstawieniaMotywu = {
            "jasny": {"tlo_okna": "#FFFFFF", "tlo_ramki": "#F0F0F0", "kolor_tekstu": "#000000"},
            "ciemny": {"tlo_okna": "#303030", "tlo_ramki": "#2E2E2E", "kolor_tekstu": "#FFFFFF"}
        }
        self.history_text = None

        # Wczytaj ikonę
        icon_url = "https://raw.githubusercontent.com/djqbuz/TTSVF/main/icon.png"
        icon_path = os.path.join(os.getenv('APPDATA'), "TechTwinsSystems", "MyAiFriend", "icon.png")
        self.download_file(icon_url, icon_path)
        self.icon = tk.PhotoImage(file=icon_path)
        self.root.iconphoto(True, self.icon)

        # Pobierz plik logika.py jako plik tymczasowy
        logika_url = "https://raw.githubusercontent.com/djqbuz/TTSVF/main/logika.py"
        logika_temp_path = os.path.join(os.getenv('APPDATA'), "TechTwinsSystems", "MyAiFriend", "logika_temp.py")
        self.download_file(logika_url, logika_temp_path)

        # Importuj moduł logika jako moduł tymczasowy
        with open(logika_temp_path, 'r') as file:
            logika_code = file.read()

        logika_module = types.ModuleType("logika")
        exec(logika_code, logika_module.__dict__)
        sys.modules["logika"] = logika_module

        # Dodaj pola na pytania i odpowiedzi
        self.history_text = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, width=50, height=15)
        self.history_text.pack(pady=10)

        self.entry = tk.Entry(self.root, width=50)
        self.entry.pack(pady=10)

        self.send_button = tk.Button(self.root, text="Wyślij", command=self.send_message)
        self.send_button.pack(pady=10)

        self.motyw_button = tk.Button(self.root, text="Zmień Motyw", command=self.zmien_motyw)
        self.motyw_button.pack(pady=10)

        # Binduj klawisz Enter do przycisku Wyślij
        self.root.bind('<Return>', lambda event=None: self.send_button.invoke())

        # Wyświetl okno
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.after(100, self.ustaw_motyw, self.motyw)  # Poprawka
        self.wczytaj_historie()

        self.root.mainloop()

    def wczytaj_motyw(self):
        try:
            with open("dane_uzytkownika.json", "r", encoding="utf-8") as file:
                dane_uzytkownika = json.load(file)
                return dane_uzytkownika.get("motyw", "jasny")
        except (FileNotFoundError, json.JSONDecodeError):
            return "jasny"

    def ustaw_motyw(self, motyw):
        ustawienia = self.UstawieniaMotywu.get(motyw, self.UstawieniaMotywu["jasny"])
        if self.history_text:
            self.history_text.configure(bg=ustawienia["tlo_ramki"], fg=ustawienia["kolor_tekstu"])
        self.root.configure(bg=ustawienia["tlo_okna"])
        self.entry.configure(bg=ustawienia["tlo_ramki"], fg=ustawienia["kolor_tekstu"])
        self.send_button.configure(bg=ustawienia["tlo_ramki"], fg=ustawienia["kolor_tekstu"])
        self.motyw_button.configure(bg=ustawienia["tlo_ramki"], fg=ustawienia["kolor_tekstu"])

    def zmien_motyw(self):
        if self.motyw == "jasny":
            self.motyw = "ciemny"
        else:
            self.motyw = "jasny"
        self.ustaw_motyw(self.motyw)
        self.zapisz_dane_uzytkownika()

    def download_file(self, url, save_path):
        try:
            response = request.urlopen(url)
            with open(save_path, 'wb') as file:
                file.write(response.read())
        except Exception as e:
            print(f"Błąd podczas pobierania pliku {url}: {e}")

    def zapisz_dane_uzytkownika(self):
        dane_uzytkownika = {
            "motyw": self.motyw
        }
        with open("dane_uzytkownika.json", "w", encoding="utf-8") as file:
            json.dump(dane_uzytkownika, file, indent=2)

    def send_message(self):
        message = self.entry.get()
        if message:
            self.history_text.insert(tk.END, f"Ty: {message}\n")
            self.entry.delete(0, tk.END)
            ai_response = logika.generate_ai_response(message)
            self.history_text.insert(tk.END, f"Ai: {ai_response}\n")
            self.zapisz_do_historii({"user": message, "ai": ai_response})

    def wczytaj_historie(self):
        try:
            with open("historia.json", "r", encoding="utf-8") as file:
                historia = json.load(file)
                for wpis in historia:
                    self.history_text.insert(tk.END, f"Ty: {wpis['user']}\n")
                    self.history_text.insert(tk.END, f"Ai: {wpis['ai']}\n")
        except (FileNotFoundError, json.JSONDecodeError):
            pass

    def zapisz_do_historii(self, wpis):
        try:
            with open("historia.json", "r", encoding="utf-8") as file:
                historia = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            historia = []
        historia.append(wpis)
        with open("historia.json", "w", encoding="utf-8") as file:
            json.dump(historia, file, indent=2)

    def on_closing(self):
        self.zapisz_dane_uzytkownika()
        self.root.destroy()
        logika_temp_path = os.path.join(os.getenv('APPDATA'), "TechTwinsSystems", "MyAiFriend", "logika_temp.py")
        if os.path.exists(logika_temp_path):
            os.remove(logika_temp_path)

if __name__ == "__main__":
    app = VirtualFriendApp()
