import smtplib
from email.message import EmailMessage


class Email:
    # Se hace una insercion del correo y contraseña
    def __init__(self, remitente, clave):
        self.remitente = remitente
        self.clave = clave

    # Redacta el correo, en el cual incluye el destino, el nombre y el carnet del estudiante
    def rendimientodef(self, destinatario, nombre, carnet):
        mensaje = f"{nombre} de carnet: {carnet} su rendimiento de asistencia de clases esta siendo muy deficiente"
        email = EmailMessage()
        email["From"] = self.remitente
        email["To"] = destinatario
        email["Subject"] = "Asistencia Ineficiente"
        email.set_content(mensaje)
        smtp = smtplib.SMTP("smtp-mail.outlook.com", port=587)
        smtp.starttls()
    # Loggea la cuenta con el usuario y contraseña
        smtp.login(self.remitente, self.clave)
    # Envia el correo
        smtp.sendmail(self.remitente, destinatario, email.as_string())
        smtp.quit()
