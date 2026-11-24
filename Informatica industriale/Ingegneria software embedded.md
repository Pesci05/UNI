# Ingegneria software embedded

> Nota derivata da [[Informatica industriale]] — macro-argomento: **SOLID per embedded, Design Patterns, State Pattern, HAL**.

---

## SOLID programming (adattato all'embedd)

Nato da OOP, in sistemi embedded **3 pilastri diventano critici**:

| Principio | Significato in embedded |
|-----------|-------------------------|
| **1. Single Responsibility** | Un modulo (file `.c` + `.h`) ha **una sola** ragion d'essere / funzionalità |
| **4. Interface Segregation** | Ogni funzionalità espone un'**interfaccia stretta** (`.h` minimale); client non dipende da metodi che non usa |
| **5. Dependency Inversion** | Moduli high-level **non dipendono** da low-level; entrambi dipendono da **astrazioni** (interfacce). Le dipendenze concrete iniettate in **un unico modulo** (composition root) |

> Gli altri due (Open/Closed, Liskov) restano validi ma meno vincolanti in C puro.

---

## Design Patterns in embedded

### Cosa **danno**
- **Vocabolario condiviso** tra sviluppatori
- Risolvono problemi ricorrenti **prima** che diventino debiti tecnici
- Base per **scelte di design documentate e difendibili**

### Cosa **NON danno**
- Soluzione **esatta** per ogni progetto (vanno adattati)

### Ti **forzano** a
1. Tradurre il **dominio** in codice (ubiquitous language)
2. Decidere **granularità** degli oggetti/moduli
3. Definire chiaramente **interfacce (`.h`)** e **implementazioni (`.c`/`.cpp`)**
4. Scrivere codice **riutilizzabile** e testabile

### Struttura di un pattern (GoF)
1. **Nomi, scopi, alias**
2. **Motivazione** (problema reale)
3. **Applicabilità** (quando usarlo)
4. **Struttura** (diagramma classi/oggetti)
5. **Partecipanti** + **Collaborazioni**
6. **Implementazione** (code snippets, trade-off)
7. **Esempi noti**, **pattern correlati**, **effetti collaterali**

---

## State Pattern — Implementare FSM pulite

**Problema:** `switch`/`if` annidati per gestire stati → codice illeggibile, fragile, difficile da estendere.

**Soluzione:**
- **Un modulo per stato** (es. `State_Idle.c`, `State_Running.c`, `State_Error.c`)
- Ogni modulo implementa le **azioni** di quel stato (`on_entry`, `on_event`, `on_exit`)
- **Context** (oggetto macchina) delega allo stato corrente
- Transizioni = cambio puntatore a stato

**Vantaggi:**
- `main` / loop principale **ordinato** (solo `currentState->handle(event)`)
- **Struttura progetto elegante**, aperto a nuovi stati (OCP)
- Testabilità: ogni stato testabile in isolamento

> **Riferimento:** classico GoF *State Pattern*; in embedded spesso senza allocazione dinamica (stati `static const`).

---

## HAL — Hardware Abstraction Layer

> **Scopo:** separare **logicamente** software da hardware → **stesso codice applicativo** su piattaforme diverse.

### Architettura a due livelli

```
┌─────────────────────┐
│   Application       │  ← usa solo interfacce astratte (API)
├─────────────────────┤
│   HAL Interface     │  ← .h puri: init(), read(), write(), config()
│   (Proxy)           │     tipi opachi, nessuna dipendenza HW
├─────────────────────┤
│   HAL Implementation│  ← una per piattaforma (STM32, ESP32, Linux, …)
│   (Adapter)         │     mappa API → register map / driver vendor
└─────────────────────┘
```

| Componente | Ruolo |
|------------|-------|
| **Proxy** (in HAL Interface) | Espone **API neutre**; definisce struct opachi (`typedef struct I2C_Handle I2C_Handle;`); inoltra chiamate all'adapter |
| **Adapter** (in HAL Impl) | Implementa API per **specifico HW**: mappa `i2c_write()` → `HAL_I2C_Master_Transmit()` (STM32) o `Wire.write()` (Arduino) |

### Vantaggi concreti
- **Portabilità**: cambiare MCU = riscrivere solo adapter, non app
- **Testabilità**: mock dell'interfaccia HAL → unit test su host (Linux)
- **Disaccoppiamento**: app non include header vendor (`stm32f4xx_hal.h`)

> **Riferimento slide:** ![[Pasted image 20261109152041.png]]

---

## Collegamenti
- [[Informatica industriale]] — Indice generale
- [[Concorrenza e sincronizzazione]] — Primitive per task/ISR in embedded (mutex, semafori)
- [[PLC e automazione industriale]] — Embedded reale in automazione (PLC = embedded specializzato)