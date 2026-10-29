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


# Modello a memoria condivisa
Le risorse in memoria condivisa possono essere allocate in modo:
- **statico**
- **dinamico**
L'accesso alla risorsa può essere:
- **Dedicato**
- **Condiviso**
## Mutua esclusione e Data races
Un problema di questo modello è la **Mutua esclusione** e **data races**.

Questo è un problema quando le operazioni fatte da un thread non sono atomiche.
[[08 - Concurrency.pdf#page=28|08 - Concurrency, pagina 28]]

Un'istruzione si definisce **atomica**, viene eseguita come un'**unità singola e indivisibile o viene completata interamente, oppure non viene eseguita affatto**, senza che nessun altro processo o thread possa intercettarla, modificarne lo stato intermedio o interromperla a metà.

Una **critical section** è una porzione di codice deve operare soltanto un thread alla volta, deve essere visto come una **regione atomica** di codice, questo significa che la risorsa che i thread devono lavorare deve avere un accesso di tipo **mutua esclusione**, questo si può fare con:
- **Opreazioni atomiche**
- **Semafori**
- **Mutex**

## Semafori
Meccanismo proposto da Djikstra.

Un **semaforo** è un oggetto, che consiste in:
- **contatore**
- **una coda**

Con 2 funzioni principali:
- **Wait**
	1. Decrementa il valore del semaforo: 𝑆 =𝑆 −1.
	2. **Se 𝑆 <0**: il contatore indica che non ci sono risorse disponibili. Il thread chiamante viene **bloccato** (sospeso) e inserito nella coda del semaforo.
	3. **Se 𝑆 ≥0**: la risorsa è disponibile, il thread decremente il valore e continua l'esecuzione senza bloccarsi
	- **Logica concettuale:**

```c
void wait(Semaphore S) {
    S.value--;
    if (S.value < 0) {
        // aggiungi il thread chiamante a S.queue;
        // blocca il thread (block/suspend);
    }
}
```

- **Signal**(Post):
	Viene chiamata quando un thread finisce di utilizzare un risorsa così da **rilasciarla**
	1. Incrementa il valore del semaforo: 𝑆 =𝑆 +1.
    2. **Se 𝑆 ≤0**: significa che c'era almeno un thread bloccato in attesa nella coda del semaforo. Ne estrae uno dalla coda e lo **risveglia** (lo passa allo stato _ready_).
    3. **Se 𝑆 >0**: non c'erano thread in attesa, il permesso restituito rimane disponibile per richieste future.
	- **Logica concettuale:**
```c
void signal(Semaphore S) {
    S.value++;
    if (S.value <= 0) {
        // rimuovi un thread P dalla coda S.queue;
        // risveglia il thread P (wakeup/unblock);
    }
}
```

>Queste operazioni devono essere gestite come **operazioni atomiche**

Per implementare una **Muta esclusione** si utilizza un **semaforo binario**.

**Init**: Inizializzare un semaforo:
```c++
int sem_init(sem_t *sem, int pshared, unsigned int value);
int sem_destroy(semt_t *sem);
```

**Wait** di un semaforo:
```c++
int sem_wait(sem_t* sem);
int sem_trywait(sem_t* sem); //funzione non bloccante
```


## MUTEX
Sono na struttura dati che si utilizzano soltanto per la **mutua esclusione**.
**Eempio Mutex:**
```c
#include <stdio.h>
#include <pthread.h>
#include <semaphore.h> 

typedef struct
{
    pthread_mutex_t* mut;
    char car[3];
    int id;
}Mutex;

void * body(void * arg);

int main()
{
    pthread_t thread[3];
    pthread_attr_t myattr;
    int err;
    pthread_mutex_t mut;
    Mutex m[3];

    err = pthread_mutex_init(&mut,0);

    for(int i = 0; i < 3 ;i++){
        m[i].id = i;
        m[i].mut = &mut;
    }
    m[0].car[0] = '.';
    m[1].car[1] = '#';
    m[2].car[2] = 'o';

    pthread_attr_init(&myattr);
    
    for(int i = 0; i < 3; i++){
        err = pthread_create(&thread[i],&myattr,body,(void*)&m[i]);
    }

    /*err = pthread_create(&t1, &myattr, body, (void *)&s1); // Boxing of parameters

    err = pthread_create(&t2, &myattr, body, (void *)&s2);

    err = pthread_create(&t3, &myattr, body, (void *)&s3);*/
    pthread_attr_destroy(&myattr);

    for(int i = 0; i < 3; i++){
        pthread_join(thread[i],NULL);
    }

    err = pthread_mutex_destroy(&mut);
    return 0;
}
void * body(void * arg)
{
    Mutex* m = (Mutex *) arg; // Unboxing of function params
    pthread_mutex_lock(m->mut);
    //printf("%d",s->id);
    for (int i=0; i<40; i++)
    {
        for (int j=0; j<20; j++)
        {
            printf("%c", m->car[m->id]);
        }
        printf("\n");
    }
    pthread_mutex_unlock(m->mut);
}
```

E' un **semaforo binario**, specializzato nelle **mutue esclusioni**.

# Pattern producer/consumer
Per implementare questo tipo di pattern di programmazione, si deve implementare una **libreria**.

Questo tipo di pattern viene utilizzato soprattutto sulle risorse che vengono condivise tra più thread.
Per implementare un array circolare gestito da più array in pattern producer consumer, deve essere gestito da **funzioni primitive**(pop,push), e queste funzioni devono essere gestite da:
- Semaforo per gestire la **sincronizzazione tra producer e consumer**
- Semaforo per proteggere la **struttura data**
Questi thread devono essere gestiti da dei semafori che però possono casuare un **deadlock**, evento che causa il completo blocco di un programma.
[[08 - Concurrency.pdf#page=48|08 - Concurrency, pagina 48]]

Per ovviare al deadlock, si deve **evitare di** **inserire parti di codice bloccante** all'interno di una critical sections.
[[08 - Concurrency.pdf#page=50|08 - Concurrency, pagina 50]]



