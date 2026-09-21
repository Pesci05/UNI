# LEZIONE 1
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


