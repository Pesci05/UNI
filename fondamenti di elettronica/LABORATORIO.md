# Sistemi embedded
Sistemi che elaborano informazioni all'interno dei prodotti, con risorse limitate.
Solitamente sono **sistemi misti** cioé sia analogici, sia digitali.
Sistemi fortemente legati all' **Hardware**.
Garantire un'esecuzione **real-time**.
[[Lezione_Lab_1.pdf#page=8|Lezione_Lab_1, page 8]]

I **sensori** trasformano grandezze fisiche in segnali elettrici.
Gli **attuatori** trasformano segnali elettrici in variazione di quantità fisiche.
[[Lezione_Lab_1.pdf#page=14|Lezione_Lab_1, page 14]]

Un sistema è **affidabile** se svolge la sua funzione e/o fornisce un servizio con un'elevata probabilità e non provoca alcun danno.
[[Lezione_Lab_1.pdf#page=17|Lezione_Lab_1, page 17]]


# Microcontrollori
I microcontrollori possiedon 2 tipi di memorie:
- **SRAM**
	Memoria di tipo volatile, dove vengono immagazzinati i dati utilizzati dal codice.
	512MB

- **FLASH**
	Memoria non volatile in cui viene scritto il codice da eseguire dal microcontrollore.
	512MB
[[Lezione_Lab_1.pdf#page=26|Lezione_Lab_1, page 26]]

All'interno del microcontrollore esiste una regione di memoria, che si occupa di gestire le perfiferiche tramite dei **registri**.
Ad ogni registro viene associata la periferica, e impostato anche il funzionamento della stessa periferica.

Il **clock** del microcontrollore serve per avere un segnale di sincronismo esterno o interno al microcontrollore, per fare questo si utilizza un **cristallo** che oscilla ad una certa frequenza.

Per avere una potenza di calcolo maggiore si può raggiungere grazie al **calcolo parallelo**.

Esistono dei protocolli seriali, che si dividono in:
- **UART**
- **SPI**
- **I2C**
- **USB**

L'alimentazione può essere effettuata da presa elettrica e batterie.
Per mantenere l'alimentazione nel tempo si utilizzano strategie di **low-power**, abbassando la frequenza del clock, oppure spegendo cicruiti che non is utilizzano.



