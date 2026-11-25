# Termodinamica di base

> Nota derivata da [[Macchine e Sistemi Energetici]] — macro-argomento: **Sistemi, funzioni di stato, principi, gas perfetto, scambiatori, lavoro espansione/compressione, Carnot**.

---

## Sistema termodinamico

**Sistema:** porzione di universo in cui si concentra l'attenzione  
**Ambiente:** resto dell'universo che può scambiare energie e materia

> **Riferimento slide:** [[001_Termodinamica_di_base_MN.pdf#page=2|001_Termodinamica_di_base_MN, pagina 2]]

| Tipo | Scambia materia | Scambia energia |
|------|-----------------|-----------------|
| **Isolato** | No | No |
| **Chiuso** | No | Sì |
| **Aperto** | Sì | Sì |

Un sistema non in equilibrio evolve **spontaneamente** verso l'equilibrio.

> **Riferimento slide:** [[001_Termodinamica_di_base_MN.pdf#page=3|pagina 3]]

---

## Funzioni di stato

Il valore dipende **solo dallo stato corrente**, non dal percorso.

| Funzione | Simbolo | Significato |
|----------|---------|-------------|
| Energia interna | $U$ | Energia microscopica contenuta (cinetica + potenziale particelle) |
| Entalpia | $H = U + pV$ | Energia scambiabile con l'esterno (sistemi aperti) |
| Entropia | $S$ | Grado equilibrio termico, direzione spontanea processi, freccia del tempo |

> **Riferimento slide:** [[001_Termodinamica_di_base_MN.pdf#page=4|pagina 4]], [[001_Termodinamica_di_base_MN.pdf#page=5|pagina 5]]

**Calore ($Q$) e Lavoro ($L$)** **NON** sono funzioni di stato (dipendono dal percorso).

---

## Trasformazioni termodinamiche

Processo in cui un sistema passa da uno stato di equilibrio a un altro.  
Stato determinato da **$p, V, T$**.

**Equilibrio termodinamico** = equilibrio termico + meccanico + chimico.

> **Riferimento slide:** [[001_Termodinamica_di_base_MN.pdf#page=6|pagina 6]]

| Tipo | Descrizione |
|------|-------------|
| **Reversibili** | Attraverso stati di equilibrio, assenza forze dissipative, percorribili al contrario |
| **Irreversibili** | Stati di non equilibrio e/o forze dissipative, non tornano allo stato iniziale |

> **Riferimento slide:** [[001_Termodinamica_di_base_MN.pdf#page=7|pagina 7]]

---

## Gas Perfetto

Modello ideale (gas nobili si avvicinano).

**Equazione di stato:**
$$pV = nRT$$

| Simbolo | Significato |
|---------|-------------|
| $p$ | Pressione |
| $V$ | Volume |
| $n$ | Moli |
| $R$ | Costante gas |
| $T$ | Temperatura assoluta |

**Proprietà:**
1. Volume particelle trascurabile
2. Forze attrattive nulle (particelle indipendenti)
3. Collisioni perfettamente elastiche
4. Energia cinetica media $\propto T$

> **Riferimento slide:** [[001_Termodinamica_di_base_MN.pdf#page=8|pagina 8]]

---

## Calori specifici

| Tipo | Definizione |
|------|-------------|
| $C_v$ | Calore per alzare 1 K a **volume costante** (1 kg sostanza) |
| $C_p$ | Calore per alzare 1 K a **pressione costante** (1 kg sostanza) |

$C$ indica "resistenza" a scaldarsi: più grande → più calore serve.

> **Riferimento slide:** [[001_Termodinamica_di_base_MN.pdf#page=5|pagina 5]]

---

## 1° Principio — Energia interna

$$U = \sum \text{energia microscopica (cinetica + potenziale interazioni)}$$

$$\Delta U = Q - L$$

- $\Delta U$: variazione energia interna
- $Q$: calore scambiato (entrante = +)
- $L$: lavoro compiuto **dal** sistema (uscente = +)

> **Significato:** conservazione energia, non distingue lavoro da calore.  
> **Riferimento slide:** [[001_Termodinamica_di_base_MN.pdf#page=11|pagina 11]]

---

## Entalpia

$$H = U + pV$$

Per **gas perfetto** ($pV=nRT$, $U=U(T)$):
$$dH = dU + d(pV) = nC_V dT + nR dT = n(C_V+R)dT = nC_p dT$$

---

### Trasformazione isobara
$Q = \Delta U + L$, con $L = p\Delta V$:
$$Q = \Delta U + p\Delta V = \Delta H$$

- **Esotermica**: $Q<0$ (rilascia calore)
- **Endotermica**: $Q>0$ (assorbe calore)

> **Riferimento slide:** [[001_Termodinamica_di_base_MN.pdf#page=14|pagina 14]]

---

## 2° Principio — Entropia

**Enunciato Kelvin-Planck:** Impossibile trasformazione il cui *unico* risultato sia conversione completa di calore (da sorgente a $T$ costante) in lavoro.

**Enunciato Clausius:** Impossibile processo il cui *unico* risultato sia passaggio calore da corpo più freddo a più caldo.

> **Riferimento slide:** [[001_Termodinamica_di_base_MN.pdf#page=15|pagina 15]]

**Variazione entropia (trasf. reversibile):**
$$dS = \frac{\delta Q}{T}$$

**Proprietà entropia:**
- Funzione di stato
- Misura "grado equilibrio termico"
- Criterio oggettivo spontaneità
- Legata a freccia del tempo
- Misura probabilità dello stato

> **Riferimento slide:** [[001_Termodinamica_di_base_MN.pdf#page=16|pagina 16]], [[001_Termodinamica_di_base_MN.pdf#page=18|pagina 18]]

---

## Principi generali — Macchine a fluido

**Macchina a fluido:** dispositivo meccanico che scambia/trasforma energia con fluido operatore (acqua, vapore, aria, gas combusti).

| Tipo | Funzione | Esempi |
|------|----------|--------|
| **Motrici** | Energia fluido → lavoro albero | Turbine vapore, turbine gas, MCI |
| **Operatrici** | Lavoro albero → energia fluido | Pompe, compressori, ventilatori |
| **Volumetriche** | Scambio via variazione volume camera | Pistone/cilindro (MCI) |
| **Dinamiche (Turbomacchine)** | Scambio via interazione pale girante-fluido | Turbine, compressori assiali/centrifughi |

> **Riferimento slide:** [[002_IntroduzioneAlleMacchine_MN.pdf#page=7|pagina 7]]

### Trasformazioni caratteristiche
| Simbolo | Nome | Condizione |
|---------|------|------------|
| $v=cost$ | Isocora | Volume costante |
| $p=cost$ | **Isobara** | Pressione costante |
| $h=cost$ | **Isoentalpica** | Entalpia costante |
| $s=cost$ | **Isoentropica** | Entropia costante |
| $T=cost$ | **Isotermica** | Temperatura costante |
| $x=cost$ | Isotitolo | Titolo costante |

> **Diagramma:** ![[Pasted image 20260930225110.png]]

---

## Equazioni generali moto fluidi (sistema aperto)

Ipotesi: proprietà costanti su sezioni 1 e 2, volume costante.

> **Schema:** ![[Screenshot From 2025-09-24 13-16-48.png]]

**Forma energetica:**
$$\begin{aligned}
dE &= dQ_e - dL + dm_1\left( \frac{c_1^2}{2}+gz_1+u_1 \right) - dm_2\left( \frac{c_2^2}{2}+gz_2+u_2 \right) + p_1A_1ds_1 - p_2A_2ds_2 \\
dE &= dQ_e - dL + dm_1\left( \frac{c_1^2}{2}+gz_1+h_1 \right) - dm_2\left( \frac{c_2^2}{2}+gz_2+h_2 \right)
\end{aligned}$$

> **Riferimento slide:** [[002_IntroduzioneAlleMacchine_MN.pdf#page=7|pagina 7]]

**Forma meccanica:**
$$\frac{c_2^2}{2} - \frac{c_1^2}{2} + g(z_2 - z_1) + R + \int_1^2 v\,dp + 1 = 0$$

> **Riferimento slide:** [[002_IntroduzioneAlleMacchine_MN.pdf#page=11|pagina 11]]

---

## Scambio di calore a pressione costante

$dq = T\,ds$

> **Diagramma:** ![[Screenshot From 2025-10-01 10-38-18.png]]

Trasformazione liquido → gas a $p=cost$:
$$\int_1^2 dq = h_2 - h_1 = c_{pi}(T_2-T_1) + r x_2$$

> **Riferimento slide:** [[002_IntroduzioneAlleMacchine_MN.pdf#page=12|pagina 12]]

---

## Lavoro di espansione (Turbina)

**Turbina** = macchina motrice: fluido cede energia → lavoro albero.

Attraverso la turbina il fluido subisce:
- ↓ Pressione
- ↓ Temperatura  
- ↑ Volume specifico
- ↑ **Portata volumetrica**

> **Riferimento slide:** [[002_IntroduzioneAlleMacchine_MN.pdf#page=13|pagina 13]]

### Lavoro isoentropico (ideale)
$ds=0$ (adiabatica reversibile)
$$l_{is} = \left(h_1 + \frac{c_1^2}{2}\right) - \left(h_2 + \frac{c_2^2}{2}\right) = h_{r1} - h_{r2}$$

> **Riferimento slide:** [[002_IntroduzioneAlleMacchine_MN.pdf#page=14|pagina 14]], [[002_IntroduzioneAlleMacchine_MN.pdf#page=15|pagina 15]]

### Lavoro reale
$$l_{reale} = h_1 - h_2$$

### Rendimento interno
$$\eta_i = \frac{l_{reale}}{l_{is}} = \frac{h_1-h_2'}{h_1-h_2}$$

> **Riferimento slide:** [[002_IntroduzioneAlleMacchine_MN.pdf#page=17|pagina 17]]

**Catena ideale → reale → utile:** ogni passaggio moltiplica per il suo rendimento.

> **Schemi:** ![[Screenshot From 2025-10-01 12-50-31.png]] ![[Screenshot From 2025-10-01 12-51-54 1.png]]

---

## Lavoro di compressione (Compressore)

**Compressore** = macchina operatrice: cede energia al fluido.

Fluido subisce:
- ↑ Pressione
- ↑ Temperatura
- ↓ Volume specifico

**Lavoro isoentropico:** $l_{is} = h_2 - h_1$

> **Riferimento slide:** [[002_IntroduzioneAlleMacchine_MN.pdf#page=19|pagina 19]], [[002_IntroduzioneAlleMacchine_MN.pdf#page=20|pagina 20]]

Il compressore deve compensare le perdite (rendimento < 1).

---

## Teorema di Carnot

Ciclo **completamente reversibile** tra due sorgenti a $T$ costante.

$l = q_1 - q_2$ (calore assorbito - calore ceduto)

**Rendimento termodinamico Carnot:**
$$\mu_{thC} = \frac{l}{q_1} = \frac{q_1-q_2}{q_1} = 1 - \frac{q_2}{q_1} = 1 - \frac{\Delta S \cdot T_A}{\Delta S \cdot T_B} = 1 - \frac{T_A}{T_B}$$

> **Riferimento slide:** [[001_Termodinamica_di_base_MN.pdf#page=15|pagina 15]]

---

## Cicli termodinamici

Il calore scambiato dipende dal **percorso**.

> **Diagramma:** ![[Screenshot From 2025-10-01 13-29-53.png]]

| Tratto | Processo | Lavoro/Calore |
|--------|----------|---------------|
| $O \to A$ | Compressione | $l_{OA} = \int_O^A v\,dp = h_A - h_O$ |
| $A \to B$ | Riscaldamento | $q_{AB} = q_1 = h_B - h_A$ |
| $B \to C$ | Espansione | $l_{BC} = \int_B^C v\,dp = h_B - h_C$ |
| $C \to O$ | Raffreddamento | $q_{CO} = q_2 = h_C - h_O$ |

**Lavoro isoentropico** e **Rendimento termodinamico**:

> **Schemi:** ![[Screenshot From 2025-10-01 13-35-56.png]] ![[Screenshot From 2025-10-01 13-43-17.png]]

---

## Scambiatori di calore

Apparecchi per trasferire calore tra fluidi a $T$ diverse **senza contatto diretto** (scambio a superficie).

> **Riferimento slide:** [[002_IntroduzioneAlleMacchine_MN.pdf#page=12|pagina 12+]]

### Funzionamento
1. **Convezione** fluido caldo → parete
2. **Conduzione** attraverso parete metallica
3. **Convezione** parete → fluido freddo

**Esempi impianti:** generatori vapore, condensatori, surriscaldatori, HRSG.

---

### Configurazioni flusso

| Tipo | Descrizione | Caratteristica |
|------|-------------|----------------|
| **Equicorrente (parallelo)** | Fluidi stesso lato, stessa direzione | $T_{freddo,out} \le T_{caldo,out}$, efficienza limitata |
| **Controcorrente** | Fluidi lati opposti, direzioni opposte | **Più efficiente**: $T_{freddo,out}$ può superare $T_{caldo,out}$, max recupero calore |

---

## Collegamenti
- [[Macchine e Sistemi Energetici]] — Indice generale
- [[Motori a combustione interna – Principi e classificazione]] — Applicazione 1°/2° principio a MCI
- [[Sistemi a vapore – Cicli Rankine/Hirn, ORC]] — Ciclo Hirn usa funzioni di stato vapore
- [[Sistemi a gas – Turbogas e ciclo Brayton]] — Ciclo Brayton usa $C_p$, $\eta_i$ turbina/compressore
- [[Generatori di vapore – Tipologie e componenti]] — Scambiatori reali (E, V, S)
- [[Rendimento, rugiada acida e parametri combustione]] — Bilancio energetico caldaia, perdite