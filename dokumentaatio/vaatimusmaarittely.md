# Vaatimusmäärittely: OT-ristinolla

## Sovelluksen tarkoitus

Sovelluksen avulla käyttäjä voi pelata ristinolla-tyyppisiä pelejä. Ohjelma on toteutettu täysin Pythonilla.

## Käyttäjät

Aluksi sovelluksella on yksi käyttäjä, joka pystyy käyttämään kaikkia toimintoja, ja pelin siirrot tehdään vuorotellen kyseisen käyttäjän roolissa (tehty). Myöhemmin voidaan lisätä erillinen pääkäyttäjä/pelimestari, ja rajata tavallisen pelaajan toimintoja.

## Käyttöliittymäluonnos

Peruskäyttöliittymä tulee olemaan tekstipohjainen. Sovellus aukeaa valikkoon, jossa voi tekstikomennoilla määritellä pelin tyypin ja aloittaa pelin. Pelinäkymä toimii vuoropohjaisesti siten, että käyttäjä valitsee, mihin ruutuun/koordinaattiin merkki pelataan (tehty).

## Sovelluksen perustoiminnot
- Asetuksien muutto päävalikossa: pelilaudan koko (tehty) ja voittoon tarvittavien peräkkäisten merkkien määrä (toistaiseksi koko rivi/sarake/diagonaali)
- Pelinäkymä: Pelin nykytilanteen näyttö (tehty), seuraavan hyväksyttävän siirron tekeminen pelitilaan (tehty), voittajan määrittely (tehty), loki pelatuista peleistä (tehty)

## Jatkokehitysideoita
Kun perustoiminnot on toteutettu, sovellukseen saatetaan lisätä mm. seuraavia toimintoja
- Kahden pelaajan tila
- Pelaajanimen/-nimien tallennus
- Tietokonetta vastaan pelaaminen
- Graafinen käyttöliittymä
