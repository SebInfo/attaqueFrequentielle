from unidecode import unidecode
from collections import Counter
import string

texteChiffreSubstitution = """
Z J’ZDDRFPH DAH AB XZBV, VPBL JPBAORD, ZIRV OFP
RO HRYZHQRH KRD YRBD, OZBO LA’U RB Z
OR GZHKRH QA XFB ORJGD, LAP RDO JFHO FA LAP HRIPRBQHZ
RB DRHHZBO QZBD JZ JZPB ORD GROPOD QFPYOD
GPD QFBBRH Z XFAWWRH Z QRD GPYRFBD PQPFOD
KRAH WPKRH QRD VFAGD QR GPRQ GFAH QR WZAC
RO RBORBQHR OFB HPHR LAP KREZHQR KRD JAHD
LAP DZPO DAHOFAO YARHPH JRD XKRDDAHRD
OR HZVFBORH AB GRA VFJJRBO N’ROZPD, JPBFO
KRD XFJXRVD WZXAKRAC LA’FB GPLAZPO VTRE K’JZHVTZBQ
VZH-RB-DZV RO JPBOF, VZHZJRKD Z AB WHZBV
RO KRD JPDOHZK YZYBZBOD
Z HRJZHVTRH DFAD KZ GKAPR, VPBL JPBAORD, ZIRV OFP
RO HRYZHQRH KZ IPR, OZBO LA’U RB Z
OR HZVFBORH KZ ORHHR RB OR XFAWWZBO QRD URAC
OR GZHKRH QR OZ JRHR, AB GROPO GRA
RO DZAORH QZBD KRD WKZLARD GFAH KZ WZPHR HZKRH
XFADPKKRH BFD YFQZDDRD RO D’JZHHRH
RO RBORBQHR OFB HPHR VFJJR FB RBORBQ KZ JRH
D’ZHHRORH, HRGZHOPH RB ZHHPRHR
OR HZVFBORH DAHOFAO KRD VZHZJXZHD Q’ZBOZB RO KRD VFVF XFRHD
RO KRD IHZPD HFAQFAQFAD LAP BFAD VFAGZPRBO KRD KRIHRD
RO BFAD BPLAZPRBO KRD QRBOD
RO KRD JPDOHZK YZYBZBOD
Z J’ZDDRFPH DAH AB XZBV, VPBL JPBAORD, ZIRV OFP
HRYZHQRH KR DFKRPK LAP D’RB IZ
OR GZHKRH QA XFB ORJGD, LAP RDO JFHO RO NR J’RB WFAD
OR QPHR LAR KRD JRVTZBOD, V’RDO GZD BFAD
LAR DP JFP NR DAPD XZHYR, VR B’RDO LAR QR ORD URAC
VZH PKD FBO K’ZIZBOZYR Q’ROHR QRAC
RO RBORBQHR OFB HPHR D’RBIFKRH ZADDP TZAO
LAR D’RBIFKRBO KRD VHPD QRD FPDRZAC
OR HZVFBORH, RBWPB, LA’PK WZAO ZPJRH KZ IPR
K’ZPJRH JRJR DP KR ORJGD RDO ZDDZDDPB RO RJGFHOR ZIRV KAP
KRD HPHRD QRD RBWZBOD
RO KRD JPDOHZK YZYBZBOD
RO KRD JPDOHZK YZYBZBOD"""

def analyse_frequentielle(monTexte):
    # Convertir le texte en version ASCII (supprimer les accents)
    texte_ascii = unidecode(monTexte)
    texte_ascii = texte_ascii.upper()
    # Filtrer uniquement les lettres de l'alphabet
    texte_filtre = ''.join([char for char in texte_ascii if char in string.ascii_uppercase])
    # Compter le nombre de chaque lettre
    frequences = Counter(texte_filtre)
    # Calculer le total des lettres pour avoir les pourcentages
    total_lettres = sum(frequences.values())
    # Créer un dictionnaire pour stocker les fréquences en pourcentage
    resultat = {}
    # Remplir le dictionnaire avec les lettres de A à Z
    for lettre in string.ascii_uppercase:
        frequence = frequences.get(lettre, 0)
        pourcentage = (frequence / total_lettres) * 100 if total_lettres > 0 else 0
        resultat[lettre] = round(pourcentage, 2)

    return resultat

frequences_francais = {
    'E': 14.7, 'A': 7.6, 'I': 7.5, 'S': 7.2, 'N': 7.0, 'R': 6.5, 'T': 6.1,
    'O': 5.2, 'L': 5.1, 'U': 4.4, 'D': 3.6, 'C': 3.3, 'M': 3.2, 'P': 3.0,
    'G': 1.3, 'B': 1.1, 'V': 1.1, 'H': 1.0, 'F': 1.0, 'Q': 0.9, 'Y': 0.3,
    'X': 0.3, 'J': 0.3, 'K': 0.1, 'W': 0.1, 'Z': 0.1
}

print(frequences_francais)
frequences_lettres_chiffre=analyse_frequentielle(texteChiffreSubstitution)
frequences_lettres_chiffre_tri = sorted(frequences_lettres_chiffre.items(), key=lambda item: item[1], reverse=True)
print(frequences_lettres_chiffre_tri)

table = str.maketrans("REZADSOTKMHYGQJPIWFBNVXLCU",
                      "EZAUS3THL5RGPDMIVFON7CBQXY")

# Appliquer la traduction
nouveau_texte = texteChiffreSubstitution.translate(table)

print(nouveau_texte)