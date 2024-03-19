import tkinter as tk

def calculate():
    secret_data = float(secret_data_entry.get())
    multiplicator_sd = 0.26
    suma_finala_sd = secret_data * multiplicator_sd
    suma_finala_sd_label.config(text="{:.3f}".format(suma_finala_sd) + " (" + str("x") + str(multiplicator_sd) + ")")

    data_service_group = float(data_service_group_entry.get())
    multiplicator_dsg = 0.26
    suma_finala_dsg = data_service_group * multiplicator_dsg
    suma_finala_dsg_label.config(text="{:.3f}".format(suma_finala_dsg) + " (" + str("x") + str(multiplicator_dsg) + ")")

    rbc = float(rbc_entry.get())
    multiplicator_rbc = 0.35
    suma_finala_rbc = rbc * multiplicator_rbc
    suma_finala_rbc_label.config(text="{:.3f}".format(suma_finala_rbc) + " (" + str("x") + str(multiplicator_rbc) + ")")

    conectari_gprs = int(conectari_gprs_entry.get())
    multiplicator_gprs = 91
    suma_finala_conectari_gprs = conectari_gprs * multiplicator_gprs
    suma_finala_conectari_gprs_label.config(text=str(suma_finala_conectari_gprs) + " (" + str("x") + str(multiplicator_gprs) +  ")")

    conectari_lan = int(conectari_lan_entry.get())
    multiplicator_lan = 116
    suma_finala_conectari_lan = conectari_lan * multiplicator_lan
    suma_finala_conectari_lan_label.config(text=str(suma_finala_conectari_lan) + " (" + str("x") + str(multiplicator_lan) + ")")

    reconectari_gprs = int(reconectari_gprs_entry.get())
    multiplicator_reconectari_gprs = 50
    suma_finala_reconectari_gprs = reconectari_gprs * multiplicator_reconectari_gprs
    suma_finala_reconectari_gprs_label.config(text=str(suma_finala_reconectari_gprs) + " (" + str("x") + str(multiplicator_reconectari_gprs) + ")")

    total_calculat = suma_finala_sd + suma_finala_dsg + suma_finala_rbc + suma_finala_conectari_gprs + suma_finala_conectari_lan + suma_finala_reconectari_gprs
    total_calculat_label.config(text=str(total_calculat))

# Crearea ferestrei principale
root = tk.Tk()
root.title("Calculator")

# Ajustarea dimensiunilor ferestrei
root.geometry("1000x600")  # Lățime x Înălțime

# Etichetele pentru fiecare câmp de intrare și rezultat
tk.Label(root, text="Secret Data:", font=("Helvetica", 20)).grid(row=0, column=0, pady=10, padx=10, sticky="e")
tk.Label(root, text="DSG:", font=("Helvetica", 20)).grid(row=1, column=0, pady=10, padx=10, sticky="e")
tk.Label(root, text="RBC:", font=("Helvetica", 20)).grid(row=2, column=0, pady=10, padx=10, sticky="e")
tk.Label(root, text="Conectări GPRS:", font=("Helvetica", 20)).grid(row=3, column=0, pady=10, padx=10, sticky="e")
tk.Label(root, text="Conectări LAN:", font=("Helvetica", 20)).grid(row=4, column=0, pady=10, padx=10, sticky="e")
tk.Label(root, text="Reconectări GPRS:", font=("Helvetica", 20)).grid(row=5, column=0, pady=10, padx=10, sticky="e")
tk.Label(root, text="Total calculat:", font=("Helvetica", 20)).grid(row=6, column=0, pady=10, padx=10, sticky="e")

# Câmpurile de intrare pentru fiecare valoare
secret_data_entry = tk.Entry(root, font=("Helvetica", 20))
secret_data_entry.grid(row=0, column=1, pady=10, padx=10)
data_service_group_entry = tk.Entry(root, font=("Helvetica", 20))
data_service_group_entry.grid(row=1, column=1, pady=10, padx=10)
rbc_entry = tk.Entry(root, font=("Helvetica", 20))
rbc_entry.grid(row=2, column=1, pady=10, padx=10)
conectari_gprs_entry = tk.Entry(root, font=("Helvetica", 20))
conectari_gprs_entry.grid(row=3, column=1, pady=10, padx=10)
conectari_lan_entry = tk.Entry(root, font=("Helvetica", 20))
conectari_lan_entry.grid(row=4, column=1, pady=10, padx=10)
reconectari_gprs_entry = tk.Entry(root, font=("Helvetica", 20))
reconectari_gprs_entry.grid(row=5, column=1, pady=10, padx=10)

# Etichetele pentru afișarea rezultatelor
suma_finala_sd_label = tk.Label(root, text="", font=("Helvetica", 20))
suma_finala_sd_label.grid(row=0, column=2, pady=10, padx=10)
suma_finala_dsg_label = tk.Label(root, text="", font=("Helvetica", 20))
suma_finala_dsg_label.grid(row=1, column=2, pady=10, padx=10)
suma_finala_rbc_label = tk.Label(root, text="", font=("Helvetica", 20))
suma_finala_rbc_label.grid(row=2, column=2, pady=10, padx=10)
suma_finala_conectari_gprs_label = tk.Label(root, text="", font=("Helvetica", 20))
suma_finala_conectari_gprs_label.grid(row=3, column=2, pady=10, padx=10)
suma_finala_conectari_lan_label = tk.Label(root, text="", font=("Helvetica", 20))
suma_finala_conectari_lan_label.grid(row=4, column=2, pady=10, padx=10)
suma_finala_reconectari_gprs_label = tk.Label(root, text="", font=("Helvetica", 20))
suma_finala_reconectari_gprs_label.grid(row=5, column=2, pady=10, padx=10)
total_calculat_label = tk.Label(root, text="", font=("Helvetica", 20))
total_calculat_label.grid(row=6, column=1, pady=10, padx=10)

# Butonul de calcul
calculate_button = tk.Button(root, text="Calculează", font=("Helvetica", 20), command=calculate)
calculate_button.grid(row=7, columnspan=2, pady=10, padx=10)

# Rularea buclei principale a aplicației
root.mainloop()
