# IIOT
La diffusione dei dispositivi elettronici è esplosa soprattutto grazie all'avvento dei smartphone, che sono dispositivi che comunicano tra loro grazie ad un infrastruttura che si chaima **INTERNET**, questo vale per tutti i tipi di dispositivi che comunicano tramite internet.

## IOT
**Internet Of Things** è una rete di reti, dove ogni oggetto viene **identificato univocamente**, in una rete **strutturata simile internet**.

Un **Smart Object** sono oggetti che fanno qualcosa d'intelligente, come percepire qualcosa e trasmettere un dato.
[[01_IoT_Introduction.pdf#page=12|01_IoT_Introduction, pagina 12]]

**CARATTERISTICHE**
[[01_IoT_Introduction.pdf#page=13|01_IoT_Introduction, pagina 13]]

**ETEROGENEITÀ**
- Tecnologie di comunicazione
- Prtocolli
- Hardware
- Software

## SFIDE IOT
- **Connectivity e Connection**
- **Mantenere l'eterogeneità**
- **Interazione e interoperabilità**
- **Sicurezza**
- **Memorizzazione e processo di dati**
- **Utilizzo standard dei protocolli**
- **Performance e real time performance**

### CONNETTIVITÀ
Si può utilizzare un sensore creato ad hoc per il dispositivo.
La **TELEMETRIA** permette di raccogliere misure effettuate da macchine remote, e puù essere utilizzata da:
- **Low range Measurement**
- **Short range Measurement**
**M2M**(Machine To Machine) è un generalizzazione della telemetria, che permette comunicazione bidirezionali tra una macchina comandata autonomamente e un collettore di dati.
M2M viene utilizzato soprattutto da aziende che progettano, producono e implementano **hardware personalizzato** per ogni oggetto progettato, questo vale anche per la **progettazione software**, questo però non permette la scalabilità.

![[Pasted image 20260916215308.png]]

| **M2M**                                                                              | **IoT**                                                                    |
| ------------------------------------------------------------------------------------ | -------------------------------------------------------------------------- |
| Dispositivi semplici che comunicano<br>tramite un software embedded e un sito client | Progetti a grande scala e un approccio di tipo totale                      |
| Sistemi isolati che utilizzano gli stessi standard                                   | Dispositivi integrati, tramite dati e applicazioni attraverso più standard |
| Poche opzione di scalabilità                                                         | Intrinsicamente più scalabile                                              |
| Connettività gestita via cavo o tramite rete cellulare                               | Solitamente richiede che i dispositivi siano connessi ad internet          |
| Storicamente utilizzato in svariate applicazioni                                     | In questo momento di sviluppo si hanno comunque delle radici in M2M        |
### IoT HARDWARE
![[Pasted image 20260916221241.png]]
- **Comunicazione**
	Questo permette di agli smart-objects, di comunicare tramite radio ricetrasmittente con un'antenna o una connessione via cavo.
- **Micro-controller**
	È un microprocessore che esegue software dgli smart objects, e questo sw dà il comportamento all'oggetto
- **Sensori e attuatori**
	Permettono agli oggetti un metodo per interagire con il mondo esterno.
- **Sorgente di energia**

### IoT Stack protocol
Per permettere agli oggetti di comunicare tutti tra loro, devono utlizzare dei meccanismi che permettono lo scambio d'informazioni.
![[Pasted image 20260916223323.png]]

I possibili protocolli utilizzabili sono:
- IP
- Bluetooth
- Mobile
- etc...

### INTEROPERABILITÀ
Un sistema fatto da IoT, permette di comunicari tra più oggetti che fanno cose diverse per raccogliere e gestire dati in input dai sensori di questi oggetti.



# SCAMBIO DI DATI
Lo scambio di dati avviene tramite infrastrutture dedicate/create per un certo tipo di progetto, il quale però si basa comunque su tutti i **protoccolli** che vengono utilizzati da **Internet**.

Alcuni di questi protocolli possono essere:

|Layer|Protocol|Unit (PDU)|Adds|
|---|---|---|---|
|Application|HTTP|Data|Request/response message|
|Transport|TCP|Segment|Ports, sequence numbers|
|Network|IP|Packet|Source/destination IP address|
|Data Link|Ethernet|Frame|MAC addresses, CRC trailer|

Come è stato detto in precedenza la progettazione di sistemi IOT avviene tramite un approccio web, perché:
- Il web viene utilizzato come base di questi sisetemi perché l'**esperienza**,**best practices** e il suo sviluppo sono maturati negli anni.
- **HTTP** è il protocolle predominante per **l'application layer** dello stack internet, questo significa avere una compatibilita molto ampia grazie alle infrastrutture internet.
- Una grande disposizione di **librerie** e **tools** utilizzabili da protocolli web a disposizione per ogni linguaggio di programmazione.
- Metodi di progettazione consolidati negli anni per lo sviluppo di web app, possono essere messi in pratico per progettare **sistemi IOT**, basandosi su simili archittetture, metodi di lavoro.
- L'architettura web ha dimostrato un **eccezionale scalabilità**, questo lo rende cruciale per supportare **miliardi di oggetti IOT connessi**.

## HTTP
Uno di questi protoclli può essere **HTTP**, il quale permette grazie ai suoi metodi di scambiare dati tra 2 oggetti, (**CLIENT/SERVER**).

Per evitare che ognuno sviluppi i propri metodi e **garantire una standardizzazione**, si introduce l'approccio RESTful, che sono delle **convenzioni** che permettono agli sviluppatori di creare sistemi **interoperabili**, **scalabili** e facili da integrare con con altre soluzione che si basano sull'architettura di internet.

## MESSAGGI HTTP
- # GET
	![[Pasted image 20261014190559.png]]
	La richiesta HTTP è fondamentale per modellare le comunicazioni **client-server** sia sul web sia su sistemi IOT.
	Questo messaggio rappresenta **come** un **client** inizia le interazioni con il **server**, per cercare, aggiornare o modificare risorse.
	In IoT HTTP viene comunemente usato per utilizzare le **RESTful API**, le quali  permettono di utilizzare uno standardizzato e efficiente gestione di memoria degli oggetti e servizzi.
	La richiesta HTTP è un messaggio che parte da un client vrso un server, chiedendo una specifica risorsa o una certa azione che il server deve fare.

| **Field Type** | **Description**                                | **Example Value**               |
| -------------- | ---------------------------------------------- | ------------------------------- |
| Status Line    | Protocol version, status code, textual message | HTTP/1.0 200 OK                 |
| Content-Type   | Format and encoding of returned content        | application/json; charset=utf-8 |
| Content-Length | Size of response content body                  | 610                             |
| Server         | Server software/version info                   | Werkzeug/1.0.1 Python/3.8.5     |
| Date           | Timestamp of response                          | Fri, 02 Oct 2020 15:22:10 GMT   |
| Content Body   | Requested data or output (after headers)       | { "location_info": [...] }      |
Questa struttura va bene per un messaggio che utilizza il metodo GET.

- # POST
Però per utilizzare il metood **POST**, la struttura cambia anche se di poco.
![[Pasted image 20261014192726.png]]
Questo metodo permette al client di **trasmettere dati** ad un server, per eleaborare o memorizzazare questi dati.
Bisogna **definire chiaramente** il **metodo**, il **percorso della risorsa**, gli **header** e un **body**, questo metodo fornisce un framework standardizzato per la modellazione di API **interoperabili** e **scalabili**.
È formato da:
- **content-type** $\to$ Dichiara il **formato** dei dati
- **user-agent** $\to$ Identifica il software utilizzato dal client
- **Host** $\to$ IP o Dominio del server

 
Per lo scambip di dati si utilizzano dei formati speciali come:
- **XML**
	Utilizza sintassi html
- **JSON**
	Utilizza sintassi JavaScript
- **YAML**
Questo permette agli oggetti che ricevono e mandano dati, di non dover inventarsi un proprio formato, infatti questo tipo di formati sono diventati **standard**.


# REST vs SOAP
## RESTful HTTP
Formato da più livelli:
- **LIVELLO 0**
- # LIVELLO 1
- # LIVELLO 2 
	l livello 2 si basa sulle operazioni **CRUD** di HTTP, questo tipo di metodo permette la scalabilità e chiarezza nello scambio di dati.
	Ogni dato/risorsa viene identificato da un **URI**.
	
	Il livello 2 mappa i metodi di HTTP per ottenere le operazioni CRUD:
	- **GET**
	- **POST**
	- **PUT**
	- **DELETE**
	Ogni metodo ha un suo codice di risposta, i quali sono stati **standardizzati** sin dalla nascita di HTTP, per questo bisogna utilizzarli senza crearne di nuovi, alcuni di questi errori possono essere:
	- **2xx** $\to$ **SUCCESSO**
	- **3xx** $\to$ Server **Ridireziona** il client, la risorsa richiesta dal client è stata spostata
	- **4xx** $\to$ **Errore** del **Client**, può essere una brutta richiesta da aprte del client al server
	- **5xx** $\to$ **Errore** del **Server**, 
	Per utilizzare le funzioni CRUD con un tipo di modellazione REST si divide in:
	- **Create** $\to$ post
	- **Read** $\to$ get
	- **Update** $\to$ put
	- **Delete** $\to$ delete

I metodi CRUD vengono divisi in:

| Method | Safe | Idempotent | CRUD Operation |
| ------ | ---- | ---------- | -------------- |
| GET    | Yes  | Yes        | Read           |
| POST   | No   | No         | Create         |
| PUT    | No   | Yes        | Update         |
| DELETE | No   | Yes        | Delete         |

- **LIVELLO 3**

# The Constrained Application Protocol (CoAP)
Le reti IOT, soprattutto quelle a **bassa potenza e lossy network**, hanno caratteristiche molto diverse da quelle di internet.

- **Pacchetti dalla grandezza ridotta**
- **Larghezza di banda minore**
- **Bassa potenza**
- **Bassi costi**
- **Inaffidabilità**
- **Duty cycling**

## HTTP e TCP non sono adatti
Per utilizzare i protocolli di livello applicativo, in un'applicazione di tipo IOT dve essere progettata in modo tale che il prtocollo, debba mantenere le **limitazioni dei layer sottostanti** e dalla natura del **smart object**.

- **HTTP**: Prtocollo testuale che può facilmente fuoriuscire dalla dimensione massima che un sistema IOT possa contenere in un network frame. Analizzare il testo del messaggio HTTP serve potenza di calcolo che degli oggetti non posseggono.
- **TCP**: Protocollo bastato sulle connessione, e le procedure di connessione possono essere molto aggravanti su oggetti, perchè sono lavori pesanti per dispositivi molto limitati.

Però l'adozione di API RESTful nell'application layer può trasformare la rete di dispositivi in una rete con **architetura simile a quella di Internet**.

## Protocollo CoAP
Il protocolla **Contrained Application Protocol**, è un protocolla di livello applicativo
