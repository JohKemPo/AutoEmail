from imap_tools import MailBox, AND
from datetime import date

#INFORMAÇÕES A SEREM SUBSTITUIDAS--------------------------

user = "joaovitormoraesjp@gmail.com"
password = "8GVRUA7T"
remet = "joaovitormoraesjp@gmail.com"
name_arq = "PassWrd"

#----------------------------------------------------------

box = MailBox("imap.gmail.com").login(user, password)

email_list = box.fetch(AND(from_= remet, date = date.today()))
for email in email_list:
    if len(email.attachments) > 0:
        for anexo in email.attachments:
            if name_arq in anexo.filename:
                info = anexo.payload
                with open("PassWrd_{}".format(date.today()),"wb") as senhas:
                    senhas.write(info)
                    print('Succesfully Downloaded')