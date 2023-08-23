from datetime import datetime
now = datetime.now()
# print(now)

day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
second = now.second

timestamp = now.timestamp()

# print(f"{day}/{month}/{year} {hour}:{minute}:{second}")
# print(f"timestamp: {timestamp}")

new_year = datetime(2020, 1, 1, 15, 30, 14, 13)
format_dd_mm_YY = new_year.strftime("%d/%m/%Y, %H:%M:%S %p")
# print(format_dd_mm_YY)
# print(format_dd_mm_YY)
# print(new_year)
day = new_year.day
month = new_year.month
year = new_year.year
hour = new_year.hour
minute = new_year.minute
second = new_year.second
# print(f'{day}/{month}/{year}, {hour}:{minute}:{second}')

# ----------------------------------------------------------------------
now = datetime.now()
t = now.strftime("%H:%M:%S")
# print(t)

# mm/dd/YY H:M:S format
time_one = now.strftime("%m/%d/%Y, %H:%M:%S")
# print(time_one)
# dd/mm/YY H:M:S format
time_two = now.strftime(("%d/%m/%Y, %H:%M:%S %p"))
# print(time_two)

# -----------------------------------------------
date_string = "5 December, 2019"
# print("date_string", date_string)
date_object = datetime.strptime(date_string, "%d %B, %Y")
# print("date_object", date_object)

# ---------------------------------------------------
from datetime import date
# date
d = date(2020, 1, 1)
# print(d)

# print("Current date:", d.today())

today = date.today()
diff = today - d
# print(diff)
# print("Current year:", today.year)
# print("Current month:", today.month)
# print("Current day:", today.day)

# -----------------------------------------

from datetime import time
# time(hour = 0, minute = 0, second = 0)
a = time()
# print("a =", a)

b = time(10, 30, 50)
# print("b =", b)

c = time(hour=10, minute=30, second=50)
# print("c =", c)

# time(hour, minute, second, microsecond)
d = time(10, 30, 50, 200555)
# print("d =", d)

# -----------------------------------------------------
today = date(year=2019, month=12, day=5)
new_year = date(year=2020, month=1, day=1)
time_left_for_newyear = new_year - today

# Time left for new year:  27 days, 0:00:00
# print("Time left for new year", time_left_for_newyear)

t1 = datetime.now()
t2 = datetime(year=2024, month=1, day=1, hour=0, minute=0, second=0)
diff = t2 - t1
# print("Time left for new year:", diff)

# --------------------------------------------
from datetime import datetime, timedelta
t1 = timedelta(weeks=12, days=10, hours=4, seconds=20)
t2 = timedelta(days=7, hours=5, minutes=3, seconds=30)
t3 = t1 - t2

# Definir una fecha inicial
fecha_inicial = datetime(2023, 6, 1, 15, 30)  # 1 de junio de 2023, 3:30 PM

# Definir una duración de tiempo
duracion = timedelta(days=2, hours=5, minutes=15)

# Agregar la duración a la fecha inicial
nueva_fecha = fecha_inicial + duracion

# Imprimir la nueva fecha
# print(nueva_fecha)


# ----------------------------
# ejercicios
now = datetime.now()
day, month, year, hour, minute, now_timestamp = now.day, now.month, now.year, now.hour, now.minute, now.timestamp()
# print(f"Current day: {day}\nCurrent month {month}\nCurrent year: {year}\nCurrent hour {hour}\nCurrent minute {minute} \
# \nCurrent timestmap {now_timestamp}")

format_mm_dd_YY_HH_MM_SS = now.strftime("%m/%d/%Y, %H:%M:%S")
# print(format_mm_dd_YY_HH_MM_SS)

today = "5 December, 2019"
format_date = datetime.strptime(today, "%d %B, %Y")
# print(format_date)

now = datetime.now()
new_year = datetime(year=2024, month=1, day=1, hour=0, minute=0, second=0)
diff = new_year - now
# print("Time left for new year:", diff)
# Time left for new year: 137 days, 12:47:05.468202

date_pass = "1 January 1970"
format_date = datetime.strptime(date_pass,"%d %B %Y")
# format_dd_mm_YY = format_date.strftime("%d/%m/%Y %H:%M:%S")
# print(format_dd_mm_YY)
now = datetime.now()
difference = (now - format_date).days
print("Difference between 1 January 1970 and now are:", difference, "days.")
years, rest = divmod(difference, 365)
months, days = divmod(rest, 30)

print(f"Years {years}, months {months} days {days}")












