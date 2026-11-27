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
	Attaccente crea un'arma, malware creata appositamete progettata per le vulnerabilità.
- **CONSEGNA**
	Attaccane trasmette l'arma al target, attraverso vari vettori di attacco
- **Esecuzione dell'exploit**
	Il codice dell'arma malware viene attivato sul sistema vittima
- **Installation**
	L'arma malware installa un punto d'accesso nascosto e permanente(**backdoor**), che l'attaccante può sfruttare per mantenere l'accesso al sistema.
- **Command & Control**
	Il malware abilita l'attacante a mettere mano sul sistema, instaurando un canale di comunicazione con la propria infrastruttura e ottenendo persistenza nella rete privata.
- **Azioni sugli obiettivi**
	L'attaccante può controllare direttamente l'host compromesso per i propri scopi: esfiltrazione di datiriservati, distruzione di risorse o cifratura del file per richiesta di riscatto.

![[Pasted image 20261005111000.png]]

## MITRE ATT&CK
#05/10
Il mitre ATT&CK (**Adversarial Tactics Techniques and Common Knowledge framework**) è un catalogo omnicomprensivo di tutte le principali procedure usate degli attaccanti per:
- Enumerare sistemi
- Violare sistemi
- Rendere persistente l'accesso ai sistemi
### TATTICHE DI ATTACCO
Le procedure di attacco sono suddivise in **tattiche**. 
**Tattica**: è un obiettivo finale dell’attaccante, motivo principale delle sue azioni.
Raccoglie tutte le azioni che confdividono una finalità.

Ogni tattica di attacco contiene diverse **tecniche**. 
**Tecnica**: è un’azione concreta volta ad uno specifico obiettivo.
Specifica cosa ottiene un attaccante al termine della tecnica.

### ATT&CK MATRIX
Correla in modo efficace le **tattiche** con le rispettivi **tecniche**
![[Pasted image 20261005111624.png]]

Esistono **3 tipi di matrici**:
- **Enterprise**
	Per sistemi tradizionali e tecnologie cloud
	Composta da 14 tattiche: [[3_StrategieSicurezzaVuln.pdf#page=23|3_StrategieSicurezzaVuln, pagina 23]]
- **Mobile**
	Per sistemi di comunicazione mobili
	Composta da 14 tattiche: [[3_StrategieSicurezzaVuln.pdf#page=24|3_StrategieSicurezzaVuln, pagina 24]]
- **ICS**
	Per sistemi di controllo industriali
	Composta da 12 tattiche: [[3_StrategieSicurezzaVuln.pdf#page=25|3_StrategieSicurezzaVuln, pagina 25]]
All'interno di ogni matrice, è possibile selezionare la piattaforma di riferimento e vedere la lista di tecniche e sotto-tecniche che possono essere applicate.

## DIFFERENZE TRA KILL CHAIN E MITRE&CK
- **KILL CHAIN**
	- **Focus** sugli stadi dell’attacco **dalla prospettiva dall’attaccante**. 
	- Alto livello
	- Fornisce una **Scaletta chiara e concise delle fasi di un attacco**
	- Utilizzata nelle fasi iniziali della threat detection e prevention, con lo **scopo principale di identificare potenziali minacce e impedire che causino danni**
	- Sviluppata da Lockheed Martin e **aggiornata sporadicamente**
- **MITRE&CK**
	- Focus sulle **tecniche di attacco utilizzate dagli attaccanti**. Basso livello, permette di comprendere l’attività dell’attaccante fino al dettaglio delle tattiche d’attacco.
	- Fornisce una **descrizione** chiara e concisa delle **tecnice utilizzate dagli attaccanti**, fornendo anche spunti su strategie di mitigazione e di rilevazione
	- Utilizzata lungo tutto il ciclo di vita di sicurezza
	- Sviluppo community-driven (mantenuto da MITRE) e **aggiornata continuamente**

---
# Vulnerabilità Software e bug
**Tutti i software hanno dei bug**. Alcuni bug possono essere funzionali, mentre altri sono creati per elevare i privilegi, i più problematici sono quelli di privazione del servizio e questi possono essere chiamati **vulnerabilità**.

## PERCHè esistono le vulnerabilità
1. I Programmatori non pensano in ottico multi-utente
2. I Programmatori **sono umani**, e molto spesso si **sceglie l'approccio più semplice e veloce al posto di un approccio più sicuro.**
3. Molti programmatori non sono buoni programmatori
4. La maggior parte dei programmatori non pensano ad un possibile attacco.
5. Molti modelli di sicurezza dei computer sono terribili
6. Presenza di molto software _legacy_ difficile da correggere
7. Agli utenti non importa abbastanza della sicurezza
8. La sicurezza comporta ad un costo extra
9. Sicurezza comporta costi di test aggiuntivi

## CICLO DI VITA DIUNA VULNERABILITÀ
1. **$𝑡_{v}$ (Vulnerability introduced):** Il fornitore rilascia un software contenente la vulnerabilità.
2. **$𝑡_{e}$ (Exploit released in the wild):** Un attaccante scopre la falla e rilascia un exploit senza avvisare il fornitore.
3. **$𝑡_{d}$(Vulnerability discovered):** Il fornitore si accorge della vulnerabilità (internamente o tramite segnalazioni).
4. **$𝑡_{0}$ (Vulnerability disclosed publicly):** La vulnerabilità viene resa pubblica.
5. **$𝑡_{s}$ (AV signatures released):** Vengono rilasciate le firme per gli antivirus/sistemi di rilevazione.
6. **$𝑡_{p}$(Patch released):** Il fornitore rilascia la patch correttiva.
7. **$𝑡_{a}$ (Patch deployment completed):** L'installazione della patch sui sistemi è completata.

![[Pasted image 20261005121047.png]]

- **zero-day attack**: Nel periodo di tempo $[t_{e},t_{0}]$, l'attacco avviene in assenza di una sua pubblica conoscenza. Si parla di attacco zero-day.
- **follow-on attack**: Nel periodo di tempo $[t_{0},t_{a}]$, l'attacco avviene in presenza di una sua pubblica conoscenza. La sua forza è notevolmente rispetto al periodo $[t_{e},t_{0}]$.

>[!note] Gli exploit hanno molto mercato, si può decidere di **segnalare** l'exploit all'azienda, oppure anche di vendere l'**exploit** ad un'azienda terza la quale deciderà lei cosa farne.
>Spesso la seconda opzione è **più remunerativa**, ma dal punto di vista etico non è il meglio

---
## CATALOGAZIONE DELLE VULNERABILITÀ
Svariati team di sicurezza scoprono e divulgano le vulnerabilità in modo indipendente.
Ciascun team di sicurezza costruisce un proprio archivio storico degli attacchi passati:
- **Enumerazione**
	Costruzione di una tupla univoca a partire dalla vulnerabilità 
- **Catalogazione**
	Inserimento della tupla in un apposito database
Ogni team manteneva un proprio catalgo, questo però poteva dare diversi problemi come:
- **Duplicazione dello sforzo**
	Vulnerabilità scoperta da più team
- **Eterogeneità del catalogo**
	Formati diversi tra loro

Per questo MITRE ha introdotto un **catalogo uniforme** delle vulnerabilità.
Questo sistema si chiama **CVE** (**Common Vulnerability and Exposure**), cataloga in modo uniforme vulnerabilità e esposizioni.
- **Vulnerabilità**
	Una debolezza nel software e/o nel firmware che, se sfruttata, viola almeno una tra confidenzialità, integrità, disponibilità
- **Esposizione**
	Un errore nel software/nella sua configurazione che permette l’accesso a funzioni ed informazioni
Ogni vulnerabilità viene identificata da un **identificatore CVE**, formata dall'anno e da un numero progressivo.
Ad ogni identificativo corrisponde a una **scheda descrittiva**:
- **Descrizione**
	Una descrizione testusale del problema
- **Riferimento**
	URL che porta ad un approfondimento del problema
- **Date entry created**
	Data di inserimento della CVE nel database,

Le vulnerabilitò **non sono tutte uguali**, infatti possono avere effetti diverso tra loro e nei diversi sistemi, nel tempo e possono avere gravità differenti , per questo si è creato il **CVSS**(Common Vulnerability Scoring System), il quale introduce uno **scoring system**.
![[Pasted image 20261005124107.png]]

### CVSSv4
Il punteggio si basa su 4 metriche di valutazione:
- **Base**
	Misurano la gravità intrinseca della vulnerabilità, queste metrice sono:
	- **Attack Vector**: contesto dove posso sfruttare le vulnerabilità
	- **Attack Complexity**: complessità delle azioni perpetrate dall'attaccante
	- **Attack Requirements**: prerequisiti necessari per sfruttare le vulnerabilità
	- **Privilege Required**: livello di privilegio richiesto dall'attacante
	- **User Interaction**: necessità di avere qualche tipo di interazione con l'utente
	Queste metriche hanno impatto su:
	- **Confidentiality**(VS/SC): confidenzialità delle informazioni gestote dal sistema (VC) e dai sistemi collegati (SC)
	- **Integrity**(VI/SI): integrità delle informazioni gestite dal sistema (VI) e dai sistemi collegati (SI)
	- **Availability**(VA/SA): disponibilità delle informazioni gestite dal sistema (VA) e dai sistemi collegati (SA)
	
- **Minaccia**
	Misurarno la probabilità di sfruttamento attuale:
	- Not Defined (X) 
	- Attacked (A) 
	- Proof-of-Concept (P) 
	- Unreported (U)
	
- **Ambiente**
	Permettono di considerare l’impatto della vulnerabilità in terms di confidenzialità/integrità/disponibilità del sistema target in base alla tipologia di servizio del sistema stesso \[Not Defined (X), High (H), Medium (M), Low (L)\],
	(requisiti `CR/IR/AR`,*[[3_StrategieSicurezzaVuln.pdf#page=83|Modified base metrics]]*, e impatto sulla  *[[3_StrategieSicurezzaVuln.pdf#page=84|Safety fisica]]* )
- **Supplementi**
	Aggiungono attributi espliciti come automatizzabilità (_Automatable_), capacità di ripristino (_Recovery_), dettagli sulla _Safety_ (Marginal, Critical, Catastrophic), _Value Density_, _Vulnerability Response Effort_ e _Provider Urgency_.

Tutte queste metriche vengono sintetizzate in una stringa testuale compatta chiamata **Vector String** (es. `CVSS:4.0/AV:N/AC:L/...`).

### ALTRI STANDARD
Oltre a CVE e CVSS, esistono altri cataloghi standard:

- **CPE (Common Platform Enumeration):** Enumera gli asset hardware e software.
- **OVAL (Open Vulnerability Assessment Language):** Definisce procedure standard per verificare la presenza di vulnerabilità.
- **CWE (Common Weakness Enumeration):** Cataloga le **debolezze** hardware e software _in modo indipendente dalla loro sfruttabilità_ (a differenza della CVE che identifica una specifica istanza in un prodotto). Ogni voce ha un `CWE-ID` (es. `CWE-121: Stack-based Buffer Overflow`) e include descrizione, modalità di introduzione, mitigazioni possibili, conseguenze comuni, esempi di codice ed esempi di CVE reali che la espongono.

# INITIAL ACCESS
## RISCHIO CYBER E MALWARE
Riprendendo il concetto di [[Attacchi e vulnerabilità#RISCHIO|Rischio]], le vulnerabilità sfruttate da una minaccia non sono solo software, ma anche **umane**.
Il **Malware** (*MALicious softWARE*, definizione moderna di "virus") include qualsiasi programma implementato per scopi malevoli:
- Furto di informazioni e spionaggio (**spyware**)
- Indebolimento delle difese e creazione di "porte di ingresso" nascoste (**backdoor**, collegato alla fase di *Installation* della [[Attacchi e vulnerabilità#CYBER KILL CHAIN|Cyber Kill Chain]])
- Danneggiamento e sabotaggio (**cracking**)
- Ricatto (**ransomware**) e truffe (**scamware**)
- Acquisizione del controllo remoto del computer fino allo stato di **zombie** all'interno di una **botnet**

### EVOLUZIONE E CARATTERISTICHE DEL MALWARE
Negli ultimi quarant'anni si è ridotto il numero di virus con intenti puramente distruttivi (nota: il ransomware non è categorizzato come distruttivo) ed è aumentato il **malware latente** (*ghostware*):
- Tende a nascondersi in profondità e a riprodursi automaticamente in diversi posti e formati (simile a virus/retrovirus biologici)
- **Obiettivi comuni**: installarsi al verificarsi di un evento, mascherarsi, replicarsi localmente o tra computer (es. agganciandosi a funzioni ripetute spesso come l'invio di mail)
- **Effetti** (non mutuamente esclusivi): manifestarsi in modo distruttivo, attivarsi in modalità nascosta, contattare il creatore appena connesso a Internet, diffondersi via cartelle condivise/contatti
- **Vettori di infezione**: il **95%** del malware si riceve tramite allegati e-mail (es. [[Attacchi e vulnerabilità#CRIMINI TECNOLOGICI|phishing]]), file sharing e programmi infetti scaricati (oltre a link URL, app Web, software non certificato)

### TIPI DI MALWARE
L'importante non è la distinzione sintattica tra i nomi, ma focalizzarsi sulle **funzionalità** del malware:
- **Virus**: programmi di piccole dimensioni in grado di replicarsi e diffondersi autonomamente. È un frammento di codice che **non può essere eseguito separatamente** da un programma ospite (es. macro Word/Excel, `.exe`).
	- **Bomba logica**: caratteristica aggiuntiva per cui il virus si attiva dopo un certo tempo o al verificarsi di una ricorrenza
	- **Virus polimorfico**: codice crittografato in modo variabile; modifica la routine di decifratura a ogni infezione (mantenendo l'algoritmo) con *trash code* o permutazioni
	- **Virus metamorfico**: muta completamente il proprio codice per evitare il riconoscimento a runtime degli antivirus, usando crittografia e suddivisione/inserimento del codice in punti diversi del file infetto
- **Worm**: applicativo **a sé stante** (non ha bisogno di un programma ospite). Usa la rete per trovare [[Attacchi e vulnerabilità#Vulnerabilità Software e bug|vulnerabilità di sicurezza]] nei computer raggiunti e diffondersi automaticamente, senza necessariamente ingannare l'utente.
- **Trojan**: veicolo per diffondere malware collegato a un file apparentemente innocuo (videogame, PDF, file multimediale). Richiede il **coinvolgimento dell'utente**, convinto tramite tecniche di *social engineering* (es. allegati email, download volontari, chiavette USB).
- **Spyware** (*SPYing softWARE*): creato per spiare la vittima, raccogliere informazioni sulle sue attività e inviarle a un host esterno.
	- **Scopi**: criminosi (furto password, conti online, carte di credito), fastidiosi (**adware** per pubblicità), potenzialmente dannosi (tracciamento come primo passo per altri attacchi), investigativi (**policeware** o parental control)
	- **Problemi di privacy**: intercettazione traffico Web non cifrato, *hijacking* della homepage del browser, vendita dati a terze parti, degrado delle prestazioni (viola la confidenzialità della [[Attacchi e vulnerabilità#PRINICIPI FONDAMENTALI|Triade CIA]])
	- **Policeware**: spyware legale usato dalle forze dell'ordine (es. *MagicLantern* e *CIPAV* dell'FBI, *Room641a* dell'NSA, *Oasis* della CIA), tipicamente *whitelisted* dagli antivirus
- **Ransomware**: malware con richiesta di riscatto (primi casi nel 2005, esplosione nel 2016; es. *WannaCry*, *Petya*).
	- **Funzionamento**: arriva via allegati email, link o P2P; una volta eseguito cifra o cancella i file della vittima (violando disponibilità e integrità della [[Attacchi e vulnerabilità#PRINICIPI FONDAMENTALI|Triade CIA]]) e invia una richiesta di riscatto per ottenere la chiave di decifrazione (senza garanzia che venga poi fornita).

## ADVANCED PERSISTENT THREAT (APT)
Con l'avanzamento delle difese, gli attacchi condotti da professionisti (non *script junkies*) sono diventati sempre più sofisticati, mascherati e **persistenti nel tempo**.
- **Target e attori**: riguardano soprattutto aziende medio-grandi, poiché richiedono alti investimenti (risorse umane, finanziarie e temporali) e puntano a un sostanzioso ROI. Sono tipicamente organizzazioni para-statali o organizzazioni criminali altamente specializzate.
- **Esempi storici**: Attacco a Sony (PlayStation, 2012), Google (Operazione Aurora), Stuxnet, RSA → Lockheed Martin, Sony (2014).

### PASSI DELL'ATTACCO APT
Il flusso operativo ricalca le fasi della [[Attacchi e vulnerabilità#CYBER KILL CHAIN|Cyber Kill Chain]] e le tattiche di [[Attacchi e vulnerabilità#MITRE ATT&CK|MITRE ATT&CK]]:
1. **Reconnaissance**: ricerca e identificazione dei singoli individui target (via ricerche pubbliche) per ottenere indirizzi email o contatti di messaggistica.
2. **Intrusion into the network**: inizia tipicamente con email di **spear-phishing** (variante mirata del [[Attacchi e vulnerabilità#CRIMINI TECNOLOGICI|phishing]]) con link o allegati malevoli (PDF, Office) per infettare la macchina del dipendente e ottenere un primo accesso.
3. **Establishing a backdoor**: ricerca ed estrazione delle credenziali di amministratore di dominio (spesso decifrate con *pass-the-hash*) per elevare i privilegi, muoversi lateralmente (*lateral movement*) e installare **backdoor** (via *process injection*, modifica del registro o servizi pianificati).
4. **Obtaining user credentials**: utilizzo di credenziali valide rubate (soprattutto di *domain-administrator*) per accedere in media a circa 40 sistemi nella rete vittima.
5. **Installing multiple utilities**: installazione di utility di amministrazione di sistema per gestire backdoor, raccogliere password, leggere email ed elencare i processi attivi.
6. **Privilege escalation, lateral movement e data exfiltration**: raccolta di email, allegati e file dai server tramite l'infrastruttura **C&C** (*Command & Control*); i dati vengono convogliati su *staging server*, cifrati, compressi ed esfiltrati (poi eliminati dallo staging server).
7. **Maintaining persistence**: se rilevati o contrastati, gli attaccanti adottano nuovi metodi (incluso il rinnovamento del malware) per non perdere la presenza nella rete vittima.

## DENIAL OF SERVICE (DoS)
La negazione del servizio (**DoS**) colpisce direttamente la **disponibilità** della [[Attacchi e vulnerabilità#PRINICIPI FONDAMENTALI|Triade CIA]] e può essere causata da:
- **Volume di dati trasmessi alla vittima**: provoca la saturazione delle risorse del sistema (*starvation*)
- **Contenuto dei dati inviati**: progettati per sfruttare [[Attacchi e vulnerabilità#Vulnerabilità Software e bug|vulnerabilità]] nei servizi, nei protocolli o nell'implementazione hardware/software

Caratteristiche principali: ogni host in rete è potenzialmente soggetto a DoS; non serve compromettere il sistema né avere conoscenze avanzate (script reperibili in rete) ed è spesso difficile evitarli del tutto.

### METODI E CLASSIFICAZIONE
- **Metodo di attacco**:
	- **Diretto**: rivolto direttamente alla risorsa da rendere indisponibile
	- **Indiretto**: rivolto contro una risorsa diversa dall'obiettivo ma indispensabile per esso (es. *DNS poisoning*)
- **Attaccante**:
	- **Reale**: il traffico parte direttamente dall'attaccante
	- **Riflesso**: il traffico arriva alla vittima da altri host "complici" o vittime a loro volta (es. saturazione banda)
- **Evoluzione**: dalla seconda metà degli anni '90 (pacchetti malformati per sfruttare bug) si è passati a fine anni '90 all'esaurimento di risorse, fino agli attacchi indiretti (1999) e ai **DDoS** (*Distributed DoS*, dagli anni 2000) basati su reti di host compromessi (botnet).

### DoS CHE SFRUTTANO VULNERABILITÀ (PACCHETTI MALFORMATI)
L'attaccante sfrutta bug noti per provocare crash, hang o reboot del sistema vittima:
- **Ping of Death (1996)**: invio di pacchetti ICMP *echo request* frammentati di dimensione complessiva $> 65535$ byte (massimo consentito dal protocollo IP), causando errore di riassemblaggio nello stack TCP/IP.	![[Pasted image 20261109104724.png]]

- **Teardrop**: invio di frammenti IP con *offset* sovrapposti; in fase di riassemblaggio il sistema operativo non sa come procedere e va in crash, questo attacco è frutto di una cattiva implementazione dello stack TCP/IP.
![[Pasted image 20261116224634.png]]

- **WinNuke (1996)**: invio di pacchetti OOB (*Out Of Band*, bit `URG=1`) malformati sulla porta TCP 139 verso sistemi Windows 9x/NT (errore in NetBIOS).
	
- **LAND (1997)**: invio di pacchetti `TCP SYN` con indirizzo IP e porta sorgente identici a quelli di destinazione; la vittima tenta un *3-way handshake* infinito con sé stessa. Si mitiga filtrando sul firewall i pacchetti provenienti dall'esterno con IP sorgente interno.
![[Pasted image 20261116230138.png]]



### DoS PER ESAURIMENTO DI RISORSE
L'attaccante satura una risorsa del sistema (**Resource starvation**: CPU, memoria, spazio su disco, numero di connessioni) o la banda di rete (**Bandwidth consumption**):
- **Flooding**: inondazione di traffico (ICMP, TCP, UDP) spesso combinata con *IP spoofing* e pacchetti malformati.
- **TCP SYN Flood**: invio massiccio di `TCP SYN` con IP sorgente *spoofed* senza mai completare il *3-way handshake*, esaurendo la coda delle connessioni (*backlog queue*).
	- **Contromisure lato vittima**: aumentare la coda, ridurre il timeout, usare *SYN cookies* o scartare SYN casualmente (riducono ma non risolvono).
	- **Contromisure lato attaccante**: *egress filtering* contro l'IP spoofing.
- **Smurf e Fraggle**: attacchi amplificati (*broadcast storm*) che coinvolgono attaccante, rete amplificatrice e vittima.
	- **Smurf**: invia `ICMP Echo Request` con IP sorgente *spoofed* (quello della vittima) all'indirizzo di broadcast di una rete; tutti gli host rispondono con `ICMP Echo Reply` alla vittima, saturandola.
	- **Fraggle**: analogo a Smurf, ma usa pacchetti UDP.
	- **Contromisure**: filtrare il traffico ICMP diretto a indirizzi broadcast (in ingresso e in uscita) e bloccare le risposte `ECHO REPLY` non richieste.
	![[Pasted image 20261116233239.png]]
### PROBLEMI ED ESEMPI STORICI
- **Difficoltà di tracciamento**: uso di architetture multi-livello (*attaccante → master → demoni → vittima*), *spoofing* e pacchetti sintatticamente leciti.
- **Esempi storici**: Yahoo (1999, 12 ore), Amazon (2000, 10 ore, ~600.000$ di danni), Root Name Server (2006, 2 ore), Estonia (2007, oltre una settimana di malfunzionamenti).
## Distributed Denial of Service (DDoS)
Attacchi DoS che spingonoall’**estremo il concetto i flooding tramite bandwitdhcon- sumption**. Utilizzando **più sorgenti (anche migliaia)** per la generazione del traffico di flood (vittime di II livello).
Una o più vittime finali(vittime di I livello).
Possibilità di **eseguire più attacchi** di tipi flooding.
Da vari anni si fa uso di **[[Attacchi e vulnerabilità#BOTNET|botnet]]**.

### Sistemi di amplificazione
L'amplificazione partendo dal 2018 sfrutta sistemi **memcachedmalconfig**. Memcached è una **funzione** di caching nata per migliorare i tempi di risposta da dischi e database e utilizzata per ridurre i tempi di caricamento dei dati via rete da siti Web.
Questo servizio però non è pubblico, ma 17.000 server esponevano i servizi **Memcached**, i quali li rendevano vulnerabili a messaggi UDP, poichè rispondeva con i propri dati a chiunque.

## BOTNET
Una **botnet** è una rete di dispositivi compromessi (chiamati **bot** o **zombie**) controllati da remoto da un attaccante (*botmaster*) senza che i proprietari ne siano consapevoli.
- **Formazione e propagazione**: gli host vengono "conquistati" tramite la proliferazione di [[Attacchi e vulnerabilità#RISCHIO CYBER E MALWARE|malware]] (virus, worm, trojan), spam e [[Attacchi e vulnerabilità#CRIMINI TECNOLOGICI|phishing]].
- **Architettura multi-livello**: per rendere difficile il tracciamento degli esecutori, le botnet adottano una struttura gerarchica:
	- **Attaccante** (*botmaster*) → **Master** (nodi intermedi) → **Demoni / Zombie** (host infetti) → **Vittima**
	- Il controllo avviene tramite canali **Command & Control (C&C)**, analoghi a quelli visti nella [[Attacchi e vulnerabilità#CYBER KILL CHAIN|Cyber Kill Chain]] e negli [[Attacchi e vulnerabilità#ADVANCED PERSISTENT THREAT (APT)|attacchi APT]].
- **Dal DoS al DDoS**: l'epoca delle botnet ha segnato il passaggio dagli attacchi [[Attacchi e vulnerabilità#DENIAL OF SERVICE (DoS)|DoS]] singoli agli attacchi **DDoS** (*Distributed Denial of Service*), in cui un numero elevato di demoni invia traffico simultaneamente contro un bersaglio, rendendo possibile saturare la banda di qualunque host connesso a Internet.
Le botnet possono essere **create** anche solo per **venderle a cybercriminali**.


# PRIVILEGE ESCALATION
Nei sistemi UNIX può capitare che un processo debba eseguire con privilegi elevati (tipicamente `root`), ad esempio per leggere/modificare `/etc/shadow`, interagire con periferiche (`/dev/sda`) o inviare datagrammi tramite *raw socket*.

## ELEVAZIONE DEI PRIVILEGI: MANUALE VS AUTOMATICA
Esistono due modalità per eseguire un comando da superuser:
- **Elevazione manuale**: l'utente si identifica prima come amministratore e poi esegue il comando.
```bash
user@localhost ~ % su -
Password:
root@localhost ~ # passwd bros
```
	**Problemi**: diffusione delle credenziali privilegiate (rischio per la [[Attacchi e vulnerabilità#PRINICIPI FONDAMENTALI|Triade CIA]]) e scomodità d'uso.
- **Elevazione automatica**: l'utente esegue direttamente il comando e il SO eleva i privilegi all'utente opportuno (spesso `root`).
```bash
user@localhost ~ % passwd bros
```
	- Nei sistemi UNIX moderni è la modalità usata per i programmi di sistema, ma va gestita rispettando il [[Attacchi e vulnerabilità#PRINCIPIO DEL MINIMO PRIVILEGIO|Principio del Minimo Privilegio]].

## PERMESSI UNIX, SETUID E SETGID
In UNIX "tutto è un file" e i permessi sono divisi in tre terne (`rwx`) per **Creatore (u)**, **Gruppo (g)** e **Altri (o)**:
- **Rappresentazione ottale**: `Read = 4`, `Write = 2`, `eXecute = 1` (es. `rwxrwxr-x` = `775` / `0775`).
- **Bit speciali SETUID e SETGID**:
	- **SETUID** (ottale `4`, simbolico `s` sui permessi utente): il processo assume lo **User ID del creatore del file** (es. `root`).
	- **SETGID** (ottale `2`, simbolico `s` sui permessi gruppo): il processo assume il **Group ID primario del file**.
	- Nell'output di `ls -l` appaiono con la `s` (evidenziati in rosso per SETUID, giallo per SETGID).

```bash
# Individuazione sistematica di file SETUID/SETGID
find / -perm -6000 2>/dev/null
# Oppure singolarmente: -perm -4000 (SETUID) o -perm -2000 (SETGID)

# Impostazione SETUID / SETGID root
chown root binario && chmod u+s binario
chgrp root binario && chmod g+s binario
```

### CREDENZIALI DI UN PROCESSO (REALE, EFFETTIVO, SALVATO)
A partire da UNIX System V, il descrittore di un processo memorizza **tre coppie** di credenziali (User ID e Group ID):

| **Tipologia** | **Significato** |
| :--- | :--- |
| **Reale (RUID / RGID)** | ID di chi ha lanciato il comando |
| **Effettivo (EUID / EGID)** | ID usato per il controllo dei permessi; se `SETUID/SETGID = 1`, assume l'ID del file (`File = Effettivo`) |
| **Salvato (SUID / SGID)** | Copia delle credenziali effettive all'avvio del processo, usata per il ripristino |

Per verificare gli ID di un processo in esecuzione:
```bash
ps -p $(pgrep -n passwd) -o ruid,rgid,euid,egid
```

## DEBOLEZZE DELL'ELEVAZIONE AUTOMATICA E MITIGAZIONI
Un processo SETUID/SETGID `root` ottiene **pieni poteri** e li mantiene per **tutta la durata dell'esecuzione** ([[5_PrivilegeEscalation_pt1.pdf#page=26|5_PrivilegeEscalation_pt1, pagina 26]]). Da sola non è una vulnerabilità, ma unita ad altri bug può avere conseguenze devastanti.
Le **mitigazioni** principali sono:
1. **Abbassamento e ripristino dei privilegi** (*privilege drop* / *privilege restore*): abbassare i privilegi a quelli dell'utente reale quando non servono operazioni critiche e ripristinarli solo quando necessario ([[5_PrivilegeEscalation_pt1.pdf#page=31|5_PrivilegeEscalation_pt1, pagina 31]]).
2. **Destrutturazione dei diritti di `root`** tramite **capabilities** (`man 7 capabilities`), dividendo i poteri di `root` in capacità granulari.

### GESTIONE DEI PRIVILEGI IN C (API DI SISTEMA)
- **Recupero ID**: `getuid()` (reale), `geteuid()` (effettivo), `getresuid(&ruid, &euid, &suid)` (tutti e tre).
- **Abbassamento permanente** (non più ripristinabile a `root`):
```c
setuid(getuid());          // Imposta RUID, EUID e SUID a uid (se privilegiato)
setresuid(uid, uid, uid);  // Equivalente esplicito su Linux (LSB/POSIX)
```
- **Abbassamento temporaneo e ripristino**:
	- `seteuid(uid)` modifica **solo** l'EUID (lascia intatti RUID e SUID, ma il SUID resta "opaco" all'utente).
	- `setresuid(u, e, s)` permette controllo completo su tutti e tre gli ID (`-1` lascia invariato il campo):
```c
uid_t uid = getuid();
uid_t priv_uid = geteuid(); // Salvo EUID iniziale (es. 0 = root)

/* Abbassamento temporaneo */
setresuid(-1, uid, -1);     // Equivalente a seteuid(uid)

/* Ripristino temporaneo */
setresuid(-1, priv_uid, -1);
```
*(Per il bit SETGID si applicano le stesse logiche sostituendo `u` con `g`, es. `setresgid()`).*

## INIBIZIONE DEL MECCANISMO SETUID/SETGID
Per impedire l'esecuzione di shell o programmi con pieni poteri di `root`:
- **Opzione di mount `nosuid`**: alcuni file system (es. virtuali o temporanei) sono montati con `nosuid`, inibendo SETUID/SETGID (`mount | grep nosuid`).
- **Abbassamento privilegi di BASH**: shell moderne come `bash` ignorano i bit SETUID/SETGID abbassando automaticamente EUID/EGID all'utente invocante (a meno di non usare esplicitamente l'opzione `bash -p` in *privilege mode* su un binario già reso SETUID `root` dall'amministratore).
- **Copia di file SETUID**: copiando un binario SETUID/SETGID, il bit viene rimosso automaticamente dal sistema operativo.
- **Tracciamento di processi**: debugger (`gdb`) e tracciatori (`strace`, `ltrace`, `ptrace`) non possono agganciarsi a processi con privilegi superiori, e un processo avviato sotto tracciamento non può elevare i propri privilegi tramite SETUID/SETGID.
- **Linguaggi di scripting dinamici**: i bit SETUID/SETGID sugli script vengono ignorati (bisognerebbe rendere SETUID `root` l'interprete stesso, pratica estremamente pericolosa).






# PHOENIX
