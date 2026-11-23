---
name: debug-segfault-and-ub
description: Diagnostica errori di basso livello in C/C++, Segmentation Fault, Undefined Behavior, memory leak, race condition e problemi di build/Makefile. Usa questa skill quando l'utente incolla un crash, un output di GDB/Valgrind o chiede perché un programma C/C++ si comporta in modo anomalo.
---

# Low-Level Debugging & Memory Diagnostics

Quando analizzi un bug o un crash in C/C++ o sistemi Unix/Linux:

1. **Diagnosi della causa radice (Root Cause)**:
   - Spiega *esattamente* cosa succede in memoria (Stack, Heap, Data/BSS segment, dereferenziazione di puntatore invalido, buffer overrun, dangling pointer, data race).
   - Non limitarti a dire "c'è un segfault alla riga X": indica quale operazione viola i permessi di memoria o lo standard del linguaggio.
2. **Verifica con strumenti da terminale**:
   - Fornisci i comandi esatti per riprodurre e isolare il problema su Linux (es. compilazione con `-Wall -Wextra -g -fsanitize=address,undefined` oppure esecuzione sotto `valgrind --leak-check=full`).
3. **Soluzione pulita**:
   - Mostra il diff o la funzione corretta spiegando perché la modifica risolve definitivamente il problema senza introdurre nuovi leak.
