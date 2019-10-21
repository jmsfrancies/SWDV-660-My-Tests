def EmailChecker(emailaddress):
    for i in emailaddress:
        if i == "@":
            if emailaddress[-4:] == ".com" or emailaddress[-4:] == ".org":
                print("Personal or Company email address: {0}".format(
                    emailaddress))
            elif emailaddress[-4:] == ".edu":
                print("School email address: {0}".format(emailaddress))
            else:
                print("invalid email address")


def PasswordHasher(username, password):
    new_password = " "
    hash_list = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQURSTUVWXYZ"
    for i in password:
        i = int((ord(i) / 3)*2)
        if i > len(hash_list):
            i = i - len(hash_list)
            j = hash_list[i]
            new_password = new_password + j
        else:
            j = hash_list[i]
            new_password = new_password + j

    print("Your Username that you had chosen: {0}\nYour Newly hashed password is: {1}".format(
        username, new_password))


def main():
    emailaddress = "jmsfrancies@yahoo.com"
    username = "jmsfrancies"
    password = "burrito"
    EmailChecker(emailaddress)
    PasswordHasher(username, password)


main()
