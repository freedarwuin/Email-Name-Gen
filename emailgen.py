import random

import random

def generate_username(prefixes, names, email_domain):
    random_prefix = random.choice(prefixes).capitalize()
    
    # Select one name without spaces
    random_name = random.choice(names).strip().replace(" ", "").capitalize()

    # Ensure the name has at least 3 characters
    while len(random_name) < 3:
        random_name += random.choice("abcdefghijklmnopqrstuvwxyz")

    # Optionally Take the last three characters off the name
    # random_name = random_name[-3:]

    # Optionally Generate three random digits
    random_digits = random.randint(0, 999)

    username = f"{random_prefix}{random_name}{random_digits}{email_domain}" # You can remove random digits

    return username



def main():
    try:
        with open('prefix.txt', 'r') as prefix_file:
            prefixes = [prefix.strip() for prefix in prefix_file.readlines()]

        with open('names.txt', 'r') as names_file:
            names = [name.strip() for name in names_file.readlines()]
    except FileNotFoundError as e:
        print(f"Error: {e}. Asegúrese de que existan los archivos 'prefix.txt' y 'names.txt'.")
        return

    num_usernames = input("¿Cuántos nombres de usuario te gustaría generar? ")

    while not num_usernames.isdigit() or int(num_usernames) <= 0:
        print("Introduzca un número entero positivo.")
        num_usernames = input("¿Cuántos nombres de usuario te gustaría generar? ")

    num_usernames = int(num_usernames)

    email_domain = input("Dominio de correo electrónico comodín: (p. ej.: @dominio.com) ")

    with open('emails.txt', 'w') as output_file:  # Change the file name to 'emails.txt'
        for _ in range(num_usernames):
            username = generate_username(prefixes, names, email_domain)
            output_file.write(username + '\n')

    print(f"{num_usernames} Correos electrónicos generados y guardados en emails.txt")

if __name__ == "__main__":
    main()
