class Phone:

    def __init__(self, phone_number):

        self.number = phone_number
        self.os = None

    def call(self, number):

        print(f'calling {number}')

class iPhone(Phone):

    def __init__(self, phone_number, owner):
        super().__init__(phone_number)
        self.os = 'iOS'
        self.manufacturer = 'Apple'
        self.owner = owner

    def take_photo(self):
        print('taking photo')

    def unlock(self):
        print('unlocked')

    def set_fingerprint(self,fingerprint):
        self.fingerprint = fingerprint

class Android(Phone):

    def __init__(self, phone_number):
        super().__init__(phone_number)
        self.manufacturer = ['samsung', 'pixel']




# my_phone = iPhone('099112233', owner='jack')
# my_phone.call('92919293478')
# my_phone.take_photo()
# print(my_phone.manufacturer)
# print()
# your_phone = Android('09872344')
# print(your_phone.manufacturer)
# your_phone.call(my_phone.number)


my_iphone = iPhone(151)
my_iphone.unlock()
my_iphone.set_fingerprint("Jory's Fingerprint")
my_iphone.unlock()
my_iphone.unlock("Jory's Fingerprint")

# And we can call the Phone methods:
my_iphone.call(515)
my_iphone.text(51121, "Hi!")
