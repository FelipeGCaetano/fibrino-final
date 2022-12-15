import smtplib
import email.message
from datetime import datetime, timezone, timedelta



def enviar_email():  

    data_e_hora_atuais = datetime.now()
    diferenca = timedelta(hours=-3)
    fuso_horario = timezone(diferenca)
    data_e_hora_sao_paulo = data_e_hora_atuais.astimezone(fuso_horario)
    data_e_hora_sao_paulo_em_texto = data_e_hora_sao_paulo.strftime("%d/%m/%Y %H:%M")

    print(data_e_hora_sao_paulo_em_texto)

    #corpo_email = """
    #<p>Parágrafo1</p>
    #<p>Parágrafo2</p>
    #"""

    corpo_email = f"API Caiu em {data_e_hora_sao_paulo_em_texto}"

    msg = email.message.Message()
    msg['Subject'] = "Queda API"
    msg['From'] = 'fibrinobot@gmail.com'
    msg['To'] = 'fibrinobot@gmail.com'
    password = 'ojmodktzctgxeshi' 
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')
