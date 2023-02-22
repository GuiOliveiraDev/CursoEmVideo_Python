from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

msg = MIMEMultipart()
texto = 'Estou enviando um email com Python'

senha = 'SUA SENHA'
msg['From'] = 'SEU EMAIL'
msg['To'] = 'E-MAIL DESTINO'
msg['Subject'] = 'ASSUNTO'

msg.attach(MIMEText(texto, 'plain'))

Server = smtplib.SMTP('smtp.gamil.com: 587')
Server.starttls()

Server.login(msg['From'], senha)
Server.sendmail(msg['From'], msg['To'], msg.as_string())

Server.quit()

print('Mensagem enviada com sucesso')