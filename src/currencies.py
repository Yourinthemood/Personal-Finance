import customtkinter as ctk
import styles

types = {
    "Afghan Afghani": 63.94,
    "Argentine Peso": 1381.42,
    "Australian Dollar": 1.46,
    "Bahraini Dinar": 0.38,
    "Botswana Pula": 13.79,
    "Brazilian Real": 5.21,
    "British Pound": 0.76,
    "Bruneian Dollar": 1.29,
    "Canadian Dollar": 1.40,
    "Chilean Peso": 929.45,
    "Chinese Yuan": 6.90,
    "Chinese Yuan Renminbi": 6.90,
    "Colombian Peso": 3659.59,
    "Czech Koruna": 21.30,
    "Danish Krone": 6.48,
    "Emirati Dirham": 3.67,
    "Euro": 0.87,
    "Hong Kong Dollar": 7.84,
    "Hungarian Forint": 334.72,
    "Icelandic Krona": 124.34,
    "Indian Rupee": 93.77,
    "Indonesian Rupiah": 16960.68,
    "Iranian Rial": 1314438.75,
    "Israeli Shekel": 3.16,
    "Japanese Yen": 158.97,
    "Kazakhstani Tenge": 477.11,
    "Kuwaiti Dinar": 0.31,
    "Laotian Kip": 21994.17,
    "Libyan Dinar": 6.40,
    "Malaysian Ringgit": 4.05,
    "Mauritian Rupee": 47.09,
    "Mexican Peso": 18.02,
    "Nepalese Rupee": 150.11,
    "New Zealand Dollar": 1.75,
    "North Korea Won": 900.01,
    "Norwegian Krone": 9.74,
    "Omani Rial": 0.38,
    "Pakistani Rupee": 278.97,
    "Philippine Peso": 60.65,
    "Polish Zloty": 3.72,
    "Qatari Riyal": 3.64,
    "Romanian New Leu": 4.42,
    "Russian Ruble": 81.33,
    "Saudi Arabian Riyal": 3.75,
    "Singapore Dollar": 1.29,
    "South African Rand": 17.06,
    "South Korean Won": 1521.05,
    "Sri Lankan Rupee": 315.32,
    "Swedish Krona": 9.51,
    "Swiss Franc": 0.80,
    "Taiwan New Dollar": 31.97,
    "Thai Baht": 32.65,
    "Trinidadian Dollar": 6.79,
    "Turkish Lira": 44.48,
    "Turkmenistani Manat": 3.49,
    "US Dollar": 1.00,
    "Uzbekistani Som": 12184.33,
    "Vietnamese Dong": 26339.98,
}

def convert():
    root = ctk.CTk()
    root.attributes("-fullscreen", True)
    if styles.selected_mode == "1440p":
        root.geometry("2560x1440+0+0")
    elif styles.selected_mode == "1080p":
        root.geometry("1920x1080+0+0")
    elif styles.selected_mode == "fullscreen":
        root.attributes("-fullscreen", True)
    ctk.set_appearance_mode("dark")

    foreground = styles.Foreground(root)
    foreground.show()

    titleframe = styles.TitleBoxText(foreground.foreground)
    titleframe.show()

    title = styles.OutputBox(titleframe.title, "Currency Changer")
    title.show()

    x = styles.RedX(foreground.foreground, root)
    x.show()

    scroll_frame = ctk.CTkScrollableFrame(
        master=foreground.foreground,
        label_text="Select Currency",
        label_font=("Arial", 18),
        width=880,
        height=680,
    )
    scroll_frame.place(x=40, y=200)

    result_box = ctk.CTkFrame(
        foreground.foreground,
        fg_color="#4a7c59",
        corner_radius=14,
        width=480,
        height=300,
    )
    result_box.place(x=980, y=200)

    result_label = ctk.CTkLabel(
        result_box,
        text="Select a currency\nand enter an amount",
        font=("Arial", 28, "bold"),
        text_color="white",
        wraplength=440,
        justify="center",
        fg_color="transparent",
    )
    result_label.place(relx=0.5, rely=0.5, anchor="center")

    amount_entry = ctk.CTkEntry(
        foreground.foreground,
        placeholder_text="Enter USD amount...",
        font=("Arial", 22),
        width=480,
        height=52,
    )
    amount_entry.place(x=980, y=540)

    selected_currency = {"value": None}
    currency_buttons = {}

    def run_conversion():
        sel = selected_currency["value"]
        raw = amount_entry.get().strip()

        if not sel and not raw:
            result_label.configure(text="Select a currency\nand enter an amount")
            return
        if not sel:
            result_label.configure(text="Select a currency")
            return
        if not raw:
            result_label.configure(text="Enter an amount below")
            return
        try:
            usd_amount = float(raw)
        except ValueError:
            result_label.configure(text="Enter a valid number")
            return

        converted = usd_amount * types[sel]
        result_label.configure(
            text=f"{usd_amount:,.2f} USD\n=\n{converted:,.2f}\n{sel}"
        )

    def on_currency_select(name):
        prev = selected_currency["value"]
        if prev and prev in currency_buttons:
            currency_buttons[prev].configure(fg_color="transparent", text_color="white")
        selected_currency["value"] = name
        currency_buttons[name].configure(fg_color="#1f6aa5", text_color="white")
        run_conversion()

    submit = styles.SumbitButton(foreground.foreground, command=run_conversion)
    submit.show(x=1600, y=850)

    amount_entry.bind("<Return>", lambda e: run_conversion())

    for i, name in enumerate(types.keys()):
        row, col = divmod(i, 5)
        btn = ctk.CTkButton(
            scroll_frame,
            text=name,
            width=160,
            height=40,
            fg_color="transparent",
            border_width=1,
            border_color="#555555",
            text_color="white",
            hover_color="#2a2d2e",
            corner_radius=8,
            font=("Arial", 15),
            command=lambda n=name: on_currency_select(n),
        )
        btn.grid(row=row, column=col, padx=5, pady=5, sticky="ew")
        currency_buttons[name] = btn

    root.mainloop()