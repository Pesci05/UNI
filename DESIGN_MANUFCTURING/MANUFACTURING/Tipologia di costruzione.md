**3D PRINTING**: termine non corretto, indica in realtà una specifica tecnica additiva
**RAPID PROTOTYPING**: processo utilizzato per processo utilizzato per realizzare velocemente un componente o un insieme di componenti prima della produzione. Termine obsoleto e non più rappresentativo.
**==ADDITIVE MANIFACTURING==**: processo di unione del materiale per l’ottenimento di componenti a partire da un modello 3D, generalmente strato su strato, all’opposto delle tecnologie sottrattive.

# ADDITIVE MANUFACTURING
## VANTAGGI
- **LIBERTÀ DI PROGETTAZIONE**: diventa possibile produrre oggetti molto complessi, anche pre-assemblati, con canali interni e sottosquadri. Diventa possibile realizzare i risultati delle ottimizzazioni topologiche quindi componenti alleggeriti. 
- **Costi legati al MATERIALE e al TEMPO DI COSTRUZIONE**
- **PERSONALIZZAZIONE**
- **Tempi di setup ridotti, e TOOLING INESITTENTE**(o quasi)
### SVANTAGGI
- Molte variabili e parametri di processo da controllare e minore stabilità del processo. Minore ripetibilità. 
- Gestione della qualità di processo e prodotto ancora in fase di sviluppo. 
- Processo e materiale sono strettamente legati, ancora più che nelle tecnologie tradizionali, rendendo più complessa la certificazione della qualità di un prodotto.

## APPLICAZIONI
- **AEROSPAZIALE**
- **AUTOMOTIVE**
- **FONDERIA**
- **MEDICALE**
- **MODELLI**
- **PROTOTIPI FUNZIONALI**

# AM WORKFLOW
Il lavoro di qeusto tipo di tecnica, viene eseguito in un certo modo e parte da:
1) **CAD**: Per progettare il pezzo
2) **[[Tipologia di costruzione#STL|FILE STL]]** 
3) **ORIENTAZIONE**: Orientare il pezzo nella maniera corretta, poichè può cambiare le proprietà del pezzo
4) **SUPPORTI**: Materiale extra che deve essere utilizzato per costruire il pezzo
5) **SLICING e GENERAZIONI PERCORSI**
6) **PRODUZIONE**
7) **POST-PROCESSING**: 
	- Rimozione dei supporti
	- Finitura superficiale
	- Trattamenti termici
8) **COMPONENTE FINALE**

## STL
==Formato standard== per la gestione delle geometrie nell’additive manufacturing. **Rimuove ogni dato di costruzione** e **approssima** le superfici con facce **triangolari**.


# MATERIAL EXTRUSION
Processo **additivo** in cui il **materiale** è selettivamente **estruso attraverso un ugello**, anche chiamata come **FDM**(Fused Deposition Modeling).
## Principio di funzionamento:
Il componente è prodotto attraverso un filamento di polimero fuso:
- Un filamento **termoplastico** prelevato da una bobina e alimentato dentro un estrusione
- L'ugello è scaldato fian alla temperatura di rammolimento, così da rendere il polimero malleabile e fargli prendere la forma voluta.
- L'ugello si muove verso 2 direzioni X  e Y

Tipo di polimero che scaldato si rammollisce, e questo permette di cambiargli la forma così da manipolare la forma del prodotto.
Esistono anche **polimeri termoindurenti**, che grazie ad una reazione chimica il polimero parte da una forma liquida per poi indurirsi prendendo la forma voluta, anche se si prova a scaldarlo non si può fondere, ma il polimero si brucierà, così da non poterlo più utilizzarlo.

L'estrusore può essere:
- **diretto**: dove l'unità di spinta è diretta nell'ugello, questo provoca ad una poca deformazione del filamento, **maggiore qualità** ma con l'unità motrice montata sull'ugello il quale comporta una **minore velocità**.
- **bowden**: unità motrice staccata dall'ugello, non c'è proporzione tra la spinta dellìunità motrice e la quantità di filamento all'interno dell'ugello, questp provoca una qualità **minore**, ma **maggiore** velocità si stampa.

In questo tipo di processi è **necessario** utilizzare i **supporti**, per sostenere le superfici del prodotto, generalmente è necessario per superfici orientate a meno di 45° rispetto alla tavola di produzione.

I materiali utilizzati per questa tecnica devono essere polimeri **termoplastici**.
[[L03 - Costruzione Additiva.pdf#page=60|L03 - Costruzione Additiva, pagina 60]]
E questi polimeri sono:
- **PLA**
	- Facilemente stampabile
	- Buone proprietà meccaniche 
	- Biodegradabile
	- Non tossico
	- Materiale **più utilizzato** 
	- **ALTAMENTE IGROSCOPICO**: assorbe l'umidità quidni bisogna conservarlo in modo adeguato
- **ABS**
	- Migliori prestazione meccaniche del PLA
	- Richiede maggiori temperature di estrusione, però è necessaria anche una camera chiusa e riscaldata a temperatura costante
	- Rifinitura facile tramite carta abrasiva
	- **PRODUCE FUMI TOSSICI DURANTE LA STAMPA**
- **PETG**
	- Ottima alternativa al PLA
	- Non tossico
	- Più complicato da stanmpare del PLA
	- Ottima resistenza e tenacia
	- Aspetto tipicamente lucido
	- Buona resistenza ai raggi UV
- **TPU**
	- Per oggetti che necessitano alta deformabilità
	- Solo per macchine ad estrusore diretto
- **FILAMENTI CARICATI**
	- Fibre corte disperse nella matrice polimerica
	- Fibre lunghe, orientamento lungo l'asse del filamento
	- Alta rigidità
	- Diffcoltà di stampa, alta usura dell'ugello dell'estrusore
- **ULTEM e PEEK**
	- Altissime prestazione meccaniche
	- resistenza al calore
	- Altissimi costi
	- Applicazione nell'aerospaziale e nei trasporti

Si può anche fare una rifinitura, il quale permette di migliorare l'aspetta della superficie.

# VAT PHTOPOLYMERIZATION
Processo additivo in cui un **fotopolimero liquido** contenuto in una vasca è reticolato (solidificato) selettivamente da una radiazione luminosa, utilizzati materiali di tipo **termoindurenti**.
Questa tecnica indurisce materiali tramite raggi UV, questa tecnica può essere:
- **LASER(SLA)**: Stereolitografia
- **Display o proiettore(DLP)**
Un esempio di materiale possono essere le **resine**.

## SLA
Si utilizza un **laser UV** che viene focalizzato su una **vasca di foto-polimero liquido** versata dall'operatore. Il volume di polimero irradiato dal laser reticola e solidifica.
La tecnologia SLA si basa sulla **foto-polimerizzazione**, cioè il processo mediante il quale un polimero termoindurente liquido solidifica in seguito ad irraggiamento.
Per avere questo fenomeno deve avere:
- **Monomeri e oligomeri**
- **Fotoiniziatori**

La macchina può essere:
- **STANDARD**: laser arriva dall'alto, bisgna riempira un'intera vasca di più litri di resina, mentre il piatto sprofonda verso il fondo della vasca.
- **INVERTITA**: il laser colpisce la resina dal basso, permettendo un utilizzo minore di resina liquida, facendo alzare la piattoforma.

## DLP
Digital Light Processing, questo tipo di macchine riesce a proiettare grazie a dei display un immaggine così da poter velocizzare la stampa