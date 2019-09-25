#A program that takes the last name in a list, makes it lowercase, reverses it, then capitalizes it.
names = ["Jacob", "Roger", "nhoJ"]
name_change = names[2].lower()
def reverse(name_change):
    name_change = name_change[::-1]
    return name_change
print(reverse(name_change).lower().capitalize())
