import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):   
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kassapaate_olemassa(self):
        self.assertNotEqual(self.kassapaate, None)

    def test_konstruktori_toimii_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_syo_maukkaasti_kateisella_toimii(self):
        self.kassapaate.syo_maukkaasti_kateisella(410)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1004)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(410), 10)

    def test_syo_maukkaasti_kateisella_hylkaa_jos_raha_ei_riita(self):
        self.kassapaate.syo_maukkaasti_kateisella(300)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(300), 300)
    
    def test_syo_edullisesti_kateisella_toimii(self):
        self.kassapaate.syo_edullisesti_kateisella(240)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1002.4)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(250), 10)

    def test_syo_edullisesti_kateisella_hylkaa_jos_raha_ei_riita(self):
        self.kassapaate.syo_edullisesti_kateisella(200)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(200), 200)

    def test_syo_maukkaasti_kortilla_toimii(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(self.maksukortti.saldo_euroina(), 6)

    def test_syo_maukkaasti_kortilla_hylkaa_jos_raha_ei_riita(self):
        self.maksukortti=Maksukortti(300)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(self.maksukortti.saldo_euroina(), 3.0)

    def test_syo_edullisesti_kortilla_toimii(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.maksukortti.saldo_euroina(), 7.6)

    def test_syo_edullisesti_kortilla_hylkaa_jos_raha_ei_riita(self):
        self.maksukortti=Maksukortti(200)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.maksukortti.saldo_euroina(), 2.0)

    def test_rahan_lataaminen_kortille_toimii(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 1000)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1010)
        self.assertEqual(self.maksukortti.saldo_euroina(), 20)

    def test_rahan_lataaminen_kortille_negatiivinella_summalla_hylkaa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -1000)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)
        self.assertEqual(self.maksukortti.saldo_euroina(), 10)