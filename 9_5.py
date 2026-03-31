class User:
    def __init__(self, first_name, last_name, email, phone_number, age, 
                login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.age = age
        self.login_attempts = 0
    def describe_user(self):
        print(
            f"The user is {self.first_name.title()} {self.last_name.title()}.\n\
    Email: {self.email}\n\
    Phone Number: {self.phone_number}\n\
    Age: {self.age}"
            )
    def greet_user(self):
        print(f"Welcome, {self.first_name.title()} {self.last_name.title()}.")
    def increment_login_attempts(self, login_attempts):        
        self.login_attempts += 1
        print(f"{self.first_name.title()} {self.last_name.title()}\n\
Login Attempts: {self.login_attempts}")
    def reset_login_attempts(self, login_attempts):
        self.login_attempts = 0
        print(f"{self.first_name.title()} {self.last_name.title()}\n\
Login Attempts: {self.login_attempts}")

new_user = User('john', 'smith', 'johnsmith@gmail', '828-123-4567', '30',
                'login_attempts')
new_user.increment_login_attempts('login_attempts')
new_user.increment_login_attempts('login_attempts')
new_user.increment_login_attempts('login_attempts')
new_user.increment_login_attempts('login_attempts')
new_user.reset_login_attempts('login_attempts')
new_user.increment_login_attempts('login_attempts')

