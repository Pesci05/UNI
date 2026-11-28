# Istogrammi

> **Slide:** [[03_Istogrammi.pdf]]
> **Indice:** [[IMAGE PROCESSING]]

#22/09
Gli algoritmi di image processing usano gli **istogrammi** come **struttura dati di base**.
Un istogramma indica quante volte ogni valore quantizzato di intensità compreso in $\{0, \dots, K-1\}$ è presente in un'immagine.

Un istogramma per un'immagine a un canale avrà intensità nel range:
$$
I(u,v) \in \{0, K-1\}
$$
Ha esattamente $K$ **bin**, ovvero $K$ elementi.
Nel caso di un'immagine grigia a 8 bit si ha $K = 2^8 = 256$ bin.

L'istogramma contiene informazioni di tipo statistico sulla **distribuzione** dei valori dei pixel, però la **distribuzione spaziale** non viene presa in considerazione.

Gli istogrammi **non mantengono** i dati di disposizione dei pixel: si perde l'informazione riguardo alla **distribuzione spaziale** dell'immagine.

## Luminosità e Contrasto dell'Immagine
La luminosità di un'immagine ad un canale è l'intensità media di tutti i pixel dell'immagine:
$$
L(I)=\frac{1}{AL}\sum^{L}_{u=1}\sum^{A}_{v=1}I(u,v)
$$
In modo equivalente si può calcolare prendendo in esame l'istogramma:
$$
L(I)=\frac{1}{AL}\sum^{K-1}_{i=0}h(i)\,i
$$
![[Pasted image 20260922142939.png]]

Il **contrasto** in un'immagine indica la differenza tra le parti chiare e quelle scure e, di conseguenza, la "facilità" con cui gli oggetti nell'immagine possono essere distinti:
- Immagine a contrasto elevato: sono presenti molti valori distinti di intensità.
- Immagine a basso contrasto: l'immagine utilizza solo pochi valori di intensità.

Per definire il contrasto si può utilizzare una formula come:
$$
C_{M}(I)=\frac{\max(I)-\min(I)}{\max(I)+\min(I)}
$$
dove il denominatore è uguale a 2 volte la media delle luminosità massime e minime, $\text{media}=\frac{\max(I)+\min(I)}{2}$.
In questo caso però un valore isolato molto basso rispetto al resto dell'istogramma corromperà il risultato della media, e per questo bisogna mettere una **soglia**, così da scartare quel valore.
![[Pasted image 20260922144047.png]]

Gli istogrammi permettono di rilevare dei difetti dell'immagine grazie alla loro forma, per esempio:
- Problemi di **esposizione** $\to$ valori di illuminazione fuori dall'intervallo percepibile del sensore
- **Manipolazioni** $\to$ picchi e lacune presenti nell'istogramma

Gli istogrammi possono **mostrare** la **modifica dell'immagine**, ma il caso contrario non garantisce che non sia stata manipolata.

Anche la **compressione** e le **codifiche** possono influenzare l'istogramma.

## Binning
Immagini ad alta risoluzione dei livelli d'intensità possono produrre istogrammi molto grandi.
Per ovviare a questo problema si effettua il **binning**, cioè l'intervallo totale viene suddiviso in sotto-intervalli.
![[Pasted image 20260922145201.png]]

Gli intervalli sono suddivisi per avere la stessa dimensione, quindi:
$$
\frac{K}{\text{number\_of\_bins}}
$$
Per sapere a quale bin appartiene un livello d'intensità:
$$
I(u,v) \cdot \frac{B}{K}
$$
dove:
- $I(u,v)$ indica il valore del pixel
- $K$ è il numero di intensità dell'immagine
- $B$ è il numero totale di bin dell'istogramma
- la divisione è intera

## Immagini a più colori
Per immagini a più colori, quindi a 3 canali, i loro istogrammi possono essere calcolati:
- Convertendo l'immagine a un solo canale
- Calcolando un istogramma per ogni canale dell'immagine

Ma in entrambe le soluzioni si perdono informazioni.
Per rappresentare tutti i colori è necessario un **istogramma tridimensionale**, dove tutti i colori vengono congiunti e **ogni bin è associato ad una possibile terna di valori RGB**.
In tal caso, per rappresentare l'istogramma tridimensionale, ho bisogno di un tensore di dimensioni $K \times K \times K$.
![[Pasted image 20260922153114.png]]

Anche in questo caso è possibile effettuare **binning**.

---
> **Vedi anche:** [[04 - Operatori Puntuali#Equalizzazione degli istogrammi]] | [[IMAGE FORMATION#Esposizione e Gain|Esposizione in acquisizione]]
