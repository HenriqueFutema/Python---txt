print('Salve')
count = 0
try:
    with open('testfile.txt', 'r') as r:
        print('Usuários: ')
        for line in r:
            print(line)
            count += 1
    print(count)
    print(' ---------------------- ')
    answ = input('Deseja continuar y/n/l: ')
    if answ.upper() == 'Y':
        correct = False
        while correct == False:
            mail = input(' Adicione um email: ')
            mail_count = 0
            print(' ---------------------- ')
            password = input(' Adicione sua senha: ')

            for i in mail:
                if i == '@':
                    mail_count += 1

            if len(mail) != 0 and len(password) != 0 and mail_count == 1:
                print('Concluído')
                with open('testfile.txt', 'a') as f:
                    f.write('{} - {}\n'.format(mail, password))
                continue_inp = input('Deseja continuar y/n: ')
                if continue_inp.upper() == 'Y':
                    correct = False
                else:
                    correct = True
                    print('Até logo')
            else:
                print('Digite um email e uma senha válida')
    elif answ.upper() == 'N':
        print('Até logo')
    elif answ.upper() == 'L':
        print('Login:')
        logado = False
        login_mail = input('Digite seu email: ')
        ext_mail = False
        with open('testfile.txt', 'r') as l:
            for line in l:
                only_login = line.split()
                if login_mail == only_login[0]:
                    password_user = only_login[2]
                    ext_mail = True
        if ext_mail == True:
            incorrect_password = True
            while incorrect_password == True:
                login_password = input('Senha do usuário {}: '.format(login_mail))
                if login_password == password_user:
                    print('Logado!!!!')
                    incorrect_password = False
                elif login_password == 'sair':
                    exit()
                else:
                    print('Senha incorreta!!!')
                    incorrect_password = True

    else:
        print('Tente Novamente')

    pass
except Exception as e:
    raise
