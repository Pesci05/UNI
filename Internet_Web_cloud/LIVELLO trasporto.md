Offre **comunicazione logica** end-to-end tra i processi in esecuzione su host diversi
Il **mittente**, spezza i messaggi **in segmenti** e li passa a livello rete.
Il **ricevente**, **riassembla i segmenti** ricevuti e li passa al livello applicazione.

- Livello **trasporto**: comunicazione logica tra processi
- Livello **rete**: comunicazione logica tra host

I protocolli che vengono utilizzati in questo livello sono:
 - **UDP**(servizzi minimi)
	 Che permette il **multiplexing**, e effettua il **controllo d'integrità**
 - **TCP**(aggiunge servizi)
	 Aggiunge la **garanzia sulla consegna**, controllo del flusso e controllo di congestione.
	Non offre servizi su **ritardo, banda disponibile e throughput**.

# Multiplexing/Demultiplexing
Tipicamente in un unico host, sono presenti più **processi** in esecuzione.
Per capiere a quale processo appartiene un messaggio, oltre alla suddivisoione con le **porte**, si utilizzano le **socket**, che nel caso del mittente, grazie alle intestazioni del livello di trasporto, crea i **segmenti e li passa al livello rete**, invece il ricevente utilizza quelle intestazioni proprio per **smistare** i segmenti alla socket corretta.

## PORTE
La porta è un numero da **16 bit**, che possono essere suddivise in:
- **WELL KNOWN**: Queste porte possono assumere un valore tra **0 e 1023**, e queste sono assegnate specifici protocolli, come la 80 è riservata al protocollo HTTP.
- **USER**: Queste variano da **1024 a 49151**, utilizzabili dai protocolli di trasporto per identificare servizi di livello applicativo
- **DYNAMIC**: Queste variano da **49152 a 65535**, vengono assegnate dinamicamente, dal sistema operativo.

## SOCKET
Il comportamento delle socket variano in base a quela protocollo utilizziamo.

Nel caso di una connessione tramite TCP, 2 host possono **instaurare più connessioni**, e queste vengono identificate **dalla coppia di socket** sui 2 host.
Questo comporta che il segmento, viene identificato non solo dall'indirizzo IP e porta del mittente, ma **anche da quelle del destinatario**. 
In un server possono risiedere più socket per processo, questo permette di avere una socket differente aperta per **ogni connessione**, questa vale anche per connessioni HTTP non persistenti.

Nel caso di UDP, invece il segmento viene identificato solo dall'**indirizzo IP mittente e destinatario ma anche la porta del destinatario.**
# UDP
Questo protocollo è molto leggero, però offre **un controllo sull'errore**, però non dà sicurezza sulla consegna del messaggio,e **non instaura nessuna connesione** a differenza di TCP.

Un segmento UDP è formato da:
![[Pasted image 20260702171154.png|512]]
![[Pasted image 20260407171021.png]]

Questo protocollo si utilizza perchè non ha bisogno di instaurare nessuna connessione, **è semplice**, è **più leggero** essendo che lo spazio utilizzato dagli header è minore, e non effettua **controllo di congestione**, perchè le applicazioni basate su questo protocollo richiedono velocità di trasmissioni minime, però offre comunque un controllo per individuare **errori di trasmissione** come il **checksum**.
# TCP/IP
TCP si basa sui principi di **trasferimento affidabile** , infatti gestisce un trasferimento di dati ordinati in **stream dati**, per questo esistono meccanismi che soddisfano questi principi.
## VERSIONI
### V 1.0
Il protocollo funziona in modo completamente ideale, sicurezza sulla ricezione del messaggio e nessun tipo di errore su i bit.

### V 2.X
Trasferimento che implementa funzioni di correzzioni di bit in caso di errori.
- **2.0**
	Il canale trasmissivo può causare la corruzione di 1 o più bit, questo può essere evitato grazie ad un controllo di **checksum**, che consente anche di recuperare e correggere l'errore.
	Utilizzo di una notifica **ACK**(Acknowledgement) che consente al destinatario di comunicare la ricezione del pacchetto, che può essere **positivo**(ACK) se ricevuto senza errori, **negativo(NAK)** se ricevuto con un errore, in questo caso il mittente ritrasmette il pacchetto.
	**PROBLEMA** $\to$ il canale può corrompere gli ACK, questo può comportare alla trasmissione dello stesso pacchetto.
	Si può introdurre il checksum anche sul messaggio di conferma, e se risulta alterato si rispedisce il messaggio, però questo causa **duplicazione** dei messaggi inviati.
 - **2.1**
	 Per risolvere il problema del 2.0, si può introdurre un **numero di sequenza**.
	 Il mittente deve aggiungere al pacchetto un numero di sequenza ad ogni pacchetto.
	 Così se il destinatario riceve più pacchetti cono lo stesso numero può scartarli.
- **2.2**
	Si può migliorare mandando solo ACK escludendo così NAK, l'ACK deve riportare il **numero di sequenza** del **pacchetto appartenente**.
	Il destinatario per comunicare che il pacchetto ricevuto è alterato, manda un ACK con il **numero di sequenza** del **pacchetto precedente**.

### V 3.0
Il canale può subire anche una perdita di pacchetti, per questo si può introdurre un **timer**. Il mittente deve tenerne conto nel momento che **non riceve un ACK entro la fine del timer**, in questo caso si ritrasmette il pacchetto.
Questa versione però risulta **inefficiente**, essendo che per mandare il prossimo pacchetto deve sempre aspettare l'ACK di quello prima, per questo si introducono le **PIPELINE**

## PIPELINE
Per rendere questo protocollo più efficiente, si può utilizzare un menccanismo di **PIPELINE**, che peremtte di inviare più pacchetti prima di ricevere **un ACK**.

Per implemetare questo meccanismo serve:
- **BUFFER MITTENTE**: Per mantenere i pacchetti che a cui non sono ancora arrivati ACK
- **BUFFER DESTINATARIO**: Per mantenere le sequenza di pacchetti dove non tutti i pacchetti sono arrivati o sono arrivati correttamente(fuori ordine)
- **FINESTRA DI SCORRIMENTO**: Numero massimo di pacchetti da mandare senza aver ricevuta ACK, dove **N** è la lunghezza della finestra, invece **base**(indice del pacchetto più vecchio che deve ancora ricevere ACK), e **nextseqnum** numero del pacchetto che deve essere ancora inviato.
Per implementare la finsetra servono dgli algoritmi che la gestiscono, come:
- **GO-BACK-N**
	Mittente può trasmettere N pacchetti senza riceve ACK, l'ACK in questo caso sarà **cumulativo** cioè questo conferma la ricezione di tutti i precedenti pacchetti, comprendendo l'ultimo ricevuto in ordine, il destinatario **scarta** i pacchetti **non in ordine**, il mittente se non riceve ACK ritrasmette tutti i pacchetti da quello per cui non ha ricevuto l'ACK
- **SELECTIVE REAPEAT**
	Il mittente può trasmettere **al massimo N pacchetti in pipeline** senza attendere ACK, il destinatario in questo casa manda **ACK singoli per ogni pacchetto ricevuto**, nel mentre il mittente **mantiene un timer** per ogni pacchetto senza ACK, quindi ritrasmette soltanto quelli per cui **non ha ricevuto ACK** entro il time-out.

# TCP
Protocollo che fornisce un livello di trasporto **affidabile e orientato alla connessione**, rispetto ad **UDP** offre servizi come:
- **Connessioni**: Comprende della fasi apposite per l'instaurazione delle connessioni
- **Connessioni di tipo full-duplex**: Consente lo scambio di dati contemporaneo in entrambe le direzioni
- **Orientato al flusso di dati**: Significa che la connessione viene trattata come un flusso di byte continuo dal mittente al destinatario
- **Trasferimento con buffer**: i dati da spedire sono memorizzati in un buffer di invio e da lì prelevati a blocchi e spediti.

Il TCP non può garantire, comunicazioni in tempo reale, disponibilità di banda e il multicast.

Però il TCP ha bisogno di:
- Meccanismo per **iniziare e conludere** una connessione in modo esplicito
- Meccanismo di **timeout adattivo**
- Possibilità di gestire i **pacchetti in ritardo**

Il fatto che sia orientato alle connessioni significa **prima** di trasferire dati si **instaura** una connessione tra i 2 host, che viene chiusa alla fine della comunicazione.
La connessione viene trattata come un **Byte stream**, cioè un flusso di byte continuo tra mitennte e destinatario.

TCP può effettuare **trasferimenti contemporanei in entrambe le direzioni(FULL DUPLEX)** della connessione, nell’ambito della stessa sessione.
Consente di sovrappore (**piggybacking**), comunicazioni di dati/controllo con l'invio di informazioni di controllo(**ACK**).

Il segmento del TCP viene formato da.
![[Pasted image 20260407224422.png]]

Per instaurare una connessione nel modello client/server:
- **Client** inizia la connessione, inviando un segmento TCP detto **SYN**
- **Server** per accettare la richiesta di connessione deve essere già attivo e in attesa di un possibile contatto da parte del client, che risponderà  a sua volta con un segmento **SYN**(SYN ACK)
- **Inizializzazione** delle variabili TCP
- **Definizione** del **Maximum Segment Size** cioè la massima dimensione del segmento

L'instaurazione di una connessione viene detta **THREE WAY HANSHAKING**:
![[Pasted image 20260407225410.png]]

## CONTROLLO DI FLUSSO
Il protocollo TCP offre un **controllo di flusso**, cioè il mittente **non deve inviare** più dati si qualli che il ricevitore può memorizzare nel buffer.
Il destinatario ad ogni ricezione **informa il mittente** specificando lo spazio libero nel buffer o **Receive Window**.
La grandezza della receive window può essere dedotta dall'ACK, specificando quanti byte ha ricevuto e quanti ne sono liberi, in base a questo il mittente regola la sua sliding window, se il destinatario comunica che ha 0 byte liberi, il mittente sospende la trasmissione.

## CONTROLLO DI CONGESTIONE
La **congestione** è un fenomeno che accade nel momento in cui un numero elevato di sorgenti inviano contemporaneamente troppi dati generando un traffico che la rete (Internet) non è in grado di gestire.
Questo può causare:
- **PERDITÀ DI PACCHETTI**
- **RITARDI**

Il controllo di congestione puù essere effettuato in 2 modi:
- **end-to-end**
	Viene regolato dal mittente, la velocità d'invio varia in base **congestione percepita sulla rete**, questa può essere dedotta dalla **perdità di pacchetti**, **occorrenza di timeout** o dalla **ricezione di 3 ACK duplicati**.
	La ritrasmissione di pacchetti oltre ad essere causa di congestione ne è anche sintomo
	La prestazione in questo caso viene calcolata $Throughput=\frac{w*MSS}{RTT}$
	Dove **w** è il numero di segmenti della finestra d'invio e viene **definito dalla congestion window** (**cwnd**), **MSS** dimensione massima del segmento e **RTT** round trip time

- **Assistito dalla rete**
	 Router forniscono dei **feedback** che esplicitano lo stato della rete.

Il controllo di congestione avviene attarvereso 3 fasi:
- **Slow start**
	All'inizio la **cwnd** viene **inizializzata ad 1 MSS**, ogni volta che il mittente riceverà un ACK non duplicato la cwnd aumenterà di 1 MSS, così da raddoppiare il numero di sementi e la velocità ad ogni RTT, fino a quando non ci sarà una **perdita di segmento**, il quale farà ripartire dall'inizio l'operazione, il **treshold ssthresh** sarà a cwnd/2 che è il valore di quando è avvenuta la prima congestione.
	Una volta che è ripartita e ci sarà di nuovo l'incremento esponenziale, ma nel momento che la cwnd arriverà al valore del treshold, la connessione passerà dalla fase di **slow start** alla fase di **Congestion avoidance**.
- **Congeston Avoidance**
	La cwnd aumenterà di 1 MSS ad ogni RTT, così da avere un **incremento lineare**, fino a quando non si rileverà di nuovo una congestione, se si verifica un timeout strehold = cwdn/2 e cwnd=1MSS.
	**Invece nel caso di 3 ACK duplicati** entra in **fast recovery**.
- **Fast Recovery**
	La finestra cwnd sarà 
$$
	cwnd = \frac{cwnd}{2}+3MSS
$$
Cioè dimezza la finestra però aggiungendo anche 1 MSS per ogni ACK duplicato ricevuto, ssthreshold sarà uguale a cwnd/2 e continuerà in Congestion Avoidance.

Esistono 2 tipi di politriche di controllo di congestione, le quali sono:
- **TCP RENO**
	Utilizza un approccio di tipo **AIMD** (**Additive Increase Multiplicative Decrease**), cioè **aumenta la window size** per **ACK arrivati entro il timeout** e diminuisce la window di un fattore moltiplicativo in caso di perdita rilavata con ACK duplicati.
	Versione di TCP più utilizzata.
- **TCP TAHOE**
	Non utilizza il meccanismo di **fast recovery**

### TCP FAIRNESS
La TCP fairness consiste nel **distribuire equamente le risore** di uno stesso link **tra le connessioni TCP che attraversano quel link.**

Lo scopo del controllo di congestione è quello di regolare il **tasso trasmissivo** delle connessioni TCP, per questo cere applicazioni come **videochiamate** o **telefonia via IP** non possono essere supportate da TCP ma da **UDP**, poichè si preferisce la perdita di qualche pacchetto che la variazione del tasso trasmissivo.
Di fatto dal puntodi vista di TCP, **UDP non è fair** poichè TCP abbassa il proprio tasso trasmissivo, invece UDP non lo fa, così da **soffocare il traffico su internet**.


