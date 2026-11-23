Analizza {selection} (oppure {activeNote}) e genera un diagramma **Mermaid** pulito e sintatticamente valido per Obsidian che rappresenti il flusso, l'architettura o la macchina a stati descritta.

Vincoli tecnici:
- Scegli il tipo più adatto: `flowchart TD` (processi/algoritmi), `stateDiagram-v2` (FSM/automi), `sequenceDiagram` (protocolli/chiamate di sistema) o `classDiagram` (architetture software).
- Racchiudi sempre le etichette dei nodi tra virgolette doppie `["Testo nodo"]` per evitare errori di parsing con parentesi o caratteri speciali.
- Mantieni i nodi concisi (max 4-5 parole per nodo).
- Sotto il blocco ````mermaid`, aggiungi una legenda in massimo 5 punti elenco che riassuma i passaggi critici.
