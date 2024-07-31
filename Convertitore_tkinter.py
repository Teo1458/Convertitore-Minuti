import tkinter as tk

#creazione finestra di dialogo
window = tk.Tk()
window.geometry("300x300")
window.title("CONVERTITORE MINUTI ver2.0")
window.configure(background="white")
window.resizable(True, True)

#funzione principale
def convert():
        global minuti
        global somma
        minuti=entry.get()
        minuti = float (minuti)
        ore = minuti // 60
        resto = (minuti % 60)
        #opzione con risultato unico somma = float(ore +resto)
        label1 = tk.Label(text= '%0.0f minuti equivalgono a:\n %0.0f ore e %0.0f minuti' 
                          %(minuti,ore,resto),borderwidth=2, relief="groove",bg='light goldenrod',font=('consolas',12))
        label1.pack() 
              
label = tk.Label(text="Inserisci i minuti",borderwidth=2, relief="groove")
label.pack()

entry=tk.Entry (fg="black", bg="white",width=10,justify='center',bd=5)
entry.pack()

first_button = tk.Button(text="Converti",bd=5, command=convert)
first_button.pack()

if __name__ == "__main__":
    window.mainloop()