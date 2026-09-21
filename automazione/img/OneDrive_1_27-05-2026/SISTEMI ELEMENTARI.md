	Per decrivere un qualunque sistema, è possibile utilizzare **la trasformata di Laplace**, la quale viene rappresentata come un **rapporto di 2 polinomi**.

Nell’ipotesi che le **radici del polinomio a denominatore** presentino **molteplicità pari a uno**, una volta che la G(s) sia stata decomposta in fratti semplici, dà luogo ad espressioni del tipo:
$$
G(s)=\frac{R}{s} +  \sum^K_{i=1} \frac{R_{i}}{s-p_{i}} + \sum^l_{i=1} \left[ \frac{u_{i}+jv_{i}}{s-\sigma_{i}-j\omega_{i}} + \frac{u_{i}-jv_{i}}{s-\sigma_{i}+j\omega_{i}} \right]
$$

- Il **primo termine** si riferisce ad un eventuale **polo nell’origine** 
- La **prima sommatoria** si riferisce ai termini del primo ordine, che sono **relativi ai poli reali non nulli, in numero pari a k** 
- La **seconda sommatoria** si riferisce ai termini del secondo ordine, che sono relativi a **coppie di poli complessi coniugati, in numero pari a l**


# RISPOSTE CANONICHE
1) **RISPOSTA IMPULSIVA**: Risposta all'impulso $\to$ [[SISTEMI E MODELLI#IMPULSO|trasformata Impulso]]
	La risposta impulsiva si ricava, **antitrasformando** la **funzione di trasferimento** del sistema.
	Essendo che il sistema nel dominio di Laplace viene **descritto** totalmente dalla **trasformata**, invece nel dominio del tempo viene descritta dalla **risposta impulsiva** del sistema
2) **RISPOSTA INDICIALE**: Risposta al gradino $\to$ [[SISTEMI E MODELLI#GRADINO UNITARIO|trasformata gradino]]
	La risposta al gradino è data da 2 fasi: ^d3c9db
	- **TRANSITORIA**
	- **REGIME**
	Crescendo fino a un picco massimo, per poi scendere e iniziare a **oscillare**, e prendere un valore finito.
	Il tempo che il sistema per mantenere l'uscita del sistema in un range di $\pm 5\%$ del valore finale, e si dice $T_{a}$.
	La **massima sovraelongazione**(In percentuale) è il valore massimo raggiunto all'uscita del sistema, rispetto al avalore finale.
	[[AuIn05.1- Sistemi elementari.pdf#page=13|AuIn05.1- Sistemi elementari, pagina 13]]
	  
[[AuIn05.1- Sistemi elementari.pdf#page=10|AuIn05.1- Sistemi elementari, pagina 10]]

## GUADAGNO STATICO
Si consideri una funzione di trasferimento G(s) **asintoticamente stabile**, senza poli nell’origine  Eccitando il sistema con un ingresso a gradino, si ottiene che la risposta tende a un valore di regime costante $Y_{\infty}$ pari a:
$$
y_{\infty}=\lim_{ t \to \infty } y(t) = G(0) 
$$
G(0) è detto **guadagno statico**
[[AuIn05.1- Sistemi elementari.pdf#page=15|AuIn05.1- Sistemi elementari, pagina 15]]


# SISTEMI DEL PRIMO ORDINE
Un sistema elementare del primo ordine è caratterizzato da una funzione di trasferimento nella forma:
$$
G(s)=\frac{1}{s+p}
$$
Ciò è equivale sempre a meno di un fattore costante a:
$$
G(s) = \frac{1}{1+\tau s}
$$
come $\tau = \frac{1}{|p|}$ , il quale è detto **costante di tempo**, che caratterizza la risposta dei sistemi elementari del primo ordine.

Ad ogni polo p corrisponde una **costante di tempo** $\tau$.
Se $\tau>0$ il polo p del sistema è a parte reale negativa, cio significa che il **sistema è stabile**.
$$
p = -\frac{1}{\tau}
$$
## RISPOSTA IMPULSO
[[AuIn05.1- Sistemi elementari.pdf#page=19|AuIn05.1- Sistemi elementari, pagina 19]]
La funzione nel tempo sarà data da:
$$
y(t) = Ae^{- \frac{t}{\tau}}
$$
## RISPOSTA AL GRADINO
[[AuIn05.1- Sistemi elementari.pdf#page=20|AuIn05.1- Sistemi elementari, pagina 20]]
$$
y(t) = \mathcal{L}^{-1}\left[ \frac{1}{(1+\tau s)} \right] = 1-e^{-t/\tau}
$$
Sarà molto simile a [[SISTEMI ELEMENTARI#^d3c9db|RISPOSTA INDICIALE]],ma in questo caso la **massima sovraelongazione non sarà presente**, si raggiunge il valore finale senza mai superarlo.

se $\tau$ varia la varierà a sua volta,come: [[AuIn05.1- Sistemi elementari.pdf#page=24|AuIn05.1- Sistemi elementari, pagina 24]]

# SITEMI DEL SECONDO ORDINE
[[AuIn05.1- Sistemi elementari.pdf#page=26|AuIn05.1- Sistemi elementari, pagina 26]]

I sistemi del secondo ordine possono essere scritti anche come:
$$
G(s)=\frac{1}{1+\frac{2\delta s}{\omega_{n}}+\frac{s^2}{\omega ^2_{n}}}= \frac{\omega^2_{n}}{s^2+2\delta \omega_{n} s+\omega^2_{n}}
$$
dove $\omega_{n},\delta$, caratterizzano la risposta dei sistemi del secondo oridine.

I 2 poli vengono dati dall'equazione $p_{1,2}=\sigma+j\omega$
dove:
$$
\omega_{n}=\sqrt{ \sigma^2+\omega^2 }
$$
invece:
$$
\delta=\frac{\sigma}{\omega_{n}}=\cos(\rho)
$$
![[Pasted image 20260423123722.png|198]]

## RISPOSTA GRADINO 2° ordine
[[AuIn05.1- Sistemi elementari.pdf#page=30|AuIn05.1- Sistemi elementari, pagina 30]]
La risposta a gradino dipende soprattutto da $\delta$, facendo cambiare la forma stessa della funzione.


# DIAGRAMMI DI BODE
Sono 2 diagrammi, i quali sono:
- **diagrammi dell AMPIEZZE(moduli)**
	Riporta il **logaritmo del modulo** della funzione risposta armonica **in funzione del logaritmo in base 10 della pulsazione** $\omega$
- **diagrammi delle FASI(argomenti)**
	Riporta **l'argomento della funzione di risposta in funzione del logaritmo in base 10 della pulsazion**e $\omega$

![[Pasted image 20260507115349.png|430]]

 Il tracciamento dei due diagrammi di Bode (ampiezza e fase) potrà essere eseguito **sommando i diagrammi dei fattori elementari**.

Data una funzione di trasferimento razionale fratta generica:
$$
G(s)= \frac{b_{m}s^m+b_{m-1}s^{m-1}+\dots+b_{1}s+b_{0}}{a_{n}s^n+a_{n-1}s^{n-1}+\dots+a_{1}s+a_{0}}
$$
Per effettuare il tracciamento dei diagrammi di Bode è neccessario **fattorizzare** la funzione di trasferimento nella sua forma **costanti nel tempo**.

# DIAGRAMMI PER TERMINI DEL PRIMO ORDINE
[[AuIn06.3 - Analisi Armonica.pdf#page=9|AuIn06.3 - Analisi Armonica, pagina 9]]
In presenza di termini del **primo ordine** bisogna introdurre un'**approssimazione asintotica**, la quale permette di semplificare i diagrammi di bode.

Per il **digramma delle ampiezze** l'approssimazione asintotica, è composta da una spezzata composta da 2 asisntoti dove il primo avrà $\omega \to \infty$ e l'altro $\omega \to 0$, questi 2 asintoti(**rette**) si incontreranno in un punto detto **punto di rottura** che sarà identificato da $\omega = \frac{1}{|\tau|}$ .

![[Pasted image 20260513105402.png|320]]

Invece nel caso del **diagramma delle fasi**, si approssimerà tramite asintoti in 0 e $-\frac{\pi}{2}$, collegando i 2 asintoti tramite una rette tangente a $\frac{1}{\tau}$ con una pendenza pari a $-\frac{\pi}{4}$.

![[Pasted image 20260513111019.png|354]]

Per $G(s)=\frac{1}{1+j\omega \tau}$ i diagrammi saranno:
![[Pasted image 20260513111531.png|512]]

Invece se il termine è a numeratore, i giagrammi si ribalteranno, invece che avere numeri negativi, avrà numeri posittivi.

Nel caso d $\tau < 0$ i diagrammi saranno **misti**, nel caso il termine sia a denominatore, il diagamma di ampiezza sarà decrescnte invece quello delle fasi sarà **crescente**.

# DIAGRAMMI DEL SECONDO ORDINE
Qesti sono utilizzati per rappresentare funzioni di trasferimento, che **presentano termini del secondo ordine**.

## DIAGRAMMA DELLE AMPIEZZE
Il **diagramma delle ampiezze** ha 2 asintoti:
- Il primo è coincidente con l'asse delle ascisse per $0<\omega<\omega_{n}$
- Si ha un secondo asintoto con retta a pendenza $-40 \frac{dB}{Dec}, per \space \omega>\omega_{n}$
- Il punto di rottura è dato da $\omega>\omega_{n}$
In questo caso l'**approssimazione** può **portare** ad una **grande differenza rispetto al diagramma reale**, soprattutto nel **punto di rottura**.

In un diagramma può presentarsi un fenomeno che si chiama **risonanza**, dove si presenta un **picco di risonanza** $M_{R}$ ed è il valore massimo aasunto nel diagramma delle ampiezze, invece la **pulsazione di risonanza** è quella pulsazione alla quale avvine la risonanza.
![[Pasted image 20260514111157.png|439]]

## DIAGRAMMA DELLE FASI
Come nel diagramma nel caso di termini del primo ordine, anche in questo caso saranno presenti 2 punti e una runa curva che li collega.

Le pulsazioni $\omega_{a}$ e $\omega_{b}$ sono legate alla pulsazione $\omega_{n}$ dalla relazione:
$$
\frac{\omega_{n}}{\omega_{a}}=\frac{\omega_{b}}{\omega_{n}}=e^{ \frac{\pi}{2}\delta}=4.81^\delta
$$

[[AuIn06.4 - Analisi Armonica.pdf#page=10|AuIn06.4 - Analisi Armonica, pagina 10]](**per i grafici**)

## INTERPRETAZIONE DEI DIAGRAMMI DI BODE
Per permettere l'interpretazione dei diagrammi di Bode, bisgna introdurre la **banda passante**, cioè un **intervallo di frequenze** in cui il diagramma di Bode delle ampiezze è **compreso nell'intervallo** [-3,3] dB, comprendendo il **valore massimo centrata all'interno dell'intervallo**.

### SISTEMI PASSA BASSO
**Passano** i contenuti a bassa frequenza e **tagliano/attenuano** i contenuti a bassa freqeunza.
![[Pasted image 20260514122950.png|378]]
La **banda passante** sarà compresa $[0,\omega_{b}]$.

### SISTEMI PASSA ALTO
**Passano** i contenuti a bassa frequenza e **tagliano/attenuano** i contenuti ad alta freqeunza.
![[Pasted image 20260514123458.png|371]]
La **banda passante** teoricamente sarà $[\omega_{B},\infty]$.

### SISTEMI PASSA BANDA
**Passano** i contenuti in un certo intervallo di freqeunza, e **tagliano/attenuano** gli altri.
![[Pasted image 20260514123743.png|339]]
La **banda passante** teoricamente sarà $[\omega_{B_{1}},\omega_{B_{2}}]$.

### SISTEMI ELIMINA BANDA
**Taglia** i contenuti in un certo intervallo di frequenza e **passano** gli altri.
![[Pasted image 20260514123952.png|355]]
La banda passante si può vedere come l'**unione** dei sistemi **passa basso e passa alto.**
L'intervallo sarà $[0,\omega_{B_{1}}] U [\omega_{B_{2}},\infty]$
