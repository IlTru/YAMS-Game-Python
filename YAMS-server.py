import socket
import numpy as np
import random as rn

class YAMS:
    def __init__(self, N1 = 0, N2 = 0, N3 = 0, N4 = 0, N5 = 0, N6 = 0, BONUS = 0, JOKER = 0, TRIPLA = 0, CHINTA = 0, FULL = 0, CAREU = 0, YAMS = 0, TOTAL = 0,\
                 mN1 = False, mN2 = False, mN3 = False, mN4 = False, mN5 = False, mN6 = False, mBONUS = False, mJOKER = False, mTRIPLA = False, mCHINTA = False, mFULL = False, mCAREU = False, mYAMS = False, zaruri = [], R = 2, zaruri_pastrate = []):
        self.N1 = 0 #am egalat fiecare rand al tabelului cu 0
        self.N2 = 0
        self.N3 = 0
        self.N4 = 0
        self.N5 = 0
        self.N6 = 0
        self.BONUS = 0
        self.JOKER = 0
        self.TRIPLA = 0
        self.CHINTA = 0
        self.FULL = 0
        self.CAREU = 0
        self.YAMS = 0
        self.TOTAL = 0

        self.mN1 = False #aceste variabile ne spun daca punctajul a fost modificat sau nu, m vine de la "modificat"
        self.mN2 = False
        self.mN3 = False
        self.mN4 = False
        self.mN5 = False
        self.mN6 = False
        self.mBONUS = False
        self.mJOKER = False
        self.mTRIPLA = False
        self.mCHINTA = False
        self.mFULL = False
        self.mCAREU = False
        self.mYAMS = False

        self.zaruri = [] #un vector in care memorez zarurile aruncate

        self.R = 3 #o variabila in care memorez care aruncari mai are la dispozitie jucatorul

        self.zaruri_pastrate = [] #un vector in care pastrez zarurile salvate de catre jucator

    def afisare_tabel(self): #metoda prin care returnez un string cu toate randurile tabelului, daca (exemplu) mN1 este fals nu voi scrie nimic in dreptul randului deoarece acel rand nu a fost modificat
        response = 'Punctaj:\n'
        response = response + (f'N1 -----> {self.N1}\n' if self.mN1 else 'N1 ----->\n')
        response = response + (f'N2 -----> {self.N2}\n' if self.mN2 else 'N2 ----->\n')
        response = response + (f'N3 -----> {self.N3}\n' if self.mN3 else 'N3 ----->\n')
        response = response + (f'N4 -----> {self.N4}\n' if self.mN4 else 'N4 ----->\n')
        response = response + (f'N5 -----> {self.N5}\n' if self.mN5 else 'N5 ----->\n')
        response = response + (f'N6 -----> {self.N6}\n' if self.mN6 else 'N6 ----->\n')
        response = response + (f'BONUS -----> {self.BONUS}\n')
        response = response + (f'JOKER -----> {self.JOKER}\n' if self.mJOKER else 'JOKER ----->\n')
        response = response + (f'TRIPLA -----> {self.TRIPLA}\n' if self.mTRIPLA else 'TRIPLA ----->\n')
        response = response + (f'CHINTA -----> {self.CHINTA}\n' if self.mCHINTA else 'CHINTA ----->\n')
        response = response + (f'FULL -----> {self.FULL}\n' if self.mFULL else 'FULL ----->\n')
        response = response + (f'CAREU -----> {self.CAREU}\n' if self.mCAREU else 'CAREU ----->\n')
        response = response + (f'YAMS -----> {self.YAMS}\n' if self.mYAMS else 'YAMS ----->\n')
        response = response + (f'TOTAL -----> {self.TOTAL}\n')

        return response

    def arunca_zaruri0(self): #metoda pe care o folosesc de fiecare data cand jucatorul trebuie sa arunce zarurile dupa ce a modificat punctajul sau daca este prima aruncare
        if self.R != 3: #daca jucatorul incearca sa arunce toate zarurile inainte de a completa un rand din tabel aceasta metoda va returna False si va rezulta o eroare
            return False
        self.R = 2
        self.zaruri = [] #resetez cei doi vectori in care am memorat zarurile salvate precedent
        self.zaruri_pastrate = []
        for i in range(5):
            self.zaruri.append(rn.randrange(1, 7)) #generez alte valori in mod random pentru vectorul zaruri
        return True

    def arunca_zaruri1(self): #metoda pe care o apelez atunci cand jocatorul pastreaza anumite zaruri si le arunca pe celelalte
        self.zaruri = []
        for i in range(5 - len(self.zaruri_pastrate)): #aflu cate valori trebuie sa generez scazandu-le pe cele salvate
            self.zaruri.append(rn.randrange(1, 7))

    def afisare_zaruri(self): #metoda pe care o folosesc cand trebuie sa afisez zarurile ordonate
        self.zaruri = np.sort(self.zaruri)
        self.zaruri = self.zaruri.tolist() #deoarece metoda np.sort() va genera un ndarray voi folosi instructiunea tolist() pentru a ma intoarce la o lista simpla
        return self.zaruri

    def afisare_zaruri_pastrate(self): #metoda similara cu cea in care returnez zarurile doar ca in aceasta voi returna zarurile pastrate
        self.zaruri_pastrate = np.sort(self.zaruri_pastrate)
        self.zaruri_pastrate = self.zaruri_pastrate.tolist()
        return self.zaruri_pastrate

    def keep(self, message): #metoda keep apelata atunci cand jucatorul tasteaza KEEP []
        if (self.R == 0): #daca self.R = 0 atunci inseamna ca jucatorul nu mai poate sa pastreze zaruri
            return 1 #am ales valoarea 1 pentru aceasta eroare pentru a o diferentia de cealalta eroare

        if (self.R == 3): #daca self.R = 3 atunci inseamna ca jucatorul a completat un rand din tabel in ultima comanda si trebuie sa arunce din nou toate zarurile
            return 2

        v = [] #am folosit un alt vector pentru a memora valorile introduse de catre jucator
        for char in message:
            if (char in '123456'):
                if (self.zaruri.count((int)(char)) != 0):
                    self.zaruri.remove((int)(char)) #daca acea valoare exista in self.zaruri atunci o elimin si o introduc in vectorul v
                    v.append((int)(char))
                else:
                    self.zaruri = self.zaruri + v #daca acea valoare nu exista in vectorul azaruri atunci inseamna ca jucatorul nu a introdus bine valorile asadar voi reconstrui vectorul zaruri
                    return 2 #pentru aceasta eroare am ales tot valoarea 2 tratandu-le la pachet
        self.zaruri_pastrate = self.zaruri_pastrate + v #daca totul a mers bine lipesc vectorul zaruri_salvate de vectorul v
        self.R = self.R - 1 #numarul de relansari scade cu 1
        return 0

    def tabel_completat(self): #verific daca tabelul a fost completat
        if (self.mN1 == self.mN2 == self.mN3 == self.mN4 == self.mN5 == self.mN6 == self.mJOKER == self.mTRIPLA == self.mCHINTA == self.mFULL == self.mCAREU == self.mYAMS == True):
            return True

    def modifica_punctaj(self, text): #metoda prin care modific punctajul si tratez eventualele erori
        if (self.R == 3): #daca self.R = 3 inseamna ca jucatorul trebuie sa arunce zarurile deoarece a completat deja un rand al tabelului mai inainte
            return 2
        if (self.mBONUS == 0):
            if(self.N1 + self.N2 + self.N3 + self.N4 + self.N5 + self.N6 >=63):
                self.TOTAL = self.TOTAL + 50
                self.BONUS = 50
                self.mBONUS = True

        if(text == "N1"): #verific textul introdus de jucator
            if(self.mN1 == False): #daca acest rand nu a mai fost completat in completez cu rezultatul corespunzator
                self.zaruri = self.zaruri + self.zaruri_pastrate
                self.R = 3
                self.TOTAL = self.TOTAL + self.zaruri.count(1) #actualizez punctajul total
                self.N1 = self.zaruri.count(1)
                self.mN1 = True
                return 0
            else:
                return 1 #daca acest rand a mai fost completat o data voi returna valoarea 1 si voi transmite mesajul corespunzator
        elif(text == "N2"):
            if (self.mN2 == False):
                self.zaruri = self.zaruri + self.zaruri_pastrate
                self.R = 3
                self.TOTAL = self.TOTAL + self.zaruri.count(2)*2
                self.N2 = self.zaruri.count(2)*2
                self.mN2 = True
                return 0
            else:
                return 1
        elif (text == "N3"):
            if (self.mN3 == False):
                self.zaruri = self.zaruri + self.zaruri_pastrate
                self.R = 3
                self.TOTAL = self.TOTAL + self.zaruri.count(3)*3
                self.N3 = self.zaruri.count(3)*3
                self.mN3 = True
                return 0
            else:
                return 1
        elif (text == "N4"):
            if (self.mN4 == False):
                self.zaruri = self.zaruri + self.zaruri_pastrate
                self.R = 3
                self.TOTAL = self.TOTAL + self.zaruri.count(4)*4
                self.N4 = self.zaruri.count(4)*4
                self.mN4 = True
                return 0
            else:
                return 1
        elif (text == "N5"):
            if (self.mN5 == False):
                self.zaruri = self.zaruri + self.zaruri_pastrate
                self.R = 3
                self.TOTAL = self.TOTAL + self.zaruri.count(5)*5
                self.N5 = self.zaruri.count(5)*5
                self.mN5 = True
                return 0
            else:
                return 1
        elif (text == "N6"):
            if (self.mN6 == False):
                self.zaruri = self.zaruri + self.zaruri_pastrate
                self.R = 3
                self.TOTAL = self.TOTAL + self.zaruri.count(6)*6
                self.N6 = self.zaruri.count(6)*6
                self.mN6 = True
                return 0
            else:
                return 1
        elif (text == "JOKER"):
            if (self.mJOKER == False):
                self.zaruri = self.zaruri + self.zaruri_pastrate
                self.R = 3
                self.TOTAL = self.TOTAL + np.sum(self.zaruri)
                self.JOKER = np.sum(self.zaruri)
                self.mJOKER = True
                return 0
            else:
                return 1
        elif (text == "TRIPLA"):
            if (self.mTRIPLA == False):
                self.zaruri = self.zaruri + self.zaruri_pastrate
                self.R = 3
                if(self.zaruri.count(1) >= 3 or self.zaruri.count(2) >= 3 or self.zaruri.count(3) >= 3 or self.zaruri.count(4) >= 3 or self.zaruri.count(5) >= 3 or self.zaruri.count(6) >= 3):
                    self.TOTAL = self.TOTAL + np.sum(self.zaruri)
                    self.TRIPLA = np.sum(self.zaruri)
                    self.mTRIPLA = True
                    return 0
                else:
                    self.TRIPLA = 0
                    self.mTRIPLA = True
                    return 0
            else:
                return 1
        elif (text == "CHINTA"):
            if (self.mCHINTA == False):
                self.zaruri = self.zaruri + self.zaruri_pastrate
                self.R = 3
                self.zaruri = np.sort(self.zaruri)
                self.zaruri = self.zaruri.tolist()
                if(self.zaruri[0] == (self.zaruri[1]-1) == (self.zaruri[2]-2) == (self.zaruri[3]-3) == (self.zaruri[4]-4)):
                    self.TOTAL = self.TOTAL + 20
                    self.CHINTA = 20
                    self.mCHINTA = True
                    return 0
                else:
                    self.CHINTA = 0
                    self.mCHINTA = True
                    return 0
            else:
                return 1
        elif (text == "FULL"):
            if (self.mFULL == False):
                self.zaruri = self.zaruri + self.zaruri_pastrate
                self.R = 3
                if ((self.zaruri.count(1) == 3 or self.zaruri.count(2) == 3 or self.zaruri.count(3) == 3 or self.zaruri.count(4) == 3 or self.zaruri.count(5) == 3 or self.zaruri.count(6) == 3) \
                        and (self.zaruri.count(1) == 2 or self.zaruri.count(2) == 2 or self.zaruri.count(3) == 2 or self.zaruri.count(4) == 2 or self.zaruri.count(5) == 2 or self.zaruri.count(6) == 2)):
                    self.TOTAL = self.TOTAL + 30
                    self.FULL = 30
                    self.mFULL = True
                    return 0
                else:
                    self.FULL = 0
                    self.mFULL = True
                    return 0
            else:
                return 1
        elif (text == "CAREU"):
            self.zaruri = self.zaruri + self.zaruri_pastrate
            self.R = 3
            if (self.mCAREU == False):
                if(self.zaruri.count(1) >= 4 or self.zaruri.count(2) >= 4 or self.zaruri.count(3) >= 4 or self.zaruri.count(4) >= 4 or self.zaruri.count(5) >= 4 or self.zaruri.count(6) >= 4):
                    self.TOTAL = self.TOTAL + 40
                    self.CAREU = 40
                    self.mCAREU = True
                    return 0
                else:
                    self.CAREU = 0
                    self.mCAREU = True
                    return 0
            else:
                return 1
        elif (text == "YAMS"):
            self.zaruri = self.zaruri + self.zaruri_pastrate
            self.R = 3
            if (self.mYAMS == False):
                if(self.zaruri[0] == self.zaruri[1] == self.zaruri[2] == self.zaruri[3] == self.zaruri[4]):
                    self.TOTAL = self.TOTAL + 50
                    self.YAMS = 50
                    self.mYAMS = True
                    return 0
                else:
                    self.YAMS = 0
                    self.mYAMS = True
                    return 0
            else:
                return 1
        else:
            return 1

class Server_YAMS: #clasa serverului
    def __init__(self, host='127.0.0.1', port=8888): #initializarea
        self.host = host
        self.port = port

    def start(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((self.host, self.port))
        server_socket.listen(500)
        print("Server TCP gata! ", server_socket.getsockname())
        conn_socket, client_address = server_socket.accept()

        tabel_creat = False #atentionez faptul ca jocul nu a inceput in cazul in care jucatorul doreste sa arunce zarurile sau sa faca altceva

        while True:
            message_from_client = conn_socket.recv(100)  # primeste mesajul clientului
            message_from_client = message_from_client.decode() #decodific mesajul clientului
            if message_from_client == 'START':
                response = 'Ati inceput un nou meci de YAMS!'
                tabel_creat = True #jocul a inceput, tabelul s-a creat
                tabel = YAMS()
                response = response+'\n'+tabel.afisare_tabel()
                response = response+'\nTastati ARUNCA pentru a arunca zarurile.'
                conn_socket.send(response.encode()) #formez raspunsul si il trimit codificat
            elif message_from_client == 'ARUNCA' and tabel_creat == True:
                if(tabel.arunca_zaruri0()): #daca jucatorul poate arunca zarurile in acel moment metoda aruna_zaruri va returna True, altfel va returna False
                    response = (str) (tabel.afisare_zaruri())
                    response = response + f' R={tabel.R}'
                    conn_socket.send(response.encode())
                else:
                    response = 'Nu puteti arunca zarurile in acest moment.' #atentionez jucatorul ca nu poate arunca zarurile dupa ce le-a aruncat deja o data
                    conn_socket.send(response.encode())
            elif message_from_client in 'N1N2N3N4N5N6JOKERTRIPLACHINTAFULLCAREUYAMS' and tabel_creat == True and tabel.zaruri != []:
                code = tabel.modifica_punctaj(message_from_client) #primesc codul returnat de catre metoda modifica_punctaj si tratez cele 3 coduri in parte
                if(code == 0): #verific daca nu au aparut erori
                    if (tabel.tabel_completat()): #verific daca tabelul este completat in acest moment
                        response = 'Felicitari! Ati completat tot tabelul!\n'
                        response = response + tabel.afisare_tabel()
                        response = response + 'CLOSE SESSION'
                        conn_socket.send(response.encode())
                        conn_socket.close() #daca tabelul este completat il trimit ca mesaj la pachet cu mesajul 'CLOSE SESSION' pentru a transmite masinii clientului faptul ca jocul s-a inceiat si ca trebuie sa inchida sesiunea
                        break
                    else:
                        response = 'Tabel actualizat. ' \
                                   '\nTastati PUNCTAJ pentru afisarea tabelului cu punctajele la momentul actual sau ARUNCA pentru a arunca din nou zarurile'
                        conn_socket.send(response.encode()) #in cazul in care tabelul nu este inca completat voi transmite jucatorului faptul ca tabelul a fost actualizat si ca poate continua jocul
                elif(code == 1): #prima eroare care poate fi generata cand jucatorul vrea sa completeze un rand al tabelului
                    response = 'Randul tastat nu exista in tabel sau a fost deja completat.'
                    conn_socket.send(response.encode())
                else:
                    response = 'Nu puteti completa tabelul in acest moment, trebuie sa aruncati din nou zarurile!' #a doua eroare
                    conn_socket.send(response.encode())
            elif "KEEP" in message_from_client and tabel_creat == True:
                code = tabel.keep(message_from_client) #salvez codul returnat de catre metoda keep si tratez fiecate situatie in parte
                if(code == 0):
                    tabel.arunca_zaruri1()
                    response = (str) (tabel.afisare_zaruri())
                    response = response + f' R={tabel.R}'
                    response = response + f'  zaruri pastrate: {(str) (tabel.afisare_zaruri_pastrate())}'
                    conn_socket.send(response.encode())
                elif(code == 1):
                    z = tabel.afisare_zaruri() + tabel.afisare_zaruri_pastrate()
                    z = np.sort(z)
                    z = z.tolist()
                    response = 'Nu mai puteti arunca zarurile, completati tabelul!' + f'\nZaruri la dispozitie: {(str) (z)}'
                    conn_socket.send(response.encode())
                else:
                    response = 'Eroare, nu ati tastat zarurile corect sau trebuie sa aruncati din nou zarurile.'
                    conn_socket.send(response.encode())
            elif message_from_client == 'PUNCTAJ' and tabel_creat == True:
                response = tabel.afisare_tabel()
                conn_socket.send(response.encode())
            elif message_from_client == 'ABANDON':
                response = b'Vreti sa incheiati sesiunea de YAMS?\n           DA/NU'
                conn_socket.send(response)
                message_from_client = conn_socket.recv(50)
                message_from_client = message_from_client.decode()
                if message_from_client == 'DA':
                    response = b'CLOSE SESSION'
                    conn_socket.send(response)
                    conn_socket.close()
                    break
                elif message_from_client == 'NU':
                    response = b'Sesiunea nu a fost inchisa.'
                    conn_socket.send(response)
                else:
                    response = b'Fiindca ati tastat alceva in loc de DA sau NU sesiunea nu a fost inchisa.'
                    conn_socket.send(response)
            else:
                response = 'COMANDA ERONATA'
                conn_socket.send(response.encode())

    def prepare_response(self, data):
        return data

server = Server_YAMS()
server.start()

