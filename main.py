from tkinter import *
from tkinter import ttk, messagebox
from res import enviar_mensagem_simples, envio_de_credencial_smtp, gerar_url_code

URL_PH = "http://localhost:3000/oauth/callback?code=1231231231...."
RED_PH = "http://localhost:3000/oauth/callback"
ID_PH = "123456789"
SECRET_PH = "secret_here"
NOME_PH = "Nome do Vendedor"
EMAIL_PH = "email@exemplo.com"

ex_url = "http://localhost:3000/oauth/callback?code=4/0Ab32j93rVbMG-ceifpuh-APBgvcNBnMfVeCk37HioubTSW_2PQ_MJG2OgO_0KyXCuJRX4w&scope=https://www.googleapis.com/auth/calendar"


def tratar_url(url):
    if "code=" in url:
        partes = url.split("code=")
        codigo = partes[1].split("&")[0] if "&" in partes[1] else partes[1]
        return codigo
    return None

def tratar_url_code():
    client_id_code_new = client_id_code.get()
    client_secret_code_new = client_secret_code.get()
    redirect_uri_code_new = redirect_uri_code.get()
    url = gerar_url_code(client_id_code_new, redirect_uri_code_new)
    url_resultado_code.delete(0, END)
    url_resultado_code.insert(0, url)

def envia_formulario():
    enviar = True
    
    url = campo_url.get()
    redirect_uri = redirect_url.get()
    client_id = campo_client_id.get()
    client_secret = campo_client_secret.get()
    nome = campo_name.get()
    email = campo_email.get()
    email_receiver = campo_email_receiver.get()
    
    #=============================
    #====== Tratamentos ==========
    #=============================
    
    url = tratar_url(url)
    
    
    if (url in ("", URL_PH) or
        client_id in ("", ID_PH) or
        client_secret in ("", SECRET_PH) or
        nome in ("", NOME_PH) or
        email in ("", EMAIL_PH)):
            enviar = False
            
    if enviar:
        #enviar_mensagem_simples()
        envio = envio_de_credencial_smtp(client_id, client_secret, url, redirect_uri, nome, email, email_receiver)
    if envio:
        print("Credenciais enviadas com sucesso!")
        messagebox.showinfo("Sucesso", "Credenciais enviadas com sucesso!")
    else:
        print("Falha ao enviar as credenciais.")
        messagebox.showerror("Erro", "Falha ao enviar as credenciais.")

        
        
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
root.title("Patria OAuth2 Credential Sender")
frm = ttk.Frame(root, padding=[10, 20, 10, 20])
frm.grid()


ttk.Label(frm, text="Geração da URL de Code", font=("Arial", 16)).grid(column=0, row=0, pady=10)

ttk.Label(frm, text="Client_Id").grid(column=0, row=1, pady=5)
client_id_code = ttk.Entry(frm, width=100)
client_id_code.grid(column=1, row=1, pady=5)

ttk.Label(frm, text="Client_Secret").grid(column=0, row=2, pady=5)
client_secret_code = ttk.Entry(frm, width=100)
client_secret_code.grid(column=1, row=2, pady=5)

ttk.Label(frm, text="Redirect_uri").grid(column=0, row=3, pady=5)
redirect_uri_code = ttk.Entry(frm, width=100)
redirect_uri_code.grid(column=1, row=3, pady=5)

ttk.Button(frm, text="Gerar URL de Code", command=tratar_url_code).grid(column=0, row=4, columnspan=2, pady=10)

ttk.Label(frm, text="URL Gerada:").grid(column=0, row=5, pady=5)
url_resultado_code = ttk.Entry(frm, width=100, foreground="blue")
url_resultado_code.grid(column=1, row=5, pady=5)

#=============================
#====== Segunda Parte ==========
#=============================

ttk.Label(frm, text="Envio de Credenciais OAuth2 via Email", font=("Arial", 16)).grid(column=0, row=6, pady=10)

ttk.Label(frm, text="URL:").grid(column=0, row=7)
campo_url = ttk.Entry(frm, width=100)
campo_url.grid(column=1, row=7, pady=5)
add_placeholder(campo_url, "http://localhost:3000/oauth/callback?code=1231231231....")

ttk.Label(frm, text="Redirect_URI:").grid(column=0, row=8)
redirect_url = ttk.Entry(frm, width=40)
redirect_url.grid(column=1, row=8, pady=5)

ttk.Label(frm, text="Client_ID:").grid(column=0, row=9)
campo_client_id = ttk.Entry(frm, width=40)
campo_client_id.grid(column=1, row=9, pady=5)
add_placeholder(campo_client_id, "123456789")

ttk.Label(frm, text="Client_Secret:").grid(column=0, row=10)
campo_client_secret = ttk.Entry(frm, width=40)
campo_client_secret.grid(column=1, row=10, pady=5)
add_placeholder(campo_client_secret, "secret_here")

ttk.Label(frm, text="Nome:").grid(column=0, row=11)
campo_name = ttk.Entry(frm, width=40)
campo_name.grid(column=1, row=11, pady=5)
add_placeholder(campo_name, "Nome do Vendedor")

ttk.Label(frm, text="Email do Vendor:").grid(column=0, row=12)
campo_email = ttk.Entry(frm, width=40)
campo_email.grid(column=1, row=12, pady=5)
add_placeholder(campo_email, "email@exemplo.com")

ttk.Label(frm, text="Email Receber Credenciais:").grid(column=0, row=13)
campo_email_receiver = ttk.Entry(frm, width=40)
campo_email_receiver.grid(column=1, row=13, pady=6)

botao_submit = ttk.Button(frm, text="Enviar", command=envia_formulario)
botao_submit.grid(column=1, row=14, pady=20)

redirect_url.insert(0, RED_PH)
redirect_uri_code.insert(0, RED_PH)
campo_email_receiver.insert(0, "gutodidonato@gmail.com")
root.mainloop()