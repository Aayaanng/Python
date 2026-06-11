import tkinter as tk
from tkinter import font as tkfont

BG = "#0f0f0f"
CARD = "#1a1a1a"
ACCENT = "#00e5ff"
LEAP_CLR = "#00e5ff"
NO_CLR = "#ff4d6d"
ERR_CLR = "#ffb300"
FG = "#e0e0e0"
MUTED = "#555555"
BORDER = "#2a2a2a"

class LeapYearApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Leap Year Checker")
        self.resizable(False, False)
        self.configure(bg=BG)
        title_font = tkfont.Font(family="Courier", size=22, weight="bold")
        label_font = tkfont.Font(family="Courier", size=11)
        entry_font = tkfont.Font(family="Courier", size=18, weight="bold")
        result_font = tkfont.Font(family="Courier", size=14, weight="bold")
        sub_font = tkfont.Font(family="Courier", size=9)
        wrapper = tk.Frame(self, bg=BG, padx=40, pady=36)
        wrapper.pack()
        tk.Label(wrapper, text="LEAP YEAR", font=title_font, fg=ACCENT, bg=BG).pack(anchor="w")
        tk.Label(wrapper, text="C H E C K E R", font=sub_font, fg=MUTED, bg=BG).pack(anchor="w")

        tk.Frame(wrapper, bg=ACCENT, height=2, width=320).pack(anchor="w", pady=(10, 24))

        tk.Label(wrapper, text="Enter a year:", font=label_font, fg=MUTED, bg=BG).pack(anchor="w")

        input_row = tk.Frame(wrapper, bg=BG)
        input_row.pack(anchor="w", pady=(6, 0))

        self.year_var = tk.StringVar()
        self.entry = tk.Entry(
            input_row, textvariable=self.year_var,
            font=entry_font, fg=FG, bg=CARD,
            insertbackground=ACCENT,
            relief="flat", width=12,
            highlightthickness=2,
            highlightbackground=BORDER,
            highlightcolor=ACCENT,
        )
        self.entry.pack(side="left", ipady=10, ipadx=6)
        self.entry.bind("<Return>", lambda e: self.check())
        self.entry.focus()

        btn = tk.Button(
            input_row, text="CHECK →",
            font=label_font, fg=BG, bg=ACCENT,
            activebackground="#00b8d4", activeforeground=BG,
            relief="flat", cursor="hand2",
            command=self.check, padx=16, pady=10,
        )
        btn.pack(side="left", padx=(10, 0))

        self.result_frame = tk.Frame(wrapper, bg=CARD,
                                     highlightthickness=1,
                                     highlightbackground=BORDER)
        self.result_frame.pack(fill="x", pady=(28, 0))
        self.result_frame.pack_forget()

        self.icon_lbl = tk.Label(self.result_frame, font=("Courier", 36), bg=CARD)
        self.icon_lbl.pack(pady=(20, 4))

        self.result_lbl = tk.Label(self.result_frame, font=result_font, bg=CARD)
        self.result_lbl.pack()

        self.detail_lbl = tk.Label(self.result_frame, font=sub_font,
                                   bg=CARD, wraplength=280, justify="center")
        self.detail_lbl.pack(pady=(4, 20))

        tk.Label(wrapper, text="÷400 → leap  |  ÷100 → common  |  ÷4 → leap  |  else → common",
                 font=sub_font, fg=MUTED, bg=BG).pack(pady=(22, 0))

    def check(self):
        raw = self.year_var.get().strip()

        if not raw:
            self._show(ERR_CLR, "⚠", "No input",
                       "Please type a year before checking.")
            return

        if not raw.lstrip("-").isdigit():
            self._show(ERR_CLR, "⚠", "Invalid input",
                       f'"{raw}" is not a valid year. Use digits only.')
            return

        year = int(raw)

        if year < 1:
            self._show(ERR_CLR, "⚠", "Out of range",
                       "Year must be 1 or later (proleptic Gregorian calendar).")
            return

        if year > 9999:
            self._show(ERR_CLR, "⚠", "Out of range",
                       "Please enter a year between 1 and 9999.")
            return

        if year % 400 == 0:
            self._show(LEAP_CLR, "✦", f"{year} is a Leap Year",
                       f"Divisible by 400 → always a leap year.")
        elif year % 100 == 0:
            self._show(NO_CLR, "○", f"{year} is a Common Year",
                       f"Divisible by 100 but not 400 → not a leap year.")
        elif year % 4 == 0:
            self._show(LEAP_CLR, "✦", f"{year} is a Leap Year",
                       f"Divisible by 4 and not a century → leap year.")
        else:
            self._show(NO_CLR, "○", f"{year} is a Common Year",
                       f"Not divisible by 4 → common year.")

    def _show(self, colour, icon, heading, detail):
        self.icon_lbl.config(text=icon, fg=colour)
        self.result_lbl.config(text=heading, fg=colour)
        self.detail_lbl.config(text=detail, fg=MUTED)
        self.result_frame.config(highlightbackground=colour)
        self.result_frame.pack(fill="x", pady=(28, 0))

if __name__ == "__main__":
    app = LeapYearApp()
    app.mainloop()