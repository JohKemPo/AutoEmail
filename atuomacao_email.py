from imap_tools import MailBox, AND
#DOCUMANTATION - https://pypi.org/project/imap-tools/

#Login
user = "joaovitormoraesjp@gmail.com"
password = "8GVRUA7T"

box = MailBox("imap.gmail.com").login(user, password)# Server imap gmail
#Server List imap - https://www.systoolsgroup.com/imap/

email_list = box.fetch(AND(from_= user))#List emails
for email in email_list:
    if len(email.attachments) > 0:
        for anexo in email.attachments:
            if "PassWrd" in anexo.filename:
                info = anexo.payload
                with open("PassWrd","wb") as senhas:
                    senhas.write(info)
                    print('Succesfully Downloaded')