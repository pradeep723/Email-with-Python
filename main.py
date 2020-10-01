class email_sender:
    def createAGroup(self):
        global haveToIncludeComma
        group = {}
        emaill = ''
        try:
            with open('groups.json', 'r') as err:
                haveToIncludeComma = True
                err.close()
        except FileNotFoundError as e:
            with open('groups.json', 'a') as filee:
                filee.write('[')
                filee.close()
        groups = str(input('Enter the Group Name : '))
        try:
            numberOfEmails = int(
                input('Enter The Number of Emails You want to make a Group : '))
        except ValueError as e:
            print('Enter The Number in Digits')
            main()
        for i in range(0, numberOfEmails):
            email = str(input('Enter the Email Address : '))
            emaill = emaill + ' ' + email
        group[groups] = emaill
        endingBrace = False
        with open('groups.json', 'a') as f:
            if haveToIncludeComma == True:
                f.write(',')
                endingBrace = True
            json.dump(group, f)
            f.write(']')

    def sendmail(self, sender_add, reciever_add, msg, password):
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(sender_add, password)
        server.sendmail(sender_add, reciever_add, msg)
        return 'mail sent'

    def sendEmailToAGroup(self):
        memberss = ''
        try:
            with open('groups.json', 'r') as err:
                members = json.load(err)
                memberss = str(str(members).split("'")[3]).split(' ')
                err.close()
        except FileNotFoundError as e:
            option = str(
                input('Please Create a Group First.\n\nWant to Create One?? '))
            if option == 'Yes' or option == 'yes' or option == 'YES':
                email_sender.createAGroup('Creating a Group Via Error')
            else:
                main()
        email, password = email_sender.login('get Login')
        subject = str(input('Enter The Subject : '))
        message = str(input('Enter Your Message for this Mail : '))
        msg = f"""Subject : {subject}\n\n{message}"""
        for i in memberss:
            if len(i) > 0:
                what = email_sender.sendmail(
                    'Send the mail', email, i, msg, password)
                if what == 'mail sent':
                    print(f'Your mail Have been sent to {i}')

    def login(self):
        emailtemp = str(input('Enter Your Email Address : '))
        pas = str(input('Enter Your Password : '))
        if emailtemp.split('@')[1].split('.')[1] == 'com':
            email = emailtemp
        return email, pas

    def sendEmailToAnIndividual(self):
        emaill, password = email_sender.login('Get Login Here')
        emaill_address_temp = input('Enter the Recivers Email Address : ')
        if emaill_address_temp.split('@')[1].split('.')[1] == 'com':
            emaill_address = emaill_address_temp
        else:
            emaill_address = 'alexmercerr07@gmail.com'
        sub = input('Enter Your Subject for this E-Mail : ')
        msg_temp = input('Enter Your Message : ')
        msg = f"""Subject : {sub}\n\n{msg_temp}"""
        val = email_sender.sendmail(
            'Send the mail', emaill, emaill_address, msg, password)
        print(val)
        print('Mail has been sucessfully Sent')

    def view(self):
        os.system('cls')
        print('|____________________________________________________|')
        print('------------------Welcome to Email Sender------------|')
        print('|====================================================|')
        print('1. Create a Group to email Multiple Users at once')
        print('2. Send Email to An Individual Person')
        print('3. Send Mail to a Group')
        print('4. Exit/Quit')

    def header(self):
        print('|____________________________________________________|')
        print('--------------------Email Sender---------------------|')
        print('|====================================================|')


def main():
    email_sender.view('firstProcess')
    try:
        inputNumber = int(input('Enter Your Dezired Operation Number : '))
    except ValueError as e:
        print('Enter Correct Number')
        time.sleep(2)
        main()
    while inputNumber > 0 and inputNumber < 5:
        if inputNumber == 1:
            email_sender.createAGroup('Create a Group')
        elif inputNumber == 2:
            email_sender.sendEmailToAnIndividual('Email to Individual')
        elif inputNumber == 3:
            email_sender.sendEmailToAGroup('Email to a Group')
        elif inputNumber == 4:
            exit()

        inputNumber = input('Want to Send More Emails?? : ')
        if inputNumber == 'No' or inputNumber == 'no' or inputNumber == 'N' or inputNumber == 'n' or inputNumber == 'NO':
            main()
    else:
        print('Enter Correct Number')
        time.sleep(2)
        main()


if __name__ == "__main__":
    import smtplib
    import json
    import time
    import os
    os.chdir('Send Emails with Python')
    haveToIncludeComma = False
    try:
        os.remove('groups.json')
    except FileNotFoundError as e:
        pass
    main()
