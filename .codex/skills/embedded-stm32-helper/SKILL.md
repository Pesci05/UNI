---
name: embedded-stm32-helper
description: Assistente per sviluppo embedded su microcontrollori STM32 (C/C++, HAL/LL, registri, PWM, ADC, UART/SPI/I2C, interrupt e driver motori). Attiva questa skill quando si lavora su firmware, STM32CubeIDE, datasheet o periferiche hardware.
---

# Embedded & STM32 Engineering Assistant

Quando scrivi, revisioni o fai debugging di codice firmware/embedded:

1. **Sicurezza e concorrenza hardware**:
   - Verifica che tutte le variabili condivise tra `main` e le ISR (Interrupt Service Routine) siano dichiarate `volatile` e accedute in modo atomico.
   - Mantieni le callback ISR (`HAL_GPIO_EXTI_Callback`, timer interrupt) il più brevi possibile, evitando `HAL_Delay()` o operazioni bloccanti al loro interno.
2. **Calcoli di temporizzazione e periferiche**:
   - Quando configuri Timer, PWM o baudrate, mostra esplicitamente la formula di calcolo a partire dal clock di sistema ($f_{CK}$):
     $$f_{PWM} = \frac{f_{TIM}}{(PSC + 1) \cdot (ARR + 1)}$$
   - Specifica sempre i pin coinvolti, la modalità GPIO (Push-Pull, Open-Drain, Pull-Up/Down) e la logica attiva (Active-High / Active-Low).
3. **Stile del codice**:
   - Preferisci tipi a dimensione fissa (`uint8_t`, `uint16_t`, `uint32_t` da `<stdint.h>`).
   - Evita l'allocazione dinamica (`malloc`) su microcontrollori se non strettamente necessaria; usa buffer statici dimensionati a compile-time.
