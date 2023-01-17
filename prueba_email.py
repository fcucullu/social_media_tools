# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 22:42:57 2022

@author: eugef
"""


from email.message import EmailMessage
import smtplib
remitente = "eugefervi@gmail.com"
destinatario = "luisdeharo0108@gmail.com"
mensaje = "¡Hola, mundo!"
email = EmailMessage()
email["From"] = remitente
email["To"] = destinatario
email["Subject"] = "Correo de prueba"
email.set_content(mensaje)
smtp = smtplib.SMTP_SSL("smtp.gmail.com")
smtp.login(remitente, "uovnpuvjsvfvjpzr")
smtp.sendmail(remitente, destinatario, email.as_string())
smtp.quit()