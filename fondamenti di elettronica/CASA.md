# Convenzioni
## Potenza 
La potenza è una grandezza fisica definta dal prodotto di tensione e corrente:
$P = VI$ e si misura in Watt.
La potenza viene utilizzata anche per distinguere dispositivi:
- **Dissipativi:** componente che per funzionare utilizza potenza, cioè utilizza l'energia elettrica per trasformala in altre energie.
- **Erogative:** componente che tramite altre forme di energie, le trasforma in energia elettrica.
# LEGGI DI Kirchoff
Un circuito è comosto da nodi e rami:
- **nodo:** giunzioni di 2 o più rami, i un node è prensente un solo valore di tensione
- **ramo:** percorso che collega 2 nodi, presenta un valore unico di tensione
## Leggi di Kirchoff
### 1° LEGGE
Un circuito può essere visto come un insieme di **rami** e **nodi**.
- **RAMO**
	Percorso che collega 2 nodi, con un valore unico di corrente.
- **NODO**
	Gunzione che collega 2 o più elementi, con un valore unico di tensione.

La prima legge di Kirchoff, detta anche, Kirchoff alle correnti, e afferma che , la somma di tette le correnti in un nodo è pari a 0. $\sum{_{node} ^n} I = 0$   
### 2° LEGGE 
La seconda legge di Kirchoff affrma che la somma delle tensioni in un qualsiasi anello chiuso sia pari a 0.
$\sum^n_{loop} = 0$ 
# COMPONENTI BASE
#Componenti_base 
## RESISTORI
Dispositivo a 2 terminali che stabilisce **una relazione lineare** tra la **corrente che lo attraversa** e la **tensione ai 2 terminali**, nominata anche come **legge dI OHM**:
$V = RI$ 
dove:
- **V** è la tensione ai capi del resistore, viene misurata in Volt (V)
- **I** è la corrente che attraversa il compenente, viene misurata in Ampere(A)
- **R** è la resistenza del componente, ed è anche la sua caratteristica principale, la quale viene misurata in Ohm($\Omega$)  
![[Pasted image 20251124122228.png]]

Il simbolo elettrico è:
![[Pasted image 20251124181522.png]]
### Collegamenti
 I resistori possono essere collegati in 2 modi, in **serie** o in **parallelo**.
 - **Serie (partitore di tensione)**:  nelle 2 resistenze passa la stessa corrente, viene chiamato anche partitore di tensione, poichè la tensione ai capi delle due resistenza è differente.
$$
\begin{aligned}
R_{eq}= R_{1}+R_{2} \\
V = R_{eq}*I
\end{aligned}
$$
 - **Parallelo (partitore di corrente)**: presenta la stessa tensione ai capi delle 2 resistenze, ma differente corrente attraverso i resistori, anche chiamato partitore di corrente.
$$
 R_{eq} = \frac{1}{\frac{1}{R_{1}}+\frac{1}{R_{2}}}=\frac{R_{1}*R_{2}}{R_{1}+R_{2}}
$$
**Esempio di collegamneti:**
![[Pasted image 20251220002240.png]]
## Condensatori
E un componente che immagazzina carica elettrica come un contenitore, e stabilisce una relazione tra tensione ai capi dei terminali e la carica immagazzinata.
![[Pasted image 20251220002533.png]]
La capacità del condensatore viene misurata in **Fahrad**.
$I = C * \frac{dv}{dt}$
Questo è il simbolo elettrico:
![[Pasted image 20251220004408.png]]

La carica di un condensatore varia soltanto nel monento in cui la tensione ai suoi capi varia nel tempo.
[[ESEMPI CIRCUITI#ES. carica scarica di un condensatore|ES. CONDENSATORE]]
## Induttori
L'induttore è un componente che può immagazzinare energia magnetica.
Questo componente stabilisce una relazione lineare tra la tensione ai 2 terminali e la variazione della corrente nel tempo.

**L** è l' **induttanza** e viene misurata in **Henry [H]** 
$V = L* \frac{dI}{dt}$
Il simbolo elettrico del componente è 
![[Pasted image 20251221225027.png]]

# Sovrapposizione degli effetti
Quando in un circuiti sono presenti **più generatori,** che siano di tensione o corrente, per risolvere il circuito si divide il circuito spegnendo i generatori, cioè dare 0V ad un generatori di tensione creando un cortocircuito, ivece per un generatore di corrente impostare a 0A creando un circuito aperto.
Questo permette di studiare il **circuito più complicato**, dividendolo in più **sottcircuiti semplici**, quando si riuniscono i 2 sottocircuiti bisogna stare attenti alla **polarità** delle correnti e delle tensioni, poiché questo potrebbe portare ad un errore di segno così non avendo i valori corretti.

# Circuiti Equivalenti
Un **circuito equivalente** si basa sul fatto, che anche se non si sa come sia fatto, in base all'**uscita su 2 terminali**, si possa comunque progettare un circuito che **lavori allo stesso modo**.
## Teorema di Thevenin
Il teorema di Thevenin afferma che un generico circuito lineare non dinamico osservato da due nodi può essere rappresentato **da una sorgente di tensione** (Vth) **in serie con un resistore** (Rth). Specifica inoltre come calcolare la tensione della sorgente di tensione e la resistenza del resistore.

## Teorema di Norton
Il teorema di Norton afferma che un generico circuito lineare non dinamico black box osservato da due nodi può essere rappresentato **da una sorgente di corrente**(Ino) **in parallelo con un resistore** (Rno). Specifica inoltre come calcolare la corrente della sorgente di corrente e la resistenza del resistore.

![[Pasted image 20251223183531.png]]


# [[CASA#Switch|Switch]]

# [[CASA#Transistor|Transistor]]

### [[CASA#BJT|BJT]] 

### [[CASA#MOSFET|MOSFET]]

# MATEMATICA DEI SEGNALI
ESistono 2 tipi di segnali:
- **DC**(Direct Current): che indica corrente e tensione **costante** in tutto il circuito
- **AC**:(Alternate Current): è un segnale che **varia** nel tempo, anche invertendo il proprio segno in modo periodico, così variando anche **corrente** e **tensione**, con forma sinusoidale.
![[Pasted image 20260119183941.png]]
Però si può **modulare** il segnale nel modo in cui lo si vuole, creando così segnali di tipo **pulsante** o anche segnali di forma del tutto **variabile**.
Grazie all'analisi di Fourier si può **scomporre** qualunque tipo di segnale in **N** segnali **AC**, cioè in onde sinusoidali.
![[Pasted image 20260119223546.png]]

## Impedenza

Nel momento in cui viene applicata una tensione AC ad un resistore, la corrente che lo attraverserà sara sempre AC con fase e frequenza **uguali**, ma con **ampiezza** inversamente proporzianale alle resistenza del resistore.
![[Pasted image 20260120175933.png|361]]

Invece se si prendono in considerazioni componenti come, **condenastori**  o **induttori**, mantengono sempre la stessa frequenza, ma variano di fase.
![[Pasted image 20260120214010.png]]
Infatti come si può vedere la corrente abbia **foma diversa** da quella della **tensione** (sfasata rispettivamente di 90°), l'ampiezza di I **non dipende** solo dalla **capicità** del condensatore e dall'**ampiezza** di V ma anche dalla **frequenza della tensione**.

Per i resistori:
$$
\frac{V(t)}{I(t)} = R
$$

Per condensatori e induttori:
$$
\frac{V(t)}{I(t)}=\frac{V}{\omega CV} \frac{\sin(\omega t+ \theta)}{\sin\left( \omega t+\theta+\frac{\pi}{2} \right)}= \frac{1}{\omega C} \frac{\sin(\omega t + \theta)}{\sin\left( \omega t + \theta+ \frac{\pi}{2} \right)}
$$

Nel caso dei resistori il valore della resistenza è un numero reale, invece nel caso di induttori e condensatori, il valore sarebbe in funzione del tempo, quindi non sarebbe possibile avere un numero che indichi la relazione tra tensione, e corrente.
Per questo si **introducono i numeri complessi** introducendo i **fasori**, cioè vettori rotanti che forniscono una relazione universale che permette di tarttare sia componenti resistivi che quelli reattivi.
![[Pasted image 20260120223658.png]]
![[Pasted image 20260126225844.png]]

Per calcolare l'impedenza di un condensatore:
[[01 - Nuts and Bolts of Electronics.pdf#page=27|01 - Nuts and Bolts of Electronics, pagina 27]]
[[01 - Nuts and Bolts of Electronics.pdf#page=28|01 - Nuts and Bolts of Electronics, pagina 28]]

$$
\begin{align}
Z_{c}= -j\frac{1}{\omega C} \to condensatore\\ \\
Z_{L} = j\omega L \to induttore \\ \\
\omega \to pulsazione \to 2\pi f \\
f\to frequenza
\end{align}
$$

Riassunto:
- Per i **resistori**, tensione e corrente, oltre che avere la stessa frequenza, non presentano **sfasamento**, per questo il rapporto tra tensione e corrente non dipende dalla frequenza.
- Per i **condensatori**, tensione corrente sono isofrequenziali, ma la **corrente** anticipa di 90° la tensione( in **quadatura**), il rapporto ta tnsione e corrente dipende anche dalla frequenza.
- Per gli **induttori**, tensione e corrente, scllan alla stassa fequenza, ma la **tensone antcipa la cornte** di 90°(in **quadratura**),  il rapporto ta tnsione e corrente dipende anche dalla frequenza.
Qeusto comporta che l'**impedenza** di un resistore è composto solo da un numero reale, invece quando si parla di induttori e condensatori la loro impedenza viene rappresentata da un **numero immaginario** o **complesso**(una parte reale e una parte immaginaria).
![[Pasted image 20260127163232.png]]
Quindi le relazioni tra tensione e corrente trovate per induttori, condensatori e resistenze, **permettono di utilizzarle con le leggi OHM**,usando l'impedenza al posto delle resistenze, coì facilitando il calcolo dell'impedenza utilizzando le stesse regole che si utilizzano per i resistori.  

## Diodo
È un dispositivo elettronico a 2 terminali, **non lineare** e **non simmetrico** che idealmente in una direzione la **resistenza è pari a 0**, invece nella direzione contraria la resistenza **tende ad infinito**.
Simbolo elettrico:
![[Pasted image 20260127212231.png]]

Il diodo è caratterizzato da una relazione **esponenziale** tra corrente e tensionione, per questo il diodo quando presenta una tensione positiva si comporterà come un **cortocircuito**, invece con tensioni negative **si comporterà come circuito aperto**.
![[Pasted image 20260127213150.png]]

![[Pasted image 20260127214452.png]]
Come si può capire da questo schema, si può vedere come che nell'area  **> 0,7V**($V_d$), permette alla **corrente di passare in modo esponenziale**, mentre se il diodo viene alimentato con una tensione $\lt V_d$ la corrente **viene bloccata**, e se la tensione è $\lt V_b$(tensione di breakdown) il diodo si danneggia in modo irreparabile.

Oltre ai diodi normali esistono:
- **ZENER**: diodo progettato per lavorare nella regione di breakdown.
- **LED**: Se polarizzato direttamente(tensione positiva) emette luce a una **frequenza specifica**, e lunminosità controllata dall'intensità della corrente.
- **FOTODIODO**: Risponde con una corrente una volta illuminato.

# Componenti
[[CASA#COMPONENTI BASE|Componenti base]] 
## Switch
Componente da 2 terminali che si può comporatre come **cortocircuito** o come **circuito aperto**
![[Pasted image 20260127224421.png]]

# Transistor
È un'interruttore a 3 terminali,2 che sono collegati al circuito e un **terminale di controllo**.
Di questo tipo di interruttori esistono più tipi:
- **BJT e MOSFET**: 
- IGBT
- SCR
[[01 - Nuts and Bolts of Electronics.pdf#page=34|01 - Nuts and Bolts of Electronics, pagina 34]]

## BJT
Dispositivo elettronico a tre terminali i quali vengono chiamati:
- **Base**: terminale di cotrollo
- **Collettore**: input
- **Emettitore**: output
Un transistor può comportasi o come un interruttore o come un amplificatore.
![[Screenshot From 2025-10-03 12-24-22.png]]

Il transitor in entrata si comporta come un **diodo** che dipende dalla tensione $V_{be}$, invece in uscita una volta che si supera la **tensione di saturazione** la corrente $I_{c}$ **aumenta fino ad arrivare a** $\beta*I_b$ il quale dipende dal tipo di transistor.

Il BJT lavora in tre regioni:
- **cut-off**: quando bjt polarizzato con tensione $V_{be}$ **tanto piccole**, quasto comporta ad una corrente $I_b$ altrettanto bassa così da causare una corrente $I_c$ circa 0.

- **saturazione**: quando la tensione $V_{be}$ è **abbastanza alta** e la tensione $V_{ce}$ è **inferiore alla tensione di saturazione**, quasto porta ad un comportamento simile a quello di un **cortocircuito**.

- **attiva**: quando la tensione $V_{be}$ è abbastanza alta e la tensione $V_{ce}$ maggiore alla tensione di saturazione, il dispositivo si comporterà come amplificatore.

![[Pasted image 20260128181635.png]]

### BJT come uno SWITCH
Il transistor BJT può essere utilizzato come interruttore o dispositivo digitale, questo permette di controllare la potenza di un carico resistivo R.
![[Pasted image 20260128182407.png]]
In questo caso il transistor viene pilotato da un'onda quadra, e collegato al collettore da una tensione $V_{cc}$ e all'emettitore a massa:
- $V_b$ bassa: il transitor si trova in regione di **cut-off** e questo non permette a nessuna corrente di fluire dal carico, così senza presentare nessuna caduta di tensione.
- $V_b$ alta: il transito si trova nella regione di **saturazione** che però deve avere anche la tensione $V_{ce}$ inferiore alla tensione di saturazione, quindi la corrente del carico sarà data da
![[Pasted image 20260129155834.png]]
	Invece la tensione del carico sarà data da:
	![[Pasted image 20260129214840.png]]
	e la tensione $V_{ce} = 0$
	La potenza sul carico viene calcolata grazie a:
	![[Pasted image 20260129215310.png]]
	La potenza sul BJT sarà:
	![[Pasted image 20260129215519.png]]

Questo varrà soltanto nei casi ideali, però nei circuiti reali è impossibile poichè $V_{ce}$  non è 0 (anche se ci è vicina), questo comporta ad una dissipazione di potenza sul BJT e potenza sul carico, minore di quella ideale.

## MOSFET
Il transistor a effetto di campo (MOSFET) è un dispositivo a **4 termiinali**, ed è anche il transistor più comune, si comporto in modo molto simile al BJT, e i 4 terminali sono:
- **GATE**: simile alla base del BJT
- **DRAIN**: simile al collettore del BJT
- **SOURCE**: simile all'emettirore del BJT
- **BODY**o **BULK**: ultreiore controllo per controllare l'output del transistor, ma nel nonstro caso sarà collegato ad S.
Il simbolo elettrico è:
![[Pasted image 20260129221953.png]]
Il modo in cui lavora questo dispositivo non dipende da una corrente come NEL BJT, ==ma dipende dalla tensione tra Source e Gate== $V_{GS}$, mantenendo a 0 la corrente poichè GATE è isolato.
Anche in questo caso si può dividere il modo in cui lavoro in 3 regioni:
- **cut-off**:nel caso di un tensionse $V_{GS}$ applicata con un valore minore alla tensione di soglia $V_{TH}$, in questo caso la **corrente di drain sarà 0,** in questa regione il MOSFET  si comporta come un ==interruttore  aperto==.
- **triode**:nel caso $V_{GS}$ superi la tensione $V_{TH}$ e $V_{DS}$ è inferiore a $V_{GS} - V_{TH}$(chiamata anche tensione di overdrive $V_{OD}$), in questa regione la corrente $I_D$ aumenta all'aumentare della tensione $V_{DS}$, in questa regione il MOSFET può essere utilizzato come ==interruttore chiuso==.
- **saturation**:nel caso $V_{GS}$ superi la tensione $V_{TH}$ e se $V_{DS} \ge V_{OD}$, in qeusta regione la corrente $I_D$dipende direttamente dalla tensione $V_{GS}$ 
![[Pasted image 20260130000347.png]]
## DISSIPATORI DI CALORE
Parte dell'**energia** verrà in qualunque caso dissipata, la quale si **trasformarà in calore**.
Questo fenomeno se non tenuto sotto controllo potrbbe **mettere a rischio l'integrità** oltre che del componente, anche del circuito e del sistema elettronico, quindi bisogna sempre ==tenere sottocontrollo questo fenomeno==.
Per questo esistono i dissipatori di calore che sono pezzi di metallo il quale servono per **scambiare calore con l'ambiente circostante,** e vengono disegnati in modo tale che l'area da massimizzare lo scambio di calore.

## SAFE OPERATING AREA
È un'insieme di punti di polarizzazioni di transistor, la quale non comporta rischi o minacce per l'affidabilità.

Per quanto riguarda ai transitor di tipo BJT, un malfunzionamento può essere causato da un passaggio di una ==corrente superiore== a quella che il transistor può sopportare, e può succedere anche nel caso di una ==tensione superiore== a quella massima.
In tutti e due i casi questo comporterà ad un **danno irreversibile**, e il dispositivo diverrà inutilizzabile.

Esempio di un SOA per un BJT:
![[Pasted image 20260130001914.png]]

Anche se i 2 transitor hanno valori massimi nominali simili, l'area di SOA non sarà uguale, infatti quella del MOSFET sarà più estesa, poiche **reagiscono** **diversamente** all'aumento di calore.
Il **BJT** essendo che corrente e potenza sono direttamente proporzianali, questo causato da un'**aumento di potenza che causa anche l'aumento di corrente**, poiché la potenza dissipata si trasforma in calore, iniziando un ciclo continuo portando così il dispositivo ad una **distruzione termica.**

Al contrario il MOSFET all'**aumentare** della **temperatura**, porta ad una **diminuzione** di **corrente** di drain così riducendo la dissipazione di potenza.

# AMPLIFICATORE OPERAZIONALE
Dispositivo elettronico a **5 terminali**, molto utilizzato che può essere usato come:
- **filtro**
- **amplificatore**
- **conversione A/D D/A**
È un dispositivo che **compara**(misura la differenza) 2 segnali, e produce una tensione proporzianale alla differenza dei 2 segnali.
I 5 terminali sono:
- **2 pin di ingresso**
- **1 pin di uscita**
- **2 pin di alimentazione**
![[Pasted image 20260130003747.png]]
Per assicurarsi un corretto comportamento i segnali di input uno nel terminale **non invertente(+)** e l'altro **invertente (-)**, il segnale a + deve avere una **tensione maggiore** a al segnale in input al terminale - .

L'uscita di un op-amp fornisce una tensione di uscita proporzianale alla differenza dei due segnali d'ingresso, la quale viene moltiplicata per un fattore di proporzianilità costante, chiamato anche **GAIN(guadagno)** indicato con la lettera A.
![[Pasted image 20260130152153.png]]
Il guadagno è di un op-amp è adimensionale e la sua ampiezza viene misurata in dB, questo significa che se $A \lt 0$ avviene **un'attenuazione**, invece se $A \gt 0$ avviene un'**amplificazione**.

Per funzionare come amplificatore la tensione $V_i$ deve essere piccolissima, questo lo rende inutilizzabile come amplificatore.

Per questo l'op-amp viene soprattutto utilizzato come **comparatore**, dove in base a quale dei 2 segnali sia maggiore può dare come risultato $+V_s$ o $-V_s$.
Un op-amp ideale deve avere:
- Tra i 2 terminali di ingresso non deve scorrere **corrente**, deve essere visto come un **circuito** **aperto**
- **guadagno infinito**
- Il guadagno deve **essere costante** per tutte le frequenze
- L'uscita può erogare una quantità arbitrariamente elevata di corrente
Però in un ==op-amp== reale il guadagno sarà **finito**, **costante** solo **in un certo range di frequenze**, inoltre in un op-amp reale si presentano correnti scorrere nei terminali di ingresso, però queste correnti nella maggior parte dei casi è trascurabile, infine l'uscita è data dal tipo di op-amp.

**RETROAZIONE NEGATIVA**
Sistema che serve per mantenere e correggere l'output in base all'iinput.
Condiziona l'ingresso in base al valore dell'ucita mantenendola controllata.
![[Screenshot From 2025-10-06 12-38-20.png]]
$V_o = A_{OL}(V_i - \beta V_o)$ 
$V_o = A_{OL}V_i - A_{OL}\beta V_o$ 
$V_o(1+A_{OL}\beta) = V_i*A_{OL}$
$V_o = V_i * \frac{A_{OL}}{1 + A_{OL}\beta}$ 
$V_o = V_i * A_{CL}$

Per avere le tensioni ai terminali di input:
- $V^+ = V_i$
- $V^- = \frac{A_{OL}\beta}{1 + \beta A_{OL}} * V_i$ 
- $\Delta V = V_i(1- \frac{A_{OL}\beta}{1+A_{OL}\beta}) = V_i(\frac{1}{1+A_{OL}\beta})$ questo porta ad un reciproco di un numero grandissimo, questo vuole dire che la differenza di potenziale è quasi 0


# CIRCUITI DIGITALI
Grazie ai circuiti digitali, i quali usano una codifica binaria, si possono utilizzare per eseguire **operazioni aritmetiche** e **operazioni logiche**, i quali per funzionare utilizzano delle **porte logiche** dove i valori utilizzati possono essere soltanto **1**(tensionie a 5V) o **0**(tensione a 0V).
## ALU
L'**UNITÀ LOGICO ARITMETICA**  è un comoponente molto importante per tantissimi tipi di circuiti, tra cui anche le **CPU**.
La ALU  è un circuito digitale il quale permette di eseguire **operazioni logico e aritmetiche** su **2 input**(2 numeri binari interi), e dove l'operazione viene decisa da un'altro input grazie ad un codice **(opcode)** il quale indica quale **operazione eseguire**, che verrà visualizzato grazie al terminale di **output** e un'uscita la quale indica un **FLAG** su possibili risultati di un'operazione(Es. riporto di un'addizione), e un'ulteriore terminale di entrata il quale inidicherà errorri o riporti fatti da altre operazioni di altre ALU(Es. overflow).
![[Pasted image 20260130174742.png]]

## Encoder
È un circuito che converte un parola rigorosamente **hot-one**(parola con tutti 0 trane un bit ad 1), in una numero binario che identifica la posizione del bit a 1, per questo gli ingressi devono essere $2^n$ invece le uscite devono essere n.
![[Pasted image 20260130180617.png]]
Per input differenti da parole hot-one, l'output deve essere scartato poichè non ci interessa.

## Decoder
Circuito che effettua lavoro contrario all'encoder, infatti ha **n entrate** e $2^n$ **uscite**, la combinazione di input avrà come output una parola binaria hot-one.
![[Pasted image 20260130215448.png]]

## MULTIPLEXER/DEMULTIPLEXER
Il **multiplexer** è un dispositivo a $2^n$ input, 1 output e n input di selezione.
Il valore di output sarà dato dalla linea input che **corrispone alla combinazione degli input di selezione.**
Questo permette, grazie anche al **demultiplexer**, di poter utilizzare una linea per comunicare con n dispositivi.
Invece il **demultiplexer** ha come input un unico terminale, dove il segale sarà ad un solo terminale di $2^n$ output, il quale sarà deciso da n input di controllo.

**MUX**
![[Pasted image 20260130220308.png]]

## Circuiti combinatori e sequenziali
In elettronica si distinguono i circuiti in 2 categorie, che lavorani con metodi differenti:
- **Logica Combinatoria**:l'output dipende dalle combinazioni dell'input in un peciso istante t.
- **Logica sequenziale**: l'output non dipende solo dalle combinazioni in un istante ma anche dal risultato di quelle passate.
Per questo quelli sequenziali devono tenere traccia delle vecchie combinazioni, così da introdurre meccanismi di memoria.

## Clock
Segnale che viene utilizzato per **sincronizzare** i circuiti logici, perchè questo tipo di circuiti per elaborare le informazioni serve del tempo per questo si utilizza un segnale che possa sincronizzare il sistema.
Questo segnale deve essere molto preciso e la sua freqenza deve essere stabile nel tempo, questo si fricava grazie ad un chip con al suo interno un cristallo di quarzo, il quale emette un segnale ad una certa frequenza.

Oppure si può crere tramite uno stratagemma, **RING OSCILLATOR**, il quale utilizza una sequenza di porte NOT creando un ciclo, che grazie al ritardo di propagazione intrinseco ed un numro **dispari** di porte, questo può essere considerato come un **generatore di onde quadrate**.
![[Pasted image 20260130222624.png]]
Si può manipolare la frequenza dell'onda in base al numero di porte che questo ciclo viene composto.

## FLIP FLOP
I flip flop sono dei circuiti digitali, che compiono il compito di fare da memoria, ed esistono vari tipi di flip flop
### JK
Questo tipo di flip flop ha 2 terminali di input:
- **j** set
- **k** reset
1 terminali in ingresso per il segnele di clock, dove tutti i c**ambiamenti vengono effettuati su fronte di salito o discesa** del segnale, e le due uscite di 1 invertita e l'altra no.
![[Pasted image 20260130231529.png]]
![[Pasted image 20260130231550.png]]

## Registri a scorrimento
Un registro a scorrimento, è un **insieme** di flip flop D che **condividono lo stesso clock** e l'uscita di un flip flop fa parte dell'input di quello dopo, questo permette oltre alla memorizzazione anche lo spostamento dei dati tra i vari flip flop.

In base a come vengono collegati, possoo essere divisi in 2:
- **SISO**:serial in, serial out
	Tipo di memoria più semplice, ogni volta che un dato viene immagazzinato il dato viene spostato a destra fino ad arrivare all'uscita dell'ultimo flip flop.
	Questo è un tipo di memoria distruttiva poichè se si ha una parola di 4 cifre in 4 cicli hai riempito tutte le celle, ma se si prosegue con il 5° il primo bit immagazzinato viene perso.
	
![[Pasted image 20260130232302.png]]
- **SIPO**:serial in, Parallel out
	L'immissione dei dati funziano allo stesso modo di quello SISO, ma in questo caso la lettura dei dati può esssere effettutato in modo parallelo.
	
![[Pasted image 20260130232355.png]]
- **PISO**: parallel in, serial out
	Questo tipo di collegamento fornisce un ingresso parallelo cioè può immagazzinare n bit alla volta, fornisce un' uscita seriale però per permettere che i dati si spostano in modo seriale si usare uno stratagemma attraverso il collegamento in serue di porte AND e l'ingresso parallelo, però per poterlo utilizzare bisogna aggiungere un bit che indica se LOAD o SHIFT.
	
![[Pasted image 20260130232507.png]]
- **PIPO**: parallel in, paralle out
	Considerato come un PISO ma consente la lettura in parallelo, ma si comporta come PISO se si legge sola dalla cella più a destra, si comporta come SIPO se manteniamo shift/load.
![[Pasted image 20260130233942.png]]
### BIDIREZIONALI
Le architetture precedenti consentono lo spostamento dei dati **solo in una direzione**, però è possibile crere dispositivi che spostano **bidirezionalmente** usando un'architettura di tipo **PISO** però collegando l'uscita di ogni flip flop con l'entrata di quello dopo, il bit shift/load verrà sostituita dal bit che indica la direzione dello shift.
![[Pasted image 20260130234633.png]]

## MACCHINE A STATO FINITO
Una macchina a stati finiti **FSM**, queste macchine possono passare da uno stato all'altro in base agli **input esterni** e in base allo ==stato in cui si trova in quel momento==, queste macchine possono avere anche output che si avranno lo ==stesso comportamento degli input.==
Gli stati e input possono essere codificate in stringhe binarie, e quindi permette di trasformare una macchina astratta in un cicruito digitale.

## MICROPROCESSORI
Un micoprocessore è un'**unità di calcolo**, che integra capacità di **calcolo aritemtico, logico e controllo.**

Un **microcontrollore** è come un piccolo computer, il quale può essere fabbricato in un solo circuito integtrato, che può contenere **periferiche di I/O**, e momorie **RAM**.
Per utilizzare uno di questi microcontrolori può essere porgrammato grazie ad una memoria **FLASH** la quale conterrà le istruzioni che dovrà eseguire.
Ora questi tipi di computer, sono diventati sempre più potenti così da consentire **collegamento** tramite interfacce di comunicazone come USB, e questo consente una grande sfaccettatura di utilizzi per questo tipo di dispositivo, grazie a **sensori e attuatori**.
![[Pasted image 20260131155901.png]]
Questo tipo di microcontrollori hanno al suo interno un tipo di microprocessore con un **set di istruzione ridotto**, il quale permette di fare solo le operazioni di base, che però grazie a questo tipo di architettura il microprocessore viene ottimizzato dal punto di vista economico e **energetico**, così facendolo diventare il dispositivo più diffuso per applicazioni di tipo **embedded**.

# SENSORI
Un sensore è un dispositivo che trasforma una **variazioni di una grandezza FISICA** in una **variazione di una grandezza ELETTRICA**.
I sensori sono esempi di trasduttori, ma non tutti i trasduttori sono sensori.

**Caratteristiche** dei trasduttori:
==**STATICHE**==
- **SPAN**: intervallo della grandezza in cui il sensore ha il comportamento desiderato.
- **FONDO SCALA**:intervallo coperto dalla quantità di sucita quando la grandezza di ingresso si estende attraverso l'intervallo di ingresso.
- **SENSIBILITÀ**:Rappresenta quanto sia sensibile alle variazioni di grandezza fisica in ingresso.
- **RESOLUTION**
- **LINEARITÀ**
- **OFFSET**
- **STABILITÀ**
- **ISTERESI**
- **SELETTIVITÀ**
- **EFFETTI DI CARICO**
==**DINAMICHE**==
- **FUNZIONE DI TRASFERIMENTO**
- **RISPOSTA AL GRADINO**
- **RISPOSTA IN FREQUENZA**
**==AFFIDABILITÀ==**
- **DURATA NOMINALE**
- **Numero di cicli di fondo scala**
- **TOLLERANZA AI GUASTI**
## SENSORI DI TEMPERATURA
Per misurare la temperatura si possono usare dei meccanismi fisici come **conduzione**, **convezione**  e **irraggiamento**.
Il sensore deve essere capace di misurare la temperatura dell'ambiente in cui è posto, però senza che le sua misurazioni siano sporcate dal sensore stesso.
Alcuni esempo di sensori di temperatura:
- Termocoppie 
- RTD (resistance temperature detectors, o termoresistenze) 
- Termistori 
- Sensori integrati 
- Pirometri
### TERMOCOPPIE
Le termocoppie sono un tipo di sensore termico, il più **semplice**, è composta da **2 pezzi di metallo** diversi in una giunzione, che **convertono direttamente il calore in elettricità.**
La tensione generata sarà proporzianale alla differenza di temperatura tra la giunzione calda e quella fredda.
$V = S\Delta T$ 
Questo tipo di termocoppie possono essere costruite con vari materiali, che grazie alle poprietà fisico chimiche varian in base all'applicazione come:
- **TIPO E**(chromel-costantana): sensibilità alta, migliore per applicazioni di tipo criogenico
- **TIPO J** (ferro–costantana): sensibilità maggiore ma con intervallo più ristretto, 
- **TIPO K**(chromel-allumel): quella con utilizzo più generico, con una sensibilità minore ai primi 2, è il più economico e ha un grande intervallo.

### TERMORESISTENZE
Le termoresistenze sono sensori che convertono la variazione di calore in r**esistenza elettrica**.
La resistività di una resistenza dipende oltre che dal materiale, anche dallo **spessore** e **superficie** della parte metallica, ma anche dalla **temperatura del resistore**, per questo se in uno normale la temperatura rimane sempre la stessa, in questo caso bisogna aggiungere anche la **variazione di temperatura** al calcolo della resistenza.
Resistività a **Temperatura N**:
![[Pasted image 20260131181141.png]]
Resistenza:
![[Pasted image 20260131181201.png]]

Questo tipo di sensore è **costoso**, però è molto preciso e stabile, ma soffre anche di **autoriscaldamento** poiché oltre al calore che misura il sensore, la resistenza del dispositivo deve essere ricavata facendo fluire correnete all'interno della resistenza, e questo può provocare un autoriscaldamento.

## SENSORI DI FORZA
I sensori di forza sono trasduttori utilizzati per **misurare le forze applicate** a un elemento generico. I due strumenti più adatti per farlo sono: 
- Estensimetri (strain gauge) 
- Sensori piezoelettrico

### ESTENSIMETRI
Tipo di sensori che misura la forza applicata al sensore tramite la **deformazione** di un pezzo di metallo(la deformazione del metallo fa cambiare la resistenza), così da stimare la forza che lo ha deformato tramite la variazione di resistenza.
![[Pasted image 20260201214206.png]]
La resistenza di questo tipo di sensore varia in base al fatto che il pezzo di metallo cambia resistività in base alla fomra del metallo.
![[Pasted image 20260201214423.png]]

### PIEZOELETTRICI
Tipo di sensori che dopo una sollecitazione esterna **genera tensione** a bassa frequenza.

## SENSORE DI COPPIA
### ESTENSIMETRI
Per misurare la coppia su un albero, vanno messi 2 estensimetri lungo direzioni specifiche, infatti se viene applicata una certa coppia l'albero si deformerà.
Però per utilizzare quesa soluzione bisognerebbe utilizzare **dei circuiti per calcolare la resistenza dei due estensimetri**, questo comporta a collegamentio tramite fili i quali si aggroviglierebbero essendo collegati ad un corpo rotante.

### OTTICI
Sensore composto da due dischi, 1 **emettitore di luce**, 1 **ricevitore di luce**, il disco emettiore è collegato e ruota assieme all'albero e dispone di un'insieme di led, invece il ricevitore è fermo e ha un'insieme di fotodiodi, questo permette di prendere la velocità di rotazione e **indirettamente** anche la coppia.
Questo tipo di sensori però sono delicati e molto costosi.

## SENSORI DI POSIZIONE
sesnori usati per misuarare la posizione **lineare** o **angolare** di un oggetto.

![[Pasted image 20260201230448.png]]

### POTENZIOMETRI
Sono trasduttori di posizione analogico , e possono essere **lineari**, il potenziometro è fondamentalmente un resistore a 3 terminali con elemento scorrevole o rotante.
2 terminali di input e il terzo di output.
Però se si utilizza solo uno di input e 1 di output in questo caso diventa una resistenza variabile.
![[Pasted image 20260315214602.png]]

Il materiale con cui viene composto il potenziometro deve essere omogenea, per questo se si misurano le tensioni di uscita e entrata, $V_{out}$ è una frazione della tensione di ingresso E, per queto la **posizione del cursore** è il rapporto $\frac{V_{out}}{E}$, però questo può succedere solo in caso di un potenziometro ideale.

I potenziometri sono comunemente usati per controllare dispositivi elettrici come i controlli del volume sulle apparecchiature audio. I potenziometri sono usati raramente per controllare direttamente potenze significative (più di un watt), poiché la potenza dissipata nel potenziometro sarebbe paragonabile alla potenza nel carico controllato.

### ENCODER
L'encoder è un sensore di posizione che, a differenza del potenziometro, ha un'uscita digitale. Gli encoder possono essere lineari o rotazionali. È costituito da un disco (se rotativo) o da una striscia (se lineare) di materiale opaco con una serie di fori.

Eistono 2 tipi di **encoder**
- **==INCREMENTALE==**
	Il principio di funzionamento di questo encoder, parte da un diodo LED che emette luce  e un fotodiodo ogni volta che i fori sul disco si allineano con il LED e il fotodiodo, il fotodiodo emetterà un **impulso** ogni volta che viene colpito dalla luce del LED.
	Contando il numero di impulsi si può capire l'angolo di rotazione, In particolare, ad ogni impulso generato dal fotodiodo corrisponde una rotazione di $r=\frac{360°}{n}$, dove n è il numero totale di fori. 
	Questo encoder viene denominato in questo modo perchè, questo non può risolvere la posizione dell'oggetto in modo assoluto, invece deve ricavare **il grado di rotazione**, tramite un **contatore**, e anche di uno **starter** che definisce la posizione di partenza dell'encoder, però deve essere in grado di capire **senso della rotazione**.
	![[Pasted image 20260315224549.png]]

- **==ASSOLUTO==**
	È molto simile a quello incrementale, il funzionamento è anche molto simile, solo che la **forma e il numero di fori sono disposti è molto diverso**, infatti i fori sono disposti in **più cerchi concentrici**  e i fori stessi sono diversi tra loro.
	Il numero di fori e la loro diensione varia in base al cerchio su cui sono disposti, **cioè ogni cechio ha metà della propria area coperta da fori e l'altra ne è priva**, dove il numero di fori varia di $2^{i-1}$ dove i è il numero del cerchio dove sono i fori, infatti nel primi c'è un unico foro, nel secondo 2 e nel terzo 4.
	Inoltre, se sono presenti **k anelli**, ci saranno anche **k LED e k fotodiodi**, con ciascuna coppia allineata con ciascun anello.
	Posizionando correttamente i fori, ogni posizione angolare **sarà associata ad una combinazione unica di fotodiodi in uscita**. In questo modo è possibile leggere l'uscita dei fotodiodi e **determinare immediatamente la posizione angolare assoluta**, senza utilizzare alcuno starter e/o contatore. 
	Con questo tipo di encoder si possono utilizzare anche diversi tipi di codici, **binario,ASCII,GRAY**.
	![[Pasted image 20260315230549.png]]

L'encoder assoluto:
- Costa **più** di quello incrementale
- Funziona tipicamente fino a 80-100 °C. L'intervallo di temperatura non è così ampio e non è il massimo per ambienti difficili
- Il montaggio richiede cautela
- Può anche **essere magnetico.** Quest’ultimo ha una ==maggiore durata, affidabilità e intervallo di temperatura di esercizio==. Può avere un'**uscita analogica**. Ha alta precisione e alto costo. 

### RESOLVER
l **resolver** è un trasduttore di posizione angolare molto comunemente impiegato **basato sull'induzione magnetica**. È molto robusto e affidabile, anche in ambienti difficili. Per questo motivo è spesso utilizzato nel settore automobilistico, ed è un elemento chiave nella catena cinematica dei veicoli elettrici e ibridi.
Funziona sfruttando il principio di **induzione magnetica**, cioè la capacità di produrre una forza elettromotrice attraverso un conduttore elettrico immerso in un campo magnetico.
Nel resolver vengono utilizzate delle **bobine**, dove una bobina pilotata da una corrente (o tensione) AC genererà un campo magnetico che cambia nel tempo, questo campo magnetico generato produrrà una tensione AC in un'altra bobina.
La tensione generata dalla seconda bobina avrà la stessa **frequenza della tensione** applicata alla prima bobina. 
La tensione presentata sulla seconda bobina **dipende** dalla tensione presenta sulla **prima**, dall'angolo $\alpha$ , la distanza e la composizione delle 2 bobine.
La tensione presente sulla prima bobina($V_{gen}$) e la tensione sulla seconda($V_{ind}$).
$$
\begin{aligned}
V_{gen}(t) = E_0sin(\omega t + \rho) \\
V_{ind}(t) E_0cos(\alpha)sin(\omega t + \rho)
\end{aligned}
$$
Il resolver è composto da 2 parti:
- **rotore**: parte che **ruota assieme all'oggetto** da monitorare, con una bobina eccitatta tramite corrente alternata, la quale genera un campo magnetico alternato.
- **statore**: parte **ferma**, con **2 bobine in posizione ortogonali** tra di loro, sui quali verranno indotti da una certa **tensione alternata** grazie all'induzione magnetica, 

![[Pasted image 20260316235422.png]]

## SENSORI DI ACCELERAZIONE
Sono usati per misurare le accelerazioni, possono essere **lineari** o **rotazionali**, la loro sensivilità viene misurata in $\frac{mV}{ms^{-2}}$ quando l'**uscita è tensione**, oppure $\frac{pC}{ms^{-2}}$  quando l'**uscita è una capacità**.
I sensori possono essere:
- **Piezoelettriche**
- **Piezoresistive**
- **Meccaniche**
- **Capacitive**
- **Integrate**

### PIEZO
Le accelerazioni possono essere rilevate utilizzando materiali **piezoelettrici** e **piezoresistivi**.
I sensori **piezoelettrici** non riescono a monitorare **un'accelerazione continua**, perchè soffrono di :
- Limitazioni di banda
- La frequenza di **accelerazione minima** è data dalla **costante di tempo del cristallo** 
- Mentre la **frequenza massima** è limitata dalla **risonanza maccanica**
Per questo non possono essere utilizzati per far scattare gli airbag, poichè quel tipo di accelerazione è concentrata nelle **alte frequenze** e questo rende difficile la rilevazione al sensore, in oltre a questo sensore serve un cablaggio **speciale**.
Però offrono:
- **ampia sensibilità**
- **ampio intervallo di funzionamento termico**
- **buona risposta nel tempo**

Invece i sensori **piezoresistivi** possono monitorare **accelerazioni continue**, mostrano una buona ==immunità ai campi elettrici== ma una **sensibilità** piuttosto **ampia alle variazioni di temperatura**.

### MEMS(MICRO ELCTRO MECHANICAL SYSTEM)
I **sistemi microelettromeccanici** (MEMS) sono una valida **alternativa** basata sulla stessa **tecnologia** usata per **produrre** i **circuiti integrati su microscala**, sono costruiti da componenti dalle grandezze tra i 1 e 100 micrometri, invece i dispositivi MEMS generalmente hanno dimensioni comprese tra 20 micrometri e un millimetro.

Di solito sono costituiti da un **chip**(come in un microprocessore) che elabora i dati, e diversi diversi componenti che interagiscono con l'ambiente circostante(**microsensori**).
A causa della sua grandezza forza come elettromagnetismo e la fluidodinamica, possono impattare sul risultato dato dai sensori.

Questi sensori MEMS sono diventati molto importanti, nel momento in cui si potevano applicare alla propria costruzione le **tecnologie di fabbricazione** dei dispositivi semiconduttori, questo permette la cotruzione di **sensori microintegrati** in dispositivi elettronici, che elaborano i dati ricevuti dal sensore.

Questo permette la costruzione di diversi tipi di dispositivi:
-  Stampanti a getto d'inchiostro, che utilizzano l'emissione piezoelettriche di bolle di inchiostro per depositare l'inchiostro sulla carta
- Accelerometri per vari scopi (ad esempio, attivazione dell'airbag, sicurezza, controllo di edifici)
- Giroscopi per molti scopi (ad es. controllo della stabilità, guida di droni)
- Sensori magnetici MEMS per Sistemi di Navigazione Inerziale (INS)
- Microfoni MEMS per smartphone, wearable, applicazioni smart home)
- Sensori di pressione al silicio, ad es. sensori di pressione sanguigna monouso
- Applicazioni Bio-MEMS come biosensori, incorporati in dispositivi medici come stent
- Raccolta di energia su microscala
- Trasduttori a ultrasuoni per applicazioni di monitoraggio della salute (es. ecografia)
- Altoparlanti basati su MEMS per cuffie intrauricolari e apparecchi acustici

Grazie alla tecnologia della microfabbricazione, un complesso sistema di masse mobili e stazionarie può essere ricavato nel silicio, creando un sistema sismico, come nella figura seguente.
![[Pasted image 20260318002549.png]]
Una massa mobile, che mostra una struttura interdigitata, è **collegata tramite una molla** al supporto, che è invece **fisso**. Tra le dita della massa mobile ci sono delle dita fisse: le dita fisse e mobili sono separate dall'aria e **formano** le **piastre di un condensatore**. Il **moto della massa varia la distanza tra le dita(t)** (le due piastre del condensatore), tipicamente di poche decine di micron. Pertanto, realizzando un accelerometro compatto massa-molla-smorzatore direttamente sulla base di silicio del chip, possiamo anche implementare i circuiti elettronici necessari per rilevare le variazioni di capacità e recuperare la posizione della massa mobile, quindi calcolare l'accelerazione. 

$$
C = \frac{A\epsilon_{xo}}{t}
$$
Dove **C** è la capacità, **A** è l'area, $\epsilon_{x0}$ è la costante dielettrica e **t** è la distanza tra le dita.

Per eliminare la non linearità nel rapporto tra distanza e capacità, è sufficiente v**alutare direttamente l'impedenza.**
Tipicamente, ==vengono utilizzate molte lamelle== (dita) in parallelo per **massimizzare l'area equivalente del condensatore e quindi la sensibilità del sensore.** Come tutti i MEMS, deve essere progettato per ridurre al minimo gli effetti delle forze elettrostatiche, molto dannose su microscala.

## SENSORI MAGNETICI
I sensori magnetici sono impiegati per **monitorare e misurare i campi magnetici**. Esistono molte tipologie di sensori magnetici tra cui troviamo:
- **Sensori di Hall**: i più utilizzati e si basano sull'effetto Hall
- **Sensori Magnetoresistivi**: Sfruttano le proprietà di una particolare classe di materiali, detti materiali magnetoresistivi
- **Sensori Magnetostrittivi**: basati su materiali magnetostrittivi che sfruttano la cosiddetta **magnetostrizione**. Questa è una proprietà che provoca un **cambiamento nella forma** o nelle **dimensioni** di tali materiali durante il processo di magnetizzazione.

### SENSORI DI HALL
I sensori di Hall sono sensori magnetici che **sfruttano la forza di Lorentz** per rilevare un campo magnetico. La forza di Lorentz è la **forza esercitata da un campo magnetico su una particella carica** (come un elettrone) che si muove. In particolare, è data dall'equazione vettoriale:
$$
\vec{F} = q\vec{v} \times \vec{B}
$$
dove $\vec{F}$ è la **forza di Lorentz**, **q** è la carica elettrica della particella, $\vec{v}$ la velocità e $\vec{B}$ è il campo magneticoche insiste sulla particella.
La Forza di Lorentz è **proporzionale** alla velocità della particella è anche all'intensità del campo magnetico e dipende anche dalla direzione relativa della velocità e del campo magnetico.

![[Pasted image 20260319231200.png]]
Si suppone di avere un film metallico conduttivo, a forma di parallelepipedo con spessore s, avente 6 faccia.
Su **4 di queste facce esistono dei contatti**, non sono presenti solo nella faccia superiore e inferiore.
Se il film metallico viene **attraversato da una corrente I**, come nell'esempio, si presenterà una caduta di potenziale solo sui contatti dove frontali e posteriori poiché **non essendoci** campo magnetico, la corrente fluirà **linearmente** da un contatto all'altro, invece negli altri 2 contatti la caduta di tensione sarà **pari a 0**.

Se invece è presente un campo magnetico, gli elettroni in movimento **non seguono** un movimento lineare, ma verranno deviati grazie alla forza di Lorentz, questo comporta ad un flusso di elettroni anche nella direzione **sinistra-destra**, che presenterà anche una **caduta di potenziale** sui 2 contatti.
$$
V = KBI = \frac{\mu_{q}\rho}{s}*BI
$$
e si può definire
$$
\frac{V}{I} = R_{h} = \frac{\mu_{q}\rho}{s}*B = Resistenza\space di\space Hall
$$
**I** è la corrente fronte-retro, **K** è una costante che dipende dalle proprietà del film metallico, **B** è l'intensità del campo magnetico.
K dipende dalla mobilità dei portatori di carica nel materiale, $\mu_{d}$, dalla resistività del materiale, $\rho$, e dal suo spessore s, la resistenza $R_{h}$ è **dipende solo** dall'**intensità campo magnetico** e dalle **proprietà del materiale**.
I sensori Hall sono generalmente utilizzati negli inverter elettrici e come sensori di corrente indiretta, e anche in strumenti scientifici e rivelatori per segnali fino a una larghezza di banda di $\approx$ 100 kHz, però se esposti per **lungo tempo** a campi magnetici **realtivamente forti** possono soffrire di problemi di affidabilità, poiché le proprietà del film metallico potrebberò cambiare.
Per ovviare a questo problema si può usare una **disposizione a feedback**, se il film è soggetto a un campo magnetico molto forte, si può utilizzare un **campo magnetico compensante** il quale attenuerà il campo magnetico iniziale.

![[Pasted image 20260319234333.png]]
Il filo giallo è attravarsato da una coorente ,questa corrente **genera un campo magnetico**, la cui intensità è proporzionale alla corrente, e ovviamente **dipenderà dalla distanza dal filo**. Un nucleo ferromagnetico a forma di C è posizionato attorno al filo per focalizzare il campo magnetico sulla sua apertura, dove è posizionato un sensore di Hall. In queste condizioni il campo magnetico generato dalla corrente e incidente sul sensore di Hall sarà perpendicolare al piano del sensore e la sua intensità sarà: $B = \alpha I$.

Nel caso di una disposizione feedback, è presente anche il secondo campo magnetico $B_{comp}$, e il primo avrà un valore netto $B_{net}$, il valore di uscita sarà:
$$
V_{h} = KI_{bias}B_{net}
$$
deve $I_{bias}$ è la **corrente di alimentazione** del sensore, e **K** è la costante del sensore di Hall.
Questa tensione viene convertita in una corrente, chiamata $I_{comp}$, da uno specifico circuito amplificatore con guadagno $\beta$:
$$
I_{comp} = \beta V_{h} = \beta KI_{bias}B_{net} = \beta KI_{bias}(B - B_{comp})= \beta KI_{bias}(\alpha I - B_{comp}) = \lambda(\alpha I - B_{comp})
$$
Questa corrente viene generata da una bobina arrotolata N volte, e questo genera il secondo campo magnetico
$$
\begin{aligned}
I_{comp} = \frac{I}{N} \\
E\space il\space campo \space magnetico \space generato \space sarà \\
B_{comp} = \frac{\epsilon I}{N}
\end{aligned}
$$
Dove $\epsilon$ è una costante si proporzionalità nota:
$$
I_{comp} = \lambda(\alpha I - B_{comp}) \to \frac{I}{N} = \lambda\left( \alpha I - \frac{\epsilon I}{N} \right) \to \lambda = \frac{\frac{1}{N}}{\alpha - \frac{\epsilon}{N}} = \beta KI_{bias} \to \beta = \frac{\frac{1}{N}}{KI_{bias} \left( \alpha - \frac{\epsilon}{N} \right)}
$$
Questo permette di calcolare la corrente del campo magnetico secondario solo tramite costanti note, questo permette di ricavare tramite una resistenza connessa a massa una tensione che permette così da calcolare la **corrente da misurare**.
$$
\begin{aligned}
V_{out} = R_{L}I_{comp} = R_{l} \frac{I}{N} \to
I = V_{out} \frac{N}{R_{L}}
\end{aligned}
$$

### MAGNETORESISTIVI
Qusesti sensori si basano sul **disco di Corbino**, cioè 2 anelli conduttivi con un materiale magnetoresistivo nel mezzo, materiali che cambiano la loro resistenza in funzione dell'intensità del campo magnetico.
Basati anche loro sul **principio di Lorentz**.

Quando non viene applicato un campo magnetico, e ai 2 alettrodi viene applicata della tensione, la corrente fluisce dall'anello interno a quello esterno in **direzione radiale**, ma avendo per direzione solo la componente $r_{\rho}$ invece la componente $r_{\theta} = 0$, avendo come valore della resistenza, il **valore nominare** $R_0$. Invece se applicato un campo magnetico B, questo devierà il percorso della corrente, così da avere la componente $r_{\theta} \neq 0$ così da llungare il percorso delle cariche da un anello all'altro.
![[Pasted image 20260322001246.png]]
Per questo se la tensione applicata è uguale, la corrente misurata sarà minore, così la resistenza misurata R sarà maggiore a $R_0$, misuarndo la resistenza R è **possibile recuperare l'ampiezza del campo magnetico**.
Questo tipo di sensore ha un comportamento quadratico che dipende dal valore del campo magnetico B, questo cambierà anche in base al materiale utilizzato per il sensore, però riceve la misurazione può variara cnhe in base alla temperatura, oltre a questo a meno che si abbia una coppia di questi sensori non si può sapere la direzione del campo magnetico.

## SENSORI DI CORRENTE
Sono sensori per misurare le entità delle correnti, anche se **è possibile** misurarla tramite **i sensori magnetici**, si può fare anche tramite sensori adibiti soltanto al valutare la corrente come: 
- **SHUNT**
- **TRASFORMATORI**

### SHUNT
Questo tipo di sensore può essere visto come un **resistore** con un valore di resistenza molto basso,  $>1\ohm$, la caduta di tensione su questa resistenza può essere misurata così da **ricavare il valore** della corrente, però bisogna essere attenti nel maneggiare questo tipo di resistenze poichè avendo un valore così basso, sul valore della resistenza possono influire anche i **collegamenti**, di solito ignorati, queste causa di riscrivere la legge di Ohm:
$$
I = \frac{V}{R+ 2r}
$$
Però essendo che R e r sono molto simili in valore, questo ci rende molto difficile la misura della caduta di tensione, perché noi conosciamo solo R ma **r** è molto difficile da ricavare questo ci rende impraticabile l'operazione di ricavare la corrente.
Però questo problema può essere evitato devono essere costruiti in **modo diverso**, infatti questo tipo di resistori vengono chiamati **resistori Kelvin** o **resistori a 4 terminali**, di cui 2 **terminali di corrente**, sono pin standard i quali vengono montani normalmente sui resistori, invece gli altri 2, **i terminali di tensione**, sono costruiti conmateriali a bassissima resistività i quali vengono a costare di più di quelli normali, però può garantire una **resistività trascurabile**.

I sensori shunt sono:
- Adatti per correnti DC e AC fino alle alte frequenze. Tuttavia, per frequenze molto elevate, gli effetti induttivi parassiti diventano dominanti, insieme agli di prossimità e al cosiddetto “effetto pelle”
- Semplici, robusti e affidabili
- Interessati dal problema dell'autoriscaldamento: la corrente nella resistenza provocherà un riscaldamento Joule che influirà sul valore della resistenza
- Non una buona scelta se è necessario l'isolamento galvanico
- Ingombranti e pesanti: per misurare correnti elevate possono essere necessari shunt che pesano fino a 10 kg.

### TRASFORMATORE
I sensori di corrente basati su trasformatore sfruttano dispositivi elettrici detti trasformatori,utilizzati per **scalare correnti molto elevate a valori inferiori**, rendendo possibile la loro **misura** con **altri sensori di corrente**.

![[Pasted image 20260322220740.png]]

Questo trasformatore sfruttando l'induzione magnetica **per generare un campo magnetico**, facendo fluire la corrente un una bobina primaria, sia ccopierà anche ad una seconda bobina che **indurrà una corrente**, dove l'ampiezza della corrente è proporzionale a quella della prima bobina, con una costante $\alpha$, che può essere dimanesionata tramite il **numero di avvolgimenti**, $N_{1},N_{2}$, questo permette di utilizzare questo metodo per la misurazione di correnti elevate, ma la risoluzione del sensore sarà molto ridotta.

Un vantaggio di questo tipo di sensore è l'isolamento galvanico. D'altra parte, non può funzionare con correnti DC poiché non generano campi magnetici variabili nel tempo.


# ATTUATORI
È un dispositivo elettronico che trasforma le grandezze **elettrica** in una grandezza **fisica**, come temperatura, pressione o pozizione...

A differenza dei sensori, gli attuatori, devono **erogare** una **grande quantità di potenza**, e quindi serve anche una grande potenza in input, la quale è anceh maggiore a quello di output.

## ATTUATORI TERMICI
Tipo di attuatore che serve per controllare la temperatura dell'ambiente, quelli più semplici possono solo **aumentare** la temperatura, però ne sistono alcuni che possono anche **ridurla**.

Quelli riscaldatori sono dispositivi che sfruttano **l'effetto Joule** per tfarsormare la potenza elettrica dissipata in calore, così aumentando la propria teperatura.

![[Pasted image 20260322225837.png]]

Un esempio di questo tipo di attuatore può essere una **serpentina metallica** di ferro, la quale può funzionare a regmi di bassa potenza, da pochi W a pochi kW, fino ad un l**imite massimo di emperatura**, la barra metallica deve avere una bassa resistività, data dalla grande sezione della barra setssa, così da massimizzare la dissipazione di potenza per una data potenza di pilotaggio $P = \frac{V^2}{R}$.
Però non è detto che per ogni unita di potenza la temperatura salga, poichè la **resistività** cambia in base alla temperatura del resistore, e questa può variare in base alla **resistività termica del materiale**, uno dei materiali più utilizzati è il tungsteno per il suo punto di fusione alto.

Per poter controllare la temperatura ambientale tramite attuatori, bisogna analizzare anche la temperatura circostante, cioè **il percorso** che **il calore generato effettua**.
Per questo bisogna prendere la temperatura dell'elemento attivo $T_{j}$ del resistore e la temperatura dell'ambiente $T_{e}$, e $\dot{Q}$ moltiplicato per la somma delle resistenze termiche di tutte le interfacce che separano la giunzione dall'ambiente.

Se l'attuatore ha una giunzione e un involucro, le interfacce tra **giunzione-involucro** hanno una resistenza termica $R_{J-C}$, e quella tra l'**involucro-ambiente** $R_{C-E}$, dove la resistenza termica totale è $R_{J-E}$ di un dispositivo con un'interfaccia tra **giunzione-ambiente**.
$$
T_{J}-T_{E} = \dot{Q}(R_{J-C}+R_{C-E}) = \dot{Q}R_{J-E} 
$$
Si può calcolare allo stesso modo la temperatura dell'involucro:
$$
\begin{aligned}
T_{C} - T_{E} = \dot{Q}R_{C-E} \\
T_{J} -T_{C} = \dot{Q}R_{J-C}
\end{aligned}
$$
Queste equazioni sono utili per comprendere la quantità di dissipazione di potenza necessaria per generare una data temperatura di giunzione, e quindi una data temperatura ambiente, con queste equazioni si possono calcolare anche le temperatura in caso di involucri, così da poter stimare anche la durata del dispositivo.

## DIODI METTITORI DI LUCE 
Un diodo di emissione di luce(LED) è un tipo di diodo, **non sostruito in Silicio**, ma con materiali semiconduttori a **bandgap diretto**.
Hanno una tensione di lavoro **più alta** rispetto a quello dei normali diodi, e a seconda del materiale emette colore diverso in base al materiale.

![[Pasted image 20260323225319.png]]

Il principio di funzionamento è molto simile a quello dei diodi normali, cioè se **polarizzato direttamente** il diodo emetterà luce con un'efficienza del 95%.

Quando un diodo led è accoppiato ad un fototransistor/fotodiodo, possono essere presi in considerazione per una possibile comunicazione wireless tra 2 circuiti, trasformando la'informazioni in luce, che il fotodiodo catturerà.

## SOLENOIDI
Un solenoide è un dispositivo a due terminali costituito essenzialmente da una bobina elettrica e da un nucleo ferromagnetico, può essere costruito per essere compatibile con uscita digitale o analogico.

L'ingresso elettrico è **una corrente** che alimenta la bobina, questa corrente alimeterà **la bobina** che grazie al campo magnetico generato **attirerà/respingerà** il nucleo ferromagnetico.
![[Pasted image 20260323223512.png]]

Molti solenoidi sono attuatori lineari, in modo che la corrente nella bobina generi un movimento/forza lineare con l'intensità della corrente, dove il nucleo può essere vincolato da una molla o può essere libero di muoversi.

I solenoidi possono essere progettati direttamente con segnali digitali, così facendo muovere i nucleo in **una direzione** se alimentato, invece **in una posizione morta** quando non alimentato.
Questo produce un'uscita di posizione binaria, tipicamente usata per pilotare elettrovalvole di tipo on-off. 

## ALTOPARLANTI
Un attuatore elettroacustico **converte un segnale elettrico** in un'**onda sonora (pressione) corrispondente**. 
Il più utilizzato è l'altoparlante dinamico, un **segnale AC viene applicato ad una bobina** sospesa in uno spazio sospeso tra i poli di un magnete, la **bobina eccitata** dal segnale **genera un campo magnetico** che **interagisce con quello del magnete**, così da far muovere la bobina seguendo la forma del segnale AC, dove alla bobina è fissata una diaframma di forma conica, e questo genera suono facendo vibrare l'aria creando onde di pressione.

![[Pasted image 20260323233007.png]]

Questo tipo di altiparlanti non sono efficienti dal punto di vista energetico, per questo sono accompagnati da un amplificatore audio così da poter pilotare efficaciemente l'altoparlente, però questo tipo di altoparlati per riprodurre al meglio il suono il diaframma deve essere il più largo possibile, per questo non si possono utilizzare per smartphone, in questo caso si utilizzano i MEMS.

## MEMS/PIEZOELETTRICI
I materiali piezoelettrici sono comunemente usati per **realizzare membrane di dimensioni miniaturizzate** che possono essere usate in altoparlanti e attuatori di pressione compatti e potenti. 

L'attuatore piezoelettrico funziona come la sua controparte sensore, poiché l'effetto piezoelettrico è reversibile, per questo si utilizza l'**effetto dei materiali peiezoelettroci** per generare le onde di pressione.
l movimento meccanico iniziale viene creato **applicando una tensione** a un materiale piezoelettrico e la **vibrazione di quest'ultimo** viene tipicamente convertita in fluttuazioni più ampie utilizzando diaframmi e risonatori.

Questo tipo di attuatori se messi in coppia con dei sensori piezoelettrici possono essere utilizzati per fare **l'ecografia**, essendo che gli attuatori propagano nel corpo onde ultrasoniche nel corpo, queste onde possono essere captate da dei sensori piezoelettrici che grazie al **ritardo tra onde ricevute e trasmesse** rende possibile la ricostruzione della forma dei tessuti interni del corpo umano.

Il principale vantaggio di questo approccio è la possibilità di **eliminare i grandi diaframmi**, rendendo possibile la realizzazione di **dispositivi compatti**. È possibile costruire dispositivi piezoelettrici con una gamma dinamica molto ampia, risultando in altoparlanti tascabili piccoli, potenti e affidabili, questi possono essere cotruiti tramite tecnologie MEMS e questo permette di ridurre i costi di produzione, maggiore affidabilità e controllo.

## PONTE H
Circuito impiegato per l'utilizzo di specifici tipi di attuatori, i quali sono **motori DC, ecc...**
È un circuito che permette di controllare un motore DC, che consente di impostare:
- **ROTAZIONE ORARIA**
- **ROTAZIONE ANTIORARIA**
- **CORSA LIBERA** 
- **FRENATURA**

Il circuito composta da una **sorgente di tensione DC**, e **4 interruttori**, che se configurati opportunamente consentono di comandare il motore.

![[Pasted image 20260324000754.png]]
In particolare, **se gli interruttori S1 e S4 sono chiusi con S2 e S3 aperti**, la tensione DC in ingresso, $V_{in}$, cadrà ai capi del motore così da farlo **girare in una certa direzione**, mentre la velocità di rotaziona sarà data dal valore di $V_{in}$.
Al contrario, **se gli interruttori S1 e S4 sono aperti con S2 e S3 chiusi**, la tensione DC in ingresso, $V_{in}$, cadrà sul motore con polarità opposta rispetto al caso precedente, il che metterà il motore DC in r**otazione nella direzione opposta**.
Se gli interruttori **S2 e S4 sono chiusi, con S1 e S3 aperti**, i terminali del motore sono cortocircuitati e non c'è caduta di tensione su di essi. Pertanto, **il motore frena**.
Infine, se **tutti gli interruttori sono aperti**, il motore è flottante e non può fluire corrente attraverso di esso, il che **metterà il motore in marcia libera**.

Questo sono tutte le possibili combinazioni che si possono **utilizzare** su questo tipo di circuito, poichè ogni altra combinazione comporterebbe un malfunzionamento o danneggiamento di interruttori e motore.

Nei circuiti a ponte H reali, gli interruttori sono tipicamente implementati per mezzo di **MOSFET o BJT**, per prevenire rischi di picchi di tensione assieme ai transistor si accoppiano dei **diodi di antiricircolo**.

## PWM
Tecnica utilizzata per modulare la **potenza erogata** agli attuatori,creando un'onda quadra con un duty cycle controllato.
Questa tecnica risolve parecchi problemi,tra i quali c'è il controllo della potenza media erogata ad un carico(attuatore) quando si utilizzano transistor o interruttori.
Può essere effettutato sia con **BJT** sia con **MOSFET**.

Il circuito che permette di utilizzare questa tecnica è formata da 3 parti:
- **GENERATORE DI TENSIONE A RAMPA**
- **COMPARATORE**
- INTERRUTTORE
Anche se il circuito effettivo comprende solo **generatore**, e **comparatore**, l'uscita di questo circuito sarà l'onda quadra con duty cycle controllato.

Il generatore di tensione varia la tensione partendo da una valore $V_{min}$ fino ad un valore $V_{max}$ tornando bruscamente al valore iniziale, il tempo che il generatore impiegherà per passare tra i 2 valori sarà il periodo dell'onda quadra, questa tensione verrà **comparata** con un'altra tensione $V_{control}$, compresa tra i 2 valori, che **determinerà** il **duty cycle** della dell'onda quadra.
Di fatto il valore del duty D cycle sarà:
$$
D = \frac{V_{control}-V_{min}}{V_{max}-V_{min}}
$$
Però se $V_{min} = 0$ sarà:
$$
D=\frac{V_{control}}{V_{max}}
$$
![[Pasted image 20260324230220.png]]

Per avere un certo D, $V_{control}$ deve essere:
$$
V_{control} = D(V_{max}-V_{min})+V_{min}
$$
Se $V_{min} = 0$:
$$
V_{control} = DV_{max}
$$
Il transitro varierà tra 2 stati **on**, e **off**, quando il transitor è in stato off la potenza dissipata sul carico(resistenza) sarà pari a 0.
Invece se sarà in stato di **on** la potenza dissipata sul carico sarà $P_{on} = \frac{V_{s}}{R}$, dove $V_s^2$ è la tensione di alimentazione dell'attuatore.
E la potenza media sarà:
$$
P_{avg} = DP_{on} + (1-D)P_{off} = D\frac{V_{s}^2}{R}
$$
Questa tecnica pur essendo molto efficacie, permette il controllo solo sulla potenza media e non sulla potenza immediata.

Questa tecnica permette di generare onde di forma arbitraria.

# CIRCUITI DI ALIMENTAZIONE
La maggior parte dei circuiti **necessita** infatti di una **tensione continua stabile** per funzionare correttamente, dalla quale traggono l'energia necessaria per il funzionamento.

Tipicamente una sorgente di tensione possono essere:
- **BATTERIE**: Sorgente di tensione quasi continua a meno che non inizino a scaricarsi in mdoo significativo
- **Tensione alternata**: che prima deve essere **convertita in una tensione** quasi **continua** tramite trasformatori e raddrizzatori, questa tipologia di tensione può essere fonrita dalla rete elettrica.


In ogni caso la tensione deve prima essere elaborata tramite circuiti **DC-DC Converter**, che prendono in ingresso tensioni quasi continue e hanno come uscita una tensione **completamente continua**.
L'obiettivo dei convertitori DC-DC è infatti quello di produrre alla loro uscita una tensione continua della grandezza desiderata e caratterizzata da alcune proprietà utili, come:
- Indipendenza del livello di tensione continua di uscita dal carico
- Indipendenza del livello di tensione di uscita DC rispetto al livello di tensione di ingresso DC
- basso livello di disturbo e/o fluttuazioni in uscita 

Per produrre un DC-DC si potrebbe utilizzare un partitore di tensione.
![[Pasted image 20260324235300.png]]

Ma non andrebbe beno poiché tutte le **variazioni e i disturbi** presenti in ingresso si **riflettono linearmente in uscita**, poiché la tensione di uscita è semplicemente proporzionale alla tensione di ingresso.

## CONVERTITORI LINEARI
Questo tipo di convertitore utilizza la stessa base di un partitorre di tensione, ma al posto delle resistenza $R_{2}$ utilizza un **diodo zener**(diodo utilizzato per lavorare nella zone di breakdown).
![[Pasted image 20260325000027.png]]

Questo diodo può lavorare anche con tensioni negative poiché più resistente di altri diodi, e grazie alla sua area di lavoro, **regione Zener**, dove il rapporto tra tensione e corrente diventa molto ripido, per questo per un'ampio intervallo di corrente la tensione è costante, questa tensione viene chiamata **tensione Zener**$V_z$, ogni tipologia di diodo Zener può avere questa tensione differente.
Esistono anche 2 valori di corrente $I_{Zmin}$ e $I_{Zmax}$ perchè:
- Con corrente minore di $I_{Zmin}$, la regione di lavoro **non è quella di Zener**, ma quella di polarizzazione inversa, questa comporta ad una **grande variazione di tensione in basa alla corrente in input.**
- Se la corrente è maggiore a $I_{Zmax}$, questo comporta ad una dissipazione di corrente eccessiva, e può portare ad un **danno permanente**.

**[[ESEMPI CIRCUITI#ES. Diodo zener|Esempi diodo Zener]]**

Se si varia il valore del carico, varierà di conseguenza anche il valore della corrente che attraverserà il diodo, se la corrente sarà **troppo grande** causerà un danno permanente al diodo, invece se sarà **troppo piccola** il diodo non sarà polarizzato nella regine Zener, però si può evitare introducendo un amplificatore di corrente, il quale in base alla corrente in entrata erogherà una **corrente multiplo più grande**, questo significa che per una data **corrente in uscita**, la **corrente in entrata arà molto inferiore**, questo comporta che a seguito di grandi variazioni di carico, che causerà piccole variazioni di corrente.
L'implementazione reale avviene tramite un transistor bipolare a giunzione.
![[Pasted image 20260326002739.png]]

### REGOLATORI FISSI
I regolatori fissi sono un esempio commerciale di regolatori lineari. Sono circuiti integrati a 3 **terminali**, e sono caratterizzati da una **tensione di uscita fissa**.
I 3 terminali sono:
- **Ingresso**
- **Massa**
- **Uscita**
Una serie commerciale di successo è la cosiddetta 78xx, dove xx sono due cifre che possono variare e simboleggiano il valore della tensione di uscita.
Ogni componente ha anche un dato **dropout**, che si riflette nella tensione di ingresso minima esplicitamente riportata nella scheda tecnica del componente.
La circuiteria interna funzionerà in modo tale da **mantenere fissa e stabile** la differenza di **tensione tra il terminale di uscita e il terminale “gnd”**. 

![[Pasted image 20260326003541.png]]

### REGOLATORI VARIABILI/REGOLABILI
I regolatori variabili (o regolabili) sono molto simili ai regolatori fissi, ma mostrano una notevole differenza. Il secondo terminale **adjust** al posto di **GND** non deve essere necessariamente connessa a massa, il regolatore variabile lavora per mantenere fissa la differenza di tensione tra il terminale di uscita e il terminale di “adjust”.
Tuttavia, la possibilità di collegare il terminale “adjust” a **punti del circuito non a 0 V** apre interessanti prospettive, come la possibilità di **regolare il valore della tensione di uscita**, da cui il nome regolatore regolabile.
![[Pasted image 20260326205802.png]]

Ad esempio, l'LM317 **sviluppa e mantiene una differenza nominale di 1,25 V** tra la sua uscita e il terminale di "adjust". Con riferimento allo schema elettrico sopra, questa tensione viene convertita in una corrente da R1, e questa corrente costante scorre anche attraverso R2 verso massa, dove la corrente erogata dal regolatore sarà $I_{adj}=100 \micro A$
$$
\begin{aligned}
I_{1}=\frac{1.25V}{R_{1}}\\
V_{out}=(I_{1}+I_{adj})R_{2}+1.25V\\
V_{out}=1.25V\left( 1+\frac{R_{2}}{R_{1}} \right)+I_{adj}R_{2}
\end{aligned}
$$
## CONVERITORI A COMMUTAZIONE/SWITCHNG
Un convertitore DC-DC a commutazione agisce immagazzinando periodicamente l'energia in ingresso e quindi rilasciandola all'uscita a una tensione diversa.
L'energia viene immagazzinata in un campo magnetico(**induttore/trasformatore**) o in un campo elettrico(**conensatore**).
Questo tipo di convertitori offrono 2 vantaggi:
- Efficienza della **conversione di potenza** è **molto elevata**
- L'energia che viene immagazzinata da un induttore, può esser trasformata in tensione di uscita **maggiore o minore** a quella d'ingresso.
Però presentano anche svantaggi come:
- Sono molto più **rumorosi**
- Richiedono una gestione da parte di un **circuito di controllo**
In sostanza, un convertitore DC-DC a commutazione utilizza un interruttore, un induttore, un diodo e un condensatore per trasferire l'energia dall'ingresso all'uscita, e possono essere organizzati in vari modi.

### BUCK
Il convertitore buck (o step-down) è un regolatore a commutazione caratterizzato dal fatto che la **tensione di uscita può essere regolata** ma sarà **sempre inferiore alla tensione di ingresso.**
È composto da:
- **INTERRUTTORE**
- **INDUTTORE**
- **DIODO**
- **CONDENSATORE**
![[Pasted image 20260326213504.png]]

I convertitori buck sono semplici, robusti e molto efficienti, in quanto quasi tutta l'energia disponibile in ingresso viene trasferita all'uscita.
Tuttavia, sono meno precisi e più rumorosi dei regolatori lineari. Inoltre, fanno uso di un induttore ingombrante.

Il principio di funzionamento del circuito si basa sulla **commutazione periodica dell'interruttore** tra gli stati di accensione e spegnimento. L'interruttore è quindi pilotato da un segnale periodico, ovvero un'onda quadra con periodo T e duty cycle D.
$T = \frac{1}{f} = T_{on}+T_{off}$, $D=\frac{T_{on}}{T}$.

Quando l'interruttore è in stato di ON, il diodo in questo caso si comporterà come circuito aperto, essendo **polarizzato inversamente**.
![[Pasted image 20260326214521.png]]

La caduta di tensione sull'induttore sarà $V_{L}=V_{in}-V_{out}$ o  $V_{L}=\frac{dl_{L}}{dt}$
Essendo che $V_{L}$ è costante, la corrente dell'induttore $I_{L}$ aumenterà in modo lineare.
L'aumento della corrente nell'induttore durante il periodo di accensione può essere calcolato **integrando l'equazione** di cui sopra nel tempo da t = 0 fino a $t = T_{on} = D_{T}$:
$$
\Delta I_{L,on}=\int^{T_{on}}_{0} \frac{V_{L}}{L}dt=\frac{V_{in}-V_{out}}{L}T_{on}=\frac{V_{in}-V_{out}}{L}DT
$$
Nello stato di OFF, la parte sinistra del circuito sarà isolata, la corrente scorre attraverso l'induttore scorrerà tra la **resistenza(carico) e il condensatore**, ricircolando la corrente attraverso il diodo che in questo caso essendo acceso si comporta come un cortocircuito, mettendo la tensione $V_{in}=0$
![[Pasted image 20260326221518.png]]
La tensione ai capi dell'indutore sarà $V_{L}=0-V_{out}$, o $V_{L}=L \frac{dl_{L}}{dt}$

La tensione ai capi dell'induttore sarà negativa, questo comporta ad una diminuzione lineare della corrente all'interno dell'induttore.
La diminuzione della corrente nell'induttore durante il periodo di spegnimento può essere calcolata integrando l'equazione sopra da $t = T_{on} = DT \space fino\space a\space t = T_{on} + T_{off} = T$:
$$
\Delta I_{L,off}=\int_{T_{on}}^{T_{on}+T_{off}} \frac{V_{L}}{L}dt=-\frac{V_{out}}{L}T_{off}=-\frac{V_{out}}{L}(1-D)T
$$
Durante il periodo di commutazione T, la corrente nell'induttore **aumenterà** se l'interruttore è in stato di ON, invece se in stato di OFF la corrente all'interno dell'interruttore **diminuerà**, partendo da un valore $I_{min}$.
Se supponiamo che durante lo stato di OFF la corrente dell'induttore scenda al valore $I_{min}$, ciò significa che alla fine del periodo $T_{off}$, porterà il valore della corrente $I_{min}$.
$$
\Delta I_{L,on}+I_{L,off}=0 \to \frac{V_{in}-V_{out}}{L}DT=\frac{V_{out}}{L}(1-D)T
\to D=\frac{V_{out}}{V_{in}}
$$
Il valore della tensione di uscita, sarà regolata dal **duty cycle D**, che sara compreso tra 1 e 0, però è sensibile alla variazione della tensione d'ingresso, per evitare che la tensione di uscita vari, si implementa un circuito di controllo che **misurando la tensione di uscita** riesca a controllare il duty cycle così che **la tensione di sucita rimanga costante**.

Esempio del comportamento:
![[Pasted image 20260326225751.png]]

Avendo la **tensione sul carico costante**, anche la **corrente sarà costante**, ma però attraverso all'induttore la corrente che fluirà è variabile, per questo la corrente che passa attraverso il carico sarà composta dalla **media temporale**, e le **deviazioni da essa**, che possoo essere **negative**(Il carico richiede più corrente di quanto l'induttore possa fornire, e quindi il **condensatore** ne fornirà il rimante scaricandosi), e **positive**(Il carico richiede meno corrente di quanto gli serva, per questo il resto della corrente verrà immagazzinata nel condensatore).

Per permettere che il condensatore si carichi o scarichi, ai suoi capi ci deve essere una **variazione di tensione**, per questo anche la tensione di uscita non sarà perfettamente lineare ma avrà delle ondulazioni.
Per ridurre le ondulazione(**ripple**), la capacità del condensatore viene scelta sufficientemente grande, poiché una capacità maggiore implica minori variazioni di tensione per la stessa corrente, oppure si può aumentare la frequenza di commutazione, così da dare **meno tempo** al condensatore di caricarsi e scaricarsi, però questo può causare un disturbo causato dall'interruttore.

Questo viene confermato solo se $I_{min}>0$, questo non viene soddisfatta quando il la resistenza di carico è piccola, questo comporta d una corrente $I_{min}$ più piccola, diminuendola fino a 0. La corrente presenta nello stato di OFF sarà calcolata in modo differente:
$$
\Delta I_{Loff}=\int_{T_{on}}^{T_{on}+\delta T} \frac{V_{L}}{L}dt
$$
dove $\delta T$ è il **tempo effettivo di scarica dell'induttore**.

Questo regolatore ha 2 modalità di funzione:
- **CONTINUA**: Il carico è abbastanza grande, così da non avere mai un valore di $I_{min}=0$.
- **DISCONTINUA**: Il carico è così piccolo che diminuirà anche la corrente $I_{min}$ fino a 0.

Questo regolatore avrebbe idealmente un'efficienza del 100%, ma nella realta l'efficienza diminuisce grazie a:
- La caduta di tensione diversa da zero sul diodo durante lo stato acceso (ridotta utilizzando il diodo Schottky)
- La resistenza diversa da zero dell'interruttore nello stato acceso (è necessario un interruttore a bassa resistenza)
- La dissipazione di potenza diversa da zero nell'interruttore alle transizioni off/on e on/off (maggiore per alte frequenze)
- La resistenza in serie del condensatore e dell'induttore

![[Pasted image 20260326235906.png]]

### BOOST
È il circuito gemllo del convertitore Buck, ma la differenza principale rispetto al convertitore Buck è che il Boost realizza una **conversione step-up**, il che significa che la **tensione di uscita**sarà **sempre maggiore della tensione di ingresso**.
Anche questo avrà un'efficienza del 90%, ma la potenza in uscitaal massimo uguale a quella di input.
Questo è il circuito:
![[Pasted image 20260327000513.png]]

Se la tensione di ingresso e uscita sono DC positive, il circuito è in stato di ON, il **condensatore e il carico saranno scollegati dall'input**, e invece l'induttore l'unico componente collegato alla tensione d'ingresso, il quale si caricherà, nel mentre la corrente al carico sarà **completamente fornita** dal condensatore, dove $V_{L}=V_{in}$.
![[Pasted image 20260327001408.png]]
La corrente nell'induttore aumenta linearmente:
$$
\Delta I_{Lon}=\int_{0}^{T_{on}} \frac{V_{L}}{L}dt= \frac{V_{in}}{L}T_{on}=\frac{V_{in}}{L}DT
$$
Quando l'interruttore è aperto(STATO DI OFF) il diodo è **polarzzato direttamente** e si comporta come un ortocircuito, così avendo una tensione negativa.
![[Pasted image 20260329223504.png]]
La corrente nell'induttore diminuerà linearmente:
$$
\Delta I_{Loff}=\int^{T_{on}+T_{off}}_{T_{on}} \frac{V_{in}-V_{out}}{L}dt= \frac{V_{in}-V_{off}}{L}T_{off}=\frac{V_{in}-V_{off}}{L}(1-D)T
$$
In stato stazionario sarà:
$$
\Delta I_{Lon}+\Delta I_{Loff}=0 \to \frac{V_{in}}{L}DT+\frac{V_{in}-V_{off}}{L}(1-D)T=0\to \frac{V_{out}}{V_{in}}= \frac{1}{1-D}
$$

Da questa equazione si capisce che la **relazione** tra la tensione di uscita e di entrata, è **regolata solo da D**. Se l'entrata è DC anche l'uscita sarà DC.

Schema che rappresenta il comportamento del convertitore:
![[Pasted image 20260329225115.png]]

La corrente corrente che fluisce attraverso il carico, in stato ON, è **interamente erogata** dal condensatore, portandolo a scaricaricarsi causando un **ripple**.
Durante lo stato spento, la corrente nell'induttore (che è uguale a quella nel diodo) è probabilmente maggiore di quella richiesta dal carico, il restante caricherà il diodo, pian piano che la corrente dell'induttorre diminuirà, non riuscirà a fornire la **corrente necessaria** al carico, il resto verrà fornita dal condensatore.

# CONVERTITORE A/D-D/A
Lo scopo dei convertitori analogici digitali, è **tradurre** ==**segnali analogici in una rappresentazione digitale**==.
Questa rappresentazione digitale può essere elaboratada un HW digitale.

Tipi di segnale:
- **SEGNALE ANALOGICO**:
	È un segnale continua da **valori reali** cioè continuo sul suo dominio, e ogni valore ad un preciso istante è **un valore reale**(numero infinito di cifre per rappresentarlo).

- **SEGNALE DIGITALE**:
	È un segnale discreta a **valore binario**, ad ogni dato istante il segnale può uno di 2 valori possibili, ciò significa che è **discreto** nel suo dominio, questo significa che il suo valore può essere rappresentato con uno specifico numero di cifre.

Per poter convertire un segnale analogico in uno digitale, bisogna, per prima cosa, prendere, per ogni **istante di tempo preciso**, il valore del segnale analogico scartando tutto ciò che si trova in mezzo.
Ogni valore preso deve essere convertito da un **valore reale**, ad un valore codificato in **base 2**.
Questo avviene tramite 3 specifiche operazioni, le quali sono **campionamento, quantizzazione e codifica**.
Un punto cruciale di questa conversione è mantenere inalterate le informazioni, significa mantenere **le stesse informazioni** durante tutti i processi della conversione, così da permettere anche la conversione contraria(digitale->analogico), avendo un **segnale identico a quallo originario**.

## CAMPIONAMENTO
Il processo di **campionamento** è il primo passo della conversione da analogico digitale, e il suo scopo è quello di **scattare istantanee**.
L'output di questo processo, sarà un segnale che è definito solo in istanti prederminati, mantenendo solo **i valori** in qui istanti.

Il segnele di campionamento può essere immaginato, come un'impulso di durata 0, chiamati **campioni**, questi rappresenteranno l'ampiezza del segnale in quell'istante. Questo segnale **non è continuo**, ma rimane a valore reale, con un **intervallo** da un campione e l'altro.
La durata dell'intervallo si chiama **periodo di campionamento**, e la **frequenza di campionamento** è data dal reciproco del periodo.

Immagine che rappresenta un segnale analogico convertito in uno campionato, con un periodo di campionamento T:
![[Pasted image 20260329235012.png]]

Più il perido di **campionamento è minore**, più il **segnale campionato sarà simile al segnale analogico di partenza.**
Il segnale di campionamento è un insieme di delta di Dirac.
Tuttavia, nei circuiti reali non è possibile produrre un segnale campionato ideale come quelli mostrati nella figura sopra perché:
- Impossibile produrre una **delta di Dirac a durata nulla**
- La **durata della misura non può essere 0** poichè impossibile
- La distanza di tempo tra un campionamento è l'altro non può mai essere un **perfetto multiplo di T**, ma solo molto simile.

### ALIASING/TEOREMA DI SHANNON-NYQUIST
Per capire al meglio il fenomeno di **alising**, non bisogna prendere in cosniderazione un segnale nel dominio del tempo, che viene campionato ad una data frequanza nel tempo come:
![[Pasted image 20260401180710.png]]

ma considerare invece il dominio della frequenza, cioè usando lo **spettro a doppio lato** del segnale in entrata, e campionato in base allo spettro del **treno di delta di Dirac**(Delta di Dirac che sono equidistanti con valore la frequenza di campionamento, e come ampiezza il valore sarà $\frac{1}{T}$), che grazie ad una convoluzione si ottiene il segnale campionato nel dominio della frequenza, ciò significa che lo **spettro del segnale campionato** sarà dato dallo spettro del segnale analogico sovrapposto a copie centrate dalla frequenza di campionamento.![[Pasted image 20260401202700.png]]

Il **terorema di SHANNON-NYQUIST**, ha come condizione iniziale che la **frequenza di campionamente** deve essere maggiore di 2 volte la larghezza di banda del segnale analogico oppure, deve avere la frequenza di Nyquist($F_{n}=\frac{f_{s}}{2}$dove $F_{s}$ è la frequenza di campionamento) deve essere maggiore alla larghezza di banda del segnale analogico $F_{n} > F_{0}$, in questa condizione il campionamento avverrà **correttamente.**

Quando questa condizione non viene soddisfatta, si presenta il **fenomeno di aliasing**, questo comporta una **sovrapposizione tra le curve adiacenti**, anche se permette comunque il campionamento, questo fenomeno non permette di ricreare il seganle analogico originale, come rappresentato nella seguente immagine:
![[Pasted image 20260401202700.png]]

Per prevenire che questo succeda nei circuti reali, che il segnale sia limitato in banda, e che la sua larghezza di banda soddisfi il teorema, sapendo qual'è la frequanza di campionamento è possibile introdurre un **filtro anti-aliasing**, che sarebbe un filtro passa-basso che posto prima di un circuito, così da limitarne la larghezza di banda e soddisfare così il teorema.
Questo però non elimina le frequenza, le attenua soltanto, causando sempre un minimo di aliasing, per questo solitamente la frequenza di campionamento è presa dalle 5 a 10 volte maggiore alla larghezza di banda.

## QUANTIZZAZIONE
Dopo che il segnale è stato correttamente campionato, quidni il segnale sarà una **rappresentazione discreta** ma con **valori reali**, ora bisogna definire la precisione con cui ogni valore reale, è definito con un numero finito di cifre binarie.
![[Pasted image 20260401204949.png]]

Il processo di quantizzazione agisce su ogni campione, di un segnale campionato, e permette di **sostituire** il valore reale del campione, in valore preso da un insieme di N valori discreti che possono essere scritti con precisione definita.
Per identificare l'insieme dei valori discreti Q:
$$
Q=\frac{V_{max}-V_{min}}{N}
$$
La differenza tra il segnale campionato e quello quantizzato è chiamato errore di quantizzazione, che può essere positivo o negativo ma sempre compreso tra $\frac{–Q}{2}$ e $\frac{Q}{2}$, questo 
conferma anche che più N è maggiore più la precisione la quantizzazione sarà accuarata.

## CODIFICA
Ultima parte del processo di conversione A/D.
Eseguita per **rappresentare** ogni campione del segnale quantizzato, in formato binario, da una stringa di M bit. $M=[\log_{2}N]$
In base ad ogni $\Delta$(range) di tensione, viene assegnato un numero in codice binario, di M bit di lunghezza.
Più la stringa di bit è lunga, l'errore di quantizzazione sarà sempre minore.

## CIRCUITO DI CAMPIONAMENTO
Per implementare un circuito di coversione A/D, deve essere composto da **2 blocchi consecutivi**, dove il primo si occuperà del campionamento e il secondo si occuperà della quantizzazione e della codifica.

Questo circuito funziano in 2 aree temporali, dove la **somma non deve superare il perido di campionamento**, nella prima area(fase) **funzionerà soltanto il circuito di campionamento** mentre quello dicampionamento non sarà operativo, nella seconda fase, alla fine della prima fase, invece il circuito di campionamento rimarrà stabile per ogni variazione del segnale logico, così lavorerà **soltanto il circuito di quantizzazione**, questo scambio di fasi deve essere eseguito ogni multiplo del periodo di campionamento, per questo è necessario un segnale di temporizzazione, **un clock**.

Il primo circuito di questo tipo è il **SAMPLE & HOLD**, questo tramite un interruttore comandato dal clock, permette di entrare in 2 fasi, le quali sono:
- **SAMPLE**(campionamento)
	Durante questa fase l'interruttore sarà in **stato ON**, nel mentre la tensione ai capi del condensatore sarà la stessa di quella in entrata così da potersi caricare, 
- **HOLD**(quantizzazione)
	Durante questa fase l'interruttore è in **ststo OFF**, il condensatore sarà scollegato dalla prima parte del circuito, questo permetterà al condensatore di mantenere la tensione costante al livello di quella del momento prima che l'interruttore cambi di stato, cioè manterrà la **tensione di campionamento**.
![[Pasted image 20260409225236.png]]

## CIRCUITI ADC
Nome per riferirsi a circuiti di quantizzazione che verranno pilotati dallo stesso clock utilizzato dal campionatore.

### FLASH ADC
$$
V_{th}^i = V_{min} + i \frac{V_{max}-V_{min}}{2^n}
$$
Qusta formula rappresenta le **tensione di soglia per una quantizzazione a n bit**.
Quindi per sapere a quale soglia appartiene la tensione d'ingresso, si può confrontare con le varie tensione di soglia tramite dei **comparatori**.

Il circuito sarà composto da $2^n$ resistori collegati in serie collegati a 2 sorgenti di tensione rispettivamente $V_{min}\space e\space V_{max}$ , e $2^{n}-1$ comparatori dove la **tensione d'ingresso** viene collegata al proprio **ingresso non invertente**, e una **soglia specifica** al suo **ingresso invertente**.
![[Pasted image 20260409234033.png]]

Analizzando l'uscita di ogni comparatore si può vedere che per ogni **tensione di soglia che viene superata** dalla tensione d'ingresso **tutti i comparatpri precedenti avranno come uscita 1**, invece tutti quelli **dopo** avranno **uscita pari a 0**, però questa non è una rappresentazione binaria, per questo ci serve un **priority encoder**.

Questo circuiti per questo tipo di lavoro è uno dei più veloci, così da poter utilizzare frequenze di campionamento molto più elevate, ma non può essere utilizzato per rappresentazione a **tanti bit**,  poichè per ogni bit aggiuntivo il **numero di comparatori** viene **quasi raddoppiato**, invece i **resistori** vengono **esattamente raddoppiati**, rendendo così il circuito molto più costoso.

### ADC ad Approssimazioni Successive
Quando si tratta di frequenza di campionamento minori a 10MHz, l'ADC più utilizzato è quello ad **approssimazioni successive(SAR)**, ideale per applicazioni con una precisione tra 8-16 bit.

Il circuito è formato da:
- un **COMPARATORE**
- un **SAR** (registro ad approssimazioni successive)
- un **DAC** (convertitore da digitale ad analogico):
	Da una parola digitale in input riproduce un segnale DC che rappresenta l'input.
	Questo segnale sarà nel range tra lo 0(**GND**) e la **tensione di alimentazione**($V_{dd}$).
	Il segnale in uscita sarà proporzionale in base al **numero digitale** che rieceve in ingresso, compreso tra 0 e $V_{dd}$
- un **Buffer ad uscita digitale**

![[Pasted image 20260414234941.png]]

Il funzioneamento dell'ADC SAR si basa sul fatto di **indovinare** quale potrebbe essere la **parola di uscita digitale**, poi convertendo questa parola in una tensione DC analogica con quella di input così da poter modificare la parola scelta da noi in base al risultato della comparazione, ripetendo questo processo fino al risultato finale.

Questo può funzionare se il SAR riceve in input un segnale di clock **molto più veloce** di quello di campionamento, e l'uscita del comparatore.
Il SAR all'inizio del processo imposterà il bit **più significativo** ad 1 mentre tutti gli altri a 0, questa parola verrà data al DAC il quale la passerà al comparatore, che in base al risultato comunicherà al SAR di modificare in un certo modo la parola, nel caso il segnale di input sia **maggiore** della parola il SAR manterrà il bit ad 1, invece se il segnale di input è **minore** il SAR imposterà il bit a 0, questo processo poi verrà replicato per tutti i bit della parola, fino a rovare quella che rappresenta il segnale di input.

![[Pasted image 20260415001814.png]]

### ADC SIGMA-DELTA
Questi convertitori si basano su un'architettura che comprende:
- **AMP-OP**
- **INTEGRATORE**
- **COMPARATORE**
- **DAC** ad 1 bit (configurazione feedback)
Questo convertitore offre il vantaggio di utilizzare componenti economici a bassa precisione, che però permettono un output ad **alta risoluzione**, attenuando anche il rumore.
![[Pasted image 20260415002445.png]]

## DAC
Sono convertitori Digitale-Analogico, anche detti DAC.
Questo riceve in input **n segnali** che rappresentano i bit di una parola digitale, e lo converte in un **segnale analogico** costante.
I tipi di DAC che utilizzeremo saranno i:
- **DAC R-2R Ladder**
- **DAC ad approssimazioni successive**
- **DAC Sigma-Delta**

Per capire quale DAC utilizzare bisogna prendere in considerazione:
- **Risoluzione**
	Comprende il numero di bit in input, questo è anche correlato al numero possibile di livelli in uscita.
- **Frequenza di campionamento massima**
	La velocità massima alla quale il DAC può accettare nuovi dati e comportarsi correttamente.
- **Monotonicità**
	Capacità del segnale analogico di output di muoversi solo nella direzione comandata dalla parola digitale.
- **THD**
	Misurano la distorsione e il rumore introdotti dal DAC.
- **Range dinamico**
	La differenza tra il segnale più grande e quello più piccolo che il DAC può leggere e riprodurre, espressa in decibel.
- **Consumo di energia**

### DAC R-2R
L'idea di un DAC R-2R è quella di impiegare un **circuito** in grado di **generare una corrente**, il cui valore è **proporzionale al numero rappresentato dal valore dell'ingresso digitale**, per poi convertire la corrente in tensione tramite un amplificatore.

Questo circuito viene diviso in 2 blocchi:
- Il primo agisce come generatore di corrente controllato digitalemente
- Il secondo converte la corrente in tensione con un amplificatore apposito

![[Pasted image 20260415185951.png]]

La corrente generata da una parola digitale di ingresso arbitraria è la somma delle correnti generate dai singoli bit. Possiamo estrarre da questi risultati una relazione più generale, valida per il caso generale di una parola di ingresso a n bit.
$$
I_{tot}=\sum^N_{n=1} \frac{V_{ref}}{2^n*R}*D_{n} = \frac{V_{ref}}{R}\sum^N_{n=1} \frac{D_{n}}{2^n}
$$
dove N è il **numero totale dei bit**, $D_{n}$ rappresenta il valore dell'entrata.

L'uscita generata da è proporzionale al valore numerico della parola digitale, e può variare da **0** fino a $V_{ref}$.

Gli svantaggi di questo DAC sono che la sua **precisione dipende dalla tolleranza dei resistori** che formano il circuito, ma anche dal **lavoro non ideale degli altri componenti**, questo comporta a discrepanze le quali portano a dei disturbi all'uscita 

Però questo circuito è anche molto veloce oltre che dipende dalla risoluzione, anche dal fatto che l'laborazione dei bit **avviene in parallelo**.

### DAC AD APPROSSIMAZIONE SUCCESSIVE
Concettualmente molto simile all'ADC, che avendo in **ingresso** una parola di **n bit in**
**parallelo**, la quale viene rappresentata da un'uscita analogica corrispondente.

Questo avviene grazie ad un **shift register PISO**, che trasforma la parola in parallelo in un flusso seriale di bit, partendo dal bit meno significativo.

In base al valore del bit che viene preso in considerazione, vengono **comandati 2 interruttori**, nel momento in cui il bit ha valore 1 l'**interruttore** su $V_{ref}$ sarà **acceso**, invece quello su, massa sarà aperto, **succede il contrario se il bit analizzato ha valore 0**.
Questa uscita viene fornita da un nodo sommatore che, fornirà questo segnale ad un circuito di campionamento.

![[Pasted image 20260417000418.png]]

In generale il segnale di output sarà dato da:
$$
V_{out}=V_{ref}\sum^{n-1}_{m=0} \frac{D_{m}}{2^{n-m}}=\frac{V_{ref}}{s^n}D
$$

Questo permette di evitare l'utilizzo di resistori ad alta precisione, basandosi principalmente su circuiti digitali, però essendo una soluzione **iterativa** questa sarà più lenta rispetto alla soluzione **R-2R**, però permette una risoluzione migliore.

### DAC SIGMA-DELTA
Fondamentalmente, è il **gemello dell’ADC sigma-delta**, segue gli stessi principi e condivide gli stessi vantaggi. Nello specifico, il **circuito è complesso** ma può essere **costruito** con **semplici componenti a bassa risoluzione.** Può **raggiungere** una **risoluzione equivalente molto elevata** adottando una frequenza di campionamento elevata e può vantare basso rumore.

![[Pasted image 20260419222804.png]]

## FILTRO DI RICOSTRUZIONE
Per effettura una buona converisone sia in un lato che nell'altro, in questi circuiti servono anche un **filtro anti-aliasing**, un **circuito di campionamento**(sample and hold) e un circuito di **quantizzazione**, se il teorema di Shannon-Nyquist è stato rispettato il segnale digitale sarà una rappresentazione, senza perdite di informazioni, del segnale analogico.

Nella conversione di una parola digitale in un segnale analogico, oltre ai DAC serve un altro componente, il quale permette una rappresentazione più fedele di un segnale anlogico, poichè l'uscita di un DAC **non sarà un'onda** ma un **segnale a gradini**, per avere una rappresentazione di tutte le variazioni nel tempo, serve un filtro passa-basso con la stessa frequenza del filtro anti-alising così da ottenere esattamente il segnale analogico originale.
![[Pasted image 20260419225710.png]]
Idealmente entrambi i filtri devono avere:
- Ritardo di fase costante in banda passante
- Risposta in frequenza piatta costante in banda passante
- Risposta nulla oltre la frequenza di Nyquist
Queste proprietà possono essere soddisfatte soltanto tramite, un filtro con risposta all'impulso si tipo **seno cardinale**. La funzione seno cardinale anche detta sinc, è data da $\frac{\sin(x)}{x}$, però un filtro con un funzione uguale è fisicamente **impossibile da costruire**, infatti i filtri di ricostruzione reali **lasciano passare** del segnale anche al di sopra della frequenza di Nyquist e attenua **alcune della banda passante**.

**GRAFICO SINC**
![[Pasted image 20260420221708.png]]

# WIRED PROTOCOL
Un protocollo è un insieme di regole che consente la **comunicazione tra 2 o più entità**.
Un protocollo definisce:
- **Regole**
- **Sintassi**
- **Sementica**
- **Sincronizzazione**
- **Metodi**
I protocolli possono essere hardware, software o una combinazione d'entrambi.
La maggior parte dei protocolli standard sono **pubblicati e regolamentati da comitati riconosciuti di esperti e associazioni di professionisti del settore**.

I protocolli devono specificare.
- **Formato dei dati**
	Riguarda la struttura della parola di bit dei messaggi digitali che vengono scambiati.
	La stringa di bit è divisa in due parti denominate **header** e **payload**. Il messaggio **vero** e proprio viene inserito nel **payload**. L'**header** (intestazione) contiene i **campi rilevanti per il funzionamento stesso del protocollo** e in genere fornisce informazioni accessorie.
- **Formato degli indirizzi**
	Utilizzati per identificare i destinatari previsti. Gli **indirizzi** vengono **riportati** all'interno degli **header**. 
	Spesso esistono indirizzi che hanno significati specifici, come indirizzi collettivi.
	Esistono anche diversi schemi d'indirizzamento, i quali sono:
	- **Unicast**: comunicazione 1 a 1
	- **Multicast**: comunicazioni da 1 a n specifici dispositivi
	- **Broadcast**: comunicazione da 1 a tutti i dispositive nella rete.
- **Rilevamento degli errori di comunicazione**
	Il rilevamento degli errori è **necessario** sulle reti in cui è **possibile** il **danneggiamento irreparabile dei dati**, anche se non tutti i protocolli offrono questa possibilità.
	Di solito questo controllo sugli errori viene calcolato sul payload tramite certi tipi di algoritmi, e viene aggiunto alla fine del pacchetto.
- **Riconoscimento di ricezione**
	Il riconoscimento della corretta ricezione dei pacchetti(ACKNOWLEDGEMENT), molto utile per verificare l'avvenuta trasmssione dei lati.
- **Direzione del flusso di informazioni**
	I protocolli possono essere classificati anche in base alla direzione del flusso d'informazione.
	Infatti esistono protocolli:
	- **Simplex**: Dove le informazioni viaggiano lungo un'unica direzione.
	- **Half duplex**: Canale che permette la trasmissione di dati in entrambe le direzioni, ma non contemporaneamente.
	- **Full duplex**: Le informazioni possono viaggiare in entrambe le direzioni contemporaneamente.
- **Controllo di sequenza**
	Nel caso di stringhe di bit troppo lunghe, devono essere mandate a più pezzi, questo però può portare alla perdita, ritardi o duplicati, di questi frammenti, così da far **cambiare ordine** ai pezzi di stringa inviati. Per capire se è successo uno di questi fenomeni si puù **contrassegnare il frammento** con un numero ordinale, per capire se il frammento è arrivato in rodine sbagliato, duplicato o se ne perso uno
- **Controllo di flusso**
	Necessario quando il mittente trasmette a velocità superiori alla velocità di **elaborazione del ricevitore**, e/o della velocità del canale trasmissivo.

## SPI (Serial Peripheral Interface)
È un'interfaccia di **comunicazione seriale sincrona**, tilizzata soprattutto per la comunicazione a breve distanza.

I dispositivi in SPI comunicano in **fullduplex**, utilizzanod un'architettura di tipo **master-slave**, dove la comunicazione avviene tra **un master** e **multipli slave**.
![[Pasted image 20260423222410.png]]

Il bus SPI  specifica quattro segnali logici che viaggiano su quattro fili:
- **SCLK**: Serial clock, da master a slave
- **MOSI**: Master Out Slave In, uscita dati dal master e ingresso slave 
- **MISO**: Maste In Slave Out, uscita dallo slave e ingresso master
- **SS**: Slave Select, spesso attivo nello stato logico basso, uscita del master, ingresso dello slave

SCLK è un segnale di clock, che viene portaato allo slave dal master, che **determina i tempi della comunicazione**.
SS invece può essere di 2 tipi:
- **attiva bassa**: aperta con segnale basso, 0 logico
- **attiva alta**: aperta con segnale alto, 1 logico

### FUNZIONAMENTO
La configurazione dei dispositivi, non devono essere fissi, ma **possono essere intercambibili**.
Nel caso dove lo slave non è utilizzato durante una comunicazione, lo slave sarà **scollegata elettricamente**, causando così un'alta impedenza.
![[Pasted image 20260423232436.png]]

Per iniziare la comunicazione, il master deve configurare il segnale di clock, utilizzando **una frequenza supportata anche dal slave**.
Il master per selezionare uno slave, forzerà uno 0 sulla line SS, **avviando una comunicazione**.

Una volta instaurata una connessione, ad ogni fronte di discesa avverrà una **trasmissione di un singolo bit** dal master allo slave sulla linea **MOSI**, allo **stesso tempo** un bit verrà trasmesso dallo slave al master sulla linea **MISO**, così avendo ad ogni ciclo di clock uno scambio di dati in full duplex.

Questa comunicazione avviene tra 2 registri a scorrimento, che grazie alle 2 linee di scambio di dati, sono collegati in una **topologia ad anello**, formando così un unico registro, dove il bit  viene shiftatp veros una direzione fino a raggiungere la dimensione massima del registro, per poi essere **spedito** verso l'altro dispositivo.
Al termine della comunicazione il master deseleziona lo slave, forzando un 1 sulla linea SS.
Questo però funziona su una rete formata soltanto da 2 dispositivi.

### SLAVES INDIPENDENTI
Per avere una configurazione di rete composta da puù dispositivi slaves, si può utilizzare una configurazione a **slaves indipendenti**, dove su ogni slaves è presente una linea SS, però il master potrà comunicare con un **unico slaves alla volta**.
![[Pasted image 20260425184301.png]]

### DAISY CHAIN
In questa configurazione tutti gli slaves sono **attivi contemporaneamente**.
In questo caso il MOSI del master è colegato al MOSI del primo slave, il MISO del primo slave viene collegato al MOSI del secondo, così via fino ad arrivare all'ultimo slave che collegerà il suo MISO al MISO del master.

In questo modo tutti i dispositivi insieme, formano un grande registro a scorrimento circolare, condividendo fra tutti gii stessi segnali di SCLK e  SS.
![[Pasted image 20260425185053.png]]

### CLOCK
Un' immagine che mostra il funzionamento di come avviene una comunicazione tra 2 dispositivi:
![[Pasted image 20260425192814.png]]

Da qui si può capire che in ogni istante fronte di discesa, avviene un trasferimento di dati in full duplex, però l'utente ha la possibilità di **impostare 2 valori**, i quali permettono con precisione di **trasferire o leggere** i dati sul bus.

Questi valore sono:
- **CPOL**: Polarità di clock
	Determina la Polarità del clock
- **CPHA**: Fase di clock
	determina la temporizzazione del clock, 
Quest'ultimi vengono impostati dal master, il primo valore (CPOL) con valore = 0, il clock sarà **inattivo** a livello logico 0, ma **attivo** a livello logico 1, questo significa il **fronte di salita precede quello di discesa**, invece con valore = 1il clock sarà inattivo a 1, e attivo a livello logico 0, questo signifca che il **fronte di discesa** **precede** il **fronte di salita**.
Invece per il secondo valore (CPHA) con valore = 0, i **dati verranno letti sul fronte di salta**, mntre sul **fronte di discesa** i dati verranno cambiati, invece per CPHA con valore = 1, il mittente **modifica i dati alla sua uscita** sul **fronte di salita**, mentre il ricevitore leggerà i dati sul **fronte di discesa**.

![[Pasted image 20260426231855.png]]

### REGISTRI SPI ed ERRORI
Per configurare un'interfaccia SPI, da 7 registri che ha SPI, 5 sono **pensati per la configurazione**, i quali sono:
![[Pasted image 20260427232934.png]]

- **CONTROL REGISTER**
	Il suo nome è S0SPCR è composto da 16 bit, numerati da 0 a 15, dove i primi 2 sono riservati, e avranno come valore 0, il quale non potrà essere cambiato.
	- Il **bit 2**, terzo bit, è chiamato **bit enable**, e spsecifica la quantità di bit da trasferire ad ogni ciclo di trasmissione dati, se è impostato a **0** invia e riceve **8 bit**, invece se impostato a **1** invia e riceve **16 bit**.
	- Il **bit 3** controlla il valore del **CPHA**, invece il **bit 4** controllo il **CPOL**.
	- Il **bit 5** è chiamato **master**, ed identifica se l'interfacia si deve comportare come un master, se impostato ad 1.
	- Il **bit 6** controlla la direzione d'invio della stringa di bit, cioè LSBF(prima il meno significativo) o MSBF(prima il più significativo).
	- Il **bit 7** si chiama **Interupt enable** e determina il comportamento dell'interfaccia SPI in caso di condizioni specifiche.
	- I **bit da 8 a 11** sono importanti solo quando Bit Enable è impostato su 1, nel caso ontrario specificano il numero di bit per ciclo di trasferimento, in questo modo:
	![[Pasted image 20260427235654.png]]
	Infine i **bit da 12 a 15** sono riservati.	
- **DATA REGISTER**
	L'S0SPDR è composto da un numero di bit **variabile da 8 a 16 bit**, a seconda delle impostazioni del Control Register.
	I dati da trasmettere devono essere scritti sull'S0SPDR prima del trasferimento e i dati ricevuti dopo il trasferimento possono essere letti da questo registro.
	![[Pasted image 20260428235319.png]]
	Una scrittura sul data register va direttamente a scrivere il registro a scorrimento interno, sovrascrivendone il contenuto evitando di scrivere sul data register durante uno scambio di dati.
	Ogni dato **ricevuto**, oltre che trovarsi **all'interno dello shift register**, si troverà all'interno di un **buffer di lettura**, che si interfaccia con il data register, che ogni volte che viene letto, **mostra i dati ricevuti**, la lettura di questo registro può essere effettuata anche durante una comunicazione, ogni dato che non viene letto durante un ciclo di trasferimento viene perso nel ciclo dopo, questo implica che i dati ricevuti prima se non letti saranno persi definitivamente.	
- **STATUS REGISTER**
	L'S0SPSR è un registro composta da **8 bit**, e permette **solo la lettura**.
	- I bit da **0 a 2** sono riservati
	- il bit **3** è chiamato Slave Abort(**ABRT**), quando il suo valore è 1, indica che la comunicazione con lo slave si è interrotta prima della fine della comunicazione. In questo caso i dati verranno persi, e il valore di questo bit **tornerà** a **0** nel momento in cui si **leggerà il registro**.
	- Il bit **4** viene chiamato Mode Fault(**MODF**), il suo valore sarà pari ad 1 solo nel momento in cui un **altro master sceglierà lo stesso slave per una comunicazione**. Questo bit viene cancellato leggendo S0SPSR e quindi scrivendo S0SPCR
	- Il bit **5** viene chaiamato Read Overrun(**ROVR**), quando il suo valore è 1 indica che si è verificato un **errore di overrun**, cioè quando i dati ricevuti nel ciclo di trasferimento precedenti non vengono letti, sovrascrivendo i vecchi dati perdendoli definitivamente.  Questo bit viene cancellato leggendo S0SPSR.
	- Il bit **6** Write Collision(**WCOL**), quando il suo valore è 1 indica che si è presentata una collisione di scrittura, questo avviene quando i dati vengono riscritti all'interno del data register durante un trasferimento. Questo bit viene cancellato leggendo S0SPSR.
	- Il bit **7**  SPI trasnfer complete Flag(**SPIF**), quando il suo valore è 1 indica che un ciclo di trasferimento è completato. Questo bit viene cancellato leggendo S0SPSR.
- **CLOCK COUNTER REGISTER**
	L'S0SPCCR è composto da un numero di bit che può variare da interfaccia SPI a interfaccia SPI, questo registro controlla la frequenza del segnale SCLK del master, il segnale viene creato da un segnale di clock esterno e il risultato di 
- **INTERUP FLAG REGISTER**
	L'S0SPINT è composto da 8 bit, ma i bit da 1 a 7 sono riservati, ma **l'unico rilevante** è il **bit 0**, viene impostato per generare un interrupt di processo, può essere cancellato scrivendo un 1 in questo bit.

### SEQUENZA DELLE OPERAZIONI
Per configurare correttamente queste interfacce SPI, come slave o master, bisogna seguire una sequenza di operazioni:
- **MASTER**
	S0SPCCR deve essere impostato alla frequenza di clock desiderata, e bit MSTR deve essere **impostato ad 1**.
	Per avvaiere un nuovo trasferimente, ogni dato deve essere scritto all'interno di S0SPDR, avviando effettivamente la trasmissione dei dati, attivando sia il segnale SS e impostando anche il SCLK.
	Alla fine della trasmissione il canale SS verrà disattivato come con il SCLK, attivando il bit **SPIF dell S0SPSR**.
	A questo punto è possibile la lettura del S0SPDR, per leggere i dati ricevuti.
	È possibile trasmettere più dati ripetendo la stessa procedura, ma questo deve avvenire soltanto dopo avere letto il data register così da poter resettare il bit di SPIF. 
- **SLAVE**
	Inizialmente, l'S0SPCR deve essere scritto in base alle impostazioni desiderate e il bit **MSTR** deve essere **impostato a 0**.
	I dati che lo slave deve trasmettere devono essere scritti all'interno del **S0SPDR**, attendere fino a quando il bit SPIF avrà valore 1, poichè una **lettura/scrittura non può avvenire durante una trasmissione.**
	È possibile trasmettere più dati ripetendo la stessa procedura, ma questo deve avvenire soltanto dopo avere letto il data register così da poter resettare il bit di SPIF. 

### VANTAGGI e SVANTAGGI
- **PRO**
	- Comunicazione **Full Duplex**
	- **Velocità maggiore** a $I^2C$
	- Lunghezza della **stringa binaria variabile** da 8 a 16 bit
	- **Energia** utilizzata **minore** a $I^2C$
	- **Clock solo sul master**, slave non devono avere un oscillatore
- **CONTRO**
	- Richiede più pin di $I^2C$
	- Non esiste un sistema di riconoscimento dello slave
	- Supporta un solo master
	- Gestisce solo piccole distanze
Il fatto che SPI sia full duplex lo rende molto **semplice**, soprattutto per topologie da **single master a single slave**, e viene utilizzato soprattutto per i**mplementare un flusso di dati ad alta efficienza**, come può essere:
- applicazione di audio digitale
- elaborazione del segnale digitale
- comunicazioni con sensori, dispositivi di controllo chip, fotocamere e altro...

Il bus SPI non ha un vero e proprio standard formale, ma è comune avere dimensione di parole di bit diverse da quelle elencate prima.
Ogni dispositivo definisce il proprio protocollo in modo diverso.
Poi la line SS può essere selezionata in modo diverso(livello logico alto), un'interfaccia SPI può inviare prima il bit meno significativo per primo.


## PROTOCOLLO INTER-INTEGRATED CIRCUIT I2C
I2C è un protocollo a **bassa larghezza di banda e a brevi distanze** per comunicazioni a brodo di una scheda come SPI.
I dispositivo sono connessi tramite 2 fili condivisi:
- **DATI SERIALI (SDA)**
- **CLOCK SERIALE (SCL)**
![[Pasted image 20260503002153.png]]

I2C è una **tecnologia** **di comunicazione seriale sincrona** per lo scambio di dati tra più dispositivi, tramite l'**uso di soltanto 2 linee**, dove una è utilizzate per l'invio del segnale di clock, l'altra per ricezione/invio dei dati.
Questo protocollo funziana in modalita **MASTER-SLAVE**, dove un master può comunicare più slave.
Visto che questo protocolla utilizza soltanto 2 linee, bisgona avere un **meccanismo di indirizzamento**, essendo che ogni dispositivi a solo 2 terminali, possono esistere anche indirizze che indicano un gruppo o la totalità dei sidpositivi.

Il protocollo I2C offre anche il funzionamento multi-master, inq eusto caso esiste un **mater prinicipale**, molteplici dispositivi slave e alcuni dispositivi che possono essere sia master che slave cambiando dinamicamente il proprio ruolo.
![[Pasted image 20260503003421.png]]
Anche se per la comunicazione sono richieste solo 2 linee, servono altre 2 linee che offrono alimentazione e un riferimento comune a massa per ogni chip collegato in rete.
![[Pasted image 20260503003725.png]]

### FUNZIONAMENTO
Il master avvia e controlla la comunicazione, questa **inizia grazie ad una sequenza di avvio data dal master**, dicendo a tutti i dispositive di essere in ascolto sulla linea dati.

Il master invia l'**indirizzo** dello slave con cui vuole parlare, assieme ad un **flag**, che indica se il master deve **inviare** o **ricevere** dati da/allo slave, nel caso il master debba scrivere/inviare dati agli slave, i dati possono essere mandati a più dispositivi contemporanemente.
Questo tipo di protocollo non è full-duplex, ma **half-duplex** poiché le operazioni di scittura e lettura vengono decise da un flag comandato dal master, e dal fatto che **esiste una sola line dati**.

Il **trasmettitore invia 8 bit alla volta**, ogni volta il **ricevitore** deve **rispondere con un bit** per **confermare** l'avvenuta **ricezione** del pacchetto di bit, questo và avanti fino al trasferimento di tutti i dati, quando la conunicazione è completata il master emette una condizione di stop che indica la fine della comunicazione.
![[Pasted image 20260504120226.png]]

La **condizione iniziale**, è una **trasnizione** da **livello logico alto a basso** sulla linea dati nel momento in cui il **clock è a livello logico alto**, questo farà **cominciare le variazioni** dell'SCL dove la frequenza delle variazioni indicano la velocità di trasferimento dei dati.
Alllo stesso modo funziona anche il segnale di stop, infattti è una **transizione da basso ad alto della line SDA quando l'SCL è stabilmente a livello logico alto**, per questo l'SCL deve interrompere la comunicazione prima che venga emessa la condizione di stop.
![[Pasted image 20260504121916.png]]

### VANTAGGI E SVANTAGGI
- **PRO**
	- Richiede soltanto 2 linee
	- Supporta velocità dati multiple
	- Meccanismo di rlevamento collisioni
	- Indirizzamento a 10 bit(fino a $2^{10}$ dispositivi collegati alla rete)
	- Supporta un'implementazione multimaster
	- Supporta comunicazione broadcast/multicast
- **CONTRO**
	- La frequenza di clock non può essere arbitraria
	- Comunicazioni solo half-duplex
	- Consumo di energia elevato
Esistono 3 tipi di velocità:
- **STANDARD**(100kbps)
- **VELOCE**(400kbps)
- **ALTA VELOCITÀ**(3.4Mbps)
