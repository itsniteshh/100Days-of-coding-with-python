class user:

    def __init__(self, first_name, last_name, age, city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        self.login_attempt = 0

    def describe_user(self):
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Age: {self.age}")
        print(f"City: {self.city}")

    def greet_user(self):
        print(f"Welcome bak {self.first_name}! How may I help you today?")

    def login(self):
        self.login_attempt =  0

    def increment_login_attempts(self, number):
        if number >= self.login_attempt:
            self.login_attempt += 1
            print(f"The new login attempt is {self.login_attempt}\n")
        else:
            pass

    def reset_login_attempts(self):
        self.login_attempt = 0
        print(f"Login attempt reseted to {self.login_attempt}")


user_profile1= user("Nitesh", "Jha", "25", "Mumbai")
user_profile2= user("Arjun", "jadhav", "25", "Pune")
user_profile3= user("Nishit", "Gawande", "24", "Dadar")


user_profile1.describe_user()
user_profile1.greet_user()
user_profile1.login()
user_profile1.increment_login_attempts(1)

user_profile2.describe_user()
user_profile2.greet_user()
user_profile2.increment_login_attempts(1)

user_profile3.describe_user()
user_profile3.greet_user()
user_profile3.increment_login_attempts(1 )
