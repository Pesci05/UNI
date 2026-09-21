**Automazione industriale**: insieme di discipline che permettono di analizzare e progettare e controllare un sistema di automazione

**Sistema di automazione/automatico di controllo**: sistema che permette di eseguire una certa operazione senza il diritto intervento dell'uomo.

Questo per far eseguire un certo tipo di lavori alle **macchine** in modo automatico, con solo una supervisione dell'uomo.
Si preferiscono utilizzare le macchine al posto degli umani in casi come:
- **operazioni di precisione** che richiedono **velocità** e **potenze** impossibili per l'uomo
- **sicurezza**

Un sistema di automazione è formato da una **componente operativa**(componenti meccanici progettati per interagire con il prodotto), da un **Unità di controllo** (computer con funzionalità di acquisire e trasmettere dati da sensori ad attuatori), da **sensori** e **attuatori**.

Un sistema di automazione, in caso di sistemi più complicati, si può **dividere** in **più moduli**, dove ogni modulo si occupa di un lavoro diverso, e infine **coordinare** l'insieme di tutti i moduli.

Far si che una macchina faccia ciò che vogliamo, deve rispondere ad un **problema di controllo**(un funzionamento designato), per un **processo**(impianto, apparecchiatura, macchina o fenomeno di natura fisica) e deve avere un **funzionamento desiderato** (che le variabili del processo del tempo coincidano con le variabili **preassegnate**).

## Sistema di controllo

**Controllore**: dispositivo che determina l'andatemento del sistema tramite variabili di controllo.
Il controllore deve mantenere le variabili di controllo uguali a quelle di riferimento(nella realtà ci sarà uno scarto che verrà considerato come **tolleranza**).

Per controllare un sistema esistono 2 **modalità**:
- **controllo in catena aperta**
	Il comportamento del sistema dipende **solo dalla conoscenza dell'impianto**, il controllore possiede informazioni solo sui segnali di riferimento e sul disturbo
- **controllo in retorazione/catena chiusa**
	Il comportamento del sistema dipende oltre che ==**dalla consocenza dell'impianto**== e i segnali di riferimento, variano anche in base alle **==misurazioni==** che forniscono i sensori.

![[Pasted image 20260226102946.png]]

Per progettare un controllore bisogna:
1. Costruire un **modello del sistema**
2. Definire i segnali **che corrispondono alle grandezze fisiche da controllare**
3. Definire le **specifiche del progetto** per il sistema controllato
4. Progettare un **algoritmo di controllo** basato sul modello del sistema, sui segnali disponibili e sulle specifiche
5. **Verificarne** il comportamento mediante **tecniche di simulazione**
6. Realizzare il **sistema fisico** che implementa il controllo

