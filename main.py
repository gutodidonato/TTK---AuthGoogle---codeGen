from tkinter import *
from tkinter import ttk

URL_PH = "http://localhost:3000/oauth/callback?code=1231231231...."
RED_PH = "http://localhost:3000/oauth/callback"
ID_PH = "123456789"
SECRET_PH = "secret_here"
NOME_PH = "Nome do Vendedor"
EMAIL_PH = "email@exemplo.com"

def envia_formulario():
    enviar = True
    
    url = campo_url.get()
    redirect_uri = redirect_url.get()
    client_id = campo_client_id.get()
    client_secret = campo_client_secret.get()
    nome = campo_name.get()
    email = campo_email.get()
    email_receiver = campo_email_receiver.get()
    
    if (url in ("", URL_PH) or
        client_id in ("", ID_PH) or
        client_secret in ("", SECRET_PH) or
        nome in ("", NOME_PH) or
        email in ("", EMAIL_PH)):
            enviar = False
            
    if enviar:
        print("URL:", url)
        print("Redirect_URI:", redirect_uri)
        print("Client_ID:", client_id)
        print("Client_Secret:", client_secret)
        print("Nome:", nome)
        print("Email:", email)
        
def add_placeholder(entry, placeholder):
    entry.insert(0, placeholder)
    entry['foreground'] = 'gray'

    def on_focus_in(event):
        if entry.get() == placeholder:
            entry.delete(0, "end")
            entry['foreground'] = 'black'

    def on_focus_out(event):
        if entry.get() == "":
            entry.insert(0, placeholder)
            entry['foreground'] = 'gray'

    entry.bind("<FocusIn>", on_focus_in)
    entry.bind("<FocusOut>", on_focus_out)

root = Tk()
frm = ttk.Frame(root, padding=[10, 20, 10, 20])
frm.grid()

ttk.Label(frm, text="URL:").grid(column=0, row=0)
campo_url = ttk.Entry(frm, width=40)
campo_url.grid(column=1, row=0, pady=5)
add_placeholder(campo_url, "http://localhost:3000/oauth/callback?code=1231231231....")

ttk.Label(frm, text="Redirect_URI:").grid(column=0, row=1)
redirect_url = ttk.Entry(frm, width=40)
redirect_url.grid(column=1, row=1, pady=5)

ttk.Label(frm, text="Client_ID:").grid(column=0, row=2)
campo_client_id = ttk.Entry(frm, width=40)
campo_client_id.grid(column=1, row=2, pady=5)
add_placeholder(campo_client_id, "123456789")

ttk.Label(frm, text="Client_Secret:").grid(column=0, row=3)
campo_client_secret = ttk.Entry(frm, width=40)
campo_client_secret.grid(column=1, row=3, pady=5)
add_placeholder(campo_client_secret, "secret_here")

ttk.Label(frm, text="Nome:").grid(column=0, row=4)
campo_name = ttk.Entry(frm, width=40)
campo_name.grid(column=1, row=4, pady=5)
add_placeholder(campo_name, "Nome do Vendedor")

ttk.Label(frm, text="Email:").grid(column=0, row=5)
campo_email = ttk.Entry(frm, width=40)
campo_email.grid(column=1, row=5, pady=5)
add_placeholder(campo_email, "email@exemplo.com")

ttk.Label(frm, text="Email:").grid(column=0, row=6)
campo_email_receiver = ttk.Entry(frm, width=40)
campo_email_receiver.grid(column=1, row=6, pady=6)

botao_submit = ttk.Button(frm, text="Enviar", command=envia_formulario)
botao_submit.grid(column=1, row=6, pady=10)

redirect_url.insert(0, RED_PH)
campo_email_receiver.insert(0, "gutodidonato@gmail.com")
root.mainloop()