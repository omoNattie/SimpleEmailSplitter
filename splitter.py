email = input("The email address you'd like to split (must contain \"@\" and \".\")\nYour email: ")  # get email address

if email == " ":
    print("uh... No email address?")  # if email is empty
elif email == "":
    print("uh... No email address?")  # if email is still empty
elif "." not in email:
    print("You need an extension.")  # if "." is missing
elif "@" not in email:
    print("You need a domain.")  # if "@" is missing
else:
    name = email[:email.index("@")]  # get everything before "@"
    domain = email[email.index("@")+1:]  # get everything after "@"

    final = "Name: {}\nDomain: {}".format(name, domain)
    print(final)
