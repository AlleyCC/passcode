passcode = '123456aa'
i = 3
while i > 0:
    pwd = input ('請輸入密碼:')
    if pwd == passcode:
        print ('登入成功')
        break
    else:
        i = i - 1
        print ('你還有', i ,'次機會')
        
