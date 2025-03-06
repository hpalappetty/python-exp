name = "ada lovelace"
print(name.title())

print(name.upper())
print(name.lower())

# variables in string

first_name = "ada"
last_name = "lovelace"

full_name = f"{first_name} {last_name}"
print(full_name.title())

full_name = f"Hello, {first_name} {last_name}!"
print(full_name.title())

favourite_language = ' python '
print(favourite_language.rstrip())
print(favourite_language.lstrip())
print(favourite_language.strip())

# removing prefixes

nostarch_url = 'https://nostarch.com'
res = nostarch_url.removeprefix('https://')
print(f"before {nostarch_url} and after {res}")

#underscores to make large numbers readable
universe_age=14_000_000_000
print(universe_age)