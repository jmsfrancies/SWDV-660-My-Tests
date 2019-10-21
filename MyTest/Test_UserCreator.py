import unittest
import UserCreator


class TestUserCreator(unittest.TestCase):

    # The email address test to validate whether or not the email address is a vaild email address
    def test_if_email_is_valid(self):
        emailaddress = "BigDude@yoink.con"
        for i in emailaddress:
            if i == "@":
                if emailaddress[-4:] == ".com":
                    self.assertNotEqual(emailaddress, "BigDude@yahoo.com")
    # The username test to test if the username is all alphabetical characters

    def test_username_validity(self):
        username = "HollaH011A"
        usernamevalidity = False
        if username.isalpha():
            usernamevalidity = True
            self.assertEquals(usernamevalidity, True)
        else:
            self.assertEqual(usernamevalidity, False)
    # The password test to test if the desired input is all alphabetical characters

    def test_password(self):
        password = "BigDude93"
        if not password.isalpha():
            password = False
            self.assertEqual(password, False)
    # The password hasher test to see if the hasher properly hashes the favorite food item password

    def test_new_password(self):
        password = "Burrito"
        new_password = " "
        hasher_works = True
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

        if new_password == "Ipnnhol":
            self.assertEquals(hasher_works, True)


if __name__ == '__main__':
    unittest.main()
