try:
    choice = input('You said Y to subdomain').lower()
except NameError:
    choice = raw_input('You said Y to subdomain').lower()

print(choice)
