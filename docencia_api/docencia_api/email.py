import smtplib
from email.message import EmailMessage
from docencia_api.docencia_api.usuario import Usuario


class Email:
    # Se hace una insercion del correo y contraseña
    def __init__(self, remitente: str, clave: str):
        self.remitente = remitente
        self.clave = clave

    # Recorre listado de clientes para enviar correo
    def listado(self, lista: Usuario):
        for i in lista:
            self.rendimientodef(lista[i].destino, lista[i].nombre, lista[i].carnet)

    # Redacta el correo, en el cual incluye el destino, el nombre y el carnet del estudiante
    def rendimientodef(self, destinatario: str, nombre: str, carnet: str):
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
