#verš, jeho sonoritní profily + graf
class Word:
    def __init__(self, slovo, vers = 0):
        self.slovo = slovo
        self.zmeny_slovo = slovo
        self.zmeny()
        self.sonor_profil = [] #sonoritní profil slova
        self.klasifikace_hlasek()
        self.vers = vers #id verše
        self.pozice = 0 #na které pozici slovo ve verši je
        self.pocet_sonor_vrch = 0
        self.find_pocet_sonor_vrch()
        self.hlasky_slova = []
        self.set_hlasky_slova()
    def zmeny(self):
        self.zmeny_slovo = self.zmeny_slovo.replace('ni', 'ňi')
        self.zmeny_slovo = self.zmeny_slovo.replace('di', 'ďi')
        self.zmeny_slovo = self.zmeny_slovo.replace('ti', 'ťi')
        self.zmeny_slovo = self.zmeny_slovo.replace('ní', 'ňí')
        self.zmeny_slovo = self.zmeny_slovo.replace('dí', 'ďí')
        self.zmeny_slovo = self.zmeny_slovo.replace('tí', 'ťí')
        self.zmeny_slovo = self.zmeny_slovo.replace('ně', 'ňγe')
        self.zmeny_slovo = self.zmeny_slovo.replace('dě', 'ďγe')
        self.zmeny_slovo = self.zmeny_slovo.replace('tě', 'ťγe')
        self.zmeny_slovo = self.zmeny_slovo.replace('mě', 'mγe')
        self.zmeny_slovo = self.zmeny_slovo.replace('ě', 'γe')
        self.zmeny_slovo = self.zmeny_slovo.replace('x', 'ks')
        self.zmeny_slovo = self.zmeny_slovo.replace('q', 'kv')
        self.zmeny_slovo = self.zmeny_slovo.replace('ch', 'x')
        self.zmeny_slovo = self.zmeny_slovo.replace('ů', 'ú')
        self.zmeny_slovo = self.zmeny_slovo.replace('w', 'v')
    def klasifikace_hlasek(self):
        V7 = ['o', 'e', 'a', 'ó', 'é', 'á']
        V6 = ['i', 'u', 'í', 'ú', 'γ', 'y', 'ý']  # γ - kam s nim?
        R5 = ['j']
        R4 = ['r', 'ŕ', 'l', 'ľ', 'ĺ', 'ł']
        R3 = ['m', 'n', 'ň']
        T2 = ['v', 'f', 's', 'ś', 'z', 'ź', 'š', 'ž', 'ř', 'x', 'h']
        T1 = ['p', 'b', 't', 'd', 'ť', 'ď', 'c', 'ć', 'č', 'k', 'g']

        sonor_klasifikace = [V7, V6, R5, R4, R3, T2, T1]

        hlasky_sonorita = {}
        max_sonorita = 7
        for skupina in sonor_klasifikace:
            for hlaska in skupina:
                hlasky_sonorita[hlaska] = max_sonorita
            max_sonorita = max_sonorita - 1

        for znak in self.zmeny_slovo:
            for hlaska in hlasky_sonorita.keys():
                if znak == hlaska:
                    self.sonor_profil.append(hlasky_sonorita[hlaska])

    def find_pocet_sonor_vrch(self):
        pocet_sonoritnich_vrch = 0
        nastaveni_sonority = [4, 6, 7]
        for index, hodnota in enumerate(self.sonor_profil):
            if len(self.sonor_profil) != 1:
                if index != 0 and index != len(self.sonor_profil) - 1:
                    if hodnota in nastaveni_sonority:
                        if hodnota >= self.sonor_profil[index + 1] and hodnota >= self.sonor_profil[index - 1]:
                            pocet_sonoritnich_vrch += 1
                if index == 0:
                    if hodnota in nastaveni_sonority:
                        if hodnota >= self.sonor_profil[index + 1]:
                            pocet_sonoritnich_vrch += 1
                if index == len(self.sonor_profil) - 1:
                    if hodnota in nastaveni_sonority:
                        if hodnota >= self.sonor_profil[index - 1]:
                            pocet_sonoritnich_vrch += 1
            elif len(self.sonor_profil) == 1:
                if index == 0:
                    if (hodnota == 6) or (hodnota == 7):
                        pocet_sonoritnich_vrch += 1
        self.pocet_sonor_vrch = pocet_sonoritnich_vrch

    def set_hlasky_slova(self):
        split_slova = []
        for hlaska in self.zmeny_slovo:
            split_slova.append(hlaska)
        self.hlasky_slova = split_slova


class Vers:
    def __init__(self, id):
        self.id = id
        self.slova_verse = []
        self.zmenena_slova_verse = []
        self.delka_verse = 0 #v počtu slov
        self.sonor_profil_verse = []
        self.pocet_sonor_vrch_verse = 0
        self.hlasky_verse = []

    def vloz_slovo(self, slovo):
        slovo.pozice = len(self.slova_verse)
        self.slova_verse.append(slovo)
        self.zmenena_slova_verse.append(slovo.zmeny_slovo)
        self.delka()
        self.set_sonor_prof_verse()
        self.set_sonor_vrch_verse()
        self.set_hlasky_verse()

    def delka(self):
        self.delka_verse = len(self.slova_verse)

    def set_sonor_prof_verse(self):
        sonor_profily=[]
        for slovo in self.slova_verse:
            sonor_profily.append(slovo.sonor_profil)
        self.sonor_profil_verse = sonor_profily

    def set_sonor_vrch_verse(self):
        sonor_vrcholy=[]
        for slovo in self.slova_verse:
            sonor_vrcholy.append(slovo.pocet_sonor_vrch)
        self.pocet_sonor_vrch_verse = sum(sonor_vrcholy)

    def set_hlasky_verse(self):
        split_slova_verse = []
        for slovo in self.zmenena_slova_verse:
            for hlaska in slovo:
                split_slova_verse.append(hlaska)
        self.hlasky_verse = split_slova_verse

import os
import glob
path = 'C:/Users/Michaela/Desktop/basne/'
for filename in glob.glob(os.path.join(path, '*.txt')):
    head, tail = os.path.split(filename)
    name = os.path.splitext(tail)[0]
    basen = []
    with open(os.path.join(os.getcwd(), filename), encoding="UTF-8", mode ='r') as soubor:
        #print(filename)
        pocitadlo = 0

        for radek in soubor:
            if radek != "\n":
                pocitadlo += 1
                vers = Vers(pocitadlo)
                slova = radek.split(" ")
                #print(slova)
                for slovo in slova:
                    text = ""
                    povolene_znaky = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', \
                                          'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'v', 'y', 'z', 'á', 'é', 'í', 'ó', 'ý', \
                                          'č', 'ď', 'ě', 'ň', 'ř', 'š', 'ť', 'ů', 'ž', 'ú', 'q', 'w', 'ľ', 'ĺ', 'ł', 'ś', 'ź', 'ć', 'ŕ']
                    for znak in slovo.lower():
                        if znak in povolene_znaky:
                            text += znak
                    if text != "":
                        vers_slovo = Word(text, pocitadlo)
                        vers.vloz_slovo(vers_slovo)
                basen.append(vers)

    id_verse = []
    slova_verse = []
    sonoritni_profil_verse = []
    for vers in basen:
        id_verse.append(vers.id)
        slova_verse.append(vers.zmenena_slova_verse)
        sonoritni_profil_verse.append(vers.sonor_profil_verse)

    import pandas as pd

    # pokud složka neexistuje, vytvoří se
    path_output = 'C:/Users/Michaela/Desktop/vysledky/'
    if not os.path.exists(path_output):
        os.makedirs(path_output)

    df = pd.DataFrame({'id': id_verse, 'slova': slova_verse, 'sonoritni_profil_verse': sonoritni_profil_verse})
    df.to_csv(path_output + name + '_sonor_profily.csv', index=False, encoding='utf-8')

    import matplotlib.pyplot as plt
    output_dir = "C:/Users/Michaela/Desktop/vysledky/plots_" + name + "/"  # zadej cestu, kam chceš ukládat grafy

    # pokud složka neexistuje, vytvoří se
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    barvy = ["r", "g", "b", "y", "m", "r", "g", "b", "y", "m"]
    plots = []
    for vers in basen:
        pocitadlo = 0
        d = 0
        nazev_grafu = ""
        hodnoty_x = []
        labels = []
        for slovo in vers.slova_verse:
            hodnoty_x += range(d, d + len(slovo.sonor_profil))
            plt.plot(range(d, d + len(slovo.sonor_profil)), slovo.sonor_profil, ls='solid', marker='o',
                         color=barvy[pocitadlo])
            pocitadlo += 1
            labels += slovo.hlasky_slova
            d += len(slovo.sonor_profil) + 1
        plt.xticks(hodnoty_x, labels)
        plt.title(str(vers.id) + ". verš; " + str(vers.pocet_sonor_vrch_verse) + " vrcholů")
        plt.ylabel('sonority')
        filename = "vers_" + str(vers.id)
        plt.savefig(os.path.join(output_dir, filename), dpi=300)
        plt.clf()  # vyčistí se graf, aby se mohl vytvořit další

