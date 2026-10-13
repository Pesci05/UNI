
# APERTURE
L'apertura focale **limita** il cono di luce che passa attraverso la lente, il quale raggiunge il piano dell'immagine.
- Questo significa che si può **controllare la luminosità** dell'immagine

# DA IMMAGINE CONTINUA A DIGITALE
Per passare da un'immagine reale ad una digitale serve un **sensore**.

## SENSORE
Il sensore viene raffigurato da un **rettangolo**, il quale viene diviso in **pixel**, questi permettoni di definire:
- **RISOLUZIONE**
- **La grandezza dei pixel**
- **Grandezza del sensore**
Ogni pixel contiene la media dell'informazione che riceve.

Il numero dei pixel può influire su:
- **FIELD OF VIEW**

## FIELD OF VIEW
Il FOV è collegato alla **maximum field view**, il quale è una proprietà della lente, e questo sarà un cerchio grazie alla forma della lente.
Invece il **Field of view** invece è definito si dalla lente ma anche dal **sensore**, infatti la sua grandezza sarà dettata dalla **diagonale** del sensore:
- **MINORE**
	Con la diagonale minore, significa che il sensore sarà del tutto all'interno del MAXIMUM FIELD VIEW, 
- **MAGGIORE O UGUALE**
	Invece in questo caso, il sensore starborderà dal MAXIMUM FIELD VIEW, questo comporta a degli effetti di **vigenttamento** e **spreco dimensioni del sensore**
Il FOV viene calcolato:
$$
FOV=\arctan\left( \frac{W}{2d} \right)
$$

## PIXEL DENSITY
Viene definita dal rapporto **mm/px**.
Questo rapporto può essere calcolata con:
1) **MAGNIFICATION LAW**
2) Misura contando i pixel di un oggetto in un'immaggine

## COME FUNZIONANO
Per avere un'immagine, bisogna che il sensore, il quale è un insieme di pixel, deve **essere colpita dalla luce**, questa, luce deve essere campionata ad una certa frequenza (**Nyquist**).
Il valore del pixele viene deciso tramite misurazione durante il **tempo d'esposizione**, poichè un pixel non raccoglie la luminosità instantaneamente, infatti durante questo lasso di tempo un pixel raccoglie un certo numero di **foroni**.
$$
N_{photon} = irradiance*pixelArea* exposureTime
$$
Per aumentare la luminosità si può:
- aumentare l'illuminazione
- incrementare l'apertura
- Sensore con una grandezza dei pixel più grandi
- Aumentare l'exposure time

L'**exposure time** defnisce per quanto tempo si osserva un certo oggetto durante una misurazione.

**Frame rate** definisce

## SHUTTER TYPE
Per un **global shutter**, ogni riga di pixel, condividono lo stesso intervallo d'integrazione.

Per il **rolling shutter**, ogni riga legge ogni linea una alla volta, spostando l'intervallo sempre più avanti, questo lo rende più economico ma produce degli **artefatti**, modificando l'immagine:
- oggetti dritti vengono catturati storti
- comprime e espande l'oggetto
- se l'oggetto è in rotazione può fondere l'oggetto insieme ad un altro oggetto
Questi effetti non sono riconducibile all'exposure time, ma sono errore chevengono generati dal sensore stesso.

# EFFICICIENZA
Non tutti i fotno contribuiscono allacquisizione dell'immagine, questo avviene perché essite una **probabilità** che un elettrone venga **rilasciato** come risultato.
Questa probabilità viene definita come **quantum efficiency**, e questa dipende dallla lunghezza d'onda della luce.

Un pixel **non è un contenitore infinito**, quando un sensore supera la sua massima capacità.




