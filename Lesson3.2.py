def user_data(name, s_name, year_of_birth, City_of_residence, email, phone_num):
    result = f'{name.title()}, {s_name.title()}, {year_of_birth}, {City_of_residence.title()}, {email}, {phone_num}'
    print(result)


user_data(name = input('Имя:'), s_name = input("Фамилия:"),
          year_of_birth = input("Год рождения:"),
          City_of_residence = input("Город проживания:"),
          email= input("Email:"), phone_num= input("Номер телефона:"))
