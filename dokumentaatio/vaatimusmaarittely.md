# Vaatimusmäärittely: python-ristinolla

## Sovelluksen tarkoitus

Sovelluksen avulla käyttäjä voi pelata ristinolla-tyyppisiä pelejä.

## Käyttäjät

Aluksi sovelluksella on yksi käyttäjä, joka pystyy käyttämään kaikkia toimintoja, ja pelin siirrot tehdään vuorotellen kyseisen käyttäjän roolissa. Myöhemmin voidaan lisätä erillinen pääkäyttäjä/pelimestari, ja rajata tavallisen pelaajan toimintoja.

## Käyttöliittymäluonnos

Peruskäyttöliittymä tulee olemaan tekstipohjainen. Sovellus aukeaa valikkoon, jossa voi tekstikomennoilla määritellä pelin tyypin ja aloittaa pelin. Pelinäkymä toimii vuoropohjaisesti siten, että käyttäjä valitsee, mihin ruutuun/koordinaattiin merkki pelataan.

## Sovelluksen perustoiminnot
- Asetuksien muutto päävalikossa: pelilaudan koko ja voittoon tarvittavien peräkkäisten merkkien määrä
- Pelinäkymä: Pelin nykytilanteen näyttö, seuraavan hyväksyttävän siirron tekeminen pelitilaan, voittajan määrittely

## Jatkokehitysideoita
Kun perustoiminnot on toteutettu, sovellukseen saatetaan lisätä mm. seuraavia toimintoja
- Kahden pelaajan tila
- Pelaajanimen/-nimien tallennus
- Loki pelatuista peleistä
- Tietokonetta vastaan pelaaminen
- Graafinen käyttöliittymä
