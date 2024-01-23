import random
import string

def generuj_bezpieczne_haslo():
    # Losowa długość hasła od 8 do 12 znaków
    dlugosc = random.randint(8, 12)

    # Zestaw znaków: wielkie litery, małe litery, cyfry, znaki specjalne
    znaki = string.ascii_letters + string.digits + string.punctuation

    # Tworzenie hasła
    haslo = ''.join(random.choice(znaki) for i in range(dlugosc))

    # Sprawdzenie, czy hasło zawiera przynajmniej jedną wielką literę, małą literę, cyfrę i znak specjalny
    if (any(c.islower() for c in haslo) and
        any(c.isupper() for c in haslo) and
        any(c.isdigit() for c in haslo) and
        any(c in string.punctuation for c in haslo)):
        return haslo
    else:
        # Jeśli nie, generuj ponownie
        return generuj_bezpieczne_haslo()

# Wygeneruj i wyświetl bezpieczne haslo
print(generuj_bezpieczne_haslo())
