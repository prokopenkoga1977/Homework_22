# Registration ( lvl - 1 )

# 1) Create an empty array [] (Don’t forget about names for variables)

# 2) Create an empty string and then save it in variable “register_data”

# 3) Get login and password from user and then => save data into “register_data” . 

# 4) if login length less than 5 characters print an Error

# 5) if password contains more than 10 symbols throw an Error 

# USE : split , slice , create other variables .
# Do everything that you want to , but remember that all data above must exist .


# Registration:

register_data=[]
user_name = input("Enter your name: ")
user_email = input("Enter your email: ")
user_phone = input("Enter your phone: ")
user_password = input("Enter your password: ")
is_valid = None
is_running = True
alphabet_kiril="А, Б ,В, Г, Д, Е, Ё, Ж, З, И, Й, К, Л, М, Н, О, П, Р, С, Т, У, Ф, Х, Ц, Ч, Ш, Щ, Ъ, Ы, Ь, Э, Ю, Я, а, б, в, г, д, е, ё, ж,з,и, й, к, л, м, н, о, п, р, с, т, у, ф, х, ц, ч, ш, щ, ъ, ь, э, ю, я"

print("--------------------------------------------------------------------")   
def name_lang_validation ():
    global user_name
    if alphabet_kiril in user_name:   
        return print("Error! Enter the name in latin!") 
    else:
        return True
def name_len_validation ():
    if len(user_name)<5:
        return print("Error! Enter the name more than 5 characters!")
    else:
        return True

def email_lang_validation ():
    global user_email

    if alphabet_kiril in user_email:
        return print("Error! Email entered incorrectly!") 
    else:
        return True
    
def email_symb_validation ():
    if "@" in user_email:
        return True
    else:
        return print("Error! @ character missing!")

def phone_validation():
    global user_phone
    if len(user_phone)==13:
        return True
    else:
        return print("Enter the phone in the format +38(_ _ _)-_ _ _-_ _-_ _")

def password_validation():
    global user_password
    if len(user_password)<7:
        return print("Error ! Enter the password more than 7 symbols!")
    else:
        return True
   
def registration (user_name, user_email, user_phone, user_password, register_data):
    global is_valid
    global is_running
    
    is_valid_name_lang=name_lang_validation()
    is_valid_name_len=name_len_validation()
    is_valid_email_lang=email_lang_validation()
    is_valid_email_symb=email_symb_validation()
    is_valid_phone=phone_validation()
    is_valid_password=password_validation()
    
    if is_valid_name_lang and is_valid_name_len and is_valid_email_lang and is_valid_email_symb and is_valid_phone and is_valid_password:
        is_valid = True
        while is_running:
             register_data.append({
                 "Name" : user_name,
                 "Email" : user_email,
                 "Phone" : user_phone,
                "Password": user_password
            })
             break
    else:
        is_valid = False
 
registration(user_name, user_email, user_phone, user_password, register_data)

print("--------------------------------------------------------------------")   
print(register_data) 

# Authorization:

data_base=[{
     "Name" : "Mike",
     "Email" : "mike@gmail.com",
     "Phone" : "+380501234567",
     "Password": "12345678"
 },
 {
     "Name" : "Bob",
     "Email" : "bob@gmail.com",
     "Phone" : "+380971234567",
     "Password": "asdfghjk"
 },
 {
     "Name" : "Jon",
     "Email" : "jon@gmail.com",
     "Phone" : "+380661234567",
     "Password": "zxcvbnmas"
 },
 {
     "Name" : "Tom",
     "Email" : "tom@gmail.com",
     "Phone" : "+380681234567",
     "Password": "qwertyui"
 }]


user_email = input("Enter your email: ")
user_password = input("Enter your password: ")

for user in data_base :
    for value in user.values() :
        if value == user_email: 
            print(f"Hello {user['Name']}!")
                    
            if user_password == user['Password']:
                print("Welcome!")
            else:
                print("Password is incorrect!")
