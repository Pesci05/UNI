# IMAGE PROCESSING — Indice (Teoria)

> **Corso:** Image Processing 2026 — UNIMORE  
> **Appunti di Laboratorio:** [[IMAGE FORMATION]]

---

## Argomenti del corso

| # | Argomento | Slide | Collegamenti Lab |
|---|---|---|---|
| 01 | [[01 - Introduzione]] | [[01_Introduzione.pdf]] | [[IMAGE FORMATION]] |
| 02 | [[02 - Immagini Digitali]] | [[02_Immagini_Digitali.pdf]] | [[IMAGE FORMATION#Da immagine continua a digitale]] |
| 03 | [[03 - Istogrammi]] | [[03_Istogrammi.pdf]] | [[IMAGE FORMATION#Esposizione vs Gain (a parità di luminosità finale)]] |
| 04 | [[04 - Operatori Puntuali]] | [[04_Operatori puntuali.pdf]] | [[IMAGE FORMATION#Tipi di Threshold]] |
| 05 | [[05 - Filtri]] | [[05_Filtri.pdf]] | [[IMAGE FORMATION#CANNY edge detector: Pipeline]] |
| 06 | [[06 - Rumore e Filtri Non Lineari]] | [[06_Rumore e filtri non lineari.pdf]] | [[IMAGE FORMATION#Sorgenti di rumore]] |
| 07 | [[07 - Introduzione a NumPy]] | [[07_Introduzione_Numpy.pdf]] | [[IMAGE FORMATION#OpenCV: frame come array NumPy]] |
| 08 | [[08 - Edge Detection]] | [[08_Edge detection.pdf]] | [[IMAGE FORMATION#Edges to countours]] |
| 09 | [[09 - Il Colore]] | [[09_Colore.pdf]] | [[IMAGE FORMATION#Selezione spettrale (Spectral selection)]] |
| 10 | [[10 - Complessità Computazionale]] | [[10_Introduzione_complessita_computazionale.pdf]] | — |
| 11 | [[11 - Trasformata di Fourier]] | [[11_Trasformata di fourie_I.pdf]], [[12_Trasformata di Fourier - Parte II.pdf]] | — |

---

## Mappa rapida dei contenuti

- **Fondamenti:** [[01 - Introduzione]] $\rightarrow$ [[02 - Immagini Digitali]] $\rightarrow$ [[09 - Il Colore]]
- **Elaborazione nel dominio spaziale:** [[03 - Istogrammi]] $\rightarrow$ [[04 - Operatori Puntuali]] $\rightarrow$ [[05 - Filtri]] $\rightarrow$ [[06 - Rumore e Filtri Non Lineari]] $\rightarrow$ [[08 - Edge Detection]]
- **Strumenti e analisi:** [[07 - Introduzione a NumPy]] $\rightarrow$ [[10 - Complessità Computazionale]]
- **Dominio delle frequenze:** [[11 - Trasformata di Fourier]]

---

## 📅 Piano di Studio in 14 Giorni

Un percorso strutturato giorno per giorno per coprire tutta la teoria e collegarla con la pratica di laboratorio ([[IMAGE FORMATION]]):

| Giorno | Argomento Principale | Obiettivi e Contenuti |
|:---:|---|---|
| **Giorno 1** | [[01 - Introduzione]] | Concetti base di immagine multidimensionale, tipi di output e obiettivi dell'Image Processing. |
| **Giorno 2** | [[02 - Immagini Digitali]] | Spettro elettromagnetico, occhio umano, campionamento spaziale/temporale e quantizzazione. |
| **Giorno 3** | [[07 - Introduzione a NumPy]] | Struttura degli array, slicing, indicizzazione, copie/viste e confronti prestazionali con le liste Python (fondamentale per OpenCV). |
| **Giorno 4** | [[03 - Istogrammi]] | Struttura dati di base, luminosità, contrasto, binning e istogrammi a colori. |
| **Giorno 5** | [[04 - Operatori Puntuali]] | Operatori omogenei, thresholding, clamping e equalizzazione degli istogrammi. |
| **Giorno 6** | [[05 - Filtri]] | Filtri spaziali lineari, kernel, convoluzione, gestione dei bordi (padding/cropping) e filtro gaussiano. |
| **Giorno 7** | [[06 - Rumore e Filtri Non Lineari]] | Tipologie di rumore (Salt & Pepper, Gaussiano, Speckle, Periodico), image restoration e filtri non lineari (Min, Max, Median). |
| **Giorno 8** | [[08 - Edge Detection]] | Derivate prime e seconde, differenze finite (destra, sinistra, centrale) e calcolo del gradiente (modulo e direzione). |
| **Giorno 9** | [[08 - Edge Detection]] *(Approfondimento)* | Operatori Sobel, pipeline completa di Canny (smoothing, NMS, doppia soglia e isteresi) e region masks. |
| **Giorno 10** | [[09 - Il Colore]] | Fisica e percezione del colore, spettro riflettanza, teoria tristimolo (coni S, M, L) e conversione in scala di grigi (media pesata). |
| **Giorno 11** | [[09 - Il Colore]] *(Spazi colore)* | Spazi di colore (RGB, CMY, HSL, HSV), conversioni con OpenCV e uniformità percettiva (CIELAB). |
| **Giorno 12** | [[10 - Complessità Computazionale]] | Analisi delle prestazioni, complessità temporale e spaziale, notazione O grande (Big O) applicata agli algoritmi. |
| **Giorno 13** | [[11 - Trasformata di Fourier]] | Passaggio al dominio delle frequenze, serie di Fourier, formule di Eulero, DFT 1D/2D, spettro (modulo) e fase. |
| **Giorno 14** | [[11 - Trasformata di Fourier]] *(Filtri)* | Teorema della convoluzione, filtri in frequenza (passa-basso, passa-alto, Gaussiani, Butterworth, notch) e vantaggi computazionali della FFT. |
