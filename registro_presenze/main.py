import json
import os
from datetime import datetime


class Corso:
    """Gestisce le informazioni di un corso e le sue caratteristiche."""
    
    def __init__(self, nome, ore_totali, percentuale_minima=80):
        self.nome = nome
        self.ore_totali = ore_totali
        self.percentuale_minima = percentuale_minima
        self.lezioni = []
    
    def aggiungi_lezione(self, data):
        if data not in self.lezioni:
            self.lezioni.append(data)
            return True
        return False
    
    def rimuovi_lezione(self, data):
        if data in self.lezioni:
            self.lezioni.remove(data)
            return True
        return False
    
    def get_numero_lezioni(self):
        return len(self.lezioni)
    
    def mostra_info(self):
        print(f"\n--- Corso: {self.nome} ---")
        print(f"Ore totali: {self.ore_totali}h")
        print(f"Percentuale minima: {self.percentuale_minima}%")
        print(f"Lezioni svolte: {self.get_numero_lezioni()}")
        if self.lezioni:
            print(f"Date lezioni: {', '.join(sorted(self.lezioni))}")
    
    def to_dict(self):
        """Converte l'oggetto in dizionario per JSON."""
        return {
            'nome': self.nome,
            'ore_totali': self.ore_totali,
            'percentuale_minima': self.percentuale_minima,
            'lezioni': self.lezioni
        }
    
    @staticmethod
    def from_dict(data):
        """Crea un oggetto Corso da un dizionario."""
        corso = Corso(data['nome'], data['ore_totali'], data['percentuale_minima'])
        corso.lezioni = data.get('lezioni', [])
        return corso
    
    def __str__(self):
        return f"{self.nome} ({self.ore_totali}h, min {self.percentuale_minima}%)"


class Partecipante:
    """Gestisce le informazioni di un partecipante ai corsi."""
    
    _contatore_matricola = 1000
    
    def __init__(self, cognome, nome, data_iscrizione, matricola=None):
        self.cognome = cognome
        self.nome = nome
        self.data_iscrizione = data_iscrizione
        self.matricola = matricola if matricola else self._genera_matricola()
        self.corsi_iscritti = []
    
    @classmethod
    def _genera_matricola(cls):
        matricola = f"MAT{cls._contatore_matricola}"
        cls._contatore_matricola += 1
        return matricola
    
    @classmethod
    def set_contatore(cls, valore):
        """Imposta il contatore per la prossima matricola."""
        cls._contatore_matricola = valore
    
    def modifica_nome(self, nuovo_nome):
        self.nome = nuovo_nome
    
    def modifica_cognome(self, nuovo_cognome):
        self.cognome = nuovo_cognome
    
    def iscrivi_corso(self, nome_corso):
        if nome_corso not in self.corsi_iscritti:
            self.corsi_iscritti.append(nome_corso)
            return True
        return False
    
    def rimuovi_corso(self, nome_corso):
        if nome_corso in self.corsi_iscritti:
            self.corsi_iscritti.remove(nome_corso)
            return True
        return False
    
    def get_nome_completo(self):
        return f"{self.cognome} {self.nome}"
    
    def mostra_info(self):
        print(f"\n--- Partecipante: {self.get_nome_completo()} ---")
        print(f"Matricola: {self.matricola}")
        print(f"Data iscrizione: {self.data_iscrizione}")
        print(f"Corsi iscritti: {len(self.corsi_iscritti)}")
        if self.corsi_iscritti:
            for corso in self.corsi_iscritti:
                print(f"  - {corso}")
    
    def to_dict(self):
        """Converte l'oggetto in dizionario per JSON."""
        return {
            'cognome': self.cognome,
            'nome': self.nome,
            'data_iscrizione': self.data_iscrizione,
            'matricola': self.matricola,
            'corsi_iscritti': self.corsi_iscritti
        }
    
    @staticmethod
    def from_dict(data):
        """Crea un oggetto Partecipante da un dizionario."""
        partecipante = Partecipante(
            data['cognome'],
            data['nome'],
            data['data_iscrizione'],
            data['matricola']
        )
        partecipante.corsi_iscritti = data.get('corsi_iscritti', [])
        return partecipante
    
    def __str__(self):
        return f"{self.matricola} - {self.get_nome_completo()}"


class Presenza:
    """Gestisce le presenze dei partecipanti ai corsi."""
    
    def __init__(self):
        self.registro = {}
    
    def registra_presenza(self, nome_corso, data, matricola, stato='presente'):
        if nome_corso not in self.registro:
            self.registro[nome_corso] = {}
        
        if data not in self.registro[nome_corso]:
            self.registro[nome_corso][data] = {}
        
        self.registro[nome_corso][data][matricola] = stato
    
    def modifica_presenza(self, nome_corso, data, matricola, nuovo_stato):
        if (nome_corso in self.registro and 
            data in self.registro[nome_corso] and 
            matricola in self.registro[nome_corso][data]):
            self.registro[nome_corso][data][matricola] = nuovo_stato
            return True
        return False
    
    def get_presenza(self, nome_corso, data, matricola):
        if (nome_corso in self.registro and 
            data in self.registro[nome_corso] and 
            matricola in self.registro[nome_corso][data]):
            return self.registro[nome_corso][data][matricola]
        return None
    
    def get_presenze_corso(self, nome_corso):
        return self.registro.get(nome_corso, {})
    
    def get_presenze_data(self, nome_corso, data):
        if nome_corso in self.registro:
            return self.registro[nome_corso].get(data, {})
        return {}
    
    def get_presenze_partecipante(self, nome_corso, matricola):
        presenze_partecipante = {}
        if nome_corso in self.registro:
            for data, presenze in self.registro[nome_corso].items():
                if matricola in presenze:
                    presenze_partecipante[data] = presenze[matricola]
        return presenze_partecipante
    
    def calcola_percentuale(self, nome_corso, matricola):
        presenze = self.get_presenze_partecipante(nome_corso, matricola)
        if not presenze:
            return None
        
        totale = len(presenze)
        presenti = sum(1 for stato in presenze.values() if stato == 'presente')
        return round((presenti / totale) * 100, 2)
    
    def mostra_assenti_per_data(self, nome_corso, data):
        presenze = self.get_presenze_data(nome_corso, data)
        assenti = [mat for mat, stato in presenze.items() if stato == 'assente']
        
        print(f"\n--- Assenti per {nome_corso} il {data} ---")
        if assenti:
            for matricola in assenti:
                print(f"  - {matricola}")
        else:
            print("Nessun assente registrato")
        return assenti
    
    def mostra_report_corso(self, nome_corso, lista_partecipanti):
        print(f"\n{'='*60}")
        print(f"REPORT PRESENZE - {nome_corso}")
        print(f"{'='*60}")
        
        if nome_corso not in self.registro or not self.registro[nome_corso]:
            print("Nessuna presenza registrata per questo corso")
            return
        
        for partecipante in lista_partecipanti:
            if nome_corso in partecipante.corsi_iscritti:
                presenze = self.get_presenze_partecipante(nome_corso, partecipante.matricola)
                percentuale = self.calcola_percentuale(nome_corso, partecipante.matricola)
                
                print(f"\n{partecipante.get_nome_completo()} ({partecipante.matricola})")
                print(f"  Lezioni registrate: {len(presenze)}")
                if percentuale is not None:
                    print(f"  Percentuale presenza: {percentuale}%")
                    
                    presenti = sum(1 for s in presenze.values() if s == 'presente')
                    assenti = sum(1 for s in presenze.values() if s == 'assente')
                    print(f"  Presenze: {presenti} | Assenze: {assenti}")
    
    def elimina_presenze_corso(self, nome_corso):
        if nome_corso in self.registro:
            del self.registro[nome_corso]
            return True
        return False
    
    def elimina_presenze_partecipante(self, matricola):
        for nome_corso in self.registro:
            for data in self.registro[nome_corso]:
                if matricola in self.registro[nome_corso][data]:
                    del self.registro[nome_corso][data][matricola]
    
    def to_dict(self):
        """Converte l'oggetto in dizionario per JSON."""
        return self.registro
    
    @staticmethod
    def from_dict(data):
        """Crea un oggetto Presenza da un dizionario."""
        presenza = Presenza()
        presenza.registro = data
        return presenza


class Menu:
    """Gestisce l'interfaccia utente e coordina le operazioni."""
    
    def __init__(self):
        self.corsi = {}
        self.partecipanti = {}
        self.presenze = Presenza()
        self.file_corsi = 'corsi.json'
        self.file_presenze = 'presenze.json'
        self.carica_dati()
    
    def carica_dati(self):
        """Carica i dati dai file JSON all'avvio."""
        # Carica corsi
        if os.path.exists(self.file_corsi):
            try:
                with open(self.file_corsi, 'r', encoding='utf-8') as f:
                    dati_corsi = json.load(f)
                    
                    # Ripristina corsi
                    for nome, dati in dati_corsi['corsi'].items():
                        self.corsi[nome] = Corso.from_dict(dati)
                    
                    # Ripristina partecipanti
                    for matricola, dati in dati_corsi['partecipanti'].items():
                        self.partecipanti[matricola] = Partecipante.from_dict(dati)
                    
                    # Ripristina contatore matricole
                    if dati_corsi['partecipanti']:
                        max_num = max(int(m.replace('MAT', '')) for m in dati_corsi['partecipanti'].keys())
                        Partecipante.set_contatore(max_num + 1)
                    
                    print("✅ Dati corsi e partecipanti caricati con successo")
            except Exception as e:
                print(f"⚠️  Errore nel caricamento di {self.file_corsi}: {e}")
        
        # Carica presenze
        if os.path.exists(self.file_presenze):
            try:
                with open(self.file_presenze, 'r', encoding='utf-8') as f:
                    dati_presenze = json.load(f)
                    self.presenze = Presenza.from_dict(dati_presenze)
                    print("✅ Dati presenze caricati con successo")
            except Exception as e:
                print(f"⚠️  Errore nel caricamento di {self.file_presenze}: {e}")
    
    def salva_corsi(self):
        """Salva corsi e partecipanti nel file JSON."""
        try:
            dati = {
                'corsi': {nome: corso.to_dict() for nome, corso in self.corsi.items()},
                'partecipanti': {mat: part.to_dict() for mat, part in self.partecipanti.items()},
                'ultimo_aggiornamento': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
            
            with open(self.file_corsi, 'w', encoding='utf-8') as f:
                json.dump(dati, f, ensure_ascii=False, indent=2)
            
            print(f"💾 Dati salvati in {self.file_corsi}")
        except Exception as e:
            print(f"❌ Errore nel salvataggio: {e}")
    
    def salva_presenze(self):
        """Salva le presenze nel file JSON."""
        try:
            with open(self.file_presenze, 'w', encoding='utf-8') as f:
                json.dump(self.presenze.to_dict(), f, ensure_ascii=False, indent=2)
            
            print(f"💾 Presenze salvate in {self.file_presenze}")
        except Exception as e:
            print(f"❌ Errore nel salvataggio presenze: {e}")
    
    def seleziona_da_lista(self, lista, messaggio="Seleziona un'opzione"):
        """
        Mostra una lista numerata e permette la selezione.
        
        Args:
            lista: Lista di elementi da mostrare
            messaggio: Messaggio da visualizzare
            
        Returns:
            L'elemento selezionato o None se annullato
        """
        if not lista:
            return None
        
        print(f"\n{messaggio}:")
        for num, elemento in enumerate(lista, start=1):
            print(f"  {num}. {elemento}")
        print(f"  0. Annulla")
        
        while True:
            try:
                scelta = int(input("\nScegli numero: ").strip())
                if scelta == 0:
                    return None
                if 1 <= scelta <= len(lista):
                    return lista[scelta - 1]
                else:
                    print(f"❌ Inserisci un numero tra 0 e {len(lista)}")
            except ValueError:
                print("❌ Inserisci un numero valido")
    
    def avvia(self):
        """Avvia il menu principale dell'applicazione."""
        while True:
            self.mostra_menu_principale()
            scelta = input("\nScegli un'opzione: ").strip()
            
            if scelta == '1':
                self.gestione_corsi()
            elif scelta == '2':
                self.gestione_partecipanti()
            elif scelta == '3':
                self.gestione_presenze()
            elif scelta == '4':
                self.visualizza_report()
            elif scelta == '0':
                print("\n💾 Salvataggio dati finale...")
                self.salva_corsi()
                self.salva_presenze()
                print("\nGrazie per aver utilizzato il sistema. Arrivederci!")
                break
            else:
                print("\n❌ Opzione non valida. Riprova.")
    
    def mostra_menu_principale(self):
        """Visualizza il menu principale."""
        print("\n" + "="*50)
        print("SISTEMA GESTIONE PRESENZE")
        print("="*50)
        print("1. Gestione Corsi")
        print("2. Gestione Partecipanti")
        print("3. Gestione Presenze")
        print("4. Visualizza Report")
        print("0. Esci")
    
    # ========== GESTIONE CORSI ==========
    
    def gestione_corsi(self):
        """Menu per la gestione dei corsi."""
        while True:
            print("\n--- GESTIONE CORSI ---")
            print("1. Aggiungi nuovo corso")
            print("2. Visualizza tutti i corsi")
            print("3. Modifica corso")
            print("4. Elimina corso")
            print("5. Aggiungi lezione a corso")
            print("0. Torna al menu principale")
            
            scelta = input("\nScegli: ").strip()
            
            if scelta == '1':
                self.aggiungi_corso()
            elif scelta == '2':
                self.visualizza_corsi()
            elif scelta == '3':
                self.modifica_corso()
            elif scelta == '4':
                self.elimina_corso()
            elif scelta == '5':
                self.aggiungi_lezione()
            elif scelta == '0':
                break
            else:
                print("❌ Opzione non valida")
    
    def aggiungi_corso(self):
        """Aggiunge un nuovo corso al sistema."""
        print("\n--- Nuovo Corso ---")
        nome = input("Nome corso: ").strip()
        
        if nome in self.corsi:
            print(f"❌ Corso '{nome}' già esistente")
            return
        
        try:
            ore_totali = int(input("Ore totali: "))
            if ore_totali <= 0:
                print("❌ Le ore devono essere maggiori di 0")
                return
            
            perc_min = int(input("Percentuale minima (default 80): ").strip() or "80")
            if perc_min < 0 or perc_min > 100:
                print("❌ La percentuale deve essere tra 0 e 100")
                return
            
            nuovo_corso = Corso(nome, ore_totali, perc_min)
            self.corsi[nome] = nuovo_corso
            print(f"✅ Corso '{nome}' aggiunto con successo")
            self.salva_corsi()
            
        except ValueError:
            print("❌ Errore: inserire valori numerici validi")
    
    def visualizza_corsi(self):
        """Visualizza tutti i corsi disponibili."""
        if not self.corsi:
            print("\n📋 Nessun corso presente")
            return
        
        print("\n--- LISTA CORSI ---")
        for corso in self.corsi.values():
            corso.mostra_info()
    
    def modifica_corso(self):
        """Modifica i parametri di un corso esistente."""
        if not self.corsi:
            print("\n📋 Nessun corso da modificare")
            return
        
        nomi_corsi = list(self.corsi.keys())
        corso_selezionato = self.seleziona_da_lista(nomi_corsi, "Seleziona corso da modificare")
        
        if not corso_selezionato:
            print("❌ Operazione annullata")
            return
        
        corso = self.corsi[corso_selezionato]
        print(f"\nModifica di: {corso}")
        
        try:
            ore = input(f"Nuove ore totali (attuale: {corso.ore_totali}, invio per mantenere): ").strip()
            if ore:
                corso.ore_totali = int(ore)
            
            perc = input(f"Nuova percentuale minima (attuale: {corso.percentuale_minima}, invio per mantenere): ").strip()
            if perc:
                corso.percentuale_minima = int(perc)
            
            print(f"✅ Corso '{corso_selezionato}' modificato con successo")
            self.salva_corsi()
            
        except ValueError:
            print("❌ Errore: valori non validi")
    
    def elimina_corso(self):
        """Elimina un corso e le presenze associate."""
        if not self.corsi:
            print("\n📋 Nessun corso da eliminare")
            return
        
        nomi_corsi = list(self.corsi.keys())
        corso_selezionato = self.seleziona_da_lista(nomi_corsi, "Seleziona corso da eliminare")
        
        if not corso_selezionato:
            print("❌ Operazione annullata")
            return
        
        conferma = input(f"⚠️  Eliminare '{corso_selezionato}' e tutte le presenze associate? (si/no): ").strip().lower()
        if conferma == 'si':
            del self.corsi[corso_selezionato]
            self.presenze.elimina_presenze_corso(corso_selezionato)
            
            for partecipante in self.partecipanti.values():
                partecipante.rimuovi_corso(corso_selezionato)
            
            print(f"✅ Corso '{corso_selezionato}' eliminato con successo")
            self.salva_corsi()
            self.salva_presenze()
        else:
            print("❌ Eliminazione annullata")
    
    def aggiungi_lezione(self):
        """Aggiunge una lezione a un corso."""
        if not self.corsi:
            print("\n📋 Nessun corso disponibile")
            return
        
        nomi_corsi = list(self.corsi.keys())
        corso_selezionato = self.seleziona_da_lista(nomi_corsi, "Seleziona corso")
        
        if not corso_selezionato:
            print("❌ Operazione annullata")
            return
        
        data = input("Data lezione (YYYY-MM-DD): ").strip()
        if self.corsi[corso_selezionato].aggiungi_lezione(data):
            print(f"✅ Lezione del {data} aggiunta al corso '{corso_selezionato}'")
            self.salva_corsi()
        else:
            print(f"⚠️  Lezione del {data} già presente")
    
    # ========== GESTIONE PARTECIPANTI ==========
    
    def gestione_partecipanti(self):
        """Menu per la gestione dei partecipanti."""
        while True:
            print("\n--- GESTIONE PARTECIPANTI ---")
            print("1. Registra nuovo partecipante")
            print("2. Visualizza tutti i partecipanti")
            print("3. Modifica partecipante")
            print("4. Iscrivere partecipante a corso")
            print("5. Elimina partecipante")
            print("0. Torna al menu principale")
            
            scelta = input("\nScegli: ").strip()
            
            if scelta == '1':
                self.registra_partecipante()
            elif scelta == '2':
                self.visualizza_partecipanti()
            elif scelta == '3':
                self.modifica_partecipante()
            elif scelta == '4':
                self.iscrivi_partecipante_corso()
            elif scelta == '5':
                self.elimina_partecipante()
            elif scelta == '0':
                break
            else:
                print("❌ Opzione non valida")
    
    def registra_partecipante(self):
        """Registra un nuovo partecipante."""
        print("\n--- Nuovo Partecipante ---")
        cognome = input("Cognome: ").strip()
        nome = input("Nome: ").strip()
        data_iscrizione = input("Data iscrizione (YYYY-MM-DD): ").strip()
        
        nuovo_partecipante = Partecipante(cognome, nome, data_iscrizione)
        self.partecipanti[nuovo_partecipante.matricola] = nuovo_partecipante
        
        print(f"✅ Partecipante registrato con matricola: {nuovo_partecipante.matricola}")
        self.salva_corsi()
    
    def visualizza_partecipanti(self):
        """Visualizza tutti i partecipanti."""
        if not self.partecipanti:
            print("\n📋 Nessun partecipante registrato")
            return
        
        print("\n--- LISTA PARTECIPANTI ---")
        for partecipante in self.partecipanti.values():
            partecipante.mostra_info()
    
    def modifica_partecipante(self):
        """Modifica i dati di un partecipante."""
        if not self.partecipanti:
            print("\n📋 Nessun partecipante da modificare")
            return
        
        matricole = list(self.partecipanti.keys())
        lista_display = [f"{mat} - {self.partecipanti[mat].get_nome_completo()}" 
                        for mat in matricole]
        
        selezionato = self.seleziona_da_lista(lista_display, "Seleziona partecipante da modificare")
        
        if not selezionato:
            print("❌ Operazione annullata")
            return
        
        matricola = selezionato.split(' - ')[0]
        partecipante = self.partecipanti[matricola]
        
        print(f"\nModifica di: {partecipante}")
        
        nuovo_nome = input(f"Nuovo nome (attuale: {partecipante.nome}, invio per mantenere): ").strip()
        if nuovo_nome:
            partecipante.modifica_nome(nuovo_nome)
        
        nuovo_cognome = input(f"Nuovo cognome (attuale: {partecipante.cognome}, invio per mantenere): ").strip()
        if nuovo_cognome:
            partecipante.modifica_cognome(nuovo_cognome)
        
        print(f"✅ Partecipante modificato con successo")
        self.salva_corsi()
    
    def iscrivi_partecipante_corso(self):
        """Iscrive un partecipante a un corso."""
        if not self.partecipanti:
            print("\n📋 Nessun partecipante disponibile")
            return
        if not self.corsi:
            print("\n📋 Nessun corso disponibile")
            return
        
        # Seleziona partecipante
        matricole = list(self.partecipanti.keys())
        lista_display = [f"{mat} - {self.partecipanti[mat].get_nome_completo()}" 
                        for mat in matricole]
        
        selezionato = self.seleziona_da_lista(lista_display, "Seleziona partecipante")
        
        if not selezionato:
            print("❌ Operazione annullata")
            return
        
        matricola = selezionato.split(' - ')[0]
        
        # Seleziona corso
        nomi_corsi = list(self.corsi.keys())
        corso_selezionato = self.seleziona_da_lista(nomi_corsi, "Seleziona corso")
        
        if not corso_selezionato:
            print("❌ Operazione annullata")
            return
        
        partecipante = self.partecipanti[matricola]
        if partecipante.iscrivi_corso(corso_selezionato):
            print(f"✅ {partecipante.get_nome_completo()} iscritto a '{corso_selezionato}'")
            self.salva_corsi()
        else:
            print(f"⚠️  Partecipante già iscritto a '{corso_selezionato}'")
    
    def elimina_partecipante(self):
        """Elimina un partecipante e le presenze associate."""
        if not self.partecipanti:
            print("\n📋 Nessun partecipante da eliminare")
            return
        
        matricole = list(self.partecipanti.keys())
        lista_display = [f"{mat} - {self.partecipanti[mat].get_nome_completo()}" 
                        for mat in matricole]
        
        selezionato = self.seleziona_da_lista(lista_display, "Seleziona partecipante da eliminare")
        
        if not selezionato:
            print("❌ Operazione annullata")
            return
        
        matricola = selezionato.split(' - ')[0]
        partecipante = self.partecipanti[matricola]
        
        conferma = input(f"⚠️  Eliminare {partecipante.get_nome_completo()} e tutte le presenze? (si/no): ").strip().lower()
        
        if conferma == 'si':
            del self.partecipanti[matricola]
            self.presenze.elimina_presenze_partecipante(matricola)
            print(f"✅ Partecipante eliminato con successo")
            self.salva_corsi()
            self.salva_presenze()
        else:
            print("❌ Eliminazione annullata")
    
    # ========== GESTIONE PRESENZE ==========
    
    def gestione_presenze(self):
        """Menu per la gestione delle presenze."""
        while True:
            print("\n--- GESTIONE PRESENZE ---")
            print("1. Registra presenza/assenza")
            print("2. Modifica presenza")
            print("3. Visualizza presenze per data")
            print("4. Visualizza assenti per data")
            print("5. Visualizza presenze partecipante")
            print("0. Torna al menu principale")
            
            scelta = input("\nScegli: ").strip()
            
            if scelta == '1':
                self.registra_presenza_menu()
            elif scelta == '2':
                self.modifica_presenza_menu()
            elif scelta == '3':
                self.visualizza_presenze_data()
            elif scelta == '4':
                self.visualizza_assenti_data()
            elif scelta == '5':
                self.visualizza_presenze_partecipante()
            elif scelta == '0':
                break
            else:
                print("❌ Opzione non valida")
    
    def registra_presenza_menu(self):
        """Registra la presenza o assenza di un partecipante."""
        if not self.corsi:
            print("\n📋 Nessun corso disponibile")
            return
        if not self.partecipanti:
            print("\n📋 Nessun partecipante disponibile")
            return
        
        # Seleziona corso
        nomi_corsi = list(self.corsi.keys())
        corso_selezionato = self.seleziona_da_lista(nomi_corsi, "Seleziona corso")
        
        if not corso_selezionato:
            print("❌ Operazione annullata")
            return
        
        data = input("Data lezione (YYYY-MM-DD): ").strip()
        
        # Seleziona partecipante
        matricole = list(self.partecipanti.keys())
        lista_display = [f"{mat} - {self.partecipanti[mat].get_nome_completo()}" 
                        for mat in matricole]
        
        selezionato = self.seleziona_da_lista(lista_display, "Seleziona partecipante")
        
        if not selezionato:
            print("❌ Operazione annullata")
            return
        
        matricola = selezionato.split(' - ')[0]
        
        # Verifica iscrizione al corso
        if corso_selezionato not in self.partecipanti[matricola].corsi_iscritti:
            print(f"⚠️  Il partecipante non è iscritto al corso '{corso_selezionato}'")
            iscrivere = input("Vuoi iscriverlo ora? (si/no): ").strip().lower()
            if iscrivere == 'si':
                self.partecipanti[matricola].iscrivi_corso(corso_selezionato)
                self.salva_corsi()
            else:
                return
        
        stato = input("Stato (p=presente, a=assente): ").strip().lower()
        if stato == 'p':
            stato_completo = 'presente'
        elif stato == 'a':
            stato_completo = 'assente'
        else:
            print("❌ Stato non valido")
            return
        
        self.presenze.registra_presenza(corso_selezionato, data, matricola, stato_completo)
        print(f"✅ Presenza registrata: {self.partecipanti[matricola].get_nome_completo()} - {stato_completo}")
        self.salva_presenze()
    
    def modifica_presenza_menu(self):
        """Modifica una presenza già registrata."""
        if not self.corsi:
            print("\n📋 Nessun corso disponibile")
            return
        
        # Seleziona corso
        nomi_corsi = list(self.corsi.keys())
        corso_selezionato = self.seleziona_da_lista(nomi_corsi, "Seleziona corso")
        
        if not corso_selezionato:
            return
        
        data = input("Data lezione (YYYY-MM-DD): ").strip()
        
        # Seleziona partecipante
        matricole = list(self.partecipanti.keys())
        lista_display = [f"{mat} - {self.partecipanti[mat].get_nome_completo()}" 
                        for mat in matricole]
        
        selezionato = self.seleziona_da_lista(lista_display, "Seleziona partecipante")
        
        if not selezionato:
            return
        
        matricola = selezionato.split(' - ')[0]
        
        presenza_attuale = self.presenze.get_presenza(corso_selezionato, data, matricola)
        if presenza_attuale is None:
            print("❌ Presenza non trovata")
            return
        
        print(f"Stato attuale: {presenza_attuale}")
        nuovo_stato = input("Nuovo stato (p=presente, a=assente): ").strip().lower()
        
        if nuovo_stato == 'p':
            stato_completo = 'presente'
        elif nuovo_stato == 'a':
            stato_completo = 'assente'
        else:
            print("❌ Stato non valido")
            return
        
        if self.presenze.modifica_presenza(corso_selezionato, data, matricola, stato_completo):
            print(f"✅ Presenza modificata in: {stato_completo}")
            self.salva_presenze()
        else:
            print("❌ Errore nella modifica")
    
    def visualizza_presenze_data(self):
        """Visualizza tutte le presenze di una specifica data."""
        if not self.corsi:
            print("\n📋 Nessun corso disponibile")
            return
        
        # Seleziona corso
        nomi_corsi = list(self.corsi.keys())
        corso_selezionato = self.seleziona_da_lista(nomi_corsi, "Seleziona corso")
        
        if not corso_selezionato:
            return
        
        data = input("Data (YYYY-MM-DD): ").strip()
        
        presenze_data = self.presenze.get_presenze_data(corso_selezionato, data)
        
        if not presenze_data:
            print(f"\n📋 Nessuna presenza registrata per {corso_selezionato} il {data}")
            return
        
        print(f"\n--- Presenze {corso_selezionato} - {data} ---")
        for matricola, stato in presenze_data.items():
            if matricola in self.partecipanti:
                nome = self.partecipanti[matricola].get_nome_completo()
                simbolo = "✓" if stato == 'presente' else "✗"
                print(f"{simbolo} {nome} ({matricola}): {stato}")
    
    def visualizza_assenti_data(self):
        """Visualizza gli assenti di una specifica data."""
        if not self.corsi:
            print("\n📋 Nessun corso disponibile")
            return
        
        # Seleziona corso
        nomi_corsi = list(self.corsi.keys())
        corso_selezionato = self.seleziona_da_lista(nomi_corsi, "Seleziona corso")
        
        if not corso_selezionato:
            return
        
        data = input("Data (YYYY-MM-DD): ").strip()
        
        assenti = self.presenze.mostra_assenti_per_data(corso_selezionato, data)
        
        if assenti:
            print("\nDettagli assenti:")
            for matricola in assenti:
                if matricola in self.partecipanti:
                    self.partecipanti[matricola].mostra_info()
    
    def visualizza_presenze_partecipante(self):
        """Visualizza tutte le presenze di un partecipante in un corso."""
        if not self.partecipanti:
            print("\n📋 Nessun partecipante disponibile")
            return
        if not self.corsi:
            print("\n📋 Nessun corso disponibile")
            return
        
        # Seleziona partecipante
        matricole = list(self.partecipanti.keys())
        lista_display = [f"{mat} - {self.partecipanti[mat].get_nome_completo()}" 
                        for mat in matricole]
        
        selezionato = self.seleziona_da_lista(lista_display, "Seleziona partecipante")
        
        if not selezionato:
            return
        
        matricola = selezionato.split(' - ')[0]
        
        # Seleziona corso
        nomi_corsi = list(self.corsi.keys())
        corso_selezionato = self.seleziona_da_lista(nomi_corsi, "Seleziona corso")
        
        if not corso_selezionato:
            return
        
        partecipante = self.partecipanti[matricola]
        presenze = self.presenze.get_presenze_partecipante(corso_selezionato, matricola)
        percentuale = self.presenze.calcola_percentuale(corso_selezionato, matricola)
        
        print(f"\n--- Presenze di {partecipante.get_nome_completo()} ---")
        print(f"Corso: {corso_selezionato}")
        
        if not presenze:
            print("📋 Nessuna presenza registrata")
            return
        
        print(f"\nTotale lezioni registrate: {len(presenze)}")
        if percentuale is not None:
            print(f"Percentuale presenza: {percentuale}%")
            
            soglia = self.corsi[corso_selezionato].percentuale_minima
            if percentuale < soglia:
                print(f"⚠️  ATTENZIONE: sotto la soglia minima ({soglia}%)")
        
        print("\nDettaglio:")
        for data in sorted(presenze.keys()):
            stato = presenze[data]
            simbolo = "✓" if stato == 'presente' else "✗"
            print(f"  {simbolo} {data}: {stato}")
    
    # ========== REPORT ==========
    
    def visualizza_report(self):
        """Menu per visualizzare report e statistiche."""
        while True:
            print("\n--- REPORT E STATISTICHE ---")
            print("1. Report completo per corso")
            print("2. Studenti sotto soglia minima")
            print("3. Statistiche generali")
            print("0. Torna al menu principale")
            
            scelta = input("\nScegli: ").strip()
            
            if scelta == '1':
                self.report_corso()
            elif scelta == '2':
                self.studenti_sotto_soglia()
            elif scelta == '3':
                self.statistiche_generali()
            elif scelta == '0':
                break
            else:
                print("❌ Opzione non valida")
    
    def report_corso(self):
        """Genera report completo per un corso."""
        if not self.corsi:
            print("\n📋 Nessun corso disponibile")
            return
        
        # Seleziona corso
        nomi_corsi = list(self.corsi.keys())
        corso_selezionato = self.seleziona_da_lista(nomi_corsi, "Seleziona corso")
        
        if not corso_selezionato:
            return
        
        partecipanti_corso = [p for p in self.partecipanti.values() 
                              if corso_selezionato in p.corsi_iscritti]
        
        if not partecipanti_corso:
            print(f"\n📋 Nessun partecipante iscritto a '{corso_selezionato}'")
            return
        
        self.presenze.mostra_report_corso(corso_selezionato, partecipanti_corso)
    
    def studenti_sotto_soglia(self):
        """Visualizza studenti con presenza sotto la soglia minima."""
        if not self.corsi:
            print("\n📋 Nessun corso disponibile")
            return
        
        # Seleziona corso
        nomi_corsi = list(self.corsi.keys())
        corso_selezionato = self.seleziona_da_lista(nomi_corsi, "Seleziona corso")
        
        if not corso_selezionato:
            return
        
        corso = self.corsi[corso_selezionato]
        soglia = corso.percentuale_minima
        
        print(f"\n--- Studenti sotto soglia {soglia}% per {corso_selezionato} ---")
        
        trovati = False
        for partecipante in self.partecipanti.values():
            if corso_selezionato in partecipante.corsi_iscritti:
                percentuale = self.presenze.calcola_percentuale(corso_selezionato, partecipante.matricola)
                if percentuale is not None and percentuale < soglia:
                    print(f"⚠️  {partecipante.get_nome_completo()} ({partecipante.matricola}): {percentuale}%")
                    trovati = True
        
        if not trovati:
            print("✅ Tutti gli studenti sono sopra la soglia minima")
    
    def statistiche_generali(self):
        """Visualizza statistiche generali del sistema."""
        print("\n" + "="*50)
        print("STATISTICHE GENERALI")
        print("="*50)
        
        print(f"\n📚 Corsi totali: {len(self.corsi)}")
        print(f"👥 Partecipanti totali: {len(self.partecipanti)}")
        
        if self.corsi:
            print("\nDettaglio corsi:")
            for nome_corso, corso in self.corsi.items():
                iscritti = sum(1 for p in self.partecipanti.values() 
                              if nome_corso in p.corsi_iscritti)
                print(f"  • {nome_corso}: {iscritti} iscritti, {corso.get_numero_lezioni()} lezioni")
        
        if self.presenze.registro:
            print("\nPresenze registrate:")
            for nome_corso in self.presenze.registro:
                totale_registrazioni = sum(len(p) for p in self.presenze.registro[nome_corso].values())
                print(f"  • {nome_corso}: {totale_registrazioni} registrazioni")


# ========== PUNTO DI INGRESSO ==========

if __name__ == "__main__":
    app = Menu()
    app.avvia()
