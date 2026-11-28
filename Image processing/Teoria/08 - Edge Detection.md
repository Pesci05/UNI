# Edge Detection

> **Slide:** [[08_Edge detection.pdf]]
> **Indice:** [[IMAGE PROCESSING]]

Un **edge** viene definito come un cambio drastico della luminosità, spesso avviene in corrispondenza dei bordi.

L'==**EDGE DETECTION**== è il processo di rilevamento degli edge; gli edge vengono utilizzati per definire la forma degli oggetti.
Il suo output sarà un'immagine binaria che rappresenta gli edge dell'immagine input.
![[Pasted image 20261008104052.png]]

Visto che può essere definito come un cambio drastico di luminosità, può essere visto come una **step function**, rispetto ad una data direzione.
![[Pasted image 20261008104154.png]]

Gli edge in realtà non sono un salto drastico tra una luminosità e l'altra, ma il cambio di luminosità avviene in maniera più *smussata*.
In altri termini, un edge reale corrisponde ad un rapido incremento o decremento dell'intensità dei pixel rispetto ad una data direzione.

Possiamo supporre che le immagini siano funzioni unidimensionali dette $I(x)$.
La derivata prima di $I(x)$ rileverà che ci sarà un picco in $I'(x)$ in corrispondenza dell'edge.
La derivata seconda $I''$ cambia segno e viene detta anche **zero crossing**.
![[Pasted image 20261008105549.png]]

L'idea generale nell'edge detection è **ricondurre il problema dell'individuazione degli edge al calcolo della derivata prima di $I$**, e poi selezionare come punti di "edge" quei pixel corrispondenti ai valori (in modulo) più alti di $I'$.

Però questo crea problemi nel calcolo della derivata poiché la funzione dell'immagine sarà:
- $I()$ è una funzione campionata, con un dominio discreto
- $I()$ non è definita in modo analitico

Soluzione: la derivata $I()$ può essere calcolata usando le **differenze finite**.
Le differenze possono essere: ^7031da
- **Destra**: $\Delta_+ f(x) = f(x+1) - f(x)$
- **Sinistra**: $\Delta_- f(x) = f(x) - f(x-1)$
- **Centrale**: $\Delta f(x) = \frac{1}{2}(f(x+1) - f(x-1))$

Però un'immagine è formata da 2 dimensioni, per cui dobbiamo estendere questo approccio alle funzioni a 2 variabili; questo si può fare grazie al **gradiente** (derivate parziali).

Per utilizzare il gradiente su un'immagine si devono calcolare le derivate parziali sia per la direzione verticale, sia per quella orizzontale:
$$\frac{\partial I}{\partial u} \quad \text{e} \quad \frac{\partial I}{\partial v}$$
Il gradiente dell'immagine sarà:
$$
\nabla I(u,v) = \begin{bmatrix}
\frac{\partial I}{\partial u}(u,v) \\
\frac{\partial I}{\partial v}(u,v)
\end{bmatrix}
$$

**Proprietà del gradiente:**
- Il gradiente calcolato in $p$ corrisponde ad un **vettore** che punta nella direzione di *massima crescita locale* di $f$ in $p$, e ha un modulo proporzionale alla quantità di crescita in quella direzione.
- I valori delle derivate parziali in $p$ rappresentano le componenti di questo vettore rispetto ad ogni dimensione del dominio di $f()$.

![[Pasted image 20261113232506.png]]

Nel caso delle immagini, il gradiente è **perpendicolare** ad un eventuale edge, per questo si utilizza il gradiente per **individuare** gli edge.

## Gradiente di un'immagine
Per calcolare il gradiente di un'immagine si devono calcolare le derivate parziali **rispetto alle direzioni**, *orizzontali* ($u$) e *verticali* ($v$):
$$
\frac{\partial I}{\partial u}(u,v) \quad \text{e} \quad \frac{\partial I}{\partial v}(u,v)
$$
Per fare questo si devono utilizzare le **[[#^7031da|differenze]]**, rispetto alle 2 direzioni.

Il gradiente di un'immagine alla posizione $(u,v)$ è:
$$
\nabla I(u,v) = \begin{bmatrix}
\frac{\partial I}{\partial u}(u,v) \\
\frac{\partial I}{\partial v}(u,v)
\end{bmatrix}
$$

Il **modulo** del gradiente è:
$$
M(u,v) = |\nabla I|(u,v) = \sqrt{\left( \frac{\partial I}{\partial u}(u,v) \right)^2 + \left( \frac{\partial I}{\partial v}(u,v) \right)^2}
$$
Il modulo non varia rispetto alla direzione dell'immagine ed è usato per l'edge detection.

In alcuni casi è utile anche calcolare la direzione del gradiente:
$$
\phi(u,v) = \arctan\left( \frac{\frac{\partial I}{\partial u}(u,v)}{\frac{\partial I}{\partial v}(u,v)} \right)
$$
![[Pasted image 20261113233929.png]]

Per calcolare il gradiente per ogni coordinata si usa la definizione di derivata parziale:
$$
\frac{\partial I}{\partial u} = \lim_{h \to 0} \frac{I(u+h,v) - I(u,v)}{h} \\
\frac{\partial I}{\partial v} = \lim_{h \to 0} \frac{I(u,v+h) - I(u,v)}{h}
$$
Per farlo posso utilizzare anche le differenze finite.
Per esempio nella **differenza centrata**:
$$
\frac{\partial I}{\partial u} = \frac{1}{2}(I(u+1,v) - I(u-1,v)) \\
\frac{\partial I}{\partial v} = \frac{1}{2}(I(u,v+1) - I(u,v-1))
$$
Queste derivate devono essere calcolate per **ogni pixel** dell'immagine.

Le derivate parziali sono formate anche da delle funzioni lineari, che prendono in considerazione anche i pixel vicini a quello preso in esame; questo significa che per calcolare il gradiente possiamo utilizzare anche **dei filtri lineari** (possono essere diversi per direzione, vedi [[05 - Filtri]]), applicati grazie alla *convoluzione*.

Nel caso della prima derivata parziale (*orizzontale*) si utilizzerà un **filtro orizzontale**, e il kernel di questo filtro sarà:
$$
H_{u} = [-0.5 \quad 0 \quad 0.5] \\
\frac{\partial I}{\partial u}(u,v) = (I * H_{u})(u,v)
$$
FILTRO per il calcolo delle derivate: [[08_Edge detection.pdf#page=30|08_Edge detection, pagina 30]]

In questo caso però il filtro sarà sensibile anche a **basse variazioni di luminosità** (edge piccoli) che vorremmo ignorare; questo si può risolvere grazie a filtri 2D (**UTILIZZATI SOLITAMENTE**), in modo che il risultato tenga conto di una differenza di luminosità calcolata in un'area più ampia.

Per questo si utilizzano filtri a 2 dimensioni di size $3\times 3$.
![[Pasted image 20261113235438.png]]

**ESEMPIO SOBEL**: [[08_Edge detection.pdf#page=32|08_Edge detection, pagina 32]]

---
> **Collegamenti Lab:** [[IMAGE FORMATION#Edges to countours]] | [[IMAGE FORMATION#CANNY edge detector: Pipeline]]
