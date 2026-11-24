# Concorrenza e sincronizzazione

> Nota derivata da [[Informatica industriale]] — macro-argomento: **Modelli di concorrenza, memoria condivisa, mutex, semafori, producer/consumer, deadlock**.

---

## Due nature della concorrenza

| Tipo | Caratteristiche | Modello tipico |
|------|-----------------|----------------|
| **Competitive** | Attività competono per stessa risorsa; ignote l'una all'altra; OS gestisce sharing | Client/Server, allocazione **centralizzata** |
| **Cooperative** | Attività si conoscono, collaborano; condividono strutture dati; sincronizzazione esplicita | Shared-memory, allocazione **decentralizzata** |

> **Riferimento slide:** [[08 - Concurrency.pdf]]

---

## Modelli di concorrenza

### 1. Message Passing
- Nessuna memoria condivisa
- Due primitive:  
  `send(destination, message)`  
  `receive(source, &message)`
- Comunicazione **sincrona** (rendezvous) o **asincrona** (buffered)
- Ricezione:  
  - **Asimmetrica** — accetta da chiunque  
  - **Simmetrica** — attende mittente specifico
- **RPC (Remote Procedure Call)**: chiamata funzione eseguita su altro nodo
- Ogni risorsa gestita da un **daemon** thread dedicato

> **Esempi slide:**  
> - Scambio sincrono: [[08 - Concurrency.pdf#page=18|pagina 18]]  
> - Solo `send` asincrona: [[08 - Concurrency.pdf#page=19|pagina 19]]

---

### 2. Modello a memoria condivisa
- Risorse allocate **staticamente** o **dinamicamente**
- Accesso: **dedicato** (un solo thread) o **condiviso** (più thread)
- Problemi chiave: **Mutua esclusione** e **Data races**

#### Atomicità
> Un'istruzione è **atomica** se si esegue come unità indivisibile: o completa interamente, o non ha effetto; nessun altro thread ne osserva stato intermedio.

#### Critical Section
Porzione di codice che **un solo thread alla volta** può eseguire → regione atomica logica.  
Realizzata con:
- **Operazioni atomiche** (CAS, fetch-and-add, ecc.)
- **Semafori**
- **Mutex**

> **Riferimento slide:** [[08 - Concurrency.pdf#page=28|pagina 28]]

---

## Semafori (Dijkstra)

Oggetto con:
- **Contatore** $S$ (intero)
- **Coda** di thread bloccati

### `wait(S)` / `P(S)` / `down()`
```c
void wait(Semaphore S) {
    S.value--;                 // atomico
    if (S.value < 0) {
        // inserisci thread corrente in S.queue
        // blocca thread (suspend)
    }
}
```

### `signal(S)` / `V(S)` / `up()` / `post()`
```c
void signal(Semaphore S) {
    S.value++;                 // atomico
    if (S.value <= 0) {
        // estrai un thread P da S.queue
        // risveglia P (ready)
    }
}
```

> **Entrambe le operazioni devono essere atomiche** (supporto HW o kernel).

### Semaforo binario → Mutua esclusione
- Inizializzato a 1
- `wait` = lock, `signal` = unlock

### API POSIX
```c++
int sem_init(sem_t *sem, int pshared, unsigned int value);
int sem_destroy(sem_t *sem);
int sem_wait(sem_t *sem);           // blocca
int sem_trywait(sem_t *sem);        // non blocca (restituisce errore se S≤0)
```

---

## Mutex (Mutual Exclusion)
- Caso speciale di semaforo binario **ottimizzato per locking**
- Solo due stati: locked / unlocked
- Proprietà: **ownership** (solo chi ha lockato può sbloccare), **priority inheritance** (evita priority inversion), **robustness** (rilevamento abbandono)

### Esempio completo (da slide)
```c
#include <stdio.h>
#include <pthread.h>
#include <semaphore.h>

typedef struct {
    pthread_mutex_t* mut;
    char car[3];
    int id;
} Mutex;

void * body(void * arg);

int main() {
    pthread_t thread[3];
    pthread_attr_t myattr;
    int err;
    pthread_mutex_t mut;
    Mutex m[3];

    err = pthread_mutex_init(&mut, 0);

    for (int i = 0; i < 3; i++) {
        m[i].id = i;
        m[i].mut = &mut;
    }
    m[0].car[0] = '.';
    m[1].car[1] = '#';
    m[2].car[2] = 'o';

    pthread_attr_init(&myattr);
    for (int i = 0; i < 3; i++) {
        err = pthread_create(&thread[i], &myattr, body, (void*)&m[i]);
    }
    pthread_attr_destroy(&myattr);

    for (int i = 0; i < 3; i++) {
        pthread_join(thread[i], NULL);
    }
    err = pthread_mutex_destroy(&mut);
    return 0;
}

void * body(void * arg) {
    Mutex* m = (Mutex *) arg;
    pthread_mutex_lock(m->mut);
    for (int i = 0; i < 40; i++) {
        for (int j = 0; j < 20; j++) {
            printf("%c", m->car[m->id]);
        }
        printf("\n");
    }
    pthread_mutex_unlock(m->mut);
    return NULL;
}
```

> **Nota:** il mutex serializza l'output — ogni thread stampa 40 righe consecutive del proprio carattere.

---

## Pattern Producer / Consumer

- Buffer condiviso (spesso **array circolare**)
- Due ruoli: **producer** (scrive), **consumer** (legge)
- Primitive thread-safe: `push()`, `pop()`
- Due semafori necessari:
  1. **Sincronizzazione** — conta elementi disponibili (producer `signal`, consumer `wait`)
  2. **Mutua esclusione** — protegge struttura dati (mutex su head/tail/buffer)

> **Riferimento slide:** [[08 - Concurrency.pdf#page=48|pagina 48]]

### Deadlock
Blocco circolare: thread A aspetta risorsa di B, B aspetta risorsa di A.  
**Prevenzione:** evitare codice bloccante (`wait`, I/O, sleep) dentro **critical section**.

> **Riferimento slide:** [[08 - Concurrency.pdf#page=50|pagina 50]]

---

## Collegamenti
- [[Informatica industriale]] — Indice generale
- [[Programmazione parallela]] — Modelli threading, work queue
- [[Ingegneria software embedded]] — Pattern per concorrenza in embedded (State, HAL)