import customtkinter as ctk
import tkinter
import mysql.connector
import re
import smtplib
from email.message import EmailMessage
import random

def otp_generator():
    otp=""
    for x in range(6):
        otp+=str(random.randint(0,9))
    return otp

def send_mail(email,subject, message):
    otp=otp_generator()
    server=smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    sender='nayranewar33@gmail.com'
    server.login(sender,'layp lbnr zlya yqac')
    receiver=email

    msg=EmailMessage()
    msg['Subject']=subject
    msg['From']=sender
    msg['To']=receiver
    msg.set_content(message)

    server.send_message(msg)

def connect_to_server():
     cnx=mysql.connector.connect(host='localhost', user='root', password='solo3111', database='data')
     cursor=cnx.cursor()
     return cnx, cursor

def close_server(cnx):
     cnx.close()

def insert_reg_data(dict):
     cnx, cursor=connect_to_server()
     cursor.execute("insert into registration"
                    "(name, email, dob, address,"
                    " phone_no, security_question, answer, user_id, password)"
                     " values(%(name)s,%(email)s, %(dob)s,"
                      " %(address)s, %(phone_no)s, %(security_question)s, %(answer)s, %(user_id)s, %(password)s)", dict)
     cnx.commit()
     close_server(cnx)

def updating_password(dict):
     cnx, cursor=connect_to_server()
     cursor.execute("update registration set password=%(password)s where email=%(email)s", dict)
     cnx.commit()
     close_server(cnx)



def show_password(p_entry, value):
    if value.get():
        p_entry.configure(show="")

    else:
        p_entry.configure(show="*")   

def check_credential(user, password):
    cnx, cursor = connect_to_server()
    try:
        cursor.execute("SELECT * FROM registration WHERE user_id=%s AND password= %s", (user, password))
        result = cursor.fetchone()

        return result

    finally:
        # Close the database connection
        close_server(cnx)


def back2main(frame):
        frame.master.Main() 


def is_valid_email( email):
    # Regular expression pattern for a valid email address
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    # Use the re.match() function to check if the email matches the pattern
    if re.match(pattern, email):
        
        return True
    else:
        return False



def email_exists(email):
    cnx, cursor = connect_to_server()
    try:
        cursor.execute("SELECT * FROM registration WHERE email like %s", (email,))
        user = cursor.fetchone()

        return user

    finally:
        # Close the database connection
        close_server(cnx)

def user_exists(user):
    cnx, cursor = connect_to_server()
    try:
        cursor.execute("SELECT * FROM registration WHERE user_id like %s", (user,))
        result = cursor.fetchone()
        return result

    finally:
        # Close the database connection
        close_server(cnx)

def is_valid_chars(input):
    # Regular expression pattern to allow only English letters and standard characters
    pattern = re.compile(r'^[a-zA-Z0-9_\-]+$')
    return pattern.match(input) 

def check_phoneno(phone_no):
    # Regular expression pattern to allow exactly 10 digits (0-9)
    pattern = re.compile(r'^[0-9]{10}$')
    return pattern.match(phone_no) 