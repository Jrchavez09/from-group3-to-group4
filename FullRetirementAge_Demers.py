month_dict = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July",
              8: "August", 9: "September", 10: "October", 11: "November", 12: "December"}

def calculate_retirement_age(year):
    if year < 1938:
        age = 65
        months = 0
    elif year == 1938:
        age = 65
        months = 2
    elif year == 1939:
        age = 65
        months = 4
    elif year == 1940:
        age = 65
        months = 6
    elif year == 1941:
        age = 65
        months = 8
    elif year == 1942:
        age = 65
        months = 10
    elif 1943 <= year <= 1954:
        age = 66
        months = 0
    elif year == 1955:
        age = 66
        months = 2
    elif year == 1956:
        age = 66
        months = 4
    elif year == 1957:
        age = 66
        months = 6
    elif year == 1958:
        age = 66
        months = 8
    elif year == 1959:
        age = 66
        months = 10
    else:
        age = 67
        months = 0
    return age, months

def calculate_retirement_date(month, year, age, months):
    retire_year = year + age
    retire_month = month + months
    if retire_month > 12:
        retire_month = retire_month - 12
        retire_year = retire_year + 1

    return retire_month, retire_year

def main():
    print("Social Security Full Retirement Age Calculator")
    while True:
        try:
            birth_year = int(input("Enter the year oF birth or to exit"))
        except ValueError:
            break
        birth_month = int(input("Enter the month of birth"))
        age, months = calculate_retirement_age(birth_year)
        retire_month, retire_year = calculate_retirement_date(birth_month,
                                                              birth_year,
                                                              age, months)
        print(f"your full retirement age is {age} and {months} months")
        print(f"This is be in  {month_dict[retire_month]} of {retire_year}")

if __name__ == '__main__':
    main()
