# MACCHINE A SISTEMI FINITI (AUTOMI)
#05/10 
Hanno una struttura rigida e il loro funzionamento vien descritto tramiti grafici.

# PROCESSI SINCRONI/ASINCRONI
- **Sincrono**
	Estremamente veloce e reattivo, ma è uno spreco di risorse 

- **Asincrono**
	Implementabile tramite **yield**, e **sleep**.
	[[02 - Automata and machines.pdf#page=31|02 - Automata and machines, pagina 31]]

# PARALLEL PROGRAMMING
- **PARALLEL COMPUTING**
	Stesso computer ma utilizzando più processi/thread
- **DITRIBUTED COMPUTING**
	Lavorare con più computer
- **SPEED UP**
	Risolvere lo stesso algoritmo, ma più velocemente
- **SCALE UP**
	Risolvere un algoritmo più complicati ma dividenolo in più problemi più piccoli

## MOTIVI PER CUI SI PREFERISCE IL PARALLELO
1. **Economico**
	I costi di produzione di un processore più veloce, rispetto ad un processore multi-core è molto maggiore
2. **Fisico**
	Questo è un limite che viene definita dalle leggi di **Moore** e **Dennard**

Per rendere più veloce un software, non si può solo aumentare un il clock, infatti si è passati al calcolo in parallelo, però per passare a questo tipo di calcolo le **architetture si devono cambiare** e deve essere il **programma a renderle ottimizzate**.
Per questo i programmatori **devono** sapere l'architettura ibettivo del software.

## Legge di Amdahl
Per quanto un programma possa essere parallelizzato, ci sarà sempre un porzione di codice fissa e non parallelizzabile che non piò essere annullata.

# TIPI DI MULTIPROCESSO
- **SIMMETRICO**
	Ogni core è uguale all'altro, e sono collegati tramite un bus
	![[Pasted image 20261005151438.png]]
- **ASSIMETRICO**
	I core di una CPU sono divisi in 2 osttosinstemi, dove un gruppo può essere uno più veloce dell'altro, solitamente con archotettura di tipo ARM
	![[Pasted image 20261005151457.png]]
- **MEMORIA DISTRIBUITA**
	Ogni core deve avere una o più **memorie cache**, queste sono sempre più veloce quando sono vicine al core ma sono anche molto piccole, più ci si allontana dal core, più le cache diventano grandi ma anche lente, fino ad arrivare alla RAM se il dato non si trova all'interno delle cache.
## DEFINIZIONI
- **CORE**
	Integrato con una ALU,RAM etc...
- **PROGRAMMA**
	Implemetazione di un algoritmo
- **PROCESSO**
	Istanza di programma
- **THREAD**
	Esecutore di una parte del programma
- **TASK**
	Parte del programma (sottoinsieme d'istruzioni)
[[07 - Parallel programming.pdf#page=20|07 - Parallel programming, pagina 20]]

## THREADING MODEL
Un modo per utilizzare il multi thread è il metodo **fork-join**, dove il thread main viene chiamata **MASTER**, e i thread generati vengono chiamati **slaves**, grazie alle funzioni **join**(elimina/unisce thread) e **fork**(genera thread)