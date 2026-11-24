# Fondamenti di Elettronica — Indice

Questa nota funge da **indice navigabile** al corso.  
Ogni voce linka una nota dedicata con una sintesi dell'argomento.

---

## [[Analisi dei circuiti - Leggi fondamentali]]
> Leggi di **Kirchhoff** (KCL nodi, KVL maglie), **legge di Ohm**, collegamenti **serie/parallelo**, **superposizione degli effetti**, **Teorema di Thevenin** ($V_{th} + R_{th}$ serie) e **Norton** ($I_{no} + R_{no}$ parallelo). Convenzioni potenza (dissipativi vs erogativi).

## [[Componenti passivi - R, C, L e impedenza]]
> **Resistori** (partitore tensione/corrente), **Condensatori** ($Q=CV$, $I=C\,dV/dt$, carica RC), **Induttori** ($V=L\,dI/dt$).  
> **Segnali AC/DC**, analisi di Fourier, **impedenza complessa** $Z_R=R$, $Z_C=-j/\omega C$, $Z_L=j\omega L$, fasori, sfasamenti $\pm90^\circ$, legge di Ohm estesa $\tilde{V}=\tilde{Z}\tilde{I}$.

## [[Dispositivi a semiconduttore - Diodi e Transistor]]
> **Diodi**: PN (Shockley, $V_\gamma\approx0.7\text{V}$), **Zener** (breakdown controllato, esempio calcolo range), **LED**, **fotodiodo**, Schottky.  
> **BJT**: NPN/PNP, regioni *cut-off / saturazione / attiva*, $\beta$, switch, curve $I_C-V_{CE}$, $f_{max}$ vs $V_{CEO}$.  
> **MOSFET**: 4 terminali, $V_{TH}$, $V_{OD}$, regioni *cut-off / triode / saturazione*, curve $I_D-V_{DS}$.  
> **Termica**: dissipatori, **SOA**, *thermal runaway* (BJT) vs autolimitazione (MOSFET), second breakdown, parallelo.

## [[Amplificatori operazionali]]
> **Op-amp ideale** ($A\to\infty$, $Z_{in}\to\infty$, $Z_{out}\to0$) vs **reale**.  
> **Comparatore** (open-loop, satura). **Retroazione negativa**: $A_{CL}=\frac{A_{OL}}{1+A_{OL}\beta}\approx1/\beta$, *virtual short* ($\Delta V\approx0$).  
> Configurazioni: non-invertente, invertente, buffer, sommatore, integratore, derivatore. Limiti: slew rate, GBW, offset, rumore, swing.

## [[Elettronica digitale]]
> **Porte logiche**, **ALU** (opcode, flag, carry-in/out). **Encoder/Decoder** (one-hot $\leftrightarrow$ binario), **MUX/DEMUX** ($2^n$ linee).  
> **Logica combinatoria** vs **sequenziale** (memoria). **Clock** (quarzo, ring oscillator).  
> **Flip-flop JK** (edge-triggered, tabella verità). **Registri a scorrimento**: SISO, SIPO, PISO, PIPO, bidirezionali.  
> **FSM** (stati binari, next-state logic). **MPU vs MCU** (Harvard/RISC, periferiche on-chip, memorie SRAM/FLASH).

## [[Sensori e trasduttori]]
> **Temperatura**: termocoppie (Seebeck, tipi E/J/K), RTD Pt100 ($R(T)$, autoriscaldamento), termistori, integrati, pirometri.  
> **Forza/Coppia**: estensimetri ($G_f$, ponte Wheatstone), piezoelettrici (solo AC), ottici/magnetostrittivi su albero rotante.  
> **Posizione**: potenziometri, **encoder incrementali** (quadratura A/B, contatore+starter) vs **assoluti** (codice Gray, $k$ anelli), **resolver** (induzione magnetica, sin/cos, automotive).  
> **Accelerazione**: piezo (no DC), piezoresistivi, **MEMS capacitivi** (massa-molla, $C=\epsilon A/t$, $\Sigma\Delta$), termici, ottici.  
> **Magnetici**: **Hall** ($V_H=KBI$, feedback per alti campi), magnetoresistivi (Corbino, $R(B)$ quadratico), magnetostrittivi.  
> **Corrente**: **Shunt Kelvin 4-terminali** ($R\ll1\Omega$), trasformatori (solo AC), bobina Rogowski ($dI/dt$).

## [[Sistemi embedded e microcontrollori]]
> **Embedded**: mixed-signal, HW-coupled, real-time, affidabilità. Sensori→MCU→attuatori.  
> **MCU**: architettura Harvard modificato, **SRAM** (dati) + **FLASH** (codice), registri periferiche (memory-mapped I/O).  
> **Clock**: HSE/LSE (quarzo), HSI/LSI (RC), PLL, albero AHB/APB, prescaler.  
> **Protocolli**: UART, SPI, I²C, USB, CAN, 1-Wire, SAI/I²S, SDIO.  
> **Low-power**: clock gating, voltage scaling, sleep/stop/standby, DMA, autonomous peripherals.  
> **Toolchain**: GCC/Clang/IAR, SWD/JTAG, OpenOCD/J-Link, FreeRTOS/Zephyr, HAL/LL.

## [[Potenza, termica e affidabilità]]
> **Potenza**: $P=VI$, dissipativi vs erogativi. Modelli: $I^2R$, $V_F I_F$, $V_{CE}I_C$, $I_D^2 R_{DS(on)}$, switching losses.  
> **Termica**: rete $R_{th(j-c)}+R_{th(c-s)}+R_{th(s-a)}$, calcolo dissipatore, airflow, pasta/pad.  
> **SOA**: limiti $I_{max}$, $V_{max}$, $P_{max}$ (DC/pulsata), **second breakdown** (BJT).  
> **BJT vs MOSFET**: runaway termico vs coeff. temp. negativo, parallelo facile/solo MOSFET.  
> **Derating**: 70% $V$, 50% $I$, 50% $P$, $T_j$ margine 20–30°C.  
> **Affidabilità**: MTBF/MTTF/FIT, bathtub curve, Arrhenius ($\times2$ per $+10^\circ\text{C}$).  
> **Protezioni**: overcurrent (shunt+eFuse), overtemperature, overvoltage (TVS/MOV), reverse polarity, ESD, watchdog.

## [[Esempi circuiti risolti]]
> 1. **Carica/scarica condensatore RC**: $V_C(t)=V_b[1-e^{-t/RC}]$, $\tau=RC$, 63% @ $1\tau$, 95% @ $3\tau$, $I(t)=\frac{V_b}{R}e^{-t/RC}$.  
> 2. **Regolatore Zener**: calcolo $I_s$, $I_Z$, $I_L$, range $V_{in,min/max}$ senza/con carico, $R_{L,min}$ per $V_{in}$ fisso, potenze su $R_s$ e Zener.

---

## Riferimenti bibliografici
- [[01 - Nuts and Bolts of Electronics.pdf]] (slide corso teoria)
- [[Lezione_Lab_1.pdf]] (slide laboratorio)
- [[Dispense del Corso - Fondamenti di Elettronica.pdf]] (dispense complete)