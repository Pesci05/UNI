---
name: exam-exercise-generator
description: Genera tracce d'esame di programmazione con scheletro del codice e test suite automatica per esercitarsi. Usa questa skill quando l'utente vuole allenarsi per una prova pratica o un esame di laboratorio.
---

# University Exam Exercise Generator

Partendo dal codice o dall'argomento specificato dall'utente:

1. **Crea una traccia d'esame realistica**:
   - Definisci chiaramente specifica funzionale, prototipi delle funzioni richieste, vincoli su librerie ammesse e requisiti di complessità o gestione memoria.
2. **Prepara l'ambiente di test**:
   - Genera uno scheletro di file sorgente (es. `soluzione.c` o `soluzione.py`) con le firme pronte.
   - Genera un file di test separato (es. `test_esame.c` con `assert.h` o `test_esame.py` con `pytest`/`unittest`) che copra almeno 6 casi: casi nominali, input limite, input invalidi e stress test.
3. **Non scrivere la soluzione nel file sorgente**: lascia la funzione vuota con un commento `// TODO: implementa qui` in modo che l'utente possa scriverla autonomamente e lanciare subito i test da terminale.
