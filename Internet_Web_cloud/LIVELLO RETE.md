È il livello posto tra il livello di trasporto e il livello di Host to Network, e si occupa di **trasportare** segmenti dell'host mittente al destinatario.
- L'host **mittente** incapsula segmenti in datagrammi IP.
- L'host **destinatario** invece estrae i segmenti e li consegna aò livello di trasporto.
ll livello di rete è **presente in ogni dispositivo di rete**.
Uno dei dispositivi più importanti è il **router** il quale si occupa di esaminare i campi degli header di ogni datagarmmi IP che atraversano i router.

ll livello di rete:
- Garantisce **indirizzamento univoco di ogni host** tramite un **indirizzo IP**
- Si chiarisce l'architettura di internet
- Si illustrano funzioni di **routing**

# IP (Internet Protocol)
Utilizzato attualmente in 2 versioni:
- **[[LIVELLO RETE#IPv4|IPv4]]**
- **[[LIVELLO RETE#IPv6|IPv6]]**

**DATAGRAM IPv4**: [[11-LivelloIP-parte1.pdf#page=8|11-LivelloIP-parte1, pagina 8]]

Il datagram IP passa attraverso diversi link, i quali hanno MTU(Maximum Trasmission Unit) diversi, e questi datagram se sono **troppo grandi** devono essere frammentati, e riassemblati una volta arrivati al destinatario.

# IPv4
Per garantire un servizio di comunicazione universale serve avere un **indirizzamento univoco** per ogni dispositivo.
Ad ogni nodo è assegnato un **indirizzo IP unico** formato da 32 bit.
L'indirizzo IP è suddiviso in 4 parti formato da 8 bit, separate da un punto(**dotted notation**).
![[Pasted image 20260622215357.png]]
Un indirizzo IP può essere:
- Di lunghezza **fissa**
- lunghezza variabile
E può avere un certo tipo di sapzio di indirizzamento:
- **Gerarchico**
	Foramata da una **spina dorsale**(insieme più grande), **regional**(Insiemi nazionali), e l'insieme più piccolo è quelloi riservato alle **LAN**.
- Flat
### SUBNETTING
ll **subnetting** è una tecnica che permette di dividere una rete in più sottoreti, utilizzando una parte delle dei bit come identificativo della sottorete.

Ogni indirizzo è formato da una coppia, <hostId,netId>:
- **netid**
	Prefisso di rete che identifica la rete.
- **hostid**
	Identifica un host all'interno di quella rete.
![[Pasted image 20260622220839.png|310]]
La **netId** può essere chiamata anche **subnet mask**, nell'immagine la subnet mask è formata da 24 bit, identificata da "**/24**", cioè i primi 24 bit identificano la sottorete.

Questo tipo si notazione si dice **CIDR**(Classless InterDomain Routing), fatta come **a.b.c.d/x** dove x rappresenta il numero di bit assegnato alla netId.
![[Pasted image 20260622221603.png|539]]

La notazione usata per descrivere una subnet mask è la stessa che viene utilizzata per gli indirizzi IP, però per **ogni bit** che viene **utilizzato** per **descrivere una rete** viene **impostato ad 1**, mentre i bit riservati per gli host sono impostati a 0.
![[Pasted image 20260622222012.png|563]]

La gestione di indirzzi per organizzazioni come Università o aziende, generalmente viene assegnato **un blocco di indirizzi contigui** avente un perfisso di rete in comune dato da x bit.
Gli indirizzi saranno formati come: **a.b.c.d/x**
I **router esetrni** comprendono solo i bit che identificano la rete, i rimenti bit vengono usati per **distinguere gli host interni alla rete**.
La lunghezza del prefisso di rete **definisce** il **numero di host** all'interno della sottorete.
Per ogni rete e sottorete bisogna togliere 2 indirizzi, che vengono utilizzati **per usi speciali e sono riservati**, i quali sono:
- **Indirizzo di rete**: bit host tutti a 0
- **Indirizzo di broadcast**: bit host ad 1

Fino al 1985 CIDR, la C stava per Classfull, dove i prefissi di rete dovevano essere:
- **A** $\to$ 8 bit di rete $\to$ $2^24\to 16.777.216\space host$
- **B** $\to$ 16 bit di rete $\to$ $2^{16}\to 65.634\space host$
- **C** $\to$ 24 bit di rete $\to$ $2^8\to256\space host$
Questo significa la dimensione della rete è fissa, e può comportare che per organizzazione medio grande la classe C sia troppo piccola, ma la calsse B sia troppo grande.

Esistono anche indirizzi riservati ad usi speciali come:
- **Limited Broadcast address**
	Tutti i bit sono 1 (255.255.255.255), permette l'invio a tutti gli host presenti in una sottorete.
 - **Direct Broadcast address**
	 Tutti i bit della parte host sono 1, messaggio inviato a tutti gli host di una specifica sottorete, come per 223.1.1.255 per la sottorete 223.1.1.0/24.
- **Loopback address**
	Usato per il testing di applicazioni di rete, comunica con la macchina stessa ed è 127.0.0.1
- **Meta-indirizzo**
	0.0.0.0 ha significati diversi in base al contesto.
- **Altri indirizzi privati** dato dal NATting

Un host può ricevere un indirizzo IP in 2 modi:
- **Permanentemente ad un host**
	Configurato **manualmente**, all'interno di un file di sistema
- **Dinanmicamente** al momento del boot di un host
	Tramite **DHCP**(Dynamic Host Configuration Protocol), allocazione di un indirizzo grazie un server speciale

## DHCP
Protocollo detto **plug and play** o **zero conf**.
Questo protocollo provvede all'ottenimento di indirizzi IP in modo **automatico** per ogni host.
Però DHCP dve essere configurabile in modo che:
- Un certo host recva **sempre lo stesso indirizzo**
- Ogni host deve ricevere un indirizzo temporaneo diverso ogni volta

L'ottenimento di un indirizzo avviene tramite:
1) Host invia un messaggio in broadcast detto **DHCP DISCOVER**
2) Il DHCP server risponde con un **DHCP offer**
3) Host accetta l'indirizzo IP con un **DHCP request**
4) DHCP server invia l'indirizzo IP con un **DHCP ack**
![[Pasted image 20260622230152.png|449]]
Il DHCP non dà solo l'indirizzo IP ma anche:
- Indirizzo del router Gateway
- Nome e IP del DNS server locale
- Subent mask

Un' organizzazione può avere un proprio indirizzo IP, che viene **fornito dalla sua ISP**, la quale attinge ad un blocco più grande che gli è già stato assegnato.
![[Pasted image 20260622231255.png]]

## NAT
Dopo la proliferazione di sottoreti di tipo Smal Office Home Office, ogni volta la ISP deve **allocare un blocco di indirizzo IP** che copra tutte le macchine, però per questo tipo di realtà è importante avere reti con un **certo tipo di host**:
- **Nessun accesso** da/a host nell'organizzazione
- **Accesso parziale**, gli host possono raggiungere l'esterno ma non sono raggiungibile dall'esetrno
- **Accesso completo**, gli host sono raggiungibili e possono raggiungere l'eseterno.

Il NATting è una **funzionalità attivabile sul router di bordo**(router gateway) cioè quello che dà all'eseterno(verso Internet).

Il NAT è una funzionalità che si interpona tra un' organizzazione e Internet, il quale ha dei compiti come:
- **Mappare gli indirizzi IP** tra 2 domini
- Garantisce la **trasparenza** tra 2 end system
- **Moltiplica** le possobilità di interconnesione all'interno di un' organizzazione
- **Aumenta la sicurezza** evitando di rendere pubblicamente visibili all’esterno alcuni computer di una organizzazione
Il NAT utilizza **indirizzi privati**, cioè indirizzi utilizzabili soltanto **all'interno di una rete privata**gli indirizzi privati sono:
- 10.0.0.0/8 $\to 2^{24} \to$ quasi 16,8 milinoni di indirizzi
- 172.16.0.0/12 $\to 2^{20} \to$ poco più di 1 milione d'indirizzi
- 192.168.0.0/16 $\to 2^{16} \to$ 65.536 indirizzi
- 127.0.0.0/8 $\to 2^{24} \to$ quasi 16,8 milinoni di indirizzi
### FUNZIONAMENTO
Usa uno **spazio di indirizzi** privati come 10.0.0.0/8, però ogni router per comunicare con l'esterno/internet deve avera un indirizzo pubblico differente da quello della sottorete interna.

Una comunicazione ramite NATting avviene:
1) Host interno 10.0.0.1 spedisce un datagram IP ad un host esterno come 128.119.40.186 porta 80
2) Il NAT cambia l'indirizzo sorgente/mittente con l'indirizzo IP esterno del router generando un nuovo numero di porta
3) Arriva un messaggio con destinazione l'indirizzo IP esterno del router 
4) Il NAT grazie ad una tabella trasforma l'indirizzo esterno con quello corrispondente degli host interni alla rete

Infatti il router **gestisce la corrispondenza tra gli indirizzi** esetrni e quelli interni grazie ad una **tabella di traduzione**, e può essere compilata in:
- **Binding statico**
	La tabella viene configurata manualmente
- **Binding dinamico**
	- La tabella viene **calcolata dinamicamente**
	- Cambia in base al traffico
	- Ciascuna **sessione** ha una riga nella tabella
	- Un numero di porta generato dal NAT **non deve essere già presente nella tabella**.
	- Questo numero di porta è formato da 16 bit
![[Pasted image 20260623192557.png|528]]

Per comunicare con un server posto dietro un router NAT bisogna utilizzare il protcollo **UPnP**(Universal Plug and Play) **Internet Gateway device protocol**, permette a un host su una rete privata di chiedere a un router di aprire una porta specifica **(binding on demand)**, questo viene chiamato anche **port forwarding/mapping**.

Il **port forwarding** è una tecnica del NAT che permette di reindirizzare un pacchetto ad una **coppia di indirizzo e porta** per un host interno alla rete, così da poter comunicare con l'esterno.

![[Pasted image 20260623194052.png]]

Questo viene utilizzato per applicazioni come:
- Web server pubblici posti in una rete privata
- P2P
- Accesso FTP a host su rete privata

Questo permette di avere anche dei vantaggi come:
- Gli host interni non possono raggiungere l'esterno
- Poco costosa e facile da implementare
- Consente massima flessibilità nella gestione interna degli indirizzi senza richiedere alcun permesso al proprio ISP

# IPv6
Soluzione al problema di **esaurimento di indirizzi** di IPv4, perchè ogni nodo internet deve avere un indirizzo IP univoco.
Infatti IPv6 propone indirizzi formati da **128 bit** al posto che 32.

L'**header** è **formato da 40 byte** fissi.
![[Pasted image 20260623213753.png]]

IPv6 **non permette la frammentazione in segmenti**, nel caso un router riceva un pacchetto troppo grande per essere trasmesso, questo verrò scartato inviando un messaggio di errore al mittente.

IPv6 non permette il **broadcast**, ma al suo posto utilizza il **multicast**, considerato più efficiente del broadcast.

Anche se IPv6 è attivo dagli anni '90, non **tutte le macchine lo supportano**, quasi il 50% del traffico internet passa attraverso IPv6, però può variare anche in base alla nazione.
I sistemi IPv6 sono **retrocompatibili** ma i sistemi IPv4 non gesticono datagrammi IPv6.
L'aggiornamento dei sistemi da IPv4 a IPv6, questo comporta costi e tempo per le aziende che si devono aggiornare, e i sistemisti si devono ancora **abituare** a sistemi IPv6, per questo per facilitare la **transizione** si applica il **tunneling**, cioè i datagrammi IPv6 vengono **incapsulati** in datagrammi IPv4.


# ROUTING 
1) **Forwarding**
	Router riceve un pacchetto lo deve trasferire sull'appropriato collegamento in uscita
2) **Routing**
	Il livello d rete deve determinare il percorso dei pacchetti attraverso **algoritmi di istradamento(routing)**

Queste funzioni possono essere divisi in:
- **Pino dei dati**
	Funziona su singolo router e detrmina come un datgram passa da una porta d'ingresso ad una porta di uscita, questo avviene in pochi millisecondi e viene implementata in hardware.
- **Piano di controllo**
	Funzioa sulla totalità della rete e determina come un datagram viene instradato attraverso i diversi router della rete nel percoso tra un host e l'altro, questa operazione può prendere interi secondi, questi percorsi possono essere decisi tramite **algoritmi di routing** che vengono implementati in ogni router, oppure attraverso **Software-Defined Networking** implementati in server remoti.

Per capire su quale porta deve essere mandato un pacchetto si deve guardare la **tabella di inoltro/forwarding**, dove i router estraggono dagli header dei pacchetti deii valori, che in base alla tabella, questi pacchetti vengono mandati sull'interfaccia d'uscita.

L'**algoritmo d'instradamento** **definisce i dati che devono essere inseriti all'interno di una forwarding table.**

Esistono 2 tipi di approcci per configurare una forwarding table:
- **TRADIZIONALE**
	Il router svolge sia funzione di inoltro che di instradamento, questo significa che l'algortimo di routing è implementato in ogni router.
- **SDN**
	Un **controller** sparato dai router interagisce con i **local control agents**.
	Il controller **calcola le tabelle** e le **distribuisce ai router**, in questo caso i router eseguono solo l'inoltro.

Un router è formato da **4 componenti fondamentali**:
- **Porta d'ingresso**
	Formato da 3 livelli:
	- Livello **fisico**: ricezione dei bit
	- Livello di **cllegamento**: protocollo di decapsulamento
	- Livello **rete**: Usa i valore dell'header per **ricercare la porta d'uscita** nella forwarding table, inoltra pacchetti di controllo al **processore di routing** e permette l'**accodamento** quando i datagrammi arrivano più veloci dello switching rate della struttura di commutazione.
- **Struttura di commutazione**
	Connette fisicamente le porte di ingresso con quelle di uscita.
	Detto anche **switching fabric** ha come funzione quello di spostare il pacchetto dalla porta d'entrata a quella d'uscita e si può fare in 3 modi:
	-  **memoria**
		Metodo utilizzato dai router di prima generazione e la commutazione viene affettuata da una **cpu**, che analizza i pacchetti e copia i pachetti in input sulla porta d'uscita giusta.
	- **bus**
		I datagrammi vengono trasferiti da input ad output tramite un **bus condiviso da tutte le porte**, dove ogni porta di uscita a una propria **etichetta di commutazione** e il **pacchetto** viene **ricevuto da ogni porta ma passerà solo su quella con l'etichetta corrispondente**, invece le altre porte lo scarteranno. 
		La velocità di commutazione viene definita dal bus.
	- **crossbar**
		Uso di **rete di interconnessioni più sofisticate**, grazie ad una **matrice di commutazione** formata da $2n$ bus che collegano $n$ porte di input/output, che viene controllata da un **controller** per inoltrare il datagramma sulla porta giusta.
	- la velocità di trasferimento da input ad output si dice **switching rate**.
- **Processore di routing**
	In **router tradizionali**, esegue **algoritmo di instradamento**.
	In **router SDN**, comunica con il controller remoto, **riceve tabelle di inoltro e le installa**. 
- **Porta d'uscita**
	Effettua **buffering**, necessario soprattutto quando i datagrammi arriavano dalla struttura di commutazione ad una freqeunza più alta del **rate di trasmissione di output**.
	Quando ci sono più pacchetti accodati sulla porta d'uscita entra in gico un  **packet scheduler**, il quale decide queli pacchetti spedire prima in base alla loro **priorità**.

![[Pasted image 20260623225716.png]]

Un accodamento può verificarsi sia alle porte d'ingresso sia alle porte d'uscita, e si verificano in base al traffico e in base alla velocità della struttura di commutazione della linea.
Quando queste code superano la capacità di memoria del router, i **pacchetti in arrivo andaranno persi**.

## SCHEDULING
Lo **scheduler di pacchetti** decide la politica d'invio dei pacchetti sul link d'uscita.
- **FIFO** (First In First Out) scheduling: invio nell'ordine d'arrivo
- **Priorità**
	Si manda il pacchetto con priorità più alta, questo significa avere code **per ciascuna priorità**, la priorità può essere decisa da un flag specifico o da dei valore nell'header.
	Le code si riempiranno con una politica FIFO.

- **RR** (Round Robin)
	Ha più classi, ma senza avere delle priorità rigide come nelle code di priorità.
	Infatti **scandisce periodicamente** le diverse code così da inviare un pacchetto per ognuna.
	Il link di output non deve **mai rimanere inutilizzato**, per questo se una coda sarà vuota si passerà **immediatamente a quella dopo**.
- **Weighted fair queing** (WFQ)
	Quello più utilizzato dai router, i pacchetti vengono classificati in base alla loro priorità, e scandisce le classi come in RR ma le classi hanno peso diverso, in base a quel peso la capacità trasmissiva del link verrà data per quella coda.

Per scartare un pacchetto si possono utilizzare diverse politiche come:
- **Tail drop**: scarto il pacchetto in arrivo
- **Priority**: scarto il pacchetto in base alla priorità
- **Random**: scarto un pacchetto random

## INOLTRO
La funzione di inoltro del router deve **selezione la porta di destinazione**, nella maggior parte dei casi viene **scelta in base all'indirizzo di destinazione**, utilizzando una **forwarding table** che lavora su **range di indirizzi**, è possibili coprire una vasta gamma di indirizzi IP anche con poche porte d'uscita.

![[Pasted image 20260625185004.png|530]]

Questa tabella può essere semplificata utilizzando anche solo i prefissi:
![[Pasted image 20260625185050.png]]
In questo caso la porta di output viene decisa in base alla **corrispondenza** del prefisso, nel caso un indirizzo possa corrispondere con più righe, in quel caso la porta viene decisa in base alla **corrispondenza più lunga**.
La ricerca della porta di output viene effattuata a **livello hardware**, questo permette di completarkla in **nanosecondi**.

## ROUTING IP
Il routing **non dipende dal mitenete**, ma solo dall'indirizzo del destinatario, ogni router deve sempre avere un link di uscita sempre disponibile tramite la tabella di forwarding.
Un **routing ottimo** è quando il pacchetto passa attraverso il minor numero di router per arrivare a destinazione.

I router **non sono sparsi a caso per internet** ma sono interconnessi tra loro e **aggregati in regioni** chiamate **Autonomous Systems**(AS).

Non tutti i router sono uguali, possono variare per potenza, configurazione e modalità di azione, ma tutti i router sotto una certa SA usano lo **stesso algoritmo di routing scambiandosi continuamnte informazioni**.
Dall'eseterno le **AS** possono essere viste come un'**entita unica**

L'obiettivo degli algoritmi di roiting è quello di **determinare il percorso ottimale**, che si definsci tramite un **grafo pesato G(N,E)** dove:
- I nodi **N** rappresentano i router o AS
- gli archi rappresentano le connessioni tra i router
- Le etchette **E** rappresentano il costo delle connessioni tra i router
Il cammino ottimale viene definito dal **costo minimo** del percorso.
Il **costo di un collegamento** può riflettere:
- Lunghezza fisica del collegamento
- Velocità del collegamento
- Prezzo del collegamento

![[Pasted image 20260625191723.png]]

I fattori che influenza di èiù gli algoritmi di routing sono:
- **Fattori statici**: topologia della rete
- **Fattori dinamici**: traffico della rete e guasti
- **Politiche di routing**

I principali algoritmi di routing sono:
- **Algoritmi di routing centralizzato**
	- Ogni nodo possiede un'informazione globale sulla rete
	- Input dell'algoritmo: tutti i collegamenti tra i nodi e relativi costi
	- Controller centralizzato o calcolo replicato per ogni nodo della rete
	- **[[LIVELLO RETE#ALGORITMI LINK STATE|ALGORITMI LINK-STATE]]**
- **Algoritmi di routing distribuiti**
	- Nessun nodo ha informazioni sul costo di tutti i link
	- Percorso calcolato in modo ditribuito e iterativo: iniziale conoscena dei collegamenti diretti, e scambio d'informazioni con i nodi adiacenti per calcolare gradualmente il percorso verso la destinazione.

### ALGORITMI LINK STATE
Gli algoritmi **LINK STATE**(LS) sono centralizzati e prevede che i costi dei link della rete siano noti:
- Ogni nodo calcola lo stato dei link ad esso connessi
- Ogni nodo effettua **link state broadcast**, cioè mando informazioni su identità e costi dei link connessi ad esso.
- Tutti i nodi hano visione identica della rete
- Ogni nodo calcola i cammini di costo minimo verso gli altri nodi tramite l'algoritmo di **Djikstra**
Periodicamente i nodi mandano in broadcast dei pacchetti **LSP**(Link State Packet) i quali comunicano:
- **NodeId**
- **Lista dei nodi vicini e relativi costi**
- **Numero di sequenza**, per accorgersi di errori
- **Time to live** così da non utilizzare informazioni datate
Questi pacchetti viaggiano per la rete seguendo un algoritmo di flooding, cioè quando il **nodi I riceve un pacchetto LSP dal nodo J**:
- Se il pacchetto è il più recente mandato dal nodo J, questo viene **salvato nel DB** e una copia viene inoltrata su tutti i link collegati al nodo I
- Altrimenti il pacchetto viene **scartato**
Alla fine degli scambi tutti i **nodi** avranno una **visione identica e completa** della rete.
Una volta effettuato questo l'algoritmo di Djikastra viene calcolato in ogni nodo.

### ALGORTIMI DISTANCE VECTOR
Usati durante il primo perdido di Internet, il **calcolo distribuito del next hop**, cioè ogni nodo riceve informazioni parziali sulla rete dai vicini **direttamenti connessi** ad esso, i quali dopo avere fatto il calcolo ritornano i risultati sulle proprie distanze.

Lo scambio viene effettuato con un **Vettore di distanze** rispetto alle varie destinazioni.

Algoritmo **adattivo** rispetto ai cambi di stato, uno di questi algoritmi è quello di **Bellman-Ford distribuito**.

**Ogni nodo**:
- **aggiorna** il proprio **vettore delle distanze**  in risposta alle variazioni dei costi sui link adiacenti
- invia **aggiornamento agli altri nodi** se il proprio vettore di distanze cambia

Ogni nodo X mantiene:
- C(x,v): costo dei link tra i nodi x e v
- $Dx=[Dx(y):y\space in\space  N]$: vettore delle distanze di x verso tutti i nodi y della rete
- $Dv=[Dv(y):y in N]$: vettori di distanze dei vicini v di x

Di fatto ogni router in questo caso mantiene informazioni solo su:
- Il proprio **vettore delle distanze**
- Le informazioni ricevute dai vicini
- Il **costo dei collegamenti verso i vicini**

## TABELLA DI ROUTING
L'algoritmo di Bellman-Ford viene utilizzato anche per calcolare i valori della **tabella di routing**.

La tabella di routing è diversa da quella d'inoltro, perchè la **tabella di routing serve per calcolare la tabella d'inoltro**.
La tebella di routing di un nodo è formata da:
- Una riga per ogni destinazione nella rete considerata
- Tante colonne quanti sono i nodi adiacenti al nodo x
- I costi di cammino come elementi della tabella

# ROUTING GLOBALE
Tutti i router vengono aggregati in **regioni** anche dette **Autonomous System(AS)**, il quale viene controllata da un'**entità di controllo centrale**.
Ciascun AS ha un **numero identificativo** assegnato da una **authority di registrazione internet**.
Il routing all'interno di un AS, avviene tramite i router che utilizzano un **Interior Gateway Protocol**(IGP) dove i router all'interno di un AS possono possedere un'informazion completa su tutti gli altri router dell'AS, invece per routing per altre AS viene utilizzato un **Exterior Gateway protocol**(EGP).

## POLITICHE DI ROUTING
Sono **regole** per decidere come instradare il traffico.
Ogni AS vuole decidere le proprie politiche e non volerle fare conoscere completamente agli altri AS.

**==TIPI DI AS==**: [[14-LivelloIP-parte4.pdf#page=7|14-LivelloIP-parte4, pagina 7]]

## PROTOCOLLI INTRA-AS
- **Routing Information Protocol**
	- Algoritmo di routing distribuito
	- Primo storico protocollo per routing intra-AS

- **Open Shosrtest Path First**
	- Algortimo di routing centralizzato
	Specifiche del protocollo sono **disponibili pubblicamente**, **il routing si basa su algoritmo link state**, ogni nodo conosce costo e topologia di ogni router nella rete, e ogni router si calcola l'albero dei cammini di costi minimo tramite l'algoritmo di Djikstra.
	Informazioni e aggiornamenti  sullo **stato dei link**, inviati in **broadcast** a tutti i router i quali vengono inviati ogni 30 minuti.
	OSPF non impone politciche sulla scelta dei **pesi dei collegamenti**, i **costi dei collegamenti** sono definiti dall'**amministratore di rete**.
	Alcune di queste scelte possono essere:
	- **Costi di collegamenti tutti a 1**: cammino di costo minimo, instradamento con il minor numero di hop, e il costo dei collegamenti viene dato in modo **inversamente proporzionale** in base alla banda disponibile del link (Es. il collegamento con banda minore sarà il collegamento con il codto maggiore)
	- **Ingegnerizzazione del traffico**: Configurazione dei pesi in base a delle specifiche tecniche da soddisfare
	OSPF offre anche:
	- **Sicurezza**: **autenticazione** dei messaggi OSPF con algoritmi di crittografia, queste permette di prendere parte alla comunicazione solo a **router fidati**
	- **Percorsi multipli con costo uguale**: Possibilità di utilizzare più percorsi senza doverne scegliere uno per instradare tutto il traffico
	- **Struttura gerarchica dgli AS**: possibilità di strutturare grandi AS in modo gerarchico
		- Un AS che utilizza OSPF  puù essere strutturato in **aree** che **utilizzano un algoritmo di OSPF** dove i router comunicano con i router della stessa area
		- Gerarchia interna strutturata **su 2 livelli**: **aree locali** e **area backbone**
		- Algoritmo Link State all'interno di ogni area
	La stuttura gerarchica di un AS è formata da:
	- **Router di confine AS**: Gestiscono l'instradamento tra diverse AS utilizzando algoritmo di routing inter-AS 
	- **Router di confine Area**: Si fa carico dell'intradamento dei pacchetti verso l'esterno di un area
	- **Area Backbone**: Intrada il traffico tra **le are AS**, e contiene tutti i roter di confine di Area
	- **Router di Backbone**: effettuano l'instradamento all'interno dell'area di Backcbone
	- **Instradamento tra aree**: Avviene tramite i roter all'interno dell'area di Backbone, e i pacchetti viaggiano da router di confine attraverso i router di backbone fino ad arrivare fino al router di confine destinazione.
	![[Pasted image 20260629184156.png|568]]

- **Border Gateway Protocol**
	Coordinato tra vari AS, questo è un protocollo **molto complicato** ma **fondamentale per il funzionamento di Internet**, infatti è il protocollo delle **aree dorsali/backbone** di Internet, che viene utilizzato per spostare pacchetti in modo **decentralizzato**.
	uò essere utilizzato anche come protocolo **intra-AS** per AS  molto grandi.
	BGP non funziona come OPSF ma:
	- I pacchetti vengono instradati verso i **prefissi CIDR**  che rappresentano **sottoreti o una collezioni di sottoreti**, una destinazione può essere **138.16.68/22**, e la tabella d'inoltro sarà (x,l) dove **x** è il prefisso di rete, invece **l** è l'interfaccia del router.
	- BGP mette a disposizione di ogni router un modo per:
		- **Ottenere informazioni** sulla raggiungibilità dei prefissi di sottorete da parte dei sistemi confinanti
		- **Determinare percorsi ottimi** verso altre sottoreti 
	BGP offre funzionalità come:
	- **Router gateway**: Router di bordo direttamente connesso a uno o più router in altre AS
	- **Router interni**: Router connessi solo a router interni alla AS
	BGP utilizza **connessioni TCP semi-permanenti** per far comunicare i router confinati (**BGP peers**).
	I 2 BGP peers si scambiano messaggi su una connessione TCP formando così una **BGP session**:
	- **Sessione esterna**(E-BGP): Formata da router che appartengono a deverse AS 
	- **Sessione Interna**(I-BGP): Tra router della stessa AS.
	I messaggi utilizzati tra i peer BGP sono:
	- **OPEN**
		Dopo la fase di three-way handshaking, questo messaggio stabilisce la sessione BGP con il router remoto, contiene anche informazioni di configurazioni della rete come Hold Time in caso non ci siano messaggi UPDATE o KEEPALIVE
	- **UPDATE**
		Comunica nuovi percorsi o cancella di vecchi annunciando i prefissi di rete
	- **KEEPALIVE**
		Tiene vive le connessioni in assenza di UPDATE, funge da ACK per i messaggi di OPEN
	- **NOTIFICATION**
		Riporta errori neimessaggi precedenti, e viene utilizzato anche per chiudere le connessioni.
	Quando viene **annunciato** un prefisso di rete significa che quasi sicuramente ci saranno dei pacchetti che viaggiano su quel percorso, oltre a quando viene annunciato un prefisso, quella comunicazione comprende anche **attributi BGP** come:
	- **AS-PATH**
		Elenco degli hop in cui l'annuncio del prefisso è passato, ogni AS attraversato aggiunge il **proprio AS number** all'attributo e dà una misura del cammino, utilizzata per preferiro un cammino ad un altro
	- **NEXT-HOP**
		Interfaccia specifica del router a cui il messaggio deve arrivare.

## SCELTA DI UN PERCORSO
Un router può venire a conoscenza di **più percorsi**, però deve **selezionarne solo uno**.
Per selezionare solo uno di quei percorsi si utilizza un **algoritmo naive(hot potato routing)**, che utilizza criteri basati su:
- AS-PATH più breve
- Valore di preferenza locale come parte delle policy
- Router di NEXT-HOP più vicino
- Altri criteri
L'algoritmo utilizzato è **molto complesso** e ha come input, tutte le rotte apprese e applica delle **regole di eliminazione** fino ad arrivare a quella migliore:
- **Preferenza locale**: impostato direttamente al router o appreso da un altro router
- In caso di rotte con lo stesso valore, si sceglie quello con **AS-PATH** più breve
- Tra rotte con stessa preferenza e lunghezza di AS-PATH si scegle quello con il **NEXT-HOP più vicino**.

Un'ISP può effettuare **accordi individuali con un'altra ISP**, le ISP stabilscono accordi si peering bilaterali o multilaterali con altre reti, questo permette anche in caso di **congestione** di effettuare **rerouting** o **modulare il traffico temporaneamente** per mantenere l'operatività.

Esiste anche il **public peering** il quale viene realizzate in un **Internet eXchange Point**, dove decine o centinaia di reti si connettono attraverso uno switch in comune, un'IXP è un'infrastruttura fisica che consente a diversi operatori Internet di scambiarsi direttamente il traffico tra loro.
# Internet Controm Message Protocol(ICMP)
ICMP è un protocollo di controllo, questo non porta dati utente e **non offre servizi**, e la sua posizione nello stack è **indipendente** da come vengono formate le PDU.

Il suo scopo è quello di **notificare** possibili errori o anomalie, e non porta dati, ICMP è **funzionale ad IP**, infatti i pacchetti ICMP viaggiano **all'interno dei pacchetti IP**.

I messaggi ICMP sono spesso rivolta al **layer IP dell'host destinazione, non all'utente**.
ICMP interviene nel momento in cui si presenta un'**anomalia nel processo d'instradamento** o in presenza di **una condizione di errore**, la quale deve essere notificata al mittenete del pacchetto, essendo che anche i pacchetti ICMP devono essere instradati può presentarsi un errore, ma questo succede **molto rararmente**.

## 3 REGOLE:
- **REGOLA 1**
	Nessnun messaggio ICMP viene generato da un errore di un messaggio ICMP
- **REGOLA 2**
	Se il pacchetto viene frammentato, solo il primo frammento può generare messaggi ICMP
- **REGOLA 3**
	I broadcast e multicast non generano messaggi ICMP

## TIPI DI MESSAGGI:
- Echo Request 
	Richiesta di echo, esiste un altro messaggio con la stessa funziona ma mostra anche i**nformazioni aggiuntive su orario d'invo**, ma anche **misura di velocità del collegamento e sincronizzazione dell'ora di sistema**, questo messaggio viene detto **TIMESTAMP**
- Echo Response 
	Risposta a Echo request
- **Destination Unreachable**
	- Un gateway vede la destinazione a distanza infinita (**net Unreachable**)
	- Host non risponde ad una chiamata ARP (**host Unreachable**)
	- Host non conosce il protocollo del pacchetto (**protocl Unreachable**)
	- Il pacchetto non può essere frammentato
- **Time Exceeded**
	Il pacchetto ha raggiunto TTL=0(TimeToLive)
- **Parameter Problem**
	Il gateway non riesce ad interpretare il pacchetto ricevuto per un valore sbagliato
- Molti altri messaggi sono disponibili 





