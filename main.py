# Tuples are immutable. Can't be changed
programming_languages_tuple = "Python", "Java", "C++", "C#"
print(type(programming_languages_tuple))

# Lists are mutable. Can be changed Add/Modify.Delete
programming_languages_list = ["Python", "Java", "C++", "C#"]
print(type(programming_languages_list))

for language in programming_languages_tuple:
  print(language)

for language in programming_languages_list:
  print(language)