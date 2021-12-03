import re
pattern=re.compile(r'')
while True:
    password=input('PLEASE ENTER PASSWORD:')
    if (len(password)<15):
        print('Password must be greater than 15 letters long!')
    elif re.search(r'[!@#$%^&*_]',password) is None:
        print('Password must contain atleast 1 special symbol!')
    elif re.search(r'\d',password) is None:
        print('Password must contain atleast 1 digit!')
    elif re.search('[A-Z]',password) is None:
        print('Password must contain 1 capital letter!')
    elif re.match(r'[a-z A-Z 0-9 !@#$%^&*_] {15}',password):
        pattern=re.compile(r'[a-z A-Z 0-9 !@#$%^&*_] {15}',password)
        result=pattern.match(password)
    else:    
        print('YEYYYY! YOUR PASSWORD IS VALID')
   
     
