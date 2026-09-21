	**Con** un campo elettrico $q\vec{E}$ = $\vec{F}$  
$\vec{E} = -\vec{\nabla{}}\circ{V}$ 
**Potenziale elettrico** è di definizione una misura differenziale, infatti non si può misurare il potenziale elettrico in un solo punto, ma si deve fare la differenza tra 2 punti.

# Tensione e Corrente
La carica elettrica è una grandezza che si **conserva** 
La corrente elettrica è la **quantità di cariche elettrica** che passa attraverso una superficie in un **certo lasso di tempo**.
[[01 - Nuts and Bolts of Electronics.pdf#page=3|01 - Nuts and Bolts of Electronics, pagina 3]] 

# Componenti base
## RESISTENZE
**Dissipazione:** trasformare energia elettrica in altre forme es calore
**Erogazione:** trasformare forme di energie in energia elettrica

[[01 - Nuts and Bolts of Electronics.pdf#page=6|01 - Nuts and Bolts of Electronics, pagina 6]] 

## DIODI
#diodo
Componente formato dispositivo che lavora in modo non lineare, formato da semiconduttori come il **silicio**.


Ogni diodo ha 2 terminali differenti un **anodo** e un **catodo**.
![[Screenshot From 2025-10-03 10-23-39.png]]

Per far si che un semiconduttore sia tale, bisogna fare un processo di **drogaggio** (aggiunta di impurità) le quali permettorno di essere un semiconduttore efficiente.

$I = I_0 * [e^{\frac{qV}{kT}} - 1]$  
$I_0$  = costante positiva
$e^{\frac{qV}{kT}}$ = numero puro
T = temperatura diodo
q = carica elementale (costante)
k = costante di Bolzman 

Se $V >> V_t$ allora $I \approx I_0 * e^\frac{V}{V_t}$   
![[Screenshot From 2025-10-03 10-40-57.png]]
**FORWARD BIAS**: regione dove un diodo si comporta come un cortocircuito.
**REVERSE BIAS**: una volta raggiunta quasta ragione il diodo non può più raggiungere le latre regioni poiché si rishia che il componente si sia rotto, e si comporta come un circuito aperto.


[[01 - Nuts and Bolts of Electronics.pdf#page=30|01 - Nuts and Bolts of Electronics, pagina 30]]

## SWITCH e TRANSISTOR
#switch
Composto da 2 terminali, e da 3 terminale i quali in base allo stato del dispositivo si comportano da circuito **aperto** o  da circuito **chiuso**. 
- 2 terminali -> **switch**
- 3 terminali -> **transistor**

[[01 - Nuts and Bolts of Electronics.pdf#page=33|01 - Nuts and Bolts of Electronics, pagina 33]]

**TIPI DI TRANSISTOR**
I transistor sono sempre costruiti in semiconduttori
Sono considerati come switch ma hanno sempre delle perdite di energia.
#transistor
- **BJT o MOSFET**
- IGBT
- SCR
[[01 - Nuts and Bolts of Electronics.pdf#page=34|01 - Nuts and Bolts of Electronics, pagina 34]]

### BJT
#BJT
Servono tre regione drogate n,p, di conseguenza il transistor è fatto da materale drogato in **NPN** o **PNP**.

![[Screenshot From 2025-10-03 12-24-22.png]]

Formato da tre terminali:
- Base B
- Collettore C
- Emettitore E
La corrente alla Base è quella che decide come si comportaranno E e C, se la corrente $I_B \approx 0$ si comprota come un **circuito aperto**, invece se è sufficientemente alta il transistor causerà un **corto circuito**.

$V_{BE}$ e $V_{CE}$ sono le tensioni che vengono prese in considerazione durante le misure di un transistor, $V_{BC}$ viene determinata automaticamente dalle altre 2.

Con il Collettore in serie ad un circuito aperto, il transitor è **uguale** ad un diodo.

La corrente massima di collettore del dispositivo è proporzionale a quella di Base.

$\frac{I_E = I_b +  I_c}{ I_{cmax} = \beta * i * b}$ 

 [[01 - Nuts and Bolts of Electronics.pdf#page=37|01 - Nuts and Bolts of Electronics, pagina 37]]
La frequanza di commutazione di un transistor BJT varia in base alla tensione che il transistor riesce a supportare, più la tensione è alta meno il transistor riesce a commutare, invece più la tensione è bassa più la frequenza del transistor è alta.
![[Screenshot From 2025-10-06 10-15-21.png]]

### MOSFET
#MOSFET
Dispositivo formato da 4 terminali, i quali sono:
- **Gate** G 
- **Drain** D
- **Source** S
- **Body** or **Bulk** B
Se il terminale di Bulk non vine eutilizzato viene cortocircuitato con il Source.
![[Screenshot From 2025-10-06 10-48-52.png]]
La tensione tra G e S **Vgs** è la tensione che decide il comportamento del transistor.
$V_{Th}$ è la tensione di soglia del transistor.

**tensione di overdrive** $V_{OD} = V_{Gs} - V_{Th}$
Il MOSFET ha 3 regioni di lavoro:
- **cut-off**: $V_{Gs} < V_{Th}$  e quindi $I_D = 0$    
- **saturation**: $V_{Gs} \ge V_{Th}$  e $V_{Ds} > V_{OD}$ e quindi $I_D > 0$ 
- **triode**: $V_{Gs} \ge V_{Th}$  e $V_{Ds} < V_{OD}$ e quindi $I_D > 0$

Esiste un'area la quale permette di lavorare in sicurezza con i dispositivi senza casuare una rottura dei dispositivi.

Nel caso dei BJT esiste un malfunzionamento, che causa una continua dissipazione di calore il quale può portare alla fusione del componente
[[01 - Nuts and Bolts of Electronics.pdf#page=45|01 - Nuts and Bolts of Electronics, pagina 45]]

## Amplificatore Operazionale
Amplifica un segnale, modificando la sua ampiezza moltiplicando il segnale per un numero.

Componente formato d 5 terminali:
- 2 terminali di ingresso
- 2 terminali di alimentazioni
- 1 di uscita
![[Screenshot From 2025-10-06 12-02-30.png]]

Terminale (-) chiamato invertente.
Terminale (+) chiamato non invertente.
I terminali di alimentazione sono rispettivamebte chiamati positivo e negativo:
Le ensioni ai capi dei terminali si chiamano:
- $V_{ss}^+$
- $V_{ss}^-$ 
**single-ended**: $V_o = A * V_i$    
Per funzionare come amplificatore la tensione $V_i$ deve essere piccolissima, questo lo rende inutilizzabile come amplificatore.

Per questo si utilizza come **comparatore**

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


# Leggi di Kirchoff
**NODO:** punto di un circuito in cui convergono 2 o più terminali 
**RAMO:** luogo di punti o un percorso su un circuito tra 2 nodi
**MAGLIA:** percorso che parte da un nodo e passa da N nodi per tornare al nodo di partenza
[[01 - Nuts and Bolts of Electronics.pdf#page=8|01 - Nuts and Bolts of Electronics, pagina 8]]

## KCL
#KCL
**Leggi di kirchoff ai nodi**
La somma algebrica delle correnti a un nodo è nulla. $\sum_{node}I = 0$          

## KVL
#KVL
**Leggi di kirchoff alle maglie**
La somma algebrica della tensione ai capi dei rami di una maglia è uguale a 0. $\sum_{ramo}V=0$ 

# CONNESSIONE IN SERIE/PARALLELO
#connessioni
**SERIE**: condividono un terminale in modo esclusivo, ovvero che in un punto condividono uno e uno solo terminale.
Corrente uguale, tensione diversa

**PARALLELO**: condividono a coppie i 2 terminali.
Corrente diversa, tensione uguale

[[01 - Nuts and Bolts of Electronics.pdf#page=9|01 - Nuts and Bolts of Electronics, pagina 9]] 

# Teorema di Norton e Thevenin
## Thevenin
Se si prende una connessione formato sia da resistenze e generatori sia di tensione che di corrente, si può sostituire con un generatore e una resistenza in serie

## Norton
Se si prende una connessione formato sia da resistenze e generatori sia di tensione che di corrente, si può sostituire con un generatore e una resistenza in parallelo
[[01 - Nuts and Bolts of Electronics.pdf#page=22|01 - Nuts and Bolts of Electronics, pagina 22]]


# Segnali
#segnali
**DC**: Direct Current, segnale che trasmette direttamente sia corrente che tensione costanti, **RETTA**

**AC**: Altarnating Current, segnale che varia tensione e corrente nel circuito, il quale si può vedere come sovrapposizione di **ONDE SINUSOIDALI**.
[[01 - Nuts and Bolts of Electronics.pdf#page=23|01 - Nuts and Bolts of Electronics, pagina 23]]


