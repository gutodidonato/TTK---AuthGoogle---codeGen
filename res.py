import requests
import smtplib
from email.message import EmailMessage
import dotenv

dotenv.load_dotenv()

smtp_senha = "gcyg wkud iciw lhuk"
smtp_email = "gutodidonato@gmail.com"
 
def post_data(url, data):
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error posting data: {e}")
        return None
    
def google_auth(code, client_id, client_secret, redirect_uri):
    token_url = "https://oauth2.googleapis.com/token"
    data = {
        'code': code,
        'client_id': client_id,
        'client_secret': client_secret,
        'redirect_uri': redirect_uri,
        'grant_type': 'authorization_code'
    }
    try:
        response = post_data(token_url, data)
        if response and 'access_token' in response:
            return response
    except Exception as e:
        print(f"Error during Google authentication: {e}")
    return None

def envio_de_credencial_smtp(client_id, client_secret, code, redirect_uri, nome, email, destinatario):
    try:
        response = google_auth(code, client_id, client_secret, redirect_uri)
        access_token = response.get('access_token') if response else None
        refresh_token = response.get('refresh_token') if response else None
        enviar_mensagem(
            mensagem_texto=f"Access Token: {access_token}\nRefresh Token: {refresh_token} \nClient ID: {client_id}\nClient Secret: {client_secret} \n Redirect URI: {redirect_uri} \n Nome: {nome}\n Email: {email}",
            sender=smtp_email,
            assunto=f"Credenciais OAuth2 - {nome} - {email}",
            senha_pass_sv=smtp_senha,
            destinatario= destinatario
        )
        
    except Exception as e:
        print(f"Error in envio_de_credencial: {e}")
        return None



def enviar_mensagem(mensagem_texto : str,
                    sender : str,
                    assunto : str,
                    senha_pass_sv : str,
                    destinatario : str
                    ):
    '''
    mensagem_texto - texto; sender - remetente; assunto - assunto;
    senha_pass_sv - senha; dest - destinatários(lista)
    '''
    print("Iniciando Envio..")
    print(f"Destinatario: {destinatario}")
    mensagem = EmailMessage()
    mensagem.set_content(mensagem_texto)
    mensagem['Subject'] = assunto
    mensagem['From'] = sender
    mensagem['To'] = destinatario


    s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    s.login(sender, senha_pass_sv)
    s.send_message(mensagem)

    s.quit()
    
def enviar_mensagem_simples():
    enviar_mensagem("teste", smtp_email, "teste", smtp_senha, smtp_email)
    
    
def gerar_url_code(client_id, redirect_uri):
    base_url = "https://accounts.google.com/o/oauth2/v2/auth"
    scope = "https://www.googleapis.com/auth/calendar"
    response_type = "code"
    
    url = (f"{base_url}?client_id={client_id}"
           f"&redirect_uri={redirect_uri}"
           f"&response_type={response_type}"
           f"&scope={scope}"
           f"&access_type=offline"
           f"&prompt=consent")
    return url