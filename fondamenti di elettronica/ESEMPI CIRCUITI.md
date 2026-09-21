# ES. carica scarica di un condensatore
![[Pasted image 20260516162059.png]]
**Per t < 0** l'interruttore è in stato OFF, per questo si comporta come un circuito aperto e questo non comporterà variazioni all'interno del circuito.
$$
\begin{aligned}
I = I_{switch} = I_{R} = I_{C} = 0 \\
I_{c} = C *\frac{dV_{c}}{dt} = 0 \to \frac{dV_{c}}{dt} = 0\\
I_{R} = \frac{V_{R}}{R} = 0 \to V_{R} = 0
\end{aligned}
$$
**Per t = 0** l'interruttore viene bruscaente commutato nel suo stato di ON, causando un cortocircuito.
Ora il circuito viene descritto da:
$$
V_{b} - RI_{R}(t) - V_{c}(t) = 0
$$
Essendo che la corrente che attraversa il resistore è la stessa che attraversa il condensatore la funzione sarà:
$$
V_{b}-RC \frac{dV_{c}}{dt}-V_{c}(t) = 0 
$$
Assumendo cha $V_{c}(0) = 0$, la soluzione sarà:
$$
V_{c}(t)=V_{b}[1-e^{- t/RC}]
$$
La carica del condensatore sarà:
$$
Q_{c}(t)=CV_{c}(t)=CV_{b}[1-e^{- t/RC}]
$$
Per questo al cambio di stato dell'interruttore la tensione ai capi del condensatore crescerà rapidamente, seguendo un esponenziale negativo, rallentando e saturando alla tensione fornita dalla sorgente.
La dinamica temporale del circuito e data da prodotto RC, di fatto a t = RC la carica del condensatore sarà al 65%, invece a t = 3RC il condensatore avrà carica pari 95/100%.
La corrente del condensatore sarà:
$$
I_{c} = I_{r} = C \frac{dV_{c}(t)}{dt} = \frac{V_{b}}{R}e^{-t/RC}
$$

# ES. Diodo zener
![[Pasted image 20260325180916.png]]

$V_{z} = 3V,V_{in} = 12V,R_{s} = 1k\ohm,I_{Zmin}=1mA,I_{Zmax}=10mA$, l'impedenza della resistenza di carico è infinita(**circuito aperto**), in questo caso la corrente che scorre nella resistenza in serie è anche la stessa che scorre attraverso al diodo:
$$
I_{s}=\frac{V_{in}-V_{z}}{R_{s}}=\frac{12V-3V}{1k\ohm}=9mA 
$$
Essendo che la corrente è c**ompresa nell'intervallo di corrente**, il diodo è **polarizzato nella zona Zener**, questo se la tensione drimane costante, ma se la tensione d'entrata variasse, la corrente deve essere al massimo $I_{Zmax}$:
$$
V_{inMax}=V_{z}+R_{s}(-I_{zMax})=13V
$$
Se la tensione aumentasse ancora il diodo non sarebbe polarizzato nella zona di Zener, ma rischierebbe un danno permanente, invece sela tensione diminuisse, la corrente attraverso il diodo deve essere almeno $I_{Zmin}$:
$$
V_{inMin}=V_{z}+R_{s}(-I_{Zmin})=4V
$$
Quindi la tensione in uscita, nel caso della tensione in ingresso tra i valori di tensioni appena trovati, sarà costante con un valore di 3V.

Nel caso invece di avere una resistenza di carico,$R_{L}=1k\ohm$, la **corrente** che fluisce sul diodo zener **non sarà uguale** a quella della **resistenza in serie**, poichè una parte scorrerà anche nella resistenza di carico, però se il diodo è polarizzato nella regione di zener la tensione ai suoi capi sarà costante, così come la corrente ai capi della resistenza di carico.

$V_{in}=12V,I_{s}=9mA,I_{L}=3mA$, solo 6mA sarà andranno al diodo zener.
In questo caso il valore di $I_{sMin}$ sarà diverso:
$$
\begin{aligned}
I_{sMin}= -I_{zMin}+\frac{V_{z}}{R_{L}} = 1mA + 3mA = 4mA \\
V_{inMin}=V_{z}+R_{s}I_{sMin}=7V
\end{aligned}
$$
Stessa vale anche per il valore di $I_{sMin}$ che diventerà:
$$
\begin{aligned}
I_{sMax}=-I_{zMax}+\frac{V_{z}}{R_{L}} = 10mA + 3mA=13mA \\
V_{inMax}=V_{z}+R_{s}I_{sMax}=16V
\end{aligned}
$$
Questo comporta ad un cambio di range di tensione in base al **valore del carico**, per questo si può dire che il rabge di tensione cambia in funzione del carico, se invece variasse il carico avendo la tensione fissa, mantenendo il diodo zener sempre in funzionamento, per questo la corrente massima che può scorrere nel carico, nel caso di $V_{in}=12V$, è:
$$
I_{LMax}=\frac{V_{in}-V_{z}}{R_{s}}-(-I_{zMin})=9mA -1mA= 8mA 
$$
Dove il valore minimo del carico è:
$$
R_{LMin}=\frac{V_{z}}{I_{LMax}}= \frac{3V}{8mA}= 375 \ohm
$$
Nella resistenza in serie la corrente $I_{s}=9mA$, e sarà costante sempre per $V_{in}=12V$, di questi 9mA, almeno 1mA deve **fluire nel diodo** così da garantirne il funzionamento, e ilresto nel carico, ma se il **carico aumenta** la **corrente che fluisce nel diodo aumenterà**, mentre quella nel carico diminurà, **mantenendo sempre la somma pari a 9mA**, anche in questo caso si dovrebbe verificare che la corrente non superi il valore $I_{ZMax}$.

