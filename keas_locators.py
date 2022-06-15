import datetime

from faker import Faker

fake = Faker(locale='en_CA')
moodle_url = 'http://52.39.5.126/'
moodle_login_url = 'http://52.39.5.126/login/index.php'
moodle_users_main_page = 'http://52.39.5.126/admin/user.php'
moodle_username = 'xiaodongwang'
moodle_password = 'Wxd2022wxd!'
moodle_dashboard_url = 'http://52.39.5.126/my/'
new_username = f'{fake.user_name()}{fake.pyint(111,999)}'
new_password = fake.password()[:12]
first_name = fake.first_name()
last_name = fake.last_name()
full_name = f'{first_name} {last_name}'
email = fake.email()
moodle_net_profile = f'https://moodle.net/{new_username}'
city = fake.city()
# description = fake.sentence(nb_words=100)
description = f'User added by {moodle_username} via Python Selenium Automated script on {datetime.datetime.now()}'
pic_desc = fake.user_name()
phonetic_name = fake.user_name()
list_of_interests = [new_username, new_password, full_name, email, city]
web_page_url = fake.url()
icq_number = fake.pyint(111111, 999999)
institution = fake.lexify(text='????????????????????')
department = fake.lexify(text='???????')
phone = fake.phone_number()
mobile_phone = fake.phone_number()
#address = fake.address()
address = fake.address().replace("\n", "")