Dal punto di visto dai cicli a gas i vapori caldi verrebbero **espulsi** nell'atmosfrea, ma questo provoca una **perdita** di un possibile **fonte di energia**, la quale si può utilizzare combinandolo con un **ciclo a vapore** il quale recuperando i vapori caldi generano altra energia.

La combinazio dei due cicli può avvenire grazie ai rendimenti delle **turbine a gas**, e quella della **turbina a vapore**, ma anche dal rednimento dello scambiatore di **calore** **HRSG**, detto anche **caldaia a recupero**, che è composta da **Economizzatore, vaporizzatore e surriscaldatore**.
[[005_SistemiCombinatiGasVapore_MN.pdf#page=2|005_SistemiCombinatiGasVapore_MN, pagina 2]]

# GRUPPO COMBINATO GAS
![[Pasted image 20251029105627.png]]
![[Pasted image 20261011233256.png]]

L'efficienze di questo tipo d'impianto viene determianta da $\sigma$:
![[Pasted image 20251029114833.png]]

Il **pinch point**, è la **differenza minima di temperatura** tra i fumi in raffreddamento e l'acqua in evaporazione. Si verifica esattamente all'**uscita dell'evaporatore lato fumi**: $$\Delta T_{pp} = T_{fumi, EVA, out} - T_{sat}(p)$$
Questo dato serve anche per definire l'**efficienza dello scmabiatore di calore**, per aumentarne l'efficienza si devono utilizzare HSRG a più livelli di pressione.
![[Pasted image 20261012000635.png]]
- **SURRISCALDATORE**
	I fumi a massima temperatura incontrano il vapore saturo secco proveniente dal corpo d'allevamento (_drum_) e lo riscaldano fino alla temperatura finale di surriscaldamento $T_{sh}$.
- **EVAPORIZZATORE**
	Avviene il cambio di fase da acqua liquida a vapore saturo alla pressione di esercizio $p$. Poiché il cambio di fase è isobaro-isotermo, **la linea dell'acqua nell'evaporatore è perfettamente orizzontale** alla temperatura di saturazione $T_{sat}(p)$.
- **ECONOMIZZATORE**
	I fumi oramai raffreddati incontrano l'acqua liquida ad alta pressione spinta dalla pompa d'alimento e la preriscaldano fino a una temperatura vicina a quella di saturazione.


Il rendimento si ricava sempre nello stesso modo cioè:
![[Pasted image 20251029114910.png]]

Per migliorare ancora di più il rendimento di questo **Ciclo si può introdurre la post-combustione:**
![[Pasted image 20261012001634.png]]

**DIFFERENZE TRA I 2 APPROCCI**

| Parametro                                              | Ciclo Combinato **Senza Post-Combustione**                                                    | <br>Ciclo Combinato **Con Post-Combustione**                                                                              |
| ------------------------------------------------------ | --------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| **Apporto di Combustibile**                            | Esclusivamente nella camera di combustione della Turbina a Gas (TG).                          | In due punti: nella TG e nei **bruciatori integrati (****duct burners****)** nei condotti dell'HRSG.                      |
| **Temperatura Fumi in HRSG**                           | Pari alla temperatura di scarico del Turbogas (**550–600 °C**).<br>                           | Fumi riscaldati ulteriormente fino a **700–900 °C** prima di entrare nello scambiatore2.                                  |
| **Potenza della Turbina a Vapore (TV)**<br>            | Vincolata rigidamente dalle condizioni operative e dal carico del Turbogas.                   | **Aumentabile su richiesta (+20% fino a +50%)** grazie alla maggiore portata di vapore generata.                          |
| **Rendimento Elettrico Globale (**$\eta_{cc}$**)**<br> | **Massimo teorico e pratico (60–62%)**; tutto il calore entra alla temperatura di picco $TIT$ | **Leggermente inferiore a bruciatore acceso (56–58%)**, poiché il calore extra ha un rendimento di conversione inferiore. |
| **Flessibilità Operativa**<br>                         | Meno flessibile; la produzione di vapore segue passivamente la turbina a gas.                 | **Molto elevata**; ideale per il _peak shaving_ (copertura dei picchi di domanda) e la cogenerazione flessible.           |
1. **Sfruttamento dell'Ossigeno Residuo nei Fumi**: La turbina a gas opera con un forte eccesso d'aria per contenere la temperatura massima di ingresso turbina ($TIT$). Di conseguenza, i fumi di scarico contengono ancora un'**elevata percentuale di ossigeno incombusto (12–15% in volume)**. La post-combustione sfrutta questo comburente già caldissimo senza dover introdurre aria esterna dall'ambiente.
2. **Compromesso tra Rendimento e Potenza Massima**:
    - **Senza post-combustione**, l'impianto è progettato per la **massima efficienza di regime**: il calore viene somministrato solo alla massima temperatura del ciclo ($TIT > 1400\text{ °C}$), permettendo di superare il $60\%$ di rendimento complessivo.
    - **Con post-combustione**, si accetta una lieve penalizzazione del rendimento globale a fronte di un **forte guadagno di potenza e flessibilità**: il calore immesso nel _duct burner_ viene convertito con il solo rendimento del ciclo vapore inferiore ($\sim 30–35\%$).

3. **Effetto sul Diagramma** $T-Q$ **dell'HRSG**: Innalzando la temperatura dei fumi all'ingresso dell'HRSG (da $550\text{ °C}$ a $750\text{–}900\text{ °C}$), si amplia la differenza di temperatura rispetto alle curve dell'acqua e del vapore. Questo consente di produrre una **portata di vapore molto più elevata** ($\dot{m}_v$) a parità di superficie radiante dell'evaporatore.

Ora l'efficienza dello scmabiatore termico sarà:
$$
\sigma= \frac{T_{4'}-T_{5}}{T_{4'}-T_{a}}
$$
