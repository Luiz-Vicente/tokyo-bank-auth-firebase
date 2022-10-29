########################
# SETUP E-MAIL
########################

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sendEmail(destiny, message):
  server = "smtp.gmail.com"
  port = 587
  username = "<YOUR_GMAIL>"
  password = "YOUR_PASSWORD"

  mail_from = "noreply@gmail.com"
  mail_to = str(destiny)
  mail_subject = "Your Tokyo bank authentication code"
  mail_body = str("Your code Authentication is: "+message)

  mensagem = MIMEMultipart()
  mensagem['From'] = mail_from
  mensagem['To'] = mail_to
  mensagem['Subject'] = mail_subject
  mensagem.attach(MIMEText(mail_body, 'plain'))

  connection = smtplib.SMTP(server, port)
  connection.starttls()
  connection.login(username,password)
  connection.send_message(mensagem)
  connection.quit()



############################
# MENU
############################

from urllib import response
import pyrebase
import random

firebaseConfig = {
    "apiKey": "<YOUR_API_KEY>",
    "authDomain": "YOUR_AUTH_DOMAIN",
    "projectId": "<YOUR_PROJECT_ID>",
    "databaseURL": "https://" + "<YOUR_PROJECT_ID>" + ".firebaseio.com",
    "storageBucket": "<YOUR_PROJECT_ID>.appspot.com",
    "messagingSenderId": "YOUR_SENDER_ID",
    "appId": "YOUR_APP_ID",
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

userName = input("Hello, what's your name?\n")
emailVerified = False
quit = False
email = ''

while quit == False:
  print(f"                 \n{userName}, select one option, please:            ")
  print("===================================================================")
  print("=                 1 - Register user                               =")
  print("=                 2 - Check email                                 =")
  print("=                 3 - Authenticate user                           =")
  print("=                 4 - Delete account                              =")
  print("=                 5 - Quit                                        =")
  print("===================================================================")

  option = input("What do you want?\n")

  if option == "1":
    email = input("\nEnter your e-mail: ")
    print("\n*******************************************************************")
    print("\n*                    SUCCESS: Registered user                     *")
    print("\n*******************************************************************")

  elif option == "2":
    if email != '':
      authCode = random.randint(1,60)

      try:
        authenticaded = False

        sendEmail(email, authCode)
        print("\n*******************************************************************")
        print("\n*             WAINTING: E-mail sent, check your inbox             *")
        print("\n*******************************************************************")

        while authenticaded == False:
          codeReceived = input("\nEnter the code received: ")

          if authCode == int(codeReceived):
            print("\n*******************************************************************")
            print("\n*             SUCCESS: E-mail successfully verified               *")
            print("\n*******************************************************************")
            emailVerified = True
            authenticaded = True
          else:
            print("\n*******************************************************************")
            print("\n*                    ATENTION: Incorrect code                     *")
            print("\n*******************************************************************")

      except Exception:
        print(Exception)
    else:
      print("\n*******************************************************************")
      print("\n*             ATENTION: You must register a user before           *")
      print("\n*******************************************************************")

  elif option == "3":
    if emailVerified == True:
      password = input(f"\n{userName}, enter your password, at least 6 characters long: ")

      try:
        user = auth.create_user_with_email_and_password(email, password)
        print("\n*******************************************************************")
        print("\n*               SUCCESS: User created successfully                *")
        print("\n*******************************************************************")
      except Exception:
        print(Exception)
    else:
      print("\n*******************************************************************")
      print("\n* ATENTION: You must register a user and verify the e-mail before *")
      print("\n*******************************************************************")

  elif option == "4":
    email = input("\nEnter your e-mail: ")
    password = input("Enter your password: ")
    user = auth.sign_in_with_email_and_password(email, password)

    try:
      auth.delete_user_account(user["idToken"])
      print("\n*******************************************************************")
      print("\n*      SUCCESS: Your account has been successfully deleted        *")
      print("\n*******************************************************************")
    except Exception:
      print(Exception)

  elif option == "5":
    quit = True

  else:
    print("\n*******************************************************************")
    print("\n*             ATENTION: You have not selected any option          *")
    print("\n*******************************************************************")
