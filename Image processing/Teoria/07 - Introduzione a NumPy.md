# Introduzione alla libreria NumPy

> **Slide:** [[07_Introduzione_Numpy.pdf]]
> **Indice:** [[IMAGE PROCESSING]]

**NumPy** è un pacchetto per operazioni numeriche (rende Python più simile a MATLAB). In Image Processing è fondamentale perché le immagini in OpenCV sono rappresentate come array NumPy (vedi [[IMAGE FORMATION#OpenCV: frame come array NumPy]]).

```python
import numpy as np
```

## Premessa: Indexing e Slicing in Python
- **Indexing**: accesso ai singoli elementi di una lista (e di una sequenza in generale):
  - `s[i]` restituisce l'$i$-esimo elemento di `s` (l'indice `i` deve essere compreso tra `0` e `len(s) - 1`).
- **Slicing**: accesso a più elementi contigui di una lista:
  - `s[i:j]` ritorna la sotto-lista costituita dagli elementi `s[i], s[i+1], ..., s[j-1]` (`s[j]` è escluso).
  - Si può usare il parametro `step` (*stride*): `s[start:stop:step]`.
- Sia nello slicing che nell'indexing, un valore negativo `-i` usato come indice viene interpretato come `len(s) - i`. Es.: `s[-1] == s[len(s)-1]`, `s[0:-2] == s[0:len(s)-2]`.

## `ndarray` vs Liste Python
Gli oggetti `ndarray` di NumPy rappresentano **array multidimensionali e omogenei** di oggetti di **dimensione fissa**:

```python
np.array([1, 2, 3, 4, 5])
```

- **Liste Python**: sono **eterogenee** (possono contenere oggetti di qualsiasi tipo e dimensione) e facilmente ridimensionabili $\to$ *versatili*.
- **`ndarray` NumPy**: sono **omogenei** (tutti gli elementi hanno lo stesso tipo `dtype`), di dimensione fissa e allocati in un **blocco contiguo di memoria** $\to$ molto più *efficienti* per operazioni matematiche (es. somma su 10.000 elementi: ~9.5 µs con `np.sum` contro ~568 µs con `sum` di Python).
- Se si crea un `ndarray` da una lista eterogenea (es. `[1, "ciao", False]`), NumPy converte tutti gli elementi a un tipo comune (es. stringhe `dtype='<U11'`).

## Attributi di un `ndarray`
I principali attributi sono:
- `dtype`: tipo degli elementi (es. `int64`, `uint8`, `float32`)
- `shape`: tupla con le dimensioni lungo ciascun asse (modificabile con `reshape()`)
- `size`: numero totale di elementi
- `ndim`: numero di dimensioni (assi)

```python
X = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
X.shape  # (3, 3)
X.size   # 9
X.ndim   # 2
```

## Creazione di `ndarray` speciali
```python
np.arange(10)                     # array([0, 1, ..., 9])
np.zeros((4, 2), dtype=np.int32)  # matrice 4x2 di zeri
np.ones((4, 2), dtype=np.int32)   # matrice 4x2 di uni
np.empty((4, 2), dtype=float)     # matrice non inizializzata
np.full((2, 2), 7.0)              # matrice riempita con 7.0
np.identity(3)                    # o np.eye(3): matrice identità 3x3
np.random.uniform(0, 1, (2, 2))   # valori casuali uniformi in [0, 1)
```

## Operazioni su `ndarray`
- **Operazioni element-wise** (elemento per elemento): `X + Y`, `X - Y`, `X * Y`, `X / Y`, `2 * X`, `np.sqrt(X)`
- **Prodotto matriciale**: `np.dot(X, Y)`
- **Sommatoria lungo gli assi**:
  ```python
  x = np.array([[1, 2], [3, 4]])
  np.sum(x)          # 10 (tutti gli elementi)
  np.sum(x, axis=0)  # array([4, 6]) (somma per colonna)
  np.sum(x, axis=1)  # array([3, 7]) (somma per riga)
  ```
- **Trasposizione**: `X.T` oppure `np.transpose(X)`

## Indicizzazione e Slicing 2D
```python
a = np.array([[1, 2, 3], [3, 4, 5], [4, 5, 6]])
a[:, 1]      # oppure a[..., 1] -> array([2, 4, 5])
a[2, :]      # oppure a[2, ...] -> array([4, 5, 6])
a[0:2, 0:2]  # sottomatrice 2x2: array([[1, 2], [3, 4]])
```

## Copia vs Vista (*View*)
Quando si opera con gli array è fondamentale sapere se i dati vengono copiati o condivisi:
- **Nessuna copia (alias)**: `arr2 = arr1` non copia i dati, crea solo un riferimento allo stesso array.
- **Vista / Copia superficiale (*view*)**: lo **slicing** produce una vista, cioè un nuovo oggetto array che **condivide gli stessi dati** in memoria. Modificare la vista modifica anche l'array originale:
  ```python
  a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
  b = a[:2, 1:3]
  b[0, 0] = 99  # modifica anche a[0, 1] -> 99!
  ```
- **Copia profonda (*deep copy*)**: `c = np.copy(a)` (o `a.copy()`) crea una copia indipendente dell'array e dei suoi dati.
