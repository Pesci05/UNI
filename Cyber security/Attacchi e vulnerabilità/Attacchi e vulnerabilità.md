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

## IL MODELLO AAA
 #02/10 
Il modello AAA è un framework di sicurezza che **controlla l’accesso** alle risorse informatiche, **applica policy** e ne verifica l’**utilizzo**.

- **Autenticazione**
	**AuthN**, l'autenticazione, è la pratica che prevede l'identificazione degli utenti mediante la fornitura di **ccredenziali di accesso univoche**
	I tipi di autenticazione possono
	- essere basati su Informazioni che conosci 
	- Dispositivi che possiedi 
	- Caratteristiche fisiche personali
	Un buon sisitema di autenticazione prevede **almeno l'utilizzo di 2 di queste tipologie**
- **Autorizzazione**
	È la pratica che prevede la **definizione di pemressi di accesso** ad un utente a seguito della sua autenticazione
	L’autorizzazione permette di specificare, per ogni utente e ogni servizio cui vuole accedere, il perimetro di operatività legittimo entro il quale l’utente può operare. 
	Simile alle *capabilities* dei sistemi UNIX.
- **Accounting**
	È la pratica di tenere traccia delle attività degli utenti mentre accedono ad una rete e/o ad unservizio, monitorando:
	- L'istante d'accesso
	- La durata dell'accesso
	- I dati scambiati
	- Indirizzo IP di accesso
	- URI utilizzato
	Per ogni servizio utilizzato
	Può essere utilizzato anche per fini di fatturazione e per monitorare le attività su un particolare servizio/sistema al fini di **identificare attività anomale**
- **NON RIPUDIO**
	Si riferisce alla condizione secondo la quale di una particolare attività non può negare di averla svolta, mantenendo al tempo stesso garanzie di affidabilità della comunicazione.
	
	Il **non ripudio** estende il concetto della triade CIA applicandolo non solo ai dati in unparticolare stato, am agli utenti coinvolti nella trasmissione adogni instante di essa.
- **Paradigma Defence in depth**
	Consiste nella stratificazione delle risorse informatiche di protezione, rallentando la penetrazione di eventuali attacchi per fornire il tempo necessario per una efficace reazione protettiva.
	Un classico esempio di DiD applicata ad un sistema di riferimento è l’autenticazione multifattore in un sistema di accesso.
	- La **strutturazione a più livelli** è sicuramente l'asso nella manica di questa startegia
	- Basando **più sistemi di sicurezza** su **differenti livelli** si va notevolmente ad ot- timizzare il livello di protezione. 
	- Potrebbe infatti accadere che, durante un attacco, un livello non dovesse funzionare o venisse facilmente bypassato: in questo caso, entrerebbe in funzione il successivo, garantendo l’aumento di tempo utile e necessario per una risposta efficace e complementare.
- **Difesa multilivello**(Defence in depth)
	Alla base della **Defense in Depth** vi è la **Difesa Multilivello**, che utilizza un insieme di soluzioni per **restringere** la **superficie di attacco**, in modo tale che il perimetro di rete sia il più possibile **protetto da ogni lato**

Le tipologie di difesa Defence in Depth e Multilivello, possono essere complementari, poiché mentre la **Defense in Depth, organizzata su più stratificazioni**, rallenta l’ingresso di terzi non autorizzati, la **Difesa Multilivello protegge in modo più efficiente le reti e gli endpoint.**

![[Pasted image 20261002114222.png]]

Questa configurazione di rete viene chaiamata  **[[Attacchi e vulnerabilità#DMZ|DMZ]]** , questa non permette a dispositivi esterni di comunicare con la rete interne, invece gli interni per comunicare conn internet, devono prima passare i propri dati al bastion Host (**PROXY**), il quale decide se i traffico può andare verso internet o viene bloccato.
Questo tipo di configurazione però è vulnerabile rispetto a gli **attacanti interni**.

## SCREENED SUBNET
Formata da 3 dispositivi:
- **Router interno**
	Protegge sia la rete privata da attachi provenienti da Internet sia i server della DMZ da eventuali attacchi provenienti dall’interno della rete
- **Router esterno**
	Filtra il traffico tra Internet e DMZ secondo le politiche definite per l’accesso ai server della DMZ consentendo esclusivamente il transito di pacchetti (selettivo) da e verso il bastion host
- **bastion host**

Evoluzione dell’architettura **two-legged network e screened-host gateway**.

# DMZ
Una sottorete isolata che non fa parte né della rete interna né della rete esterna

**SCOPO PRINCIPALE**:
- Minimizza l’esposizione della rete in- terna ad attacchi esterni. 
- Ospita esclusivamente i server che erogano servizi pubblici (Web, Mail, DNS) accessibili da Internet.
![[Pasted image 20261002115137.png]]

Il miglior tipo di configurazione è:
![[Pasted image 20261002115801.png]]


| **Rete di partenza** | **Rete di destinazione** | **Traffico permesso**                      |
| -------------------- | ------------------------ | ------------------------------------------ |
| LAN                  | Internet                 | Tutto (o quasi)                            |
| LAN                  | DMZ                      | Solo protocolli voluti                     |
| Internet             | DMZ                      | Solo protocolli voluti                     |
| Internet             | LAN                      | Nessuno (tranne risposte <br>da richieste) |
| DMZ                  | Internet                 | Solo protocolli voluti                     |
| DMZ                  | LAN                      | Nessuno (tranne risposte <br>da richieste) |

# ARCHITETTURA Web multi-Livello
**Sicurezza nel filtraggio interno (Concettuale)**
![[Pasted image 20261002121054.png]]

# PRINCIPIO DEL MINIMO PRIVILEGIO
Concetto secondo cui l'utente, un programma, o un'altra entità deve avere accesso alle sole risorse, ai dati e alle funzioni strettamente necessarie per il proprio ruolo lavorativo.

**Lo scopo è quello di ridurre i danni potenziali derivanti da un account com- promesso o da una minaccia interna, limitando la superficie d’attacco.**

# STRATEGIA DI SICUREZZA
## CYBER KILL CHAIN
Modello definito dalla Lockheed Martin, per l'identificazione e la prevenzione delle attività di intrusione delle attività di intrusione informatica attraverso l'implementazione di protocolli di sicurezza pro-attivi. Tale modello è a sua volta ispirato 

La KILL CHAIN è formata:
- **Ricognizione**
	Attaccante identifica il target, ottiene informazioni su di esso, e prova ad identificare vulnerabilità nella rete o nei sistemi dell'organizzazione.
- **ARMAMENTO**
	Attaccente crea un'arma, 
- **CONSEGNA**
	Attaccane trasmette l'arma al target, attraverso vari vettori di attacco
- **Esecuzione dell'exploit**
	Il codice dell'arma malware viene attivato sul sistema vittima
- **Installation**
	L'arma malware installa un punto d'accesso nascosto e permanente(**backdoor**), che l'attaccante può sfruttare per mantenere l'accesso al sistema.
- **Command & Control**
	Il malware abilita l'attacante a mettere mano sul sistema 
- **Azioni sugli obiettivi**
	L'attaccante può controllare direttamente l'host compromesso per i propri scopi: esfiltrazione di datiriservati, distruzione di risorse o cifratura del file per richiesta di riscatto.


