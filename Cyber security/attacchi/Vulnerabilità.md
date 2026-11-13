**[[Attacchi e vulnerabilità#Vulnerabilità Software e bug|Le vulnerabilità sono]]**
## Metriche base
- **Attack Vector**
- **Attack Complexity**
- **Attack Requirements**
- **Privilege Required**
- **User Interaction**
Dalle metriche base si dividono altre 6 metriche dette **qualcosa** le quali sono:
- **Confidentiality**(VS/SC): Impatto sulla confidenzialità delle informazioni gestote dal sistema (VC) e dai sistemi collegati (SC)
- **Integrity**(VI/SI): Impatto siull'integrità delle informazioni gestite dal sistema (VI) e dai sistemi collegati (SI)
- **Availability**(VA/SA): Impatto sulla disponibilità delle informazioni gestite dal sistema (VA) e dai sistemi collegati (SA)

## Metriche di minaccia


## Metriche ambientali
Metriche delle vulnerabilità che hanno un impatto sull'ambiente.

## Metriche supplementari
Implementate da CVSS4

# CVSSv4 
Si basano su abbreviazioni che vengono create da delle **vector string**, le quali sono delle vulnerabilità sfruttabili dalla rete, con una complessità di attacco bassa, senza alcun requisito iniziale che richiede **priveligi elevati**, ma **nessuna iterazione dell'utente**, che ha **basso impatto sullla confidenzialità**, **integrità**, e **disponibilità del sistema**, ma nessun impatto su sottoinsiemi.

>Es: di una stringa: ==CVSS4.0/AV:N/AC:L/PR:H/UI:N/VC:L/VI:L/VA:N/SC:N/SI:N/SA:N==
>Questo stringa descrive una vulnerabilità di livello 5.1

# Catalogazione delle Vulnerabilità
I sistemi CVE e CVSS,, rappresentano un importante passo verso la creazione di un catalogo uniforma di vulnerabilità.

- Common Platform Enumeration
- **Common Weakness Enueration (CWE)**: Cataloga in modo uniforme 

## CWE


# Sfruttare le vulnerabilità

## MALWARE
**Malware**: MALicious softWARE

 Software da installare sul computer, mscherarlo iniettandolo sempre più in profondità del sistema, si moltriplica e si attiva.

Può attivarsi in diversi modi:

Un malware può essere iniettato tramite:
- **Allegati e-mail**
- **Installazione di software non certificato**
- **File sharing**
- Applicazioni web
I primi tre però sono i più comuni.

### Tipi di malware
### Virus
---
### Trojan
---
Software malevolo, che per non essere rilevato si **maschera** in modo che non si possa trovare.

Questo tipo di malware può essere:
- **Polimorfo**:
	Cambia sempre la sua forma esterna ma non il suo codice, di solito la sua chiave di cifratura rimane in chiaro
- **Metamorfo**
	In questo tipo invce di cambiare la sua forma esterna, cambia il proprio codice, cambiando le suo routine.

### Worm
---
Il worm a differenza del virus è un **applicativo a sè stante**, usa la rete per trovare le vulnerabilità nei computer raggiunti

### Spyware
---
Software che spia la vittima, immagazzinando le informazioni e le trasmette all'attaccante.

Questo tipo di malware viene utulizzato soprattutto per:
- Registrare dati, azioni al computer
- Spammer
- Attaccker
- Defender
- ...
I migliori spyware modificano configurazioni e/o registri del computer per non essere indivisuati dai software anti-spyware.

### Ransomware
---


# APT
**Advanced Persistent Threat**
Tipologie di attacchi che riguardano soprattutto aziende medio-grandi in quanto sono attacchi con invesitimenti alti.

Questo attacco è formato da: 
1. Reco
2. 1
3. 1
4. 1
5. 1
6. 
7. Maintaining persistence

# DoS
**Denial of Service**

## Tipi di attacchi DoS
- Dos che sfruttano **bug, vulnerabilità, cattive configurazioni del s.o.**
	- Ping of death
	- WinNuke
	- Land
	L’attacker sfrutta uno o più bug conosciuti dei software presenti nel sistema vittima per provocarne il crash o rendere il servizio inutilizzabile.

- DoS per **esaurimento di risorse**
	- Smurf e SYN flood
	- TFN
	- Code Red Worm
	- DrDoS

## Ping of death
DoS remoto mediante pacchetti malformati.
I sistemi vulnerabili a quasto tipo di attacco sono:
- versioni di windows datate
- Linux
- macintosh
- SunSolaris
I pacchetti ICMP malformati, sfrutta un bug del protocollo IP èer cui riusciva a generare pacchetti IP di dimensioni a 64KB![[Pasted image 20261109104724.png]]

L'attaccante invia èacchetti ICMP di dimensione maggiore ai 64KB, grazie ala **frammentazione dei pacchetti, i frammenti vengono riassemblati dalla vittima, l'errore avviene in fase di riassemblaggio**, il sistema vittima nel caso riceva un pacchetto troppo grande può fare:
- Reboot
- Hang
- Crash del server

Ping of Death è frutto di una cattiva implementazione dello stack TCP/IP in diversi sistemi operativi.

## WinNuke
Attacco di tipo DoS da remoto mediante l’invio di pacchetti malformati. 
Solo i sistemi Windows 9x/NT sono affetti da questo attacco.
L'attacco vuole scaturire un blocco del sistema.

WinNuke è dovuto ad un **errore di progettazione della funzione che si occupa di NetBIOS:** non controlla la struttura dei pacchetti Out Of Band. 
In ricezione, questi **pacchetti** sono passati direttamente al kernel senza verificare la correttezza della sintassi.

## LAND
L'attacco LAND è un DoS da remoto ottenuto mediante l’invio di pacchetti creati ad hoc. 
I sistemi vulnerabili sono versioni datate di:
- **Windows, BSD**
- **SunOS**
- **Windows XP**
- **prima versione di Windows Vista**

Attaccante invia pacchetti TCP SYN (richiesta di nuova connessione) con sorgente e destinazione identiche (sia indirizzo IP che porta).
L'host di destinazione(vittima) cerca di instaurare una connessione con sè stesso sulla stessa porta, **handshake non terminerà mai**.
![[Pasted image 20261109105828.png]]

Per rilevare/bloccare questo tipo di attacco, si deve filtrare i paccetti che hanno come destinazione un sistema interno alla LAN, e come mittente una macchina che ha come indirizzo **un indirizzo che appartiene all'interno della LAN**, ma che proviene dall'esterno.

![[Pasted image 20261109110440.png]]

Però questo tipo di filtro è efficacie soltanto con attacchi provenienti dall'interno della LAN.
## DoS che sfruttano vulnerabilità
L’attaccante cerca di rendere la vittima irraggiungibile o inutilizzabile, per saturazione di una risorsa o a causa dell’overhead indotto per la gestione dell’evento di attacco.
Sono attacchi ti tipo **brute-force**.
La soluzione è in gran parte legata alla protezione delle comunicazioni con l’attaccante.

L'attacante raggiunge il suo obiettivo facendo saturare le risorse del sistema:
- Tempo CPU
- Memoria
- Spazio su disco
- Numero di connessioni

## Bandwidth consumption
Esistono 2 scenari principali:
- **Banda aggressore >> Bada vittima**
	- In questo caso l’attaccante può semplicemente inondare la vittima con una quantità enorme di traffico di dati.
- **Banda aggressore < Bada vittima**
	- L’aggressore deve utilizzare tecniche di amplificazione del traffico per riuscire a saturare tutta la banda della vittima

## Floding
Attacchi che generano DoS inondando il traffico della vittima.
- ICMP flooding 
- TCP flooding (SYN, SYN+ACK, RST) 
- UDP flooding
Tecbiche che vengono sfruttate:
- IP spoofing 
- Pacchetti malformati 
- Comunicazioni mascherate

## TCP SYN Flooding
l TCP SYN Flood è un attacco che si basa sulla **richiesta di numerose connessioni** (invio pacchetti TCP SYN) solitamente con indirizzi **IP sorgenti** "spoofed“ **generati casualmente**, senza mai completare il ”3-way handshake".

Il risultato dell'attacco porta a:
- **Esaurimento delle risorse**
- **Difficile rintracciare l'origine dell'attacco**
- **Impossibile filtrare il traffico tramite acces-list su IP sorgente**

L'attacco può essere evittao con diverse contromisure come:
- **Rispettano il protocollo TCP**
	- Aumenta della code di connessioni
	- Diminuire il tempo di time-out per il 3-way-handshake
- **Non rispettano il protocollo TCP**
	- SYN cookies
	- Scarta pacchetti SYN casualmente
Queste soluzioni **non risolvono il problema**, ma lo riducono.


## Surf e Fraggle
**Primi attacchi a coinvelgere diversi host.**

- **Broadcast strom**
	- ## **Smurf**
		Fa uso di protocollo ICMP e dei pacchetti ICMP ECHO 
		Un pacchetto ICMP con sogrente IP spoofed viene inviato all'indirizzo di broadcast di una rete di host.
		Tutti gli host della rete generano pacchetti ICMP ECHO verso quello che ritengono essere l'IP sorgente.
		![[Pasted image 20261109114822.png]]
		**Contromisure a questo tipo di attacchi**:
		- Filtrare in uscita dalla rete i pacchetti ICMP con indirizzo di destinazione broadcast address $\to$ **Non essere attaccanti**
		- Filtrare in ingresso dalla rete i pacchetti ICMP con indirizzo di destinazione broadcast address $\to$ **Non essere amplificatori**
		- Bloccare in ingresso il traffico ICMP di tipo ECHO REPLY include le risposte a ping dai propri utenti $\to$ **Non essere vittime**
	- ## **Fraggle**
- **Almeno tre reti coinvolte**

## Problemi degli attacchi DoS
Uno dei più grandi problemi è la rintracciabilità degli esecutori:
- **Reti con struttura multilivello**
	- attaccante > master > demoni > vittima
- **Utilizzo di tecniche di spoofing**
- **Pacchetti con sintassi lecita**
Possibilità di saturazione della banda di rete di qualunque host collegato ad Inter- net: basta un numero sufficiente di demoni per l’attacco

# Distributed Denial of Service (DDoS)
Attacchi DoS che spingonoall’**estremo il concetto i flooding tramite bandwitdhcon- sumption**. Utilizzando **più sorgenti (anche migliaia)** per la generazione del traffico di flood (vittime di II livello).
Una o più vittime finali(vittime di I livello).
Possibilità di **eseguire più attacchi** di tipi flooding.
Da vari anni si fa uso di **botnet**.

## Sistemi di amplificazione
L'amplificazione partenda dal 2018 sfrutta sistemi **memcachedmalconfig**. Memcached è una **funzione** di caching nata per migliorare i tempi di risposta da dischi e database e utilizzata per ridurre i tempi di caricamento dei dati via rete da siti Web.

## Botnet
Rete di computer robotizzati (zombie) che costituisce un vero e proprio esercito di computer compromessi.

Per creare queste botnet si deve:
- Ricerca dei sistemi che possono essere compromessi
- Exploit delle vulnerabilità
- Il bot viene caricato con codice servant e molteplici strumenti di exploit
- La botnet e gestita da un unico centro di comando e controllo
Le botnet possono essere **create** anche solo per **venderle a cybercriminali**.

Le botnet sono uno strumento ideale fondamentale per:
- SPAM (a pro di phising, truffe, ecc.) 
- Denial-of-Service (DoS) 
- Scansione e diffusione malware 
- Acquisizione informazioni

Le botnet si **propagano** prevalentemente grazie a *drive-by-download* che sfrutta browser e sistemi operativi vulenrabili.


# Elevazione dei privilegi
Nei sistemi UNIX come Linux o MacOS, per eseguire un comando da **superuser**, esistono 2 metodi:
- **Manuale**
	Prima si identifica come superuser, poi esegue il comando
```bash
	su -u
	# digita password superuser
	passwd bros
	# comando eseguito da superuser
```
- **Automatica**
	Il comando viene eseguito tutta in una volta, con prima l'identificazione da supersuser
```Bash
	sudo passwd bros #esegue il comando direttamente da superuser
```


Un sistema UNIX è formato da **demoni**, *utenti* che eseguono comandi, ma che non possono eseguire comandi in una bash, per questo devono essere configurati con *nologin*, se avessero il permesso di eseguire su una shell, quel demone potrebbe fare un **elevazione di privilegi**.


Oltre a normali permessi esiste un altro permesso, rappresentato dal bit SETUID:
- Rappresentazione ottale
e dal bit SETGUID:

SETUID $\to$ user ID di chi ha lanciato il programma se è attivo, rappresenta l'user ID del creatore del file
GROUPID $\to$ group ID primario di chi ha lanciato il comando, se attivo group ID primario del file.

é possibile cambiare la persona **effettiva** che esegue il file.

I sistemi UNIX il descrittore di un processo memorizza:

| **User ID Reale**                        | **Group ID Reale**                                  | **User ID Effettivo**                 | **Group ID Effettivo**                          |
| ---------------------------------------- | --------------------------------------------------- | ------------------------------------- | ----------------------------------------------- |
| User Id di chi ha lanciato<br>il comando | group ID primario di chi <br>ha lanciato il comando | user ID di chi ha lanciato il comando | group ID primario di chi ha lanciato il comando |

Se i bit di **SETUID e SETGID = 1** $\to$ **File = Effettivo**

![[Pasted image 20261113104453.png]]
Gli ID reali rappresentano gruppo e utemte di chi ha eseguito il file, invece quelli effettivi rappresentano l'utente che ha creato il file.


## MEDIAZIONE INCOMPLETA






