class NotString(Exception):
    pass

def ChekInt(string):
    try:
        string = int(string)
    except ValueError:
        return False
    else:
        return True

while True:
    try:
        file = open('Scripts/File.txt', 'a')

        lastName, firstName, patronymic, year = input("Введите ФИО и год рождения: ").split()
        year = int(year) #ValueError
        if ChekInt(lastName) or ChekInt(firstName) or ChekInt(patronymic):
            raise NotString
        if len(str(year)) != 4:
            raise Exception
    except NotString:
        print("ФИО введено некорректно. Попробуйте снова.")
    except ValueError:
        print("Год рождения должен быть числом. Попробуйте снова.")
    except Exception:
        print("Год рождения должен быть введен в формате гггг. Попробуйте снова.")
    else:
        file.write(f'{lastName} {firstName} {patronymic} {year}\n')
    finally:
        file.close()