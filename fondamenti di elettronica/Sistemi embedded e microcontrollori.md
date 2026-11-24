# Sistemi embedded e microcontrollori

> Nota derivata da [[Fondamenti di Elettronica]] — macro-argomento: **Embedded systems, Architettura MCU, Memorie, Periferiche, Clock, Protocolli seriali, Low-power**.

---

## Sistemi embedded

> **Definizione**: Sistemi che elaborano informazioni **all'interno di prodotti**, con **risorse limitate** (memoria, potenza, energia, costo).

| Caratteristica | Descrizione |
|----------------|-------------|
| **Mixed-signal** | Analogico + digitale (sensori/attuatori ↔ MCU) |
| **Hardware-coupled** | Fortemente legato all'HW (registri, timing, pinout) |
| **Real-time** | Scadenze temporali vincolanti (hard/soft real-time) |
| **Affidabilità** | Svolge funzione con alta probabilità, nessun danno |

> **Riferimento lab:** [[Lezione_Lab_1.pdf#page=8|page 8]], [[Lezione_Lab_1.pdf#page=17|page 17]]

### Sensori ↔ Attuatori
- **Sensori**: grandezza fisica → segnale elettrico
- **Attuatori**: segnale elettrico → variazione grandezza fisica

> **Riferimento:** [[Lezione_Lab_1.pdf#page=14|page 14]]

---

## Microcontrollori (MCU)

### Architettura tipica (Harvard modificato)
```
┌─────────────────────────────────────────┐
│                   CPU (RISC)            │
│  ┌─────┐  ┌─────┐  ┌────────────────┐  │
│  │Core │  │NVIC │  │ Debug (SWD/JTAG)│  │
│  └──┬──┘  └──┬──┘  └────────────────┘  │
└─────┼────────┼──────────────────────────┘
      │        │
      ▼        ▼
┌─────────────────────────────────────────┐
│           Bus Matrix / AHB/APB          │
└─────┬──────────────┬──────────────┬──────┘
      │              │              │
      ▼              ▼              ▼
┌──────────┐  ┌──────────┐  ┌──────────────┐
│  FLASH   │  │  SRAM    │  │  Periferiche │
│ (Code)   │  │ (Data)   │  │  (GPIO, UART,│
│          │  │          │  │   SPI, I²C,  │
│ 512 KB   │  │ 512 KB   │  │   ADC, PWM,  │
└──────────┘  └──────────┘  │   Timer,     │
                            │   DMA, USB,  │
                            │   Comparator,│
                            │   RTC, CRC)  │
                            └──────────────┘
```

> **Dimensioni esempio** (da slide): FLASH 512 KB, SRAM 512 KB — *valori variano per famiglia*  
> **Riferimento:** [[Lezione_Lab_1.pdf#page=26|page 26]]

### Memorie

| Tipo | Volatilità | Uso | Caratteristiche |
|------|------------|-----|-----------------|
| **SRAM** | Volatile | Variabili, stack, heap, buffer | Veloce, byte-addressable, ~0 wait state |
| **FLASH** | Non-volatile | Codice (firmware), costanti, bootloader | Settori/pagine, erase prima di write, wait state a freq. alte |
| **EEPROM** (se presente) | Non-volatile | Parametri configurazione, log | Byte-erasable, cicli limitati (~$10^5$) |
| **Backup RAM** | Non-volatile (VBAT) | Ora RTC, flag wake-up | Alimentata da batteria/tampone |

### Registri periferiche (Memory-Mapped I/O)
- Ogni periferica → blocco indirizzi (es. `0x4000_0000`–`0x400F_FFFF`)
- **Registri**: configurazione (CR), dati (DR), stato (SR), interrupt (IER/ISR), DMA
- Accesso: `volatile uint32_t *REG = (uint32_t*)0x4000xxxx;`
- **Attenzione**: atomicità (read-modify-write), allineamento, side-effects

---

## Clock system

| Sorgente | Frequenza tipica | Precisione | Uso |
|----------|------------------|------------|-----|
| **HSE** (High Speed External) | 4–48 MHz (quarzo/ceramic) | $\pm 50$ ppm | Clock principale, USB, Ethernet |
| **LSE** (Low Speed External) | 32.768 kHz (quarzo) | $\pm 20$ ppm | RTC, low-power wakeup |
| **HSI** (High Speed Internal) | 8–64 MHz (RC) | $\pm 1\%$–$5\%$ | Boot, fallback, basso costo |
| **LSI** (Low Speed Internal) | 32 kHz (RC) | $\pm 5\%$ | IWDG, RTC (se no LSE) |
| **PLL** | $\times$ da HSE/HSI | Dipende da sorgente | Moltiplica per raggiungere $f_{CPU}$ max |

> **Riferimento:** [[Lezione_Lab_1.pdf#page=26|page 26]] — cristallo per sincronismo

### Albero clock tipico (es. STM32)
```
HSE/HSI ──▶ PLL ──▶ SYSCLK (CPU)
                  ├─▶ AHB  (core, DMA, Flash)
                  ├─▶ APB1 (timer lenti, UART, I²C, SPI, USB)
                  └─▶ APB2 (timer veloci, ADC, GPIO, SDIO)
```
- Prescaler (AHB/APB) per bilanciare velocità/periferiche

---

## Protocolli seriali integrati

| Protocollo | Linee | Topologia | Velocità tipica | Uso principale |
|------------|-------|-----------|-----------------|----------------|
| **UART** (USART) | 2 (TX, RX) + GND | Point-to-point | 9.6 kbps – 10+ Mbps | Console, GPS, modem, bootloader |
| **SPI** | 4 (SCK, MOSI, MISO, CS) | Master–Slave (multi-slave via CS) | 1–50+ Mbps | Flash, display, sensori veloci, ADC/DAC |
| **I²C** | 2 (SDA, SCL) | Multi-master, multi-slave (addr 7/10 bit) | 100 kHz / 400 kHz / 1 MHz / 3.4 MHz | EEPROM, sensori, PMIC, GPIO expander |
| **USB** | 2 (D+, D−) | Host–Device | 1.5/12/480 Mbps | PC link, DFU, HID, CDC, MSC |
| **CAN** | 2 (CANH, CANL) | Bus multi-master | 125 kbps – 1 Mbps (FD: 5 Mbps) | Automotive, industrial |
| **1-Wire** | 1 (DQ) + GND | Master–Slave (parassita) | 16 kbps | DS18B20, iButton, EEPROM |
| **SAI / I²S** | 4+ | Master–Slave | MHz | Audio codec, MEMS mic |
| **SDIO** | 4/8 data + CMD + CLK | Host–Card | 25–200 MHz | SD card, eMMC, WiFi |

> **Riferimento:** [[Lezione_Lab_1.pdf#page=26|page 26]] — UART, SPI, I²C, USB

---

## Low-power / Energy management

| Tecnica | Descrizione | Risparmio |
|---------|-------------|-----------|
| **Clock gating** | Disabilita clock a periferiche inutilizzate | Dinamico |
| **Voltage scaling** | Riduce $V_{core}$ (se supportato) + freq | Quadratico in $V$ |
| **Sleep modes** | **Sleep** (CPU stop, periferiche on) → **Stop** (regulator low-power, RAM retained, wake via EXTI) → **Standby** (tutto spento, solo backup domain + WKUP pin) | Fino a $\mu$A/nA |
| **DMA** | Sposta dati senza CPU → CPU in sleep | Dinamico + latency |
| **Batch processing** | Accumula campioni → burst transfer → sleep lungo | Duty cycling |
| **Peripheral autonomous** | ADC/DAC/Timer/LPTIM/OPAMP in Stop mode (STM32U5/L5) | Deep sleep con sensing |

> **Riferimento:** [[Lezione_Lab_1.pdf#page=26|page 26]] — abbassare freq, spegnere circuiti inutilizzati

---

## Toolchain & Debug

| Componente | Esempi |
|------------|--------|
| **Compiler** | arm-none-eabi-gcc (GCC), LLVM/Clang, IAR, Keil (ARMCC/AC6) |
| **Debug probe** | ST-Link, J-Link, CMSIS-DAP, Black Magic Probe |
| **Debug interface** | SWD (2 pin: SWCLK, SWDIO), JTAG (5 pin) |
| **Flash loader** | OpenOCD, J-Link Commander, STCubeProgrammer, pyOCD |
| **RTOS** | FreeRTOS, Zephyr, ThreadX, CMSIS-RTOS2 |
| **HAL/LL** | Vendor HAL (STM32Cube, ESP-IDF, nRF Connect SDK) / Low-Layer / Register direct |

---

## Collegamenti
- [[Fondamenti di Elettronica]] — Indice generale
- [[Elettronica digitale]] — ALU, registri, FSM, logica sequenziale → base architettura CPU
- [[Dispositivi a semiconduttore - Diodi e Transistor]] — GPIO drive strength, protezione ESD, driver esterni
- [[Amplificatori operazionali]] — Condizionamento segnali sensori prima di ADC, comparator window
- [[Sensori e trasduttori]] — Interfacciamento: ADC (SAR/$\Sigma\Delta$), PGA, comparator, timer capture, DMA
- [[Potenza, termica e affidabilità]] — Dissipazione MCU ($P = C V^2 f$), thermal management, watchdog (IWDG/WWDG)