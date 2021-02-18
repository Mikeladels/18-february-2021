#michelle adelia suwarno / xi mia 1 / 25
#dengan dictionary
vowels = "aiueo"

ip_str = "Halo nama saya mikel, saya sedang belajar python"

ip_str= ip_str.casefold()

count = {}.fromkeys(vowels,0)

for char in ip_str :
    if char in count :
        count [char] += 1

print(count)