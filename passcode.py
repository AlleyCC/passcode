while True:
    passcode = input ('請輸入密碼:')
    if passcode != 'a123456':
        print ('你還有2次機會!')
        passcode = input ('請輸入密碼:')
    if passcode != 'a123456':
        print ('你還有1次機會!')
        passcode = input ('請輸入密碼:')
    if passcode != 'a123456':
        print ('登入失敗')
        raise SystemExit
    else: 
        break
print ('登入成功')
