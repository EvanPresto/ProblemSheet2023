def read_account(account):
    l_account = []
    if len(str(account)) < 10:
        print('Not enough digits')
    elif len(str(account)) > 10:
        print('Too many digits')
    else:
        for i in account:
         l_account.i
        print('Account number is XXXXXX' + l_account[5:])

print(read_account(1234567890))

