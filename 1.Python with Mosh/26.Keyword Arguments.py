def greet_users(first_name, last_name):
    print(f"hi {first_name} {last_name} 😁")
    print("Welcome aboard")


greet_users(first_name="Mohammad", last_name="Jonayed")

"""
we should use keyword argument  when necessary 
we can provide keyword argument followed by  positional argument
not otherwise.
example :

greet_users("Mohammad", last_name="Jonayed") it will work

greet_users(first_name="Mohammad", "Jonayed") it won't

 
"""