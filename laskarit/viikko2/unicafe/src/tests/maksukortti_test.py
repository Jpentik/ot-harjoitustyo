import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_konstruktori_asettaa_saldon_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_kortille_voi_ladata_rahaa(self):
        self.maksukortti.lataa_rahaa(2500)

        self.assertEqual(self.maksukortti.saldo_euroina(), 35.0)
    
    def test_saldo_vahenee_oikein(self):
        self.maksukortti.ota_rahaa(100)

        self.assertEqual(self.maksukortti.saldo_euroina(), 9.0)

    def test_saldo_sailyy_jos_raha_ei_riita(self):
        self.maksukortti.ota_rahaa(11000)

        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)
    
    def test_arvo_frue_jos_saldo_riittaa(self):

        self.assertTrue(self.maksukortti.ota_rahaa(100))

    def test_arvo_false_jos_saldo_ei_riita(self):

        self.assertFalse(self.maksukortti.ota_rahaa(1100))