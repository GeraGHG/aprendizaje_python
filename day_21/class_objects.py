class Person:
    def __init__(self, firstname="firstname", lastname="lastname", age="0", country="None", city="None"):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city
        self.skills = []

    def person_info(self):
        cadena = f"{self.firstname} {self.lastname} is " \
                 f"{self.age} years old. He lives in {self.city}, {self.country}. " \
                 f"Skills: {self.skills}"
        return cadena

    def add_skill(self, skill):
        self.skills.append(skill)

class Student(Person):
    def __init__(self, firstname, lastname, age, country, city, gender = "male"): # aqui agrega el nuevo atributo gender
        super().__init__(firstname, lastname, age, country, city) # mucho ojo aqui no utiliza el self
        self.gender = gender
    def person_info(self):
        gender = 'He' if self.gender == 'male' else 'She'
        return f'{self.firstname} {self.lastname} is {self.age} years old. {gender} lives in {self.city}, {self.country}. ' \
               f'Skills: {self.skills}'

s1 = Student("Miguel", "Ochoa", 30, "Ciudad de México", "México", "female")
s2 = Student("John", "Doe", 25, "USA", "New York", "male")

s1.add_skill("Dancer")
s1.add_skill("Singer")
#print(s1.person_info())


class Statistics:
    def __init__(self, nums: list = []):
        self.nums = nums

    def count(self):
        return len(self.nums)

    def sum(self):
        return sum(self.nums)

    def min(self):
        return min(self.nums)

    def max(self):
        return max(self.nums)

    def range(self):
        return max(self.nums) - min(self.nums)

    def mean(self):
        return sum(self.nums) / len(self.nums)

    def median(self):
        sorted_nums = sorted(self.nums)
        middle = len(sorted_nums) // 2
        if len(sorted_nums) % 2 != 0:
            return sorted_nums[middle]
        else:
            return (sorted_nums[middle - 1] + sorted_nums[middle]) / 2

    def mode(self):
        dict_mode = {}
        for num in self.nums:
            dict_mode[num] = dict_mode.get(num, 0) + 1
        sorted_mode = sorted(dict_mode.items(), key=lambda item: item[1], reverse=True)
        mode, count = sorted_mode[0]
        return {"mode": mode, "count": count}

    def std(self):
        mean = sum(self.nums) / len(self.nums)
        sum_nums_mean = sum((num - mean) ** 2 for num in self.nums)
        std_deviation = (sum_nums_mean / len(self.nums)) ** 0.5
        return round(std_deviation, 1)

    def variance(self):
        mean = sum(self.nums) / len(self.nums)
        sum_nums_mean = sum((num - mean) ** 2 for num in self.nums)
        variance = sum_nums_mean / len(self.nums)
        return round(variance, 1)

    def freq_dist(self):
        freq_dict = dict()
        for num in self.nums:
            freq_dict[num] = freq_dict.get(num, 0) + 1
        freq_dist_list = set((count, num) for num, count in freq_dict.items())
        freq_dist_list = list(freq_dist_list)
        freq_dist_list.sort(reverse=True)
        return freq_dist_list

    def describe(self):
        return f"Count: {self.count()}\n" \
               f"Sum: {self.sum()}\n" \
               f"Min: {self.min()}\n" \
               f"Max: {self.max()}\n" \
               f"Range: {self.range()}\n" \
               f"Mean: {self.mean()}\n" \
               f"Median: {self.median()}\n" \
               f"Mode: {self.mode()}\n" \
               f"Standard Deviation: {self.std()}\n" \
               f"Variance: {self.variance()}\n" \
               f"Frequency Distribution: {self.freq_dist()}"

ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
data = Statistics(ages)
# print(data.describe())

class PersonAccount:
    def __init__(self, firstname, lastname, incomes = 0, expenses = 0):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = incomes
        self.expenses = expenses

    def total_income(self):
        return f"Total incomes {self.incomes}"
    def total_expense(self):
        return f"Total expense {self.expenses}"

    def account_info(self):
        return f"{self.firstname} {self.lastname}\n" \
        f"Total incomes {self.incomes}\n" \
        f"Total expense {self.expenses}"

    def add_income(self, new_income):
        self.incomes += new_income

    def add_expense(self, new_expense):
        self.expenses += new_expense

    def account_balance(self):
        return f"Total account balance: {self.incomes - self.expenses}"


class PersonAccount:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = []
        self.expenses = []

    def total_income(self):
        return sum([income[0] for income in self.incomes])

    def total_expense(self):
        return sum([expense[0] for expense in self.expenses])

    def account_info(self):
        income_info = "\n".join([f"Income description: {income[1]} - Amount: {income[0]}" for income in self.incomes])
        expense_info = "\n".join([f"Expense description: {expense[1]} - Amount: {expense[0]}" for expense in self.expenses])
        return f"{self.firstname} {self.lastname}\n\nIncome Details:\n{income_info}\n\nExpense Details:\n{expense_info}"

    def add_income(self, amount, description):
        self.incomes.append((amount, description))

    def add_expense(self, amount, description):
        self.expenses.append((amount, description))

    def account_balance(self):
        balance = self.total_income() - self.total_expense()
        return f"Total account balance: {balance}"

person1 = PersonAccount("Gerardo", "Hernández González")
# print(person1.account_info())
person1.add_income(100, "Deposito trabajo")
person1.add_income(10, "Deposito socio")
person1.add_expense(45, "Comida")
person1.add_expense(10, "Viaje")
# print(person1.account_info())
# print(person1.total_income())

# print(person1.account_balance())

dict_items = {"amount": 45, "amor": 100}
list_dict = [(value, key) for key, value in dict_items.items()]
print(list_dict)




