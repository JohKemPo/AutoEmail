from imap_tools import MailBox, AND
from datetime import date

#ARQUIVOS COM AS INFORMAÇÕES-------------------------------
with open('infos.txt', 'r') as arquivo:
    informacoes = arquivo.readlines()
#print(informacoes,'\n')

fatiado = []
for linha in informacoes:
    fatiado.append(linha.split('"'))
#print(fatiado)

#INFORMAÇÕES A SEREM SUBSTITUIDAS--------------------------

user = fatiado[0][1]
password = fatiado[1][1]
remet = fatiado[2][1]
name_arq = fatiado[3][1]
#print(user, password, remet, name_arq)

box = MailBox("imap.gmail.com").login(user, password)

email_list = box.fetch(AND(from_= remet))#, date = date.today()

#AUTENTICAÇÃO DATA_ATUAL-----------------------------------
aut_data = (fatiado[4][1]).upper()
#print(aut_data)


#DOWNLOAD--------------------------------------------------
if aut_data == 'SIM':
    for email in email_list:
        if len(email.attachments) > 0:
            for anexo in email.attachments:
                if name_arq in anexo.filename:
                    info = anexo.payload
                    with open("PassWrd_{}".format(date.today()),"wb") as senhas:
                        senhas.write(info)
                        print('Succesfully Downloaded')
elif aut_data == 'NAO' or aut_data == 'NÃO':
    for email in email_list:
        data = str(email.date)
        data = data[:10]
        if len(email.attachments) > 0:
            for anexo in email.attachments:
                if name_arq in anexo.filename:
                    info = anexo.payload
                    with open("PassWrd_{}".format(data),"wb") as senhas:
                        senhas.write(info)
                        print('Succesfully Downloaded')
else:
    for email in email_list:
        data = str(email.date)
        data = data[:10]
        #print(data == aut_data)
        if data == aut_data:
            if len(email.attachments) > 0:
                for anexo in email.attachments:
                    if name_arq in anexo.filename:
                        info = anexo.payload

                        with open("{}_{}".format(name_arq,data), "wb") as senhas:
                            senhas.write(info)
                            print(anexo.filename)
                            print('Succesfully Downloaded')

