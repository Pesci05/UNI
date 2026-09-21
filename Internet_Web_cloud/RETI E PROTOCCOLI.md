# INTRODUZIONE
Internet nasce nel 1982 grazie al protocollo **TCP/IP**, e nel 1991 nasche il **WORLD WIDE WEB (WWW)**, grazie a Tim Berners Lee un ricercatore del CERN con il **primo sito web della storia**, grazie al linguaggio **HTML** e al protocollo **HTTP**.

Internet permette una comunicazione tra host, dove il messaggio viene scritto in **pacchetti**(insieme di bit).

L'**architettura di rete** è basata su livelli, dove il più basso è quello più fisico(connessioni via cavo Es. Eth) al più alto cioè gli applicativi o servizzi di rete come **SMTP**.

# PROTOCOLLI
Un insieme di **regole e convezioni**, le quali definiscono come funziona la comuniczione tra due host, che si basa su:
- **SINTASSI**
- **SEMANTICA**
- **TEMPORIZZAZIONE**
Ogni protocollo interpreta un blocco all'interno di uno stack.
Ogni livello di quessto **stack** utilizza solo e soltanto i dati forniti da quello **precedente**(sotto).

Nella realtà, un sistema di comunicazione complesso, **non può usare un solo protocollo** di fatto si utilizza un **insieme di protocolli** che comunicano tra loro.
Ogni protocollo di questo insieme è chiamato **blocco** o layer, e questo insieme si chiama **stack**.

Ogni blocco di questo stack , comunica solo con quelli **adiacenti**.
Per quanto riguarda comunicazioni tramite internet, un messaggio inviato da un mittente **passa per ogni blocco** dello stack, fino a risalire per quello del destinatario.
![[Pasted image 20260305224706.png]]

Il messaggoo in questo caso, è formato dai **dati** del messaggio, e da un **header** che identifica il livello, ogni livello **==incapsula il messaggio==** **aggiungendo gli header del proprio livello.**
![[Pasted image 20260305225229.png]]

# STACK
Per identificare le regole per una comunicazione, comune per tutte si sono create delle regole che inquadrano in che **modo si deve eseguire una comuicazione**.
Esistono 2 tipi di standard:
- **ISO/OSI**
- **TCP/IP**

## ISO/OSI
**ISO** è un'ente globale che che ha definito molti standard di protocolli per la **connessione eterogenea** di nodi.
Lo standard che studiamo è **OSI(Open System Interconnection)**.
È composto di **7 livelli**, dove il più alto è quallo con il **livello di astrazione** maggiore, invece il più piccolo è il **livello più fisico**.
## LIVELLI
- ==LIVELLO 7 **APPLICAZIONE**==
	Fornisce un'interfaccia standard per i programmi applicativi che utilizzano la rete.
- ==LIVELLO 6 **ASTRAZIONE**==
	Risolve problemi di **differenze di formato**, **compressione dei dati**, **sicurezza** e **autenticità dei messaggi**. 
- ==LIVELLO 5 **SESSIONE**==
	Consente di stabilire **sessioni**, così da permettere di implemetare funzioni di sincronizzazione e mantenimento dello stato.
- ==LIVELLO 4 **DI TRASPORTO**==
	Effettua il controllo end-to-end della comunicazione, questo può garantire l'affidabilità del trasporto.
- ==LIVELLO 3 **RETE**==
	Fornisce i collegamenti e l’instradamento dei pacchetti nella rete.
- ==LIVELLO 2 **COLLEGAMENTO DATI**==
	Gestisce i trasferimenti di pacchetti da un nodo (host o router) a quello successivo
- ==LIVELLO 1 **FISICO**== 
	Gestisce i particolari meccanici ed elettrici della trasmissione fisica di un flusso di bit 

## STACK TCP/IP
I protocolli basati su questo stack sono formati da **4 livelli** e non **da 7**.
![[Pasted image 20260614161817.png|423]]

- **LIVELLO APPLICAZIONE**: servizio che permette di eseguire delle operazioni, utilizza il livello sottostante per fornire i propri servizi, come:
	- HTTP
	- FTP
	- DNS 
	- SMTP

- **LIVELLO TRASPORTO**: trasferisce i messaggi del livello sopra, tra **2 hots terminali**:
	- [[LIVELLO trasporto#UDP|UDP]]
	- [[LIVELLO trasporto#TCP/IP|TCP]]

- **LIVELLO RETE**: si occupa di trasferire i pacchetti **da un host mittente a uno destinatario**, il livello superiore passa al livello rete un indirizzo ip del destinatario, questo livello comprende il **PROTOCOLLO IP**.

- **LIVELLO HOST TO NETWORK**: comprende i **livello fisico e data link** di ISO/OSI, la connessione fisica dipende **dalla connessione fisica** e dal **mezzo di trasporto** che si utilizza per trasportare i pacchetti.

La comunicazione tra 2 host, non avviene direttamente tra 2 terminali ma **tra i 2 host, e i vari router dove il messaggio passeggrà**.

## STORE AND FORWARD
I pacchetti si muovono tra un **hop e l'altro**(router in mezzo alla rete), i router prima di instradare i bit, deve prima **immagazzinare tutto il pacchetto** e poi inizia a trasmetterlo all'uscita.

Il ritardo di questo tipo di comunicazione sarà:
![[Pasted image 20260302144558.png]]

dove **L** indica il numero di bit del pacchetto inviato, **R** velocità del canale trasmissivo e **N** è il numero di router attraversati dal pacchetto.
Questo vale soltanto se il pacchetto inviato è singolo ma nel caso ne siano inviati molteplici il **delay** sarà dato da:
$$
delay=(N+(P-1)) \frac{L}{R}
$$
dove **P** è il numero di pacchetti inviati.

Nella realtà questi pacchetti oltre al delay ci si **aggiunge anche un ritardo**, oppure delle perdite, causata da un buffer, poichè ogni router ha **più** linee di entrata e uscita, quindi se il buffer si riempe, e ogni pacchetto deve **aspettare il proprio turno**, questo può causare anche un **perdita di pacchetti**.

### CIRCUIT SWITCHING
Mantenere una linea **riservata** tra 2 host sono per l'intera durata della comunicazione, anche se a basse prestazioni, ha una velocità **sempre costante**.

Se 2 host devono comunicare, la rete stabilsce una comunicazione **dedicata a loro**, ogni connessione occupa per tutto il tempo **la banda**, questo non permette ad altri host di utilizzare la stessa connessione.

È possibile utilizzare dei router che implementano più circuiti di switching, questo consente di fare più comunicazioni in contemporanea, ogni connessione instaurata occuperà fino alla fine della comunicazione **una delle possibile connessioni**, dove ogni comunicazione ottiene una frazione delle risorse del canale trasmissivo.

Questo processo nella realtà funziona graze al **multiplexing**, dove le parti sono suddivise:
- Le parti di risorse sono **assegnate alle chiamate**
- Le parti di risorse riservate da una chiamata, sono **riservate** cioè non posssono essere condivise con altre chiamate, anceh se inutilizzate.
Questo può essere implementato tramite 2 metodi:
- **FDM**(Frequency Division Multiplexing):
	Lo spettro di frequenza di un collegamento, viene suddiviso in varie bande(Numero di circuiti accessibili) dove ogni **banda è associata ad una connessione**.
	Per 4 circuiti:
	![[Pasted image 20260402232934.png]]

- **TDM**
	Il tempo viene diviso in **frame di una certa durata** che vengono divisi per ogni circuito  creando degli **slot** dedicati per igni connessione.
	![[Pasted image 20260402234746.png]]

Però il circuit switching rischia di essere **inefficiente**, in caso di traffico intenso e incostante, per questo avvenne la creazione del **PACKET WSITCHING**.
### PACKET SWITCHING
Non esistono canali dedicati, ogni pacchetto **condivide le risorse di rete**.

Ogni pacchetto viaggia sulla stassa rete cioè:
- Pacchetti da diverse sorgenti viaggiano sullo stesso link
- Può esserci **conflitto**
- I pacchetti in conflitto vengono inseriti in una coda, **buffer di output**, attendondo finchè la risorsa non ritorna disponibile, la coda viene gestita in ordine **FIFO**![[Pasted image 20260402235328.png]] 
Nel caso che la coda sia piena l'**ultimo pacchetto** arrivato **viene scartato**
# LAN E WAN
Esistono diversi tipi di reti, dove la **rete di accesso** è la rete dove sono collegati gli host, e sono collegati ad un **edge router**, il quale permette di comunicare le reti esterne, questi router si collegano con una  **ISP**(Internet Service Provider).
## LAN 
o **rete locale**, ricopre un'area geografica limitata:
- edificio
- campus
- ecc
Queste tipo di Reti sono:
- **Veloci**: poichè collegate tramite tecnologie ethernet o wifi, i quali offrono elevate prestazioni
- **bassa latenza**
- **gestione centralizzata**

## MAN
o (**Metropolitan area network**), rete che collega diverse LAN tramite una rete più grande, di solito ricopre una città o zona residenziale.
Offre una copertura maggiora ad una LAN, può collegare più edifici o campus presenti in una zona urbana, può essere gestita da enti pubblici o da grandi organizzazioni.

## WAN
Rete che si estende su aree geografiche molto ampie, come regioni, stati o addirittura a livello globale.

Questi tipi di reti hanno:
- **Copertura globale**: Collegano reti locali e/o Metropolitane, facilitando la comunicazione a distanza
- **Maggiore latenza e velocità variabile**: Le lunghe distanze e l’utilizzo di differenti tecnologie di trasmissione, possono introdurre latenze più elevate rispetto a LAN e MAN. 
- **Gestione e infastrutture complesse**: Spesso sono gestite da fornitori di servizi di telecomunicazioni e richiedono investimenti significativi in infrastrutture.

## WIRELESS
Queste tipo di rete oltre che essere collegate via cavo, possono esistere anche con collegamenti via **wireless**(Es: rete mobile):
- **Terza Generazione** (3G) – fino a 2 Mbps (ormai obsoleta) 
- **Quarta Generazione** (4G) – in teoria fino a 1 Gbps - in pratica tra 20 e 100 Mbps in mobilità 
- **Quinta Generazione** (5G) – in teoria ordine di 10 Gbps – in pratica tra 100 e 500 Mbps, fino oltre 1 Gbps in situazione ottimale e supporto per molti più device contemporanei
![[Pasted image 20260304142254.png]]

# RITARDI
Ogni pacchetto deve viaggiare attraverso la rete, passando da un router all'altro, per ogni router attraversato i pacchetti possono **subire ritardi**.
Il ritardo di un pacchetto può essere causato da diverse azioni:
- **Elaborazione**: comprende il tempo di analisi del pacchetto e dell'inidirizzo IP per determinare l'uscita.
- **Accodamento**: Ritardo dovuto alla messa in coda del pacchetto, questo causato dal numero di pacchetti ricevuti dal router.
	Questo tipo di ritardo a differenza di altri è quello che può variare più facilmente poichè non dipende solo da dispositivi e collegamenti, ma anche dalla **quantità di pacchetti in arrivo per roter**, i quali possono causare traffico.
	Per questo si deve calcolare l'**intensità di traffico**.
$$
	\frac{La}{R}
$$
	Dove **a** è la velocità media di arrvo dei pacchetti in coda, **L** dimensione dei pacchetti **uguale per tutti i pacchetti**, **R** è la velocitò di trasmissione.
	Invece la **velocità media in arrivo n coda è** $La$.
	Nel caso che continuino ad arrivare pacchetti anche quando la coda è piena, il router può solo **starcate il pacchetto arrivato** causando così **overflow**.
- **Trasmissione**: È la relazione tra la lunghezza del pacchetto **L** e la velocità di trasmissione **R**, **L/R**
- **Propagazione**: È il tempo in cui un bit riesce a propagarsi all'interno del collegamento, questo dipende dal **mezzo fisico**.



## THROUGHPUT END-TO-END
Il **throughput** è la velocità a cui i bit vengono trasferita da mittente a destinatario, e questo può essere **istantaneo**, cioè identificare la velocità in un certo istante di tempo oppure può essere **medio** cioè identificare la velocità media in un certo periodo di tempo.

La velocità tra 2 host(sia client che server) è decisa dalla **velocità del canale trasmissivo** con velocità minore.

Nel caso ci siano più coppie di host, e viaggiano sullo stesso canale trasmissivo, la velocità di questo sarà divisa per il numero di coppie(collegamenti), se il risulatato sarà minore ad altri possibili collegamenti tra i 2 host, **questo sarà il throughput**, ma se il **canale comune è molto maggiore** degli altri collegamenti, questo **non viene preso in considerazione** per il calcolo del throughput.
![[Pasted image 20260404010202.png]]

