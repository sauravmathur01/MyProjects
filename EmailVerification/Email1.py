k, j, d = 0, 0, 0
email = input("Email address is...")

# Check if the length of the email is at least 6 characters
if len(email) >= 6:
    # Check if the first character is an alphabet
    if email[0].isalpha():
        # Check if there is exactly one "@" in the email
        if ("@" in email) and (email.count("@") == 1):
            # Find the index of the "@" character
            at_index = email.index("@")
            # Check if there is at least one dot after the "@" character
            if "." in email[at_index:]:
                # Check for invalid characters
                for i in email:
                    if i.isspace():
                        k = 1  # Invalid if there's a space
                    elif i.isalpha():
                        if i.isupper():  # Check if there's an uppercase letter
                            j = 1
                    elif i.isdigit():
                        continue  # Digits are valid
                    elif i in "_." or i == "@":
                        continue  # Underscore, dot, and "@" are valid
                    else:
                        d = 1  # Invalid character found

                # Check for validity based on the flags
                if k == 1 or j == 1 or d == 1:
                    print("Invalid email6")
                else:
                    print("Valid email5")
            else:
                print("Invalid email4")  # No dot in the domain part
        else:
            print("Invalid email3")  # Invalid "@" count
    else:
        print("Invalid email2")  # First character is not a letter
else:
    print("Invalid email address1.")  # Length check