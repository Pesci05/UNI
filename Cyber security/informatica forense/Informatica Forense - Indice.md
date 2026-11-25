# Informatica Forense – Indice di Navigazione

> Hub centrale per lo studio dell'Informatica Forense. Collega slide, note tematiche, e mappa di studio.

---

## 📎 Accesso Rapido

| Risorsa | Link |
|---------|------|
| **Mappa studio completa** | [[STUDIO_INFORMATICA_FORENSE]] |
| **Nota originale (bozza)** | [[INFORMATICA FORENSE]] |
| **Cartella slide** | `Cyber security/slide/Forense/` |

---

## 📚 Slide del Corso (7 PDF)

| Codice | File | Note tematiche collegate |
|--------|------|--------------------------|
| **L1_1** | `Attori e accertamento nella procedura penale.pdf` | [[01_Procedura_Penale_Attori]] |
| **L1_2** | `Attori e accertamenti nella procedura civile.pdf` | [[02_Procedura_Civile_Attori]] |
| **L2_1** | `Elementi, ruolo e prospettive dell'Informatica forense.pdf` | [[03_Principi_Informatica_Forense]] |
| **L2_2** | `Attendibilità del dato informatico.pdf` | [[04_Attendibilita_Prova_Digitale]] |
| **L2_3** | `L'approccio metodologico nell'informatica forense.pdf` | [[05_Metodologia_Forense_NIST_ISO]] |
| **L2_4** | `ISO 27037.pdf` | [[06_ISO_27037]] |
| **L3_1** | `Raccolta, trasporto, acquisizione e conservazione.pdf` | [[07_Acquisizione_Conservazione]], [[08_Mobile_Forensics_Smartphone]] |

---

## 🗂️ Note Tematiche (Struttura Consigliata)

### Fondamenti Giuridici
- [[01_Procedura_Penale_Attori]] — PM, Giudice (GIP/GUP/Dibattimento), Imputato, Difensori, Ausiliari (Perito/CTP)
- [[02_Procedura_Civile_Attori]] — CTU, CTP, onere prova, differenze penale/civile, art. 696 bis c.p.c.

### Principi e Standard Forensi
- [[03_Principi_Informatica_Forense]] — Definizione NIST/ISO, integrità/autenticità/non ripudio/ripetibilità, catena di custodia, ruoli perito/CTP
- [[04_Attendibilita_Prova_Digitale]] — Hash (MD5/SHA), firma digitale, timestamping, write blocker, imaging bit-stream, referto peritale
- [[05_Metodologia_Forense_NIST_ISO]] — 4 fasi NIST SP 800-86 (Identificazione, Preservazione, Analisi, Presentazione), documentazione, validazione tool
- [[06_ISO_27037]] — Identificazione → Raccolta → Acquisizione → Conservazione → Trasferimento, ruoli, metodi live/dead, ambienti

### Acquisizione e Conservazione (Core Tecnico)
- [[07_Acquisizione_Conservazione]] — Sequestro, trasporto, **dead acquisition** (write blocker, E01/AFF4/RAW, hash), **live acquisition** (RAM dump, volatile data), conservazione, formati
- [[08_Mobile_Forensics_Smartphone]] — **Android/iOS**, FDE vs FBE, classi protezione iOS (A/B/C/D), stati BFU/AFU, extraction logical/physical/filesystem, lockscreen bypass

### Tool e Pratica
- [[09_Piattaforme_Commerciali_UFED]] — UFED (Smart flow, Scelta estrazione), Cellebrite, Magnet AXIOM, Oxygen Forensic
- [[10_Tool_Open_Source_Forensics]] — Autopsy, Volatility, Plaso/log2timeline, sqlite3, regripper, bulk_extractor, ewf-tools
- [[11_Referto_Peritale_Deposizione]] — Struttura referto, linguaggio tecnico-giuridico, deposizione in udienza, controesame

---

## 🔗 Collegamenti Trasversali (da integrare in ogni nota)

| Argomento | Note correlate |
|-----------|----------------|
| **Catena di custodia** | 03, 04, 06, 07 |
| **Hash / Integrità** | 04, 07, 08 |
| **Acquisizione live vs dead** | 06, 07, 08 |
| **Scrittura referto** | 03, 04, 11 |
| **Procedura penale vs civile** | 01, 02 |
| **Mobile forensics** | 07, 08, 09 |

---

## 📅 Piano Studio (da [[STUDIO_INFORMATICA_FORENSE]])

| Fase | Giorni | Focus | Slide |
|------|--------|-------|-------|
| **1. Fondamentali Giuridici** | 1-2 | Attori penale/civile | L1_1, L1_2 |
| **2. Principi e Metodologia** | 3-4 | Definizioni, attendibilità, NIST/ISO, ISO 27037 | L2_1, L2_2, L2_3, L2_4 |
| **3. Acquisizione Core** | 5-6 | Sequestro, imaging, live, mobile, conservazione | L3_1 |
| **4. Approfondimenti** | 7+ | Tool, referto, case study, cloud/network/anti-forensics | Extra |

---

## 🎯 Stato Avanzamento

| Nota | Stato | Slide rif. |
|------|-------|------------|
| [[01_Procedura_Penale_Attori]] | 🟡 Da creare (base in [[INFORMATICA FORENSE]]) | L1_1 |
| [[02_Procedura_Civile_Attori]] | 🔴 **Manca** (solo in L1_2) | L1_2 |
| [[03_Principi_Informatica_Forense]] | 🔴 **Manca** (solo in L2_1) | L2_1 |
| [[04_Attendibilita_Prova_Digitale]] | 🔴 **Manca** (solo in L2_2) | L2_2 |
| [[05_Metodologia_Forense_NIST_ISO]] | 🟡 Parziale (5W in [[INFORMATICA FORENSE]]) | L2_3 |
| [[06_ISO_27037]] | 🔴 **Manca** (solo in L2_4) | L2_4 |
| [[07_Acquisizione_Conservazione]] | 🔴 **Manca** (titolo solo in [[INFORMATICA FORENSE]]) | L3_1 |
| [[08_Mobile_Forensics_Smartphone]] | 🟡 Parziale (crittografia, BFU/AFU in [[INFORMATICA FORENSE]]) | L3_1 |
| [[09_Piattaforme_Commerciali_UFED]] | 🟡 Abbozzo (in [[INFORMATICA FORENSE]]) | — |
| [[10_Tool_Open_Source_Forensics]] | 🔴 **Manca** | — |
| [[11_Referto_Peritale_Deposizione]] | 🔴 **Manca** | — |

---

## 📝 Come Usare Questo Indice

1. **Apri [[STUDIO_INFORMATICA_FORENSE]]** per il piano dettagliato e gap analysis
2. **Segui le fasi** in ordine (giuridico → principi → acquisizione → tool)
3. **Per ogni slide**: leggi PDF → crea/aggiorna nota tematica → linka qui
4. **Usa wikilink** `[[nome_nota#sezione]]` per salti precisi
5. **Embedda immagini chiave** dalle slide: `![[slide_L3_1_pag15_writeblocker.png]]`

---

*Indice generato Novembre 2026 — Basato su `INFORMATICA FORENSE.md` + 7 slide in `Cyber security/slide/Forense/`*