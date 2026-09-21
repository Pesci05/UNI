Il livello Host to Network si occupa della **trasmissione di dati**, tra host connessi sulla stessa rete fisica.
**Modalità di interconnessione e protocolli per la trasmissione dati** tra host interconnessi sono strettamente dipendenti tra loro.
I servizi offerti da **diversi protocolli h2n sono diversi tra loro**.

Questo lovello comprende:
- **Livello 1 (fisico)**
	Connessione di host secondi diversi mezzi trasmissivi.
- **Livello 2 (data link)**
	- **Framing**
		Struttura del frame dipende dal protocollo utilizzato
	- **Accesso al link**
		Protocollo che controlla l'accesso al canale trasmissivo in caso sia condiviso da più host.(**MAC**)
	- **Recapito affidabile**
		- Meccanismi di acknowledgement e ritrasmissione
		- Spesso usato per collegamenti ed elevato tasso di errore per evitare ritrasmissione end-to-end
		- Considerata non necessaria su collegamento con bassi tassi di errore
	- **Controllo di flusso**
	- **Rilevazione di errori**
		- Errori di bit causati dall'**attenuazione del segnale** e dai **disturbi elettromegnetici**
		- **Bit di controllo** errore nel frame $\to$ **contorollo** implementato in hardware
	- **Half-duplex o Full-duplex**
I servizi sopra citati **non sono supportati** per tutti i protocolli/tecnologie.

Questo livello permette la connessione:
- **host to host**
- **host to router**
- **router to router**
Quando un datagramma parte da un host, deve attraversa N collegamenti, per ogni collegamento ci sarà un **nodo che incapsula il datagram in un frame**, e lo ritrasmette lungo un collegamento.

## COLLEGAMENTI
- **Broadcast**
	- Molti host connessi ad uno stesso canale trasmissivo
	- Necessario un **protocollo d'accesso al mezzo** per coordinare le trasmissioni e per evitare le collisioni
- **Punto-Punto (PPP)**
	- Costituito da un'unico trasmittente ed un unico ricevente collegato all'altra estremità
	- Collegamento utilizzato tra **2 router** o fra un **modem di accesso residenziale ed il router residenziale ed il router ISP**

## MODALITÀ DI TRASMISSIONE
- **Unicast**
	Comunicazione tra un unico mittente ed un unico destinatario
- **Multicast**
	Comunicazione tra un unico mittente ed un gruppo di destinatari
- **Anycast**
	Comunicazione tra un singolo mittente ed almeno un ricevente in un gruppo
- **Broadcast**
	Comunicazione tra un singolo mittente e tutti gl altri nodi

# ADATTATORI DI RETE
Il protocollo H2N è implementato in una **scheda adattatrice**, detta anche **Network Interface Card** (NIC).
Tutti i dispositivi in una rete dovono avere una **scehada di rete**.
![[Pasted image 20260629235058.png]]

L'adattatore di rete è un'**enetità semi-autonoma** rispetto all'host in cui risiede, e viene controllata dal **cuore**, che è un **controller** a livello di collegamento, implementato con un **chip dedicato**, che implementa molti servizi del livello collegamento.
La maggior parte delle funzionalità del controller vengono **implementate in hw(hardware)**, anche se una parte viene effettuata via software dalla CPU dell'host.

# ETHERNET
## HUB e SWITCH
Dispositivo di livello fisico che agisce sui **singoli bit**.
Quando un bit arriva su un'interfaccia di un hub, il dispositivo **rigenera il bit** e lo **trasmette su tutti le sue altre interfacce**.
Ma nel momento in cui riceve farem da 2 diverse interfacce si ccrea una **collisione** e i nodi dovranno ritrasmetter i frame.

Per qeusto si è passatto agli **switch**, il quale è un **commutatore di pacchetti** di tipo **store-and-forward**.

## POPOLARITÀ
La popolarità di ethernet, è data dal fatto che sia **preformante e poco costosa**, ma anche perchè si presta per l'uso con diverse:
- **Topologie**
- **Tecnologie**, come cavi coassiali, in rami e fibra ottica.

## CARATTERISTICHE
- **Connectionless**
	Non esegua nessun tipo di procedura di handshaking tra mittente e destinatario
- **Inaffidabile**
	Il destinatario non invia ACK al mittente

Può essere collegato con:
- **Canale broadcast**
	Molti host connessi allo stesso canale trasmissivo. Diventa necessario un protocollo come **MAC**
- **Canale punto a punto**

## INDIRIZZI MAC
Gli host utilizzano **indirizzi MAC** per capire chi è il destinatario del frame.
Quando un host spedisce un pacchetto, deve inserirci l'indirizzo MAC, e lo passa alla LAN(**canale broadcast**), il pacchetto viene **accettato** solo quando l'**host ricevente vede la corrispondenza tra l'indirizzo del pacchetto e il prorio** e lo passa al livello superiore dello stack, in caso **contrario** il pacchetto deve essere **scartato**.
L'indirizzo MAC è l'identificativo della **schada di rete** non **dell'host come organismo**.
Ogni scehda di rete viene definita da un indirizzo di **48 bit**, che viene rappresentato in notazione esadecimale.

**HUB** e **SWITCH NON** hanno indirizzo MAC.

## FRAME
Il **frame ethernet** è formato da:
- **Preambolo** $\to$ 8 byte
	- Primi 7 byte hanno valore 10101010 $\to$ utilizzato per **sincronizzare** gli orologi del destinatario con quello del mittente 
	- L’ultimo byte ha valore 10101011 $\to$ gli utlimi 2 bit segnalano che la dafe di sincronizzazione è finita e sta arrivando il continuo del frame.
- **Indirizzo di destinazione**(6 byte) e **Indirizzo mittete**(6 byte)
	Indirizzo MAC di destinazione e mittente.
- **Tipo**
	Permette il **multiplexing** dei protocolli di rete, identifica a quale protocollo appartiene il frame, gli host per **risolvere** gli indirizzi devo implementari protocolli come **ARP e RARP**
- **Dati**
	Contiene i dati del datagramma IP
- **CRC**
	**Controllo a Ridondanza Ciclica**, permette al destinatario di rilevare la possibile presenza di un errore all'interno del frame, il CRC viene trasmesso dal mittente calcolando il suo valore in base a tutti bit del frame, escludendo il campo Preambolo. Il destinatario ricalcola il CRC e ne verifica la corrispondenza.

# PROTOCOLLI DI ACCESSO MULTIPLO
In questo tipo di protocolli si può verificare il rischio di **collisione**, cioè quando un nodo riceve 2 o più segnali allo stesso tempo, questo causa la perdita del frame.

Per evitare questo problema si è pensato di utilizzare degli **algoritmi distribuiti** che determinano come i nodi condividono il canale di comunicazione.

## PROTOCOLLO MAC
Si  suddividono in  **3 grandi categorie**:
- **Protocolli a suddivisione del canale**
	- Suddividono il canale in piccole parti, come nel [[RETI E PROTOCCOLI^fdm|mutliplexing a FDM nel CIRCUIT SWITCHING]]
	- Allocano le parti ai nodi per un uso esclusivo
- **protocolli ad accesso casuale**
	- Il canale non è diviso e può causare collisioni
	- Infatti utilizza meccanismi di **prevenzione** e **recovery** dalle collisioni
- **Protocolli a rotazione**
	I nodi apsettano il proprio turno per inviare i propri dati, nel caso di paccehtti molto grandi quei nodi possono avere un turno più lungo.

### CSMA(Carrier Sense Multiple Access)
Ascolta prima di trasmettere (**rilevazione della portante**).
- **Canale idle** $\to$ trasmette l'intero frame
- **Canale occupato** $\to$ Posticipa la trasmissione

Questo però non basta per evitare le collisioni, infatti per colpa del **ritardo di propagazione** 2 nodi possono non sentire che sta avvenendo una trasmissione.

Per questo si cerca di **rilevare le collisioni**, per questo il nodo che trasmette deve rimanere in ascolto del canale trasmissivo, nel caso rilevi che un altro nodo che interferisce con la trasmissione del proprio frame, **deve fermare la trasmissione**.
Il rilevamento di collisioni è più facile in caso di LAN wired, ma diventa più difficile in caso di LAN wireless.

L'algoritmo di rilevazione di collisione è:
1) Scheda di rete mittente riceve un datagram dal livello rete e crea un frame
2) Se la scheda rileva che il canale è idle inizia la trasmissione del frame, invece se è occupato aspetta che si liberi.
3) La scheda trasmette tutto il frame se non rileva altre trasmissione su quel canale trasmissivo
4) Se la scheda rileva una trasmissione mentre sta trasmettendo, interrompe la sua trasmissione
5) Dopo lo stop della trasmissione la scheda aspetta un tempo casuale dato da **binary exponential backoff**, che è un range che viene formato da ${0,1,2\dots 2^{N-1}}$ dove **N** è il numero di collisioni rilevate fino a quel momento.
# Address Resolution Protocol (ARP) 
L'hardware non riconosce gli indirizzi IP, per questo **ARP** permette di trasformare l'indirizzo IP di un host della stessa LAN nel **corrispondente indirizzo MAC**.

Il protocollo ARP è incluso in TCP/IP.

ARP utilizza **2 tipi di messaggi**:
- **Richiesta**
	Contiene l'indirizzo IP del destinatario, per effettuare la richiesta ARP utilizza un **broadcast**
- **Risposta**
	Contiene il corrispondente indirizzo MAC

Questo protocollo funziona:
1) Host trasmette in broadcast una richiesta ARP, cercando un indirizzo IP
2) Host mittente risponde in unicast al host mittente e gli risponde con il proprio indirizzo MAC

Per ridurre il traffico sulla rete dato dai messaggi ARP si utilizza una **cache ARP**, la quale contiene le risoluzioni degli indirizzi IP/MAC, all'interno della propria tabella d'instradamento.
Per **ottimizzare** ancora di più si può mandare nella richesta la corrispondenza tra il proprio indirizzo IP e quello MAC.

**==INVIO DATAGRAM TRA 2 RETI DIVERSE:==** [[15-LivelloH2N.pdf#page=46|15-LivelloH2N, pagina 46]]

## INTERCONNESSIONE DI UNA LAN
Un interconnessione di una lan viene formata da **apparati di rete** si distinguono in base:
- Numero di host collegati
- Efficienza delle comunicazioni
E possono essere:
- **Switch**
	Dispositico a **livello di collegamento attivo** a differenza di un hub.
	Approccio di tipo **store-and-forward**, il pacchetto viene prima memorizzato per poi essere spedito.
	L'indirizzo MAC presente in un frame in arrivo viene utilizzato per inoltrare selettiamente il frame su uno o più collegamenti.
	**Trasparente**
	**Plug and Play**: non hanno bisogno di configurazione
	Spesso lo switch viene utlizzato con una **topologia a stella**.
	Gli host hanno **connessioni dirette e dedicate** con gli switch, il collegamento tra host e switch utilizza il protocollo ethernet.
	Grazie a questo permette di **trasmettere in contemporanea** senza causare collisioni, permettendo comunicazioni in **full-duplex**.
	Ogni switch mantiene una **switching table** composto da:
	- Indirizzo MAC del nodo
	- Interfaccia che conduce al nodo
	- Il momento in cui è stata inserita una voce
	Gli switch **imparano** quali host possono essere attraverso le interfacce.
	Quando riceve un frame lo switch impara la locazione dell'host, memorizzando la coppia mittente/destinatario nella switch table.
	Gli switch oltre che essere connessi direttamente con host, possono essere **connessi tra loro**, questo permette di creare **archietture molte complesse**.

- **Hub**
	Dispositivo di **livello fisico** dotato di 2 o più interfacce, opera come un **ripetitore** che opera a livello di singoli bit, trasmettendo i bit ricevuti a tutte le altre interfacce.
	- **Vantaggi**
		Sono dispositivi **semplici** e **economici**, utilizzato soprattutto per piccole LAN.
	- **Svantaggi**
		Gli hub **non isolano il dominio dalle collisioni**, infatti il traffico di un host può collidere con il traffico di un altro qualsi host collegato alla LAN, in pratica un LAN collegata tramte hub può essere visto come un collegamento tramite bus

## SWITCH vs ROUTER
Entrambi sono **store-and-forward**
- **Router**: dispositivi di livello rete
- **Switch**: dispositivi di livello collegamento
Ed **entrambi** fanno uso della **tabella d'inoltro**:
- **Router**: Calcolano le tabelle utilizzando gli algoritmi di routing
- **Switch**: Imparano utilizzando meccanismi di flooding e self-learning

## VIRTUAL LAN
Lo standard IEE 802.1Q definisce le specifiche che permettono di definire più **reti locali virtuali (VLAN) utilizzando una stessa infrastruttura fisica**.
Una VLAN si **comporta come se fosse una rete locale** separate dalle altre:
- **Segmentazione del dominio di braodcast**, cioè i pacchetti in broadcast sono confinti nella VLAN
- La comunicazione a livello 2 è confinanta all'interno della VLAN
- La connettività tra diverse VLAN può essere realizzata solo a livello 3, attraverso routing
Le applicazioni di questo tipo sono legate soprattutto a esigenze di divisione del traffico tra gruppi di lavoro o dipartimenti di un'azienda/organizzazione.

L'utilizzo delle VLAN permettono:
- **Risparmio**
	Non serve avere delle infrastrutture fisiche per creare una rete locale con le relative linee e apparati
- **Aumento di prestazioni**
	Il confinamento del traffico broadcast permette di evitare la propagazione di frame verso dstinazioni non volute 
- **Aumento della sicurezza**
	Un utente in un VLAN non ha la possibilità di vedere il traffico i un'altra VLAN
- **Flessibilità**
	Lo spostamento di un'entità da una rete all'altra può essere realizzato senza modifiche alla topologia fisica, ma bisogna riconfigurare gli appositi apparati di rete.

## PORT BASED VLAN
Le porte di una switch sono raggrupate in modo che un singolo switch fisico operi come **multipli** switch virtuali.

Uno **switch** che supporta una VLAN deve essere **configuarato** in modo tale che permetta la possibilità di **avere più VLAN, su una singola infrastruttura LAN fisica**. 

L'isolamento di traffico in una VLAN funziona:
- I frame provenienti da un gruppo di N porte possono raggiungere solo quel gruppo di porte
- Una **tabella di associazione** tra porte e VLAN è mantenuta all'interno dello switch
- **Dynamic membership**: le porte possono essere assegnate dinamicamente tra le VLAN
- Per consentire la comunicazione tra VLAN, bisogna dedicare una porta per ogni VLAN alla comunicazione tra virtual network 
- La comunicazione avviene ramite **routing**
- Si vendono dispositivi che contengono sia **switch e router**.

## VLAN TRUNKING
Una porta speciale per ogni switch è configurata come **porta di trunking** per interconnetere gli switch VLAN.
La **porta di trunking appartiene a tutte le VLAN**: I frame inviati a qualunque VLAN vengono inoltrati attravero il collegamento di trunking all'altro switch.
