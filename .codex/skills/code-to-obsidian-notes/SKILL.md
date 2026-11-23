---
name: code-to-obsidian-notes
description: Genera una nota di studio formattata per Obsidian a partire da uno o più file di codice o da un progetto universitario. Usa questa skill quando l'utente chiede di documentare codice per lo studio o creare appunti da un laboratorio.
---

# Code to Obsidian Study Note

Analizza i file di codice indicati dall'utente e genera un file Markdown (`.md`) ottimizzato per essere salvato direttamente in un vault di Obsidian:

1. **Struttura del documento**:
   - Titolo `# Laboratorio: <Nome Progetto/Argomento>` + tag YAML frontmatter (`tags: [uni, lab, codice]`).
   - `## Obiettivo e Architettura`: spiegazione ad alto livello di cosa fa il programma e come interagiscono i moduli/funzioni.
   - `## Diagramma di flusso / Architettura`: un blocco ````mermaid` (`flowchart TD` o `sequenceDiagram`) che illustra l'esecuzione principale.
   - `## Analisi delle funzioni chiave`: per ogni funzione critica, spiega firma, logica interna, scelte implementative e complessità $O(\cdot)$.
   - `## Trappole e concetti d'esame`: inserisci un callout `> [!warning] Punti critici` con eventuali insidie legate a puntatori, concurrency, system call o protocolli usati nel codice.
2. **Stile**: usa linguaggio tecnico universitario italiano, blocchi di codice con syntax highlighting corretto e formule LaTeX per eventuali calcoli di complessità o prestazioni.
