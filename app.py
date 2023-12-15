import tkinter as tk
import json

class VirtualFriendApp:
    def __init__(self):
        self.nazwa_uzytkownika, self.nazwa_ai, self.motyw = self.wczytaj_dane_uzytkownika_z_pliku()

        self.utworz_okno()

    def wczytaj_dane_uzytkownika_z_pliku(self):
        try:
            with open("dane_uzytkownika.json", "r", encoding="utf-8") as plik:
                dane_uzytkownika = json.load(plik)
                return dane_uzytkownika["nazwa_uzytkownika"], dane_uzytkownika["nazwa_ai"], dane_uzytkownika["motyw"]
        except FileNotFoundError:
            return None, None, None
        except Exception as e:
            print(f"Błąd podczas wczytywania danych użytkownika: {e}")
            return None, None, None

    def wczytaj_historie_z_pliku(self):
        try:
            with open("historia.json", "r", encoding="utf-8") as plik:
                historia = json.load(plik)
                return historia
        except FileNotFoundError:
            return []

    def zapisz_historie_do_pliku(self, historia):
        with open("historia.json", "w", encoding="utf-8") as plik:
            json.dump(historia, plik, indent=2)

    def utworz_okno(self):
        root = tk.Tk()
        root.title("Virtual Friend")
        root.geometry("500x500")

        self.UstawieniaMotywu = {
            "jasny": {"tlo_okna": "lightblue", "tlo_czatu": "lightpink"},
            "ciemny": {"tlo_okna": "gray10", "tlo_czatu": "gray20"}
        }

        self.motyw = self.motyw or "jasny"

        root.config(bg=self.UstawieniaMotywu[self.motyw]["tlo_okna"])

        input_text = tk.Entry(root, width=60, bg=self.UstawieniaMotywu[self.motyw]["tlo_czatu"])
        input_text.pack(padx=10, pady=10)

        send_button = tk.Button(root, text="Wyślij", command=self.wyslij_wiadomosc, bg=self.UstawieniaMotywu[self.motyw]["tlo_czatu"])
        send_button.pack(pady=5)

        zmiana_motywu_button = tk.Button(root, text="Zmień Motyw", command=self.zmien_motyw, bg=self.UstawieniaMotywu[self.motyw]["tlo_czatu"])
        zmiana_motywu_button.pack(pady=5)

        output_text = tk.Text(root, height=10, width=60, state=tk.DISABLED, bg=self.UstawieniaMotywu[self.motyw]["tlo_czatu"])
        output_text.pack(padx=10, pady=10)

        root.protocol("WM_DELETE_WINDOW", root.destroy)

        response = self.generate_ai_response("Cześć")
        self.conversation_history = [(self.nazwa_ai, response)]

        root.mainloop()

    def generate_ai_response(self, question):
        # Symulacja generowania odpowiedzi na podstawie pytania
        return f"{self.nazwa_ai}: Odpowiedź na pytanie - {question}"

    def wyslij_wiadomosc(self):
        message = input_text.get()
        input_text.delete(0, tk.END)
        output_text.config(state=tk.NORMAL)
        output_text.insert(tk.END, f"{self.nazwa_uzytkownika}: {message}\n")
        output_text.see(tk.END)
        output_text.config(state=tk.DISABLED)
        response = self.generate_ai_response(message)
        self.conversation_history.append((self.nazwa_uzytkownika, message))
        self.conversation_history.append((self.nazwa_ai, response))

        self.zapisz_historie_do_pliku(self.conversation_history)

    def zmien_motyw(self):
        if self.motyw == "jasny":
            self.motyw = "ciemny"
        else:
            self.motyw = "jasny"

        root.config(bg=self.UstawieniaMotywu[self.motyw]["tlo_okna"])
        input_text.config(bg=self.UstawieniaMotywu[self.motyw]["tlo_czatu"])
        send_button.config(bg=self.UstawieniaMotywu[self.motyw]["tlo_czatu"])
        zmiana_motywu_button.config(bg=self.UstawieniaMotywu[self.motyw]["tlo_czatu"])
        output_text.config(bg=self.UstawieniaMotywu[self.motyw]["tlo_czatu"])

if __name__ == "__main__":
    app = VirtualFriendApp()
