


from cards import Cards
from Valtakunta_app import Roles

actions = {
    "2": {
        Roles.HALLITSIJA: """Muututko kansalaiseksi?
Tartu juomaasi ja juo itsellesi kansan suosio. Kansa äänestää jatkatko hallitsijan roolia. Muuten tiput kansalaiseksi ja kansa äänestää uuden entistä humaltuneemman hallitsijan.
""",
        Roles.AATELINEN: """""Kuninkaan malja
Kuningas pitää puheen valitsemastaan aiheesta. Puheen aikana muut pelaajat juovat koko puheen ajan.
""""",
        Roles.KANSALAINEN: """Orjakauppa
Juo juomasi ja myy itsesi orjaksi. Muut pelaajat juovat kunnes viimeinen lopettaa ja saa omistajuuden.
""",
        Roles.KURTESAANI: """Petturi
Muutut omistajasi orjaksi. Omistaja juo 2.
""",
        Roles.ORJA: """Kyläjuoppo
Sammalla ja juo aina kun joku toinen juo yhden kierroksen ajan. (Pidä älämölöä kun muut juovat)

"""
        
    },
    "3": {
        Roles.HALLITSIJA: """Muututko aateliseksi?
Tartu juomaasi ja juo itsellesi kansan suosio. Kansa äänestää jatkatko hallitsijan roolia. Muuten tiput aateliseksi ja kansa äänestää uuden entistä humaltuneemman hallitsijan.
""",
        Roles.AATELINEN: """Muututko kansalaiseksi?
Tartu juomaasi ja juo itsellesi kansan suosio. Kansa äänestää jatkatko aatelisen roolia. 
Muuten tiput kansalaiseksi.
""",
        Roles.KANSALAINEN: """Naimakauppa
Juo puolet juomastasi ja myy itsesi kurtisaaniksi. Muut pelaajat juovat kunnes viimeinen lopettaa ja saa omistajuuden.
""",
        Roles.KURTESAANI: """Myrkytä itsesi
Juo lasisi tyhjäksi.
""",
        Roles.ORJA: """Rappio
Viimeistele juomasi. (Valita elämästä)
"""
        
    },
    "4": {
        Roles.HALLITSIJA: """Pöydän alle
Valitse pelaaja kenen kanssa juot kilpaa lasin tyhjäksi. Häviöstä seuraa roolin menetys voittajalle.
Kansa toimii tuomarina.
""",
        Roles.AATELINEN: """Pöydän alle
Valitse pelaaja kenen kanssa juot kilpaa lasin tyhjäksi. Häviöstä seuraa roolin menetys voittajalle. Hallitsija toimii tuomarina.
""",
        Roles.KANSALAINEN: """Koko kylän polkupyörä.
Olet yhden kierroksen ajan jokaisen pelaajan kurtisaani. Juo aina kun toinen juo
""",
        Roles.KURTESAANI: """Koko kylän polkupyörä.
Olet yhden kierroksen ajan jokaisen muun pelaajan kurtisaani. Juo aina kun toinen juo.
""",
        Roles.ORJA: """Hörppiä
Kippistä jokaisen pelaajan kanssa. (Jos olet Samuel toista kortti kahdesti)
"""
        
    },
    "5": {
        Roles.HALLITSIJA: """Orjuutta vastaan!
Jos valtakunnassasi kansalaisista puolet tai enemmän ovat orjia ja kurtisaaneja vapauta heidät kahleistaan ja laita omistajat juomaan 5 huikkaa.
""",
        Roles.AATELINEN: """Ylempi vitonen
Lyö käsi keskelle pöytää. Viimeinen pelaaja joka lyö kätensä kätesi päälle juo 5.
""",
        Roles.KANSALAINEN: """Hail
Huuda “HAIL”! Viimeinen pelaaja, joka huutaa hallitsijan nimen juo viisi huikkaa. Ilman hallitsijaa huudetaan “HITLER”.
""",
        Roles.KURTESAANI: """Hail
Huuda “HAIL”! Viimeinen pelaaja, joka huutaa hallitsijan nimen juo viisi huikkaa. Ilman hallitsijaa huudetaan “HITLER”. (Käden nosto)
""",
        Roles.ORJA: """Hail
Huuda “HEIL”! Viimeinen pelaaja, joka huutaa hallitsijan nimen juo viisi huikkaa. Ilman hallitsijaa huudetaan “HITLER”. (Käden nosto)
"""
        
    },
    "6": {
        Roles.HALLITSIJA: """Viisauden aikakausi 
Aloita lukujono, johon seuraava vastaa aina tulevan numeron.
""",
        Roles.AATELINEN: """Arvonimi
Valitse nimeesi etuliite esim. “herttuatar”. Jos toinen pelaaja unohtaa nimesi etuliitteen sinua puhutellessaan hän juo 6.
(ei voida jakaa orjille)
""",
        Roles.KANSALAINEN: """Lottokuponki
Jokainen pelaaja juo seuraavan kortin lukumäärän.
""",
        Roles.KURTESAANI: """Juo 6""",
        Roles.ORJA: """Shrek
Saat arvonimen Shrek. Jos pelaaja unohtaa mainita Shrek nimen juotte molemmat yhden hörpyn. (hörppy ei voi määrä orjalle)
"""
        
    },
    "7": {
        Roles.HALLITSIJA: """Metsästys
Huuda metsästys. Laske selkeästi kymmeneen ja laukaise kivääri. Pelaajat voivat juosta laskennan aikana karkuun. Pelaaja ketä osoitat laskennan päätyttyä juo lasinsa tyhjäksi. Muista, että jos useampi pelaaja on piipun edessä ottaa jokainen osuman.
""",
        Roles.AATELINEN: """Kategoria
Sano kategoria. Muut luettelevat järjestyksessä kategoriaan kuuluvia asioita. Jos kategoria ei kierrä kierrosta juot myös itse 7. Jos sanoo jo sanotun asian tai ei keksi kategoriaan liittyvää sisältöä häviää. Häviäjä juo 7. 
""",
        Roles.KANSALAINEN: """Kategoria
Sano kategoria. Muut luettelevat järjestyksessä kategoriaan kuuluvia asioita. Jos kategoria ei kierrä kierrosta juot myös itse 7. Jos sanoo jo sanotun asian tai ei keksi kategoriaan liittyvää sisältöä häviää. Häviäjä juo 7. 
""",
        Roles.KURTESAANI: """Juo 7""",
        Roles.ORJA: """Kategoria
Häviäjä juo lasistaan seitsemän huikkaa. (Sisällytä teemaan)
"""
        
    },
    "8": {
        Roles.HALLITSIJA: """Sääntö
Keksi vanhan säännön tilalle uusi sääntö, joka koskee muita pelaajia. 
(Asennot, juomamäärät, teot, pelin dynamiikan muuttaminen…)
""",
        Roles.AATELINEN: """Tanssipeli
Aloita eleellä. Seuraava toistaa saman eleen ja jatkaa omallaan. Jos et pääse lisäämään toista elettä juot myös itse 8. Jos unohtaa jo näytetyt eleet juo 8.
""",
        Roles.KANSALAINEN: """Laiva on lastattu
Sano “laiva on lastattu” ja keksimäsi tavara. Seuraava pelaaja tekee samoin, mutta hänen tavaransa täytyy liittyä samaan teemaan kuin ensimmäinen. 
""",
        Roles.KURTESAANI: """Never have I ever
Pelaajat, jotka ovat tehneet juovat kahdeksan huikkaa.
""",
        Roles.ORJA: """Never have I ever
Pelaajat, jotka ovat tehneet juovat kahdeksan huikkaa.
"""
        
    },
    "9": {
        Roles.HALLITSIJA: """Kuninkaan tarina
Nosta malja niin monta kertaa kuin haluat. Jokainen pelaaja tekee samoin. Jos joku luovuttaa tai ei ota kunnon hörppyjä hänestä tulee orjasi.""",
        Roles.AATELINEN: """Tarina
Aloita sanalla. Seuraava toistaa saman sanan ja jatkaa omallaan. Jos et pääse lisäämään toista sanaa juot myös itse 8. Jos unohtaa jo kerrotun tarinan juo 8.
""",
        Roles.KANSALAINEN: """Tarina
Aloita sanalla. Seuraava toistaa saman sanan ja jatkaa omallaan. Jos et pääse lisäämään toista sanaa juot myös itse 8. Jos unohtaa jo kerrotun tarinan juo 8.
""",
        Roles.KURTESAANI: """Tarina
Häviäjä juo lasistaan yhdeksän huikkaa. (Sisällytä teemaan) 
""",
        Roles.ORJA: """Tarina
Häviäjä juo lasistaan yhdeksän huikkaa. (Sisällytä teemaan)
"""
        
    },
    "10": {
        Roles.HALLITSIJA: """Hääpari
Parita kaksi pelaajaa, jotka juovat aina yhdessä. Anna heille keskenään jaettavaksi 10 huikkaa.
""",
        Roles.AATELINEN: """Älä katso! Muut pelaajat osoittavat jotain pelaajaa. Kun pelaajat ovat valmiita arvaa eniten osoitetun pelaajan nimi. Jokaisesta väärin menneestä arvauksesta kaikki muut juovat 3.
(ei voida jakaa orjille)
""",
        Roles.KANSALAINEN: """Juokaa järjestyksessä 1, 2, 3, 4… .  Äänestämällä voidaan ottaa toinen kierros.""",
        Roles.KURTESAANI: """1, 2, 3… (orjia voi käyttää apuna)""",
        Roles.ORJA: """Lihapää
Kymmenen punnerrusta tai kyykkyä. Muuten kymmenen huikkaa. (Jos olet Tuomas kerro kolmella)
"""
        
    },
    "jack": {
        Roles.HALLITSIJA: """Orjien vapauttaminen
Anna orjille mahdollisuus juoda itsensä pois orjuudesta. Näin orjat palaavat takaisin kansalaisiksi.
""",
        Roles.AATELINEN: """Ota orja
Valitse saman- tai alempiarvoinen pelaaja ja tee hänestä kurtisaanisi. Jaa kaikille orjille 11.
""",
        Roles.KANSALAINEN: """Orjakauppa
Päätä arvojärjestyksessä samalta tai alemmalta itsellesi orja lisäksi juo tai anna orjallesi 11.
""",
        Roles.KURTESAANI: """Orjakauppa
Päätä arvojärjestyksessä kansalainen tai alempi pelaaja, joka myydään orjaksi. (Pidä huutokauppa)
""",
        Roles.ORJA: """Kansanäänestys
Kaikki pelaajat äänestävät pääsetkö pois orjuudesta kansalaiseksi. (peukalo ylös tai alas)
"""
        
    },
    "queen": {
        Roles.HALLITSIJA: """Kurtisaanien vapauttaminen 
Anna kurtisaaneille mahdollisuus juoda itsensä pois orjuudesta. Näin kurtisaanit palaavat takaisin kansalaisiksi.
""",
        Roles.AATELINEN: """Ota jalkavaimo
Valitse saman- tai alempiarvoinen pelaaja ja tee hänestä kurtisaanisi. Jaa kurtisaaneille 12. 
""",
        Roles.KANSALAINEN: """Naimakauppa
Päätä arvojärjestyksessä samalta tai alemmalta itsellesi kurtisaani juo kurtisaanin kanssa 12.
""",
        Roles.KURTESAANI: """Sisarvaimot
Halutessasi kaikki orjat muuttuvat omistajasi kurtisaaneiksi. Vahdi, että muut sisarvaimot juovat aina yhden ylimääräisen huikan sinua enemmän.
""",
        Roles.ORJA: """Heruttelija
Muutut omistajasi kurtisaaniksi. Kippistä vihjailevasti omistajasi kanssa.
"""
        
    },
    "king": {
        Roles.HALLITSIJA: """Vesiputous
Vesiputous alkaa hallitsijasta, jonka jälkeen järjestyksessä aateliset, kansalaiset, kurtisaanit ja orjat saavat lopettaa. Tämän jälkeen hallitsija ottaa vielä yhden ISON huikan ja röyhtäisee.
""",
        Roles.AATELINEN: """Kokein aatelinen
Kaikki muut aateliset muuttuvat kansalaisiksi. Jaa kaikille kansalaisille 13. 
""",
        Roles.KANSALAINEN: """Turnajaiset
Haasta toinen pelaaja valitsemaasi lajiin. Voittaja nousee aateliseksi. Häviäjä juo 13.
""",
        Roles.KURTESAANI: """Noita
Muutut kansalaiseksi (noidaksi). Lisäksi myrkytät omistajasi, joka joutuu juomaan lasinsa tyhjäksi. 
""",
        Roles.ORJA: """Mellakka
Nouse omistajaasi vastaa. Juotte kilpaa samasta juomamäärästä, jonka seurauksena voittaja päättää vaihtuvatko rollit.
"""
        
    },
    "ace": {
        Roles.HALLITSIJA: """Kuninkaan malja
Kuningas pitää puheen valitsemastaan aiheesta. Puheen aikana muut pelaajat juovat koko puheen ajan.
""",
        Roles.AATELINEN: """Ylennys
Juo hallitsijaa vastaan. Enemmän juonut pääsee hallitsijaksi. Häviäjästä tulee kansalainen.
""",
        Roles.KANSALAINEN: """Vallankaappaus
Nouset hallitsijaksi. Järjestä vesiputous arvojärjestyksessä.
""",
        Roles.KURTESAANI: """Bordellin pitäjä
Muutut aateliseksi ja määräät itsellesi kaksi kurtisaania aatelisista ja/tai alemmista.
""",
        Roles.ORJA: """Hallitsija uljas pelastaa
Et ole enää kurtisaani sillä hallitsija tekee sinusta aatelisen. Voit tehdä entisestä omistajastasi kurtisaanisi.
"""
        
    }
}

def get_action(card: Cards, role: Roles):
    number = card.rsplit("_", 1)[0].replace("_of", "")
    return actions[number][role]

