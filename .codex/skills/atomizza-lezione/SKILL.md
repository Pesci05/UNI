---
name: atomizza-lezione
description: Suddivide una nota universitaria lunga o una sbobina grezza in più note atomiche separate per singolo concetto/teorema, creando una nota indice principale. Usa questa skill quando l'utente chiede di dividere, atomizzare o riorganizzare un file di appunti molto lungo.
---

# Atomic Lecture Splitter

Quando l'utente chiede di dividere una nota lunga in argomenti separati:

1. **Analizza la struttura**: identifica i blocchi concettuali autonomi (es. singole definizioni, teoremi con dimostrazione, algoritmi, protocolli) e presenta prima un breve piano dei file che verranno creati.
2. **Crea le note atomiche**:
   - Genera un file `.md` per ciascun sotto-argomento nella stessa cartella, con frontmatter YAML (`tags`, `corso`), formule LaTeX pulite e callout Obsidian (`> [!important]`, `> [!warning]`).
3. **Trasforma la nota originale in un indice (MOC)**:
   - Mantieni nella nota di partenza una panoramica della lezione con l'elenco ordinato dei `[[Wikilink]]` alle nuove note create e una breve sintesi di 1 riga per ciascuna.
