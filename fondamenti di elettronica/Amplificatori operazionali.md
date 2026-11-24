# Amplificatori operazionali

> Nota derivata da [[Fondamenti di Elettronica]] — macro-argomento: **Op-amp ideale vs reale, retroazione negativa, guadagno closed-loop, comparatore**.

---

## Struttura e terminali

Dispositivo a **5 terminali**:
- **2 ingressi**: $(+)$ non invertente, $(-)$ invertente
- **1 uscita**: $V_o$
- **2 alimentazione**: $V_{SS}^+$, $V_{SS}^-$

> **Simbolo:** ![[Pasted image 20260130003747.png]] ![[Screenshot From 2025-10-06 12-02-30.png]]

---

## Modello ideale vs reale

| Parametro | Ideale | Reale |
|-----------|--------|-------|
| Guadagno a loop aperto $A_{OL}$ | $\infty$ | Finito ($10^4$–$10^6$) |
| Impedenza ingresso $Z_{in}$ | $\infty$ | Alta ($10^6$–$10^{12}\Omega$) |
| Impedenza uscita $Z_{out}$ | $0$ | Bassa ($10$–$100\Omega$) |
| Banda passante | Infinita | Limitata (GBW product) |
| Corrente ingresso (bias) | $0$ | Piccola ($pA$–$nA$) |
| Corrente uscita max | Illimitata | Limitata dal tipo (es. $20\text{mA}$) |

> **Riferimento slide:** [[01 - Nuts and Bolts of Electronics.pdf#page=45|pagina 45+]] (sezione op-amp)

---

## Funzionamento base

### Comparatore (open-loop)
$$V_o = A_{OL} (V_+ - V_-)$$
- Se $V_+ > V_- \Rightarrow V_o \approx +V_{SS}^+$ (saturazione positiva)
- Se $V_+ < V_- \Rightarrow V_o \approx -V_{SS}^-$ (saturazione negativa)
- **Inutilizzabile come amplificatore lineare** perché $A_{OL}$ troppo alto → minima differenza satura uscita

> **Curva trasferimento:** ![[Pasted image 20260130152153.png]]

---

## Retroazione negativa

Sistema che **condiziona l'ingresso in base all'uscita** per mantenere l'output controllato.

### Schema a blocchi
$$\beta = \text{fattore di retroazione} \quad (0 < \beta \le 1)$$

> **Diagramma:** ![[Screenshot From 2025-10-06 12-38-20.png]]

### Analisi matematica
$$\begin{aligned}
V_o &= A_{OL}(V_i - \beta V_o) \\
V_o &= A_{OL}V_i - A_{OL}\beta V_o \\
V_o(1 + A_{OL}\beta) &= A_{OL}V_i \\
V_o &= V_i \frac{A_{OL}}{1 + A_{OL}\beta} = V_i \cdot A_{CL}
\end{aligned}$$

**Guadagno a loop chiuso:**
$$A_{CL} = \frac{A_{OL}}{1 + A_{OL}\beta}$$

Se $A_{OL}\beta \gg 1 \Rightarrow A_{CL} \approx \frac{1}{\beta}$ (**indipendente da $A_{OL}$**)

### Tensioni agli ingressi (virtual short)
$$\begin{aligned}
V^+ &= V_i \\
V^- &= \frac{A_{OL}\beta}{1 + A_{OL}\beta} V_i \\
\Delta V &= V^+ - V^- = V_i \left(1 - \frac{A_{OL}\beta}{1+A_{OL}\beta}\right) = \frac{V_i}{1+A_{OL}\beta} \approx 0
\end{aligned}$$

> **Principio del "virtual short":** con retroazione negativa e $A_{OL}$ alto, gli ingressi sono **virtualmente in corto** (stessa tensione), ma **nessuna corrente** fluisce tra loro ($Z_{in} \to \infty$).

---

## Configurazioni classiche (con $\beta$)

| Configurazione | $\beta$ | $A_{CL}$ | Note |
|----------------|---------|----------|------|
| **Non-invertente** | $\frac{R_1}{R_1+R_2}$ | $1 + \frac{R_2}{R_1}$ | $Z_{in}$ altissima |
| **Invertente** | $\frac{R_1}{R_1+R_2}$ | $-\frac{R_2}{R_1}$ | $Z_{in} = R_1$, virtual ground su $-$ |
| **Buffer (voltage follower)** | $1$ | $1$ | Impedenza adapter |
| **Sommatore** | — | — | Più ingressi su $-$ con $R$ diverse |
| **Integratore** | $1/(sC R)$ | $-1/(sRC)$ | $C$ in feedback |
| **Derivatore** | $sC R$ | $-sRC$ | $C$ in ingresso |

---

## Guadagno in dB
$$A_{dB} = 20 \log_{10} |A|$$
- $A < 1 \Rightarrow \text{attenuazione}$ ($A_{dB} < 0$)
- $A > 1 \Rightarrow \text{amplificazione}$ ($A_{dB} > 0$)

---

## Limiti reali

1. **Slew Rate**: max $dV_o/dt$ (es. $0.5\text{V}/\mu\text{s}$ per 741, $>100\text{V}/\mu\text{s}$ per veloci)
2. **GBW (Gain-Bandwidth Product)**: $A_{CL} \cdot f_{-3dB} \approx \text{costante}$
3. **Offset tensione/corrente**: errori DC → serve *trim* o *auto-zero*
4. **Rumore**: tensione ($nV/\sqrt{Hz}$) + corrente ($pA/\sqrt{Hz}$)
5. **Common-mode range**: ingressi devono stare dentro range alimentazione (rail-to-rail o no)
6. **Output swing**: non arriva a $\pm V_{SS}$ (headroom)

---

## Collegamenti
- [[Fondamenti di Elettronica]] — Indice generale
- [[Dispositivi a semiconduttore - Diodi e Transistor]] — Stadi interni (diff pair BJT/MOSFET, current mirror, push-pull out)
- [[Componenti passivi - R, C, L e impedenza]] — Reti $R/C$ per filtri attivi, integratori, derivatori
- [[Elettronica digitale]] — Comparatori per ADC, PWM, soglie logiche
- [[Sensori e trasduttori]] — Condizionamento segnali sensori (bridge, termocoppie, piezoresistivi)