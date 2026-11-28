# Operatori Puntuali

> **Slide:** [[04_Operatori puntuali.pdf]]
> **Indice:** [[IMAGE PROCESSING]]

Gli operatori puntuali **cambiano l'intensità di un pixel** in base ad una funzione che dipende solo da quel pixel.

Gli operatori puntuali sono chiamati **omogenei** quando $f()$ non dipende dalle specifiche coordinate $(u,v)$.

- **Addizione**
- **Moltiplicazione**
- **Funzioni a valori reali**
- **Thresholding (Soglia)**
	Se un pixel **supera** una certa soglia, il valore sarà settato ad un certo valore; la stessa cosa succede anche al contrario (approfondimento pratico e varianti in [[IMAGE FORMATION#Tipi di Threshold]]).
	![[Pasted image 20260922155030.png|359]]
- **Clamping**
	L'operatore di clamping serve a "tagliare" i valori dei pixel in un determinato intervallo.
- **Inversione dell'immagine**
	$$f_{\text{invert}}(a) = -a + a_{\max} = a_{\max} - a$$
- **Regolazione automatica del contrasto**
	Modifica le intensità dei pixel in modo tale che l'intervallo di valori sia usato completamente; si può usare anche per diminuire il contrasto. Viene definito matematicamente qui $\to$ [[04_Operatori puntuali.pdf#page=14|04_Operatori puntuali, pagina 14]]

## Equalizzazione degli istogrammi
Utilizzare gli operatori puntuali per avere una **distribuzione uniforme all'interno dell'istogramma** (vedi [[03 - Istogrammi]]).

Avviene grazie a questa funzione:
$$
s = T(i) = K\sum^{i}_{j=0} p_{r}(j)
$$
- $i = I(u,v) \to$ luminosità di un pixel all'interno di un'immagine $M \times N$
- $p_{r}(j) = \frac{h(j)}{MN} \to$ probabilità di occorrenza di $j$
- $K$ è il numero di livelli d'intensità dell'immagine
- $T(i)$ è la funzione di mapping ed è monotona non decrescente
- $s$ è il valore d'intensità del pixel alle coordinate $(u,v)$ nell'immagine risultante
![[Pasted image 20261006174009.png]]
