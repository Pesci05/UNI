# CRIMINI TECNOLOGICI
#28/09
Esistono vari tipi di crimini infomatici come:
- High tech Crime 
- Cybercrime 
- Computer crime 
- Crimine informatico 
- Internet Crime 
- Web crime 
- Digital crime
- **PHISHING**
	Tipo di attacco che punta sull'ingannare persone tramite email, per rubare sold e dati.
- etc...

Le tecnologie attuali possno essere:
- Le tecnologie digitali possono essere **obiettivo** del crimine 
- Le tecnologie digitali possono essere utilizzate come **strumento** del crimine 
- Le tecnologie digitali possono essere utilizzate come **testimoni** del crimine
Molte persone accusano **internet stesso** per l'esistenza di questo tipo di crimini, ma non è giusto poichè, internet è un mezzo che promuove il massimo scambio d'informazioni.
L'errore è stato cambiare lo scopo di Internet, perchè diventato un sistema di interconnessione  comunicazione a livello globale.

## RISCHIO
È la probabilità che una determinata **minaccia** ha di sfruttare la **vulnerabilità** di una **risorsa (asset)** e quindi di causare **impatti indesiderati**.

## VULNERABILITÀ TECNOLOGICHE
**Evoluzione dei sistemi informatici** 
**Prima**: 
- Sistemi informatici (CED) non collegati a reti esterne 
- Mainframe centrale e terminali “stupidi” (solo video/tastiera) 
- Connessioni dedicate, sempre wired, non condivise 
**Oggi**: 
- Miliardi di sistemi collegati a Internet 
- Data center con server distribuiti su reti LAN e WAN 
- Terminali intelligenti (PC, smartphone, ecc) 
- Reti non dedicate 
- Trasmissioni digitali di voce e qualunque tipo di dati 
- Reti wireless

**Evoluzione delle applicazioni e servizi informatici 
Prima**: 
- Poche applicazioni informatiche indispensabili per il funzionamento complessivo dell’organ 
- Poche informazioni digitalizzate e memorizzate in database 
- Pochi dipendenti autorizzati ad accedere alle informazioni digitali 
- Poche applicazioni (forse nessuna) con vincoli di interattività e di disponibilità deter- minanti per il successo dell’organizzazione 
**Oggi**: 
- Applicazioni informatiche diffuse 
- Tutte, ma proprio tutte, le informazioni (anche) in formato digitale 
- Molteplici applicazioni devono essere sempre attive, almeno nelle ore di ufficio, e molte operazioni avvengono di notte non presidiate

Le vulnerabilità di un sistema informatico possono essere:
- **Tecnologiche**: [[2_TerminologiaSicurezza.pdf#page=13|2_TerminologiaSicurezza, pagina 13]]
- **Complessità**: [[2_TerminologiaSicurezza.pdf#page=14|2_TerminologiaSicurezza, pagina 14]]
- **Sviluppatori software**
- **Sistemisti**
- **Management**
- **Personale**: [[2_TerminologiaSicurezza.pdf#page=15|2_TerminologiaSicurezza, pagina 15]]
- **Time To Market**:[[2_TerminologiaSicurezza.pdf#page=16|2_TerminologiaSicurezza, pagina 16]]

# ATTACANTI
Chi sono?
- **HACKER** (?) 
- **CRACKER**
- **LAMER** 
- **BLACK HAT** 
- **WHITE HAT**
- **ATTACKER INTERNO**
Si usa il termine ATTACKER o AVVERSARI. HACKER è un complimento da meritare.
![[Pasted image 20260928113901.png]]

## Evoluzione degli attacker
**Anni ’70: nasce la cultura hacker** 
- Inoffensiva nella maggior parte dei casi 
- Raramente malintenzionata 
**Anni ’80: si diffonde la cultura hacker** 
**Anni ’90: Internet vandals** 
- Prevalentemente giovanile 
- Spesso malintenzionata, ma non per denaro Intrusioni nei sistemi, Diffusione virus, Denial-of-Service 
**Anni 2000: nascono i professionisti del cybercrime** 
- “I giovani sono cresciuti: questo è il loro lavoro” 
- La motivazione è essenzialmente economica 
	- **SPAM**, nato come strategia di Web marketing, oggi nasconde: frodi (es., 419 advance fee fraud), phishing, diffusione di malware, ecc. 
	- **Brand impersonification**: la tattica più comune per acquisire informazioni personali (credenziali di accesso, identità, altri dati) 
**Presente/futuro: cyberwar, cyberterrorism**

 I tipi di attacchi più diffusi sono:
 1) **Applicativi non aggionati**
 2) **Sistemi opeativi obsoleti**
 3) **Malware**
 4) **Passord banali**
 5) **Phishing**
 6) **Man-in-the-browser**
 7) **Uso di compute condivis**
 8) **Uso di Wi-Fi aperte**

# PRINICIPI FONDAMENTALI
**TRIADE CIA**, per sopperire al problema di valutazione dell sicurezza informatica e codificare meglio il gergo tecnico, si mappano gli obiettvi della sicurezza:
- **C**onfidentiality
	La **confidenzialità** è l'obiettivo della sicurezza che si occupa di garantre che le informazioni sensibili sono accedute solamente da personale autorizzato a farlo e mantenute inaccessibili a chi non è autorizzato a possederle.
	Si garantisce la confidenzialità delle informazioni:
	- **Cifrando le informazioni**
		- Cifratura a chiave simmetrica o privata 
		- Cifratura a chiave asimmetrica o pubblica
	- **Controllando gli accessi**
		- Autenticando gli utenti 
		- Fornendo un accesso basato sui ruoli aziendali 
		- Verificando l’identità ad ogni accesso
	- **Implementando specifiche policy di sicurezza**
		- Legate alla password o ai meccanismi di autenticazione degli utenti 
		- Impostando meccanismi di gestione dei dati aziendali
- **I**ntegrity
	L'**integrità** delle informazioni è l'obiettivo della sicurezza che si occupa di garantire che le informazioni siano mantenute in un formato coerente con la loro rapresentazione orginale, evitando modifiche o cancellazioni non autorizzate.
	Esistono diverse tecniche che permettono di garantire l’**integrità** delle informazioni:
	- **Funzioni di Hash** 
	- **Firme digitali** 
	- **Codici a rilevazione d’errore**
- **A**vailability
	La **disponibilità** delle informazioni è l’obiettivo della sicurezza che si occupa di garantire che le informazioni siano disponibili per coloro che devono utilizzarle
	Esistono diverse tecniche che permettono di garantire la **disponbilità** delle infor- mazioni:
	- **Strategie di backup**
		- Completo 
		- Incrementale 
		- Differenziale
	- **Ridondanza**
		- Hardware 
		- Software 
		- Dei Dati
	- **Failover**
		- Attivo
		- Passivo
	- **Bilanciamento del carico**
Anche s CIA vene mplmntata corttamnt ci sono comunque dei limiti, però garantisce sicuezza contro:
- Identità falsificate 
- Dati creati in maniera fraudolenta
- Mancanza di fiducia nella comunicazione

Per evitare questi limiti si devono implementare diverse tecnologie che aumentano l'efficacia di CIA per la gestione delle reti e delle comunicazioni, come:
- **Il modello AAA** 
- **Garanzia del Non Ripudio** 
- **Paradigma del Defence In Depth** 
- **Principio del Minimo Privilegio**


