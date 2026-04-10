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

#define convert_currency function
def convert(mode):
    root = ctk.CTk()
    if mode == "1440p":
        root.geometry("2560x1440+0+0")
    elif mode == "1080p":
        root.geometry("1920x1080+0+0")
    elif mode == "fullscreen":
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

#   ask user for amount in US Dollars
#   store as usd_amount
    amount = styles.TextBox(foreground.foreground, "Amount: ")
    amount.show(700, 1200)

#   ask user for target currency type
#   store as target_type

#   if target_type not in types
#       display "Invalid currency type"
#       stop

#   converted_amount = usd_amount * types[target_type]

#   display converted_amount and target_type

#   when finished using converted_amount
#       usd_amount = converted_amount / types[target_type]

#   save usd_amount to file