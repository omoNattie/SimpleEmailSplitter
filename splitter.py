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
    domain = email[email.index("@"):]  # get everything after "@"
    domains = domain.split(".")[:-1]  # split everything before "."
    domains = ".".join(domains)  # put it into a string and not a list
    extension = email[email.index("."):]  # get everything after "."

    final = "Name: {}\nDomain: {}\nExtension: {}".format(name, domains, extension)
    print(final)
