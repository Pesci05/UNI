Le applicazioni di rete possono essere costruite per funzionare in:
- **CLIENT-SERVER**
- **Peer-to-Peer**

# CLIENT-SERVER
È un tipo di applicazione che fa comunicare due terminali, dove uno ha il ruolo di **client** e l'altro ha il ruolo di **server**:
- **CLIENT**:
	- Comuica col server
	- **Non comunica** con altri **client direttamente**
	- Possono essere connessi in maniera intermittente
	- Possono avere indirizzi IP **dinamici**
- **SERVER**:
	- Sempre **attivo e in ascolto** di richieste
	- **Indirizzo IP fisso e noto**
	- Utilizzo di **Data center per scalabilità**

# PEER-TO-PEER
Tipo di connessione che avviene in:
- **Comunicazione diretta** tra coppie di host(peer)
- I peer sono **connessi in intermittenza combiando indirizzo IP**
- I peer fungono sia da server che da client
- Sono più **economiche**
- Più difficili da implementare

# PROCESSI
I **processi** sono programmi in esecuzione su un host.
- **Sullo stesso host**, 2 processi comunicano usando un approccio interprocesso, definita dal SO
- **Su host diversi**, 2 processi comunicano scambiando **messaggi** atraverso la rete.
Per un'**applicazione di rete**, si deve avere un coppia di processi.
Nel caso di un'applicazione client/server i processi :
- **Client**
	È il processo che **inizia** la comunicazione
- **Server**
	Processo che **attende una richiesta**, e risponde se l'applicazione lo richiede.

Nel caso di **P2P** ogni host, ha processi di **client e server** 
## SOCKET/PORTE
Il processo invia e riceve messaggi dalla rete attraverso un'interfaccia sw detta **socket**.
**SOCKET**: interfaccia tra processo a livello applicazione e trasporto in un host.

### INDIRIZZAMENTO
Per ricevere messaggi, il processo destinatario deve avere un **identificatore**:
- **Indirizzi IP**: numero di 32 bit che identifica univocamente un host.
- **Identificatore**: deve includere **sia indirizzo IP che numero di porta** associata al processo sull'host, perchè su un unico host possono girare più processi.
- Alle applicazione più note sono assegnate numero di porte specifiche

## REQUISITI PRINCIPALI
1) **Trasferimento dati affidabile**
	- Esistono applicazioni le quali richiedono un trasferimento del **100%**, anche se esistono applicazioni, le quali non necessitano di un trasferimento completo

2) **Throughput**
	- Alcune applicazioni per essere efficaci richiedono un [[RETI E PROTOCCOLI#THROUGHPUT END-TO-END |throughput]] **minimo garantito**
	- **Applicazioni elastiche**: non hanno specifici requisiti di banda

3) **Temporizzazione**
	- Alcune applicazioni **time sensitive** richiedono un **bassa latenza per essere efficienti** 

 4) **Sicurezza**

## PROTOCOLLI DI TRASPORTO
Le applicazioni web per funzionare utilizzano uno di questi 2 protocolli, che offrono diversi servizi come:
- **TCP**
	- **TRASPORTO AFFIDABILE**
	- **CONTROLLO DI FLUSSO:** mittente non sovraccariva il desinatario
	- **CONTROLLO DI CONGESTIONE**:varia la velocità di trasmissione in base alla congestione della rete
	- **CONNECTION-ORIENTED**:setup richiesto tra processi client e server
	- Ma **NON OFFRE**, temporizzazione, sicurezza e un throughput minimo garantito.
- **UDP**
	- **TRASPORTO NON AFIIDABILE**
	- Temporarizzazione e throughput migliore del TCP

# WWW
Sistema che permette la **lettura ipertestuale** dei documenti collegati tramite **hyperlink**.

Il **WWW**(World Wide Web), offre un sistema di **pagine o librerie**, a cui si può accedere tramirte programmi come i **Web browser**.

# WWW 1.0
All'inizio il web era **statico**, l'utente non **interagiva** con le pagine web che venivano restituiti al client dai server.

## WWW 2.0
Il web diventa una **piattaforma**, dove l'utente diventa il centro, grazie ai dati forniti da loro.

## WWW 3.0
Nelle pagine web vengono integrati linguaggi, così da permettere l'interpretazione di dati e fornire **servizi costruiti attorno ad ogni utente**.


## WEB DINAMICO
Sono applicazioni web che in base a **dati forniti** dall'utente, rispondoono con **pagine web personalizzate**.
All'inizio si utilizzava un'interfacia **CGI** , che permetteva la comunicazione tra, la web app e il database, tramite la web app che analizza i dati forniti dall'utente, risponde con una **pagina web** personalizzata, grazie alle interrogazioni a DB.
### CGI(Common Gateway Interface)
Possono essere scritti in qualunque linguaggio di programmazione, e utilizza standard di comunicazione con i server per scambiare i parametri, però per ogni richiesta al server, quet'ultimo deve avviare un nuovo processo, questo aumenta di molto il carico al server.

Però questo presenta diversi **problemi** come:
- **Codice potenzialmente ripetuto**
- **Codice di dettaglio** 
- **Combinazione codice Python e HTML**
- **Combinazione di output e application logic**
- **Sconsigliabile anche per un progetto piccolo one-of-a-kind!**

### FRAMEWORK WEB
**Framework Web** progettati per ==supportare lo sviluppo di siti Web dinamici.==
Include librerie che offrono funzionalità comuni a questo tipo di applicazioni 
Base o scheletro su cui costruire 

Oggi giorno ogni tipo di web app, ha un **set comune di requisiti** e **funzioni**, infatti:
- **Framework supportano** di base queste funzionalità
- **Framework** offrono una modalità di interazioni con i DB trasparente

## ELEMENTI DEL WEB
Per un'architettura client-server, esistono 3 standard:
- **URL e PAGINE WEB**:
	**URL** è una modalità di naming che **identifica la posizione** di una risorsa web
	Una pagina web è formata da diversi oggetti:
	- Pagine HTML (solitamente il file principale) 
	- Immagini 
	- Audio 
	- Video 
	- Programmi eseguibili
	Un URL è formato in questo modo [[4-LivelloApplicazione-HTTP.pdf#page=43|4-LivelloApplicazione-HTTP, pagina 43]]
- **HTML**
	**Linguaggio di markup** per la formattazione delle pagine
	Usato per strutturare una pagina web senza la specificazione dello stile della pagina.
- [[APPLICAZIONI DI RETE#PROTCOLLO HTTP|HTTP]]
	**Protocollo di livello applicazione**

# PROTCOLLO HTTP
**==HyperText Trasmission Protocol==**, protocollo applicativo di tipo request/reply basato sulla suite di protocolli TCP/IP, che permette di **reperire file nel web**.
Usa **TCP come protocollo di trasporto**, perchè **offre affidabilità di trasmissione** che comporta l'integrità dei messaggi trassmessi.

In un'architettura di tipo client-server esistono 2 ruoli:
- **CLIENT**
	browser che invia richieste e riceve le risposte, e visualizza gli oggetti web.
- **SERVER**
	Web server che invia oggetti Web, in risposta a richieste ricevute.

Per trovare questi oggetti web bisogna darli un nome tramite il meccanismo dell'**URL**, il quale specifica la **posizione fisica** di ogni risorsa presente nel web.

Questo protocollo è definito **sateless**, cioè non conserva informazione sulle richieste passate.

La connessione instaurata tra il client e il server, può essere:
- **PERSISTENTE**(solo nella versione 1.0)
	Il server lascia la **connessione aperta** dopo aver inviato la risposta HTTP
	Tutti i messaggi tra lo stesso server e lo stesso client passa sempre sulla setssa connession, fino a quando non rimane inattiva per un certo lasso di tempo configuarbile

- **NON PERSISTENTE**(dalla versione 1.1 in poi)
	**RTT**(Round Trip Time), tempo che impiega a viaggiare dal client al server e il ritorno.
	Per ogni richiesta di un file ci si impiega minimo 2RTT + Ricezione del file, per ogni connessione aperta deve essere presente un **overhead**, e i server devono essere raggiungibili da **più client allo stesso tempo** 

**HTTP funziona con 2 tipi di messaggi**:
- **richiesta**
	- **Metodo**: Le richieste sono operazioni quando il client richiede qualcosa al server, quello più utilizzato è quello **GET** 
	- URL 
	- Identificativo della versione del protocollo HTTP (es. HTTP/1.1) 
	- Insieme di extension header: contengono **informazioni addizionali**, come orario della comunicazione o informazioni riguardo al client.
- **risposta**
	Formato da un **header** che contiene il **codice di stato**, versione del protocollo, campi header e alla fine i dati

Esistono diversi tipi di **status code**:
![[Pasted image 20260311160252.png]]


### COOKIE
Ogni volta che un client effettua una connessione, il server invia anche un cookie il quale avra un **identificativo di sessione**, il quale sarà diverso per ogni client.
Questo può permettere al server di **identificare** il client.
Ma viene usato anche per, **ricostruire le sessioni** di questo client, mantenendo informazioni che permettono, di:
- **monitorare** le attività dell'utente
- **mantenere l'accesso** in diverse pagine del sito

Esistono 2 tipi di cookie:
- **PRIMA PARTE**
	Cookie inviati al browser dirattamente dal sito che si sta visitando, gestiti dal proprietario del sito, i quali permettono **il giusto funzionamento del sito.**
- **TERZA PARTE**
	Appartengono a domini diversi dal sito che si sta visitando, questo succede quando i siti web hanno **contenuti** che **appartengono a siti web esterni**.
	

### HTTP 2.0
Nasce per migliorare le prestazioni del web, questa versione non viene codificata in **ASCII**, non è un trasferimento testuale, ma un trasferimento **binario**, e viene implemenatato anche il **multiplexing**.

==**1.1 vs 2.0**==
- ==1.1==: Utilizza un formato **testuale**, il che rende il parsing più semplice ma **meno efficiente** in termini di elaborazione e dimensione dei messaggi
- **2**: Utilizza frame binari: **dati binari organizzati in piccole unità** (‘frame’) Riduce overhead e consente una gestione più efficiente dei dati durante il trasferimento
- ==1.1==: Gli **header vengono inviati in chiaro** in ogni richiesta e risposta, aumentando l'overhead, specialmente con header ripetitivi.
- **2**: Utilizza un meccanismo di **compressione degli header**, riducendo significativamente il volume di dati inviati e migliorando le performance
- ==1.1==: Non dispone di un meccanismo nativo per inviare risorse non richieste.
- **2**: **Consente al server di "spingere" (push) risorse aggiuntive al client** prima che quest'ultimo le richieda, migliorando i tempi di caricamento

Il 2.0 introduce il concetto di **stream** (sequenza logica di bit che appartiene ad una richiesta HTTP), una stessa connessione TCP può **trasportare più stream** contemporaneamente, grazie ad un **stream ID** si riesce a identificare uno stream e questo permette ai client di capire quale sia il proprio messaggio.

![[Pasted image 20260316143924.png]]

### HTTP 3.0
Protocollo di trasporto che **non utilizza** TCP, ma utilizza **QUIC**, un protocollo basato su UDP che integra le funzionalità di TCP.
**QUIC (Quick UDP Internet Connections)** sviluppato originariamente da Google
**QUIC** permette di.
- Avere **un multiplexing avanzato**
- **Riduzione della latenza**
- **SICUREZZA INTEGRATA**
-  TLS 1.3 Integrato

### HTTPS
**HTTPS HyperText Transfer Protocol Secure**
Utilizza crittografia di tipo **TLS**(Transport Layer Security) per proteggere le comunicazione
Questo garantisce:
- **Riservatezza**
- **Integrità**
- **Autenticazione**

HTTPS funziona:
1) Il browser si collega al server tramite HTTPS (porta 443) 
2) Inizia il TLS handshake: il browser invia un messaggio con le versioni TLS e gli algoritmi supportati 
3) Il server risponde e invia il certificato digitale 
4) Il browser verifica il certificato (CA, dominio, validità) 
5) Client e server negoziano una chiave di sessione condivisa (Fine TLS handshake) 
6) La connessione diventa cifrata 
7) I dati HTTP vengono scambiati in modo sicuro 

#### CERTIFICATI
Esistono 2 tipi di certificati:
- **SSL**: Predecessore TLS, tecnologia ormai deprecata per garantire la sicurezza di una connessione a Internet mediante crittografia dei dati inviati tra un sito web e un browser
- **TLS**: Versione aggiornata e più sicura di SSL. Si mantiene il termine SSL nel nome dei certificati

# DNS
Tutti i dispositivi su internet, hanno almeno 2 identificatori:
- **INDIRIZZO IP**
	Numero utilizzato per indirizzare e instradare pacchetti nella rete
- **HOSTNAME**
	Nome logico e mnemonico utilizzato dalle persone

È un servizio che:
- utilizza un database che viene identificato come **DNS SERVER**
- Protocollo **a livello applicazione che consente agli host di interrogare il database**
È basato su una struttura Client-Server.

In caso di un grande traffico, si possono utilizzare **più indirizzi IP** associati per **un solo hostname**, queste permette di distribuire il carico di traffico a più server.

Questo servizio non è centralizzato perché causerebbe molti svantaggi come: [[5-LivelloApplicazione-DNS.pdf#page=8|5-LivelloApplicazione-DNS, pagina 8]]

Questo servizio è definito anche gerarchico perchè formato da più livelli:

| LIVELLO | NOME              | COSA FANNO                                                                                                                                            |
| ------- | ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1°      | Root server       | Forniscono indirizzi ip, ai TLD Server, in tutto il mondo ce ne sono **13**, che però sono **replicati**, e vengono gestiti da diverse organizzazioni |
| 2°      | TLD Server        | Resposabili dei **domini di primo livello** come .org, .com etc...       Questi forniscono indirrizzi ai server autorativi.                           |
| 3°      | Server autorativi | Sistema in cui sono **conservati record ufficiali per i singoli domini**, con le **risoluzioni degli hostname in indirizzi IP**                       |
| +       | Server Locali     | Gestiti da ISP o da DNS pubblici,                                                                                                                     |


## DOMINI E ZONE
**DOMINIO**: nome gerarchico nel sistema DNS che identifica un’entità su Internet (tipicamente un sito o un’organizzazione)

**SOTTODOMINIO**: fa parte di un dominio più grande, è semplicemente un livello più specifico nella gerarchia DNS. Ogni etichetta aggiunta a sinistra crea un sottodominio

**ZONA DNS**: Una zona DNS è una porzione dello spazio dei nomi DNS, gestita da una specifica organizzazione (unità amministrativa) e per la quale un server DNS è responsabile e autoritativo
Una zona dns contiene domini e sottodomini, che a loro volta **possono essere zone**.

Esistono 2 tipi di **nameserver**:
- **server primario**: Legge i dati su di una zona direttamente da un master file.
- **server secondario**: Scaricano i dati di una zona rispetto al loro server primario.

Un master file contiene i **dati relativi ad una zona**.
Per ciascuna Zona, c’è sempre un server primario e vi può essere un certo numero di server secondari, che contengono una copia del database hostname-indirizzi IP.

## DNS CACHING
Usato in modo estensivo per **migliorare le prestazioni**:
- Ridurre numero di messaggi DNS in giro per la rete 
- Ridurre ritardo per ottenere l’indirizzo IP desiderato
Una volta ottenuto un **mapping hostname-IP**, il server DNS locale lo memorizza in cache e lo restituisce su richiesta.

## DNS RECORD
I server DNS memorizzazano i **RR(RESOURCE RECORD)**
Ogni risposta DNS contiene un messaggio del tipo:
![[Pasted image 20260420151231.png]]

Il significato di name e value dipende da **type**, con **type=A (address)**:
- **name** = hostname
- **value**=indizirro ip
### RECORD NS
**Name Server**
Specifica il/i server che **contengono dati autoritativi relativi ad una Zona**, contiene dati su server primario, e possibili server secondari.
Utilizzato per **instradare le richieste DNS successive alla prima**.

### RECORD CNAME
**Canonical Name**
Record usato per fornire agli host richiedenti il nome canonico relativo ad un hostname che ha un alias.
**Nome canonico di un host** è il **nome DNS principale** e ufficiale associato a quell’host.
**Host aliasing**: possibilità per uno stesso host di **avere più alias**, cioè altri nomi che puntano allo stesso host.

Il nome canonico deve avere un record A.

### RECORD MX
**Mail eXchanger**
Record che consente ai mail server di **avere alias semplici**.
**Value** = nome canonico di un mail server che ha **Name** come alias.
Possibilità per una società di avere gli **stessi alias** per il proprio **mail server** e per il proprio **FTP server**.

## PROTOCOLLO DI TRASPORTO
Può utilizzare sia **UDP** sia **TCP**, però viene  **preferito UDP**, perchè permette velocità migliori, ma utilizza TCP per il trasferimetnto di flie da un name server all'altro.

# POSTA ELETTRONICA
Un indirizzo email, è formato da **nomeUtente**@**dominio**.

Questo servizio è formato da:
- **MAIL USER AGENT**
	Client di posta elettronica, programma per comporre e spedire una mail.
	Ha funzioni anche di memorizzare messaggi in arrivo alla **user mail box**, ma anche quelli in **uscita**, i quali vengono memorizzati all'interno **di una coda** in modo temporaneo, nel caso che il **server destinazione** non sia disponibile. 
- **MAIL SERVER**
	È formato da:
	- **MAIL TRANSFER AGENT**: ha diverse funzioni come la **memorizzazione** dei messaggi all'interno delle mail box, sia nel caso di messaggi in arrivo sia per messaggi in uscita e si occupa anche degli scambi di messaggi attraverso SMTP.
	- **Mailbox**: Contiene i messaggi in arrivo all'utente
	- **Coda di messaggi**: messaggi che devono essere inviati
	- **SMTP**: protocollo che utilizzano i server per comunicare basato su TCP	
- **Simple Mail Tranfer Protocol**
	Protocollo utilizzato per trasferire dati **da MTA mittente a MTA destinazione**, basato su TCP per garantire l'affidabilità del trasporto, utilizzando la **porta 25**.

## TRASFERIMENTO DATI
Il trasferimento dei dati avviene in **3 fasi**:
- **HANDSHAKING SMTP(diverso da quello TCP)**
- **Trasferimento messaggi**
- **Chiusura**
Utilizza **connessioni persistenti** così da permettere il trasferimento di più messaggi tra la stessa coppia di MTA.

Il messaggio è diviso in 2 parti:
1) **header**: Contiene i campi codificati
2) **body**: prime versioni consentivano solo testo in ASCII ma le successive evoluzioni anche e-mail in formati più elaborati
![[Pasted image 20260422103316.png|617]]

## SMTP vs HTTP
Sono tutti e 2 protocolli di tipo **comando/risposta**:
- **HTTP**
	Protocollo d tipo PULL, dove la connessione viene instaurata da chi vuole scaricare
- **SMTP**
	Protocollo di tipo PUSH, dove la connessione viene instaurata da chi vuole mandare.
Ma tutti e 2 utilizzano connessione persistenti.

## ESMTP
**Extend SMTP**
Attualmente lo standard ESMTP, è SMTP più alcune estensioni di sicurezza - SMTP Service Extension
Oltre a ESMTP esistono altre estensione del protocollo SMTP come:
- **AUTH**
- **STARTTLS**

## PROTOCOLLI DI ACCESSO
SMTP è il protocollo che 2 server utilizzano per comunicare tra loro, ma i client devono essere in grado di accedere alla propria casella di posta, per questo esistono protocolli di accesso alla posta, come:
- **POP3**
	Progettato per scaricare email dal server e cancellarle dopo il download, non effettua sincronizzazione tra dispositivi, protocollo vecchio e attualmente poco utilizzato
- **IMAP**
	Progettato per leggere e gestire le email direttamente sul server, senza scaricarle definitivamente sul dispositivo, permette l'organizzazione delle mail in cartelle e sottocartelle, e effettua sincronizzazione tra server e dispositivi che effettuano accesso alla casella postale
- **HTTPS**
	Permette l'accesso tramite web, ma non sostituisce gli altri 2




