---
name: vault-course-linker
description: Collega una nota universitaria appena creata alle altre note già presenti nella cartella del corso, inserendo Wikilink pertinenti e una sezione di concetti correlati. Usa questa skill quando l'utente chiede di collegare una nota al resto del corso o integrarla nel vault.
---

# Obsidian Course Linker

Quando l'utente chiede di collegare una nota al resto del corso:

1. **Esplora la cartella del corso**: leggi i titoli, gli header (`#`, `##`) e i tag delle altre note `.md` presenti nella stessa directory (o nelle sottocartelle dell'esame).
2. **Inserisci collegamenti contestuali**:
   - Nel testo della nota corrente, trasforma i riferimenti a concetti già trattati altrove in `[[Nome Nota]]` o `[[Nome Nota|alias naturale]]`, senza forzare link ridondanti.
   - Se una nota precedente cita un concetto approfondito nella nota attuale, proponi o aggiungi il backlink reciproco.
3. **Aggiungi il blocco finale**: inserisci in fondo alla nota una sezione `## Collegamenti nel corso` con massimo 4-5 link puntati accompagnati da una riga che spiega il nesso logico (es. prerequisito, dimostrazione, applicazione pratica).
