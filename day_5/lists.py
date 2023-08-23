# lista = ["first", "second", "third", "four", "five"]


# item1, item2, item3, *rest = lista
# print(rest)

# first, second, third, *elem, tenth = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(elem)
# print(tenth)
# countries = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
# gr, fr, bg, sw, *scandic, es = countries
# print(gr)
# print(fr)
# print(bg)
# print(sw)
# print(scandic)
# print(es)


# oracion = "hola a todos como se encuentran el día de hoy"


# fruits = ["orange", "apple", "pineapple", "mango", "avocado"]
# fruits.insert(2, "melon")
# print(fruits)
# fruits.remove("orange")
# print(fruits)

# fruits.pop(1)
# print(fruits)
# fruits.extend(["pine", "torange", "straberry"])
# print(fruits)


# fruits_copy = fruits.copy()
# print(fruits_copy)

# 1 2 3 4 5
# empty_list = list()
# list_items5 = [1, 2, 3, 4, 5]
# print(len(list_items5))
# print(list_items5[0], list_items5[len(list_items5) // 2], list_items5[-1])
# mixed_data_types = ["g", 21, 1.63, False, "México"]
# it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
# print(it_companies)
# print(len(it_companies))
# it_companies.append("Samsung Group")
# it_companies = it_companies.insert(len(it_companies) // 2, "Cisco Systems")
# print(it_companies)
# print("#".join(it_companies))
# print("IBM" in it_companies)
# it_companies.sort(reverse=True)
# print(it_companies[:3])
# print(it_companies[-3:])
# print(it_companies[3:-3])

# it_companies.pop(0)
# it_companies.remove("Apple")
# it_companies.pop(-1)
# print(it_companies)
# it_companies.clear()
# del it_companies

# front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
# back_end = ["Node", "Express", "MongoDB"]
# join = front_end + back_end
# full_stack = join.copy()

# index_redux = full_stack.index("Redux")
# full_stack.insert(index_redux + 1, "Pyhton")
# full_stack.insert(index_redux + 2, "SQL")
# print(full_stack)

# ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# ages.sort()
# print(max(ages))
# print(min(ages))
# print(ages)
# meddle_index = len(ages) // 2
# if len(ages) % 2 == 1:
#     median_age = meddle_index
# else:
#     median_age = (ages[meddle_index - 1] + ages[meddle_index - 1]) / 2
# print("Median age", median_age)
# print(sum(ages) / len(ages))
# print(max(ages) - min(ages))

# print(abs(min(ages) - sum(ages) / len(ages)), max(ages) - sum(ages) / len(ages))

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
  'Zip'
]
if len(countries) % 2 == 0:
    middle_countries = [countries[len(countries) // 2 - 1]] + [countries[len(countries) // 2]]
    print(middle_countries)
else:
    middle_countries = countries[len(countries) // 2]

# middle_index = len(countries) // 2
# if len(countries) % 2 == 1:
#     middle_countries1 = countries[:middle_index + 1]
#     middle_countries2 = countries[middle_index + 1:]
#     print(middle_countries1, middle_countries2)
#     print(len(middle_countries1), len(middle_countries2))
# else:
#     middle_countries1 = countries[:middle_index]
#     middle_countries2 = countries[middle_index:]
#     print(middle_countries1, middle_countries2)
#     print(len(middle_countries1), len(middle_countries2))

# cn, rs, usa, *scandic_countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
# print(scandic_countries)



