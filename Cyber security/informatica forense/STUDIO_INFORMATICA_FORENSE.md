# Struttura di Studio – Informatica Forense

> Mappa degli argomenti dalla nota [[INFORMATICA FORENSE]], slide del corso, e gap da integrare.

---

## 📚 Slide del corso (Cyber security/slide/Forense/)

| Slide | Titolo | Pagine stimate | Argomenti principali (da titolo) |
|-------|--------|----------------|----------------------------------|
| **L1_1** | Attori e accertamento nella procedura penale | ~20-25 | Attori processo penale, accertamenti, ruoli PM/Giudice/Imputato |
| **L1_2** | Attori e accertamenti nella procedura civile | ~10-15 | Differenze penale/civile, attori, CTU/CTP, onere della prova |
| **L2_1** | Elementi, ruolo e prospettive dell'Informatica forense | ~25-30 | Definizione, principi, catena di custodia, ruolo perito/CTP, scenari futuri |
| **L2_2** | Attendibilità del dato informatico | ~20-25 | Integrità, autenticità, non ripudio, hash, firma digitale, best practices |
| **L2_3** | L'approccio metodologico nell'informatica forense | ~30-35 | Metodologia NIST/ISO, fasi (identificazione, preservazione, analisi, presentazione), documentazione |
| **L2_4** | ISO 27037 | ~15-20 | Standard acquisizione dati digitali, linee guida, evidenza digitale, procedure |
| **L3_1** | Raccolta, trasporto, acquisizione e conservazione | ~35-40 | Sequestro, catena di custodia, imaging forense (dead/live), write blocker, hash verification, conservazione |

> **Totale slide:** 7 PDF | ~150-200 pagine complessive

---

## 🗂️ Mappatura: Nota [[INFORMATICA FORENSE]] ↔ Slide

| Sezione Nota | Contenuto attuale | Slide riferimento | Stato |
|--------------|-------------------|-------------------|-------|
| **Informatica in tribunale** | Attori penale (PM, Giudice GIP/GUP/Dibattimento, Imputato), Eventuali, Difensori, Ausiliari (Perito, CTP) | **L1_1** (penale), **L1_2** (civile) | ✅ Parziale (manca civile, dettagli ruoli) |
| **ANALISI** | 5W (chi, cosa, dove, quando, perché), strumenti SW/HW | **L2_3** (metodologia analisi) | 🟡 Solo intro |
| **ACQUISIZIONE DEI DATI** | Solo titolo | **L3_1**, **L2_4** (ISO 27037) | ❌ **Vuoto** |
| **SMARTPHONE / CRITTOGRAFIA** | FDE vs FBE, iOS Classi A-D, Stati BFU/AFU | (Probabile L3_1 o slide extra non in elenco) | 🟡 Parziale (manca Android, dettagli classi iOS, tool) |
| **PIATTAFORME COMMERCIALI** | UFED (Smart flow, Scelta estrazione) | (Slide non in elenco Forense) | 🟡 Solo accenno |
| **ACQUISIZIONE BFU su dispositivi bloccati** | Incompleto (tagliato a metà frase) | (Slide non in elenco) | ❌ **Incompleto** |

---

## ✅ Argomenti **già coperti** nella nota (da rivedere/approfondire con slide)

### 1. Procedura Penale – Attori e Ruoli
- [ ] PM: *dominus* indagini, archiviazione/rinvio a giudizio, imputazione
- [ ] Giudice: GIP (misure cautelari), GUP (udienza preliminare), Dibattimento
- [ ] Imputato: indagato → imputato, diritti (difensore, dichiarazioni spontanee, esame/controesame, silenzio, assenza)
- [ ] Difensore: fiducia/uffici, obbligatorietà
- [ ] Ausiliari: Perito (giudice) vs CTP (parti)

### 2. Smartphone – Crittografia e Stati
- [ ] FDE (Full Disk Encryption) – chiave unica volume
- [ ] FBE (File Based Encryption) – chiavi per file/gruppi
- [ ] iOS Classi protezione A/B/C/D (da completare con dettagli)
- [ ] Stati dispositivo: **BFU** (Before First Unlock) vs **AFU** (After First Unlock)
- [ ] UFED: Smart flow, Scelta estrazione

---

## 🟡 Argomenti **parziali/abbozzati** (integrare con slide)

### 3. Procedura Civile – Attori e Accertamenti (L1_2)
> **Gap totale nella nota** – Slide dedicata
- Differenze accertamento penale vs civile
- CTU (Consulente Tecnico d'Ufficio) vs CTP (Consulente Tecnico di Parte)
- Onere della prova, valutazione prova digitale in sede civile
- Procedimento di istruzione preventiva (art. 696 bis c.p.c.)

### 4. Elementi, Ruolo, Prospettive Informatica Forense (L2_1)
> **Manca del tutto nella nota**
- Definizione formale (NIST, ISO 27043)
- Principi cardine: **integrità, autenticità, non ripudio, ripetibilità**
- Catena di custodia (Chain of Custody) – documentazione, sigilli, log
- Ruolo Perito vs CTP – indipendenza, contraddittorio
- Prospettive: cloud forensics, IoT, AI/ML, anti-forensics

### 5. Attendibilità del Dato Informatico (L2_2)
> **Manca del tutto nella nota**
- Hash (MD5, SHA-1, SHA-256) – collision resistance, verifica integrità
- Firma digitale / timestamping (RFC 3161)
- Write blocker (hardware/software) – prevenzione alterazione
- Best practices: imaging bit-stream, hash source/target, log operazioni
- Referto peritale: struttura, requisiti forma, efficacia probatoria

### 6. Approccio Metodologico (L2_3)
> **Solo accenno "5W" nella nota**
- Modello NIST SP 800-86 / ISO 27043: **Identificazione → Preservazione → Analisi → Presentazione**
- Documentazione obbligatoria: case log, evidence log, tool log, report
- Validazione tool (NIST CFTT) – known/unknown test
- Analisi: timeline, artifact analysis, string search, file carving, registry, log correlation
- Reporting: executive summary, technical findings, conclusioni, allegati

### 7. ISO 27037 (L2_4)
> **Manca del tutto nella nota**
- Scopo: linee guida identificazione, raccolta, acquisizione, conservazione dati digitali
- Principi: proporzionalità, minimizzazione, documentazione, competenza
- Fasi: **Identificazione → Raccolta → Acquisizione → Conservazione → Trasferimento**
- Ruoli: first responder, forensic examiner, evidence custodian
- Metodi acquisizione: live vs dead, volatile vs non-volatile
- Ambienti: desktop, server, mobile, cloud, network, IoT

### 8. Raccolta, Trasporto, Acquisizione, Conservazione (L3_1)
> **Titolo solo nella nota – slide più corposa (35-40 pag)**
- **Sequestro**: verbale, descrizione dispositivo, stato (acceso/spento), foto
- **Trasporto**: buste antistatiche, faraday bag (mobile), catena del freddo se serve
- **Acquisizione**:
  - **Dead acquisition** (dispositivo spento): write blocker, imaging bit-stream (dd, E01, AFF4), hash verification
  - **Live acquisition** (acceso): RAM dump (LiME, WinPMEM), volatile data (processi, rete, chiavi crittografia), encrypted disk access
  - **Mobile**: logical vs physical vs file system extraction, BFU/AFU, lockscreen bypass
- **Conservazione**: cold storage, hash periodici, access control, disaster recovery
- **Formati**: E01 (EnCase), AFF4, RAW/dd – metadata, compressione, segmentazione

---

## ❌ Argomenti **mancanti del tutto** (da integrare da slide/altro)

| Argomento | Fonte probabile | Priorità |
|-----------|-----------------|----------|
| **Procedura civile completa** (L1_2) | Slide L1_2 | 🔴 Alta |
| **Principi forensi formali** (L2_1) | Slide L2_1 | 🔴 Alta |
| **Attendibilità/Hash/Write blocker** (L2_2) | Slide L2_2 | 🔴 Alta |
| **Metodologia NIST/ISO completa** (L2_3) | Slide L2_3 | 🔴 Alta |
| **ISO 27037 dettagliata** (L2_4) | Slide L2_4 | 🟠 Media |
| **Acquisizione completa** (L3_1) | Slide L3_1 | 🔴 Alta |
| **Android forensics** (file system, FBE, keystore, backup) | Slide/Extra | 🟠 Media |
| **iOS classi protezione dettaglio** (A: complete protection, B: unless open, C: until first unlock, D: no protection) | Slide/Extra | 🟠 Media |
| **Tool forensi open source** (Autopsy, Volatility, Plaso, sqlite3, regripper) | Slide/Extra | 🟢 Bassa |
| **Cloud forensics** (M365, Google Workspace, AWS/Azure logs) | Slide/Extra | 🟢 Bassa |
| **Network forensics** (PCAP, Zeek, flow analysis) | Slide/Extra | 🟢 Bassa |
| **Anti-forensics & countermeasures** (timestomping, encryption, wiping, steganography) | Slide/Extra | 🟢 Bassa |
| **Referto peritale / Deposizione in udienza** | Slide/Extra | 🟠 Media |

---

## 📋 Piano di Studio Consigliato

### Fase 1: Fondamentali Giuridici (Giorno 1-2)
1. Leggi **L1_1** – Attori processo penale → integra nota sezione "Informatica in tribunale"
2. Leggi **L1_2** – Attori processo civile → **crea nuova sezione** "Procedura Civile"
3. Confronta differenze penale/civile in tabella

### Fase 2: Principi e Metodologia Forense (Giorno 3-4)
4. Leggi **L2_1** – Elementi, ruolo, prospettive → **crea sezione** "Principi dell'Informatica Forense"
5. Leggi **L2_2** – Attendibilità dato → **crea sezione** "Integrità e Attendibilità della Prova Digitale"
6. Leggi **L2_3** – Approccio metodologico → **espandi sezione "ANALISI"** con metodologia completa NIST/ISO
6. Leggi **L2_4** – ISO 27037 → **crea sezione** "Standard ISO 27037"

### Fase 3: Acquisizione e Conservazione (Giorno 5-6)
7. Leggi **L3_1** – Raccolta, trasporto, acquisizione, conservazione → **riempi sezione "ACQUISIZIONE DEI DATI"** completamente
   - Sottosezioni: Sequestro, Trasporto, Dead Acquisition, Live Acquisition, Mobile, Conservazione, Formati
8. Integra **Smartphone** con dettagli da L3_1 (mobile forensics) + completamento classi iOS / Android

### Fase 4: Approfondimenti Tecnici (Giorno 7+)
9. Tool forensi (UFED dettagli, Autopsy, Volatility, ecc.)
10. Case study / esercizi pratici (imaging, hash, timeline, file carving)
11. Referto peritale: struttura, linguaggio, deposizione

---

## 🔗 Struttura Note Proposta (Obsidian)

```
Cyber security/informatica forense/
├── INFORMATICA FORENSE.md                    (nota originale - da ristrutturare)
├── STUDIO_INFORMATICA_FORENSE.md             (questa mappa)
├── 01_Procedura_Penale_Attori.md             (da L1_1 + nota esistente)
├── 02_Procedura_Civile_Attori.md             (da L1_2 - NUOVA)
├── 03_Principi_Informatica_Forense.md        (da L2_1 - NUOVA)
├── 04_Attendibilita_Prova_Digitale.md        (da L2_2 - NUOVA)
├── 05_Metodologia_Forense_NIST_ISO.md        (da L2_3 - espande "ANALISI")
├── 06_ISO_27037.md                           (da L2_4 - NUOVA)
├── 07_Acquisizione_Conservazione.md          (da L3_1 - riempie "ACQUISIZIONE DEI DATI")
├── 08_Mobile_Forensics_Smartphone.md         (espande sezione SMARTPHONE + L3_1 mobile)
├── 09_Piattaforme_Commerciali_UFED.md        (espande PIATTAFORME COMMERCIALI)
├── 10_Tool_Open_Source_Forensics.md          (NUOVA - extra)
├── 11_Referto_Peritale_Deposizione.md        (NUOVA - extra)
└── Riferimenti_Slide.md                      (tabella slide → sezioni note)
```

---

## 🎯 Prossimi Passi Operativi

1. **Apri ogni PDF slide** ed estrai indici/titoli sezioni principali
2. **Per ogni slide**: crea/aggiorna la nota tematica corrispondente sopra
3. **Usa wikilink bidirezionali** tra note (es. `[[07_Acquisizione_Conservazione#Dead Acquisition]]`)
4. **Embedda immagini chiave** dalle slide (`![[slide_L3_1_pag15_schema_writeblocker.png]]`)
5. **Aggiungi riferimenti pagina slide** in ogni sezione: `[[L3_1 - Raccolta, trasporto, acquisizione e conservazione.pdf#page=12|p.12]]`

---

## 📌 Note per l'integrazione

> **La nota originale `INFORMATICA FORENSE.md` va trattata come "bozza grezza"** – contiene buoni spunti (attori penale, crittografia smartphone, BFU/AFU) ma è **incompleta** su acquisizione, metodologia, civile, standard ISO.

**Strategia consigliata**: Non modificare direttamente la nota originale. Crea le **nuove note tematiche** (come da struttura proposta) e alla fine crea un **indice navigazione** tipo `[[Informatica Forense - Indice]]` che le collega tutte, deprecando la nota monolitica originale.

---

*Mappa generata da analisi nota `INFORMATICA FORENSE.md` + elenco slide `Cyber security/slide/Forense/` — Novembre 2026*