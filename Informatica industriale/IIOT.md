# MACCHINE A SISTEMI FINITI (AUTOMI)
#05/10 
Hanno una struttura rigida e il loro funzionamento vien descritto tramiti grafici.

# PROCESSI SINCRONI/ASINCRONI
- **Sincrono**
	Estremamente veloce e reattivo, ma è uno spreco di risorse 

- **Asincrono**
	Implementabile tramite **yield**, e **sleep**.
	[[02 - Automata and machines.pdf#page=31|02 - Automata and machines, pagina 31]]

# PARALLEL PROGRAMMING
- **PARALLEL COMPUTING**
	Stesso computer ma utilizzando più processi/thread
- **DITRIBUTED COMPUTING**
	Lavorare con più computer
- **SPEED UP**
	Risolvere lo stesso algoritmo, ma più velocemente
- **SCALE UP**
	Risolvere un algoritmo più complicati ma dividenolo in più problemi più piccoli

## MOTIVI PER CUI SI PREFERISCE IL PARALLELO
1. **Economico**
	I costi di produzione di un processore più veloce, rispetto ad un processore multi-core è molto maggiore
2. **Fisico**
	Questo è un limite che viene definita dalle leggi di **Moore** e **Dennard**

Per rendere più veloce un software, non si può solo aumentare un il clock, infatti si è passati al calcolo in parallelo, però per passare a questo tipo di calcolo le **architetture si devono cambiare** e deve essere il **programma a renderle ottimizzate**.
Per questo i programmatori **devono** sapere l'architettura ibettivo del software.

## Legge di Amdahl
Per quanto un programma possa essere parallelizzato, ci sarà sempre un porzione di codice fissa e non parallelizzabile che non piò essere annullata.

# TIPI DI MULTIPROCESSO
- **SIMMETRICO**
	Ogni core è uguale all'altro, e sono collegati tramite un bus
	![[Pasted image 20261005151438.png]]
- **ASSIMETRICO**
	I core di una CPU sono divisi in 2 osttosinstemi, dove un gruppo può essere uno più veloce dell'altro, solitamente con archotettura di tipo ARM
	![[Pasted image 20261005151457.png]]
- **MEMORIA DISTRIBUITA**
	Ogni core deve avere una o più **memorie cache**, queste sono sempre più veloce quando sono vicine al core ma sono anche molto piccole, più ci si allontana dal core, più le cache diventano grandi ma anche lente, fino ad arrivare alla RAM se il dato non si trova all'interno delle cache.
## DEFINIZIONI
- **CORE**
	Integrato con una ALU,RAM etc...
- **PROGRAMMA**
	Implemetazione di un algoritmo
- **PROCESSO**
	Istanza di programma
- **THREAD**
	Unità di esecuzione del processo
- **TASK**
	Parte del programma (sottoinsieme d'istruzioni)
[[07 - Parallel programming.pdf#page=20|07 - Parallel programming, pagina 20]]

## THREADING MODEL
Un modo per utilizzare il multi thread è il metodo **fork-join**, dove il thread main viene chiamata **MASTER**, e i thread generati vengono chiamati **slaves**, grazie alle funzioni **join**(elimina/unisce thread) e **fork**(genera thread).

## DIVIDERE I COMPITI
Per assegnare i compiti ai thread ci sono 3 modi:
- **[[#DATA PARALLELISMO|Data parallelismo]]**

- **Task parallelismo**

- **Offloading**

### DATA PARALLELISMO
Dividere i compiti in modo uguale tra tutti i thread, assumendo che il carico di lavoro sia uguale tra i thread, e che tutti ci impieghino tutti lo stesso tempo.
I thread fanno tutti lo **stesso lavoro**.
La parte del dato su cui i thread lavorano si chiamo **chunk**, e il modo in cui vengono divisi si chiama **partitioning strategy**.
La dimensione del chunk viene calcolata $chunk = \frac{N}{T}$
- N = Numero di elementi
- T = numero di thread

Ogni thread deve sapere che thread è, perché non sarebbe possibile dividere la memoria in base al numero di thread, questo è implementabile grazie ad un **identificatore**.

Però è possibile che un thread possa avere **più lavoro** da fare rispetto agli altri, questo significa che questo thread ci impiegherà **più tempo a completare il lavoro**, questo può portare agli altri thread di finire prima e quindi che non **stia facendo nulla**.
![[Pasted image 20261020104024.png|427]]

Per evitare che si sia un thread a riposo, si deve dare lavoro al thread in modo **dinamico**, così che nessun thread abbi a un momento morto.
![[Pasted image 20261020104300.png|339]]

Per implementare questo tipo di divisione di lavoro, si deve implementare la **coda di lavoro**.
Dove il lavoro viene visto come un'**unità**, e vengono gestite da delle funzione come **q_push** e **q_pop**.
Questa coda è una **risorsa condivisa**, thread safe.


| **Creational Threading** | **Sybchronization**        |
| ------------------------ | -------------------------- |
| Fork-join                | Barrier                    |
| Master-slave             | Critical-section/atomic    |
| Team of threads          | Locks, semaphores, mutexes |
| **Work partitioning**    | **Behavioral**             |
| Data-parallelismo        | Producer-consumer          |
| Reduction                | Collaborative              |
| Tasking/queue            | Competitive                |
| Offloading               |                            |

# CONCORRENZA
Viene utilizzata per scelte sia **funzionali** sia di **performance**.

Esistono due tipi di concorrenza:
- **Competitive**
	- Diverse attività competono per la stessa risorsa
	- Un'attività non sa nulla sulle altre
	- L'OS deve gestire la condivisione delle risorse tra le varie attivitò

- **Cooperative**
	- Più attività cooperano per fare un'operazione
	- Ogni attività sà delle altre attività
	- Devono sincronizzarsi in particali eventi

## COMPETITIVE
Ogni attività deve essere **protetta** dalle altre.
L'**allocazione** delle risorse e la sincronizzazione deve essere **centralizzata**.
Si basa sul modello **Client/Server**.

## COOPERATIVE
Ogni attività **conosce** le altre attività, significa che non hanno bisogno di una protezione sulla memoria.
Devono avere accesso alle stesse strutture dati.
- Allocazione delle risorse è **decentralizzato**
- Modello **shared-memory**
Molto simile ai modelli thread.

## MODELLI DI CONCORRENZA
### MESSAGE PASSING
---
Si basa sul concetto di messaggio, con 2 operazioni fondamentali:
- **send(destination, message)**
- **receive(source, &message)**
In questo modello non c'è condivisione di memoria.
La comunicazione di un messaggio può essere **sincrona** o **asincrona**.
La ricezione di un dato può essere:
- **asimmetrica** 
	Ricevo da tutti non importa da chi.
- **simmetrica**
	Ricevo solo da un certo mittente ascoltando solo lui.
Esistono anche le **Remote procedure call**, cioè una chiamata di una funzione che non viene eseguita dal programma che la chiama, ma viene eseguita da un altro computer.

Ogni risorse devono avere un thread che le gestisce, chiamato **deamon**, ed è responsabile di dare accesso alle risorse.

Esempio di uno scambio di messaggi **sincroni**:[[08 - Concurrency.pdf#page=18|08 - Concurrency, pagina 18]]
Esempio di uno scambio di messaggi con solo **send asincrona**: [[08 - Concurrency.pdf#page=19|08 - Concurrency, pagina 19]]


# POSIX
I POSIX Threads sono chiamati **PTHreads**, e sono un modello di esecuzione che esiste **indipendentemente dal linguaggio di programmazione**, come **modello di esecuzione in parallelo**.

Specifica ad un Sistema Operativo un'**interfaccia** simile ai sistemi UNIX.
POSIX mantiene una differenza tra **thread** e **processi**.
Ogni processi ha almeno un thread detto **main**, tutti i thread **condividono** lo steso indirizzo di memoria, ma mantengono uno **stack privato**.
[[Lab_PThreads.pdf#page=4|Lab_PThreads, pagina 4]]

