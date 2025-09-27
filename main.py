from datetime import date

NAME = "Глеб"
SURNAME = "Кльос"
BIRTHDAY = date(2005, 5, 20)
MAIL = "[example@gmail.com](mailto:example@gmail.com)"

class Person:
def **init**(self, name, surname, birthday, mail):
self.name = name
self.surname = surname
self.birthday = birthday
self.age = self.calculate_age()
self.mail = mail

```
def calculate_age(self):
    today = date.today()
    years = today.year - self.birthday.year
    if (today.month, today.day) < (self.birthday.month, self.birthday.day):
        years -= 1
    return years

def __str__(self):
    return f"Ім'я: {self.name}\nПрізвище: {self.surname}\nДата народження: {self.birthday}\nВік: {self.age}\nПошта: {self.mail}"
```

if name == "**main**":
person = Person(NAME, SURNAME, BIRTHDAY, MAIL)
print(person)
