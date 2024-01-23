import base64

def szyfruj(text):
    return base64.b64encode(text.encode()).decode()

def odszyfruj(text):
    return base64.b64decode(text).decode()


tekst = 'To jest ukryta wiadomosc'
zaszyfrowany_tekst = szyfruj(tekst)
odszyfrowany_tekst = odszyfruj(zaszyfrowany_tekst)

print(f'Zaszyfrowany tekst: {zaszyfrowany_tekst}')
print(f'Odszyfrowany tekst: {odszyfrowany_tekst}')
assert odszyfrowany_tekst == tekst, "Odszyfrowany tekst nie pasuje do oryginału."

