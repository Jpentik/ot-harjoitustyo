# Käyttöohje: OT-ristinolla

## Asennus
- Lataa ja pura uusin release
- Asenna riippuvuudet juurihakemistoon komennolla:
poetry install
- Pelin käynnistys (launcher.py) komennolla:
poetry run invoke start
## Pelin kulku
- Peli kysyy lukua n, joka määrää pelilaudan koon (n*n)
- Pelaajat tekevät siirrot vuorotellen, X aloittaa. Siirtoon annetaan ensin rivi, sitten sarake (molemmat 0:sta n-1:een). Kirjain "q" sarakkeeseen tai riviin keskeyttää pelin.
- Pelin voittaa saamalla omaa merkkiä kokonaisen rivin, sarakkeen tai diagonaalin. Jos pelilauta tulee täyteen ilman voittajaa, tuloksena on tasapeli.
- Pelin päätyttyä sovellus kysyy, haluaako käyttää tallentaa pelatun pelin lokitiedostoon. Vastaamalla merkillä "y" pelin lopputila tallennetaan projektin juurikansioon tiedostoon tictactoe_log.txt. Viimeisin peli aikaleimoineen lisätään lokin loppuun.
## Testit
- Suorita testit komennolla:
poetry run invoke test
## Testikattavuus
- Testikattavuusraportin generointi komennolla:
poetry run invoke coverage
- Testikattavuusraportin generointi html-tiedostoon komennolla:
poetry run invoke coverage-report
## Pylint
- Suorita tiedoston .pylintrc määrittelemät testit komennolla:
poetry run invoke lint
