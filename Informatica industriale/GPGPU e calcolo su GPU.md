# GPGPU e calcolo su GPU

> Nota derivata da [[Informatica industriale]] — macro-argomento: **GPU general-purpose, architettura, pipeline, SM, limiti SIMT**.

---

## Da grafica a calcolo generico

| Fase | Descrizione |
|------|-------------|
| **GPU tradizionale** | Pipeline fissa per rendering 3D (vertex → raster → fragment) |
| **OpenGL / DirectX** | API alto livello: luci, shader, texture, geometria — **solo grafica** |
| **GPGPU (General-Purpose GPU)** | Sfrutta **migliaia di core** per calcolo dati-parallelo: algebra lineare, ML, simulazione, imaging, crypto |

### Vendor principali
- **NVIDIA** (CUDA, driver proprietari, dominano HPC/ML)
- **AMD** (ROCm, HIP, aperto ma maturità variabile)
- **Intel** (oneAPI / SYCL, Xe / Arc / Ponte Vecchio)
- **Apple** (Metal, unified memory su Apple Silicon)
- **ARM** (Mali, Bifrost/Valhall, Vulkan Compute)

> **Differenza chiave:** ogni vendor ha **modello di programmazione diverso** (CUDA ≠ HIP ≠ SYCL ≠ Metal). Portabilità → layer astratti (SYCL, Kokkos, Raja, OpenCL deprecato).

---

## Perché GPU per calcolo?

| CPU | GPU |
|-----|-----|
| Pochi core complessi (OoO, branch pred, cache grandi) | **Migliaia di core semplici** (in-order, SIMT) |
| Ottimizzata per **latenza** single-thread | Ottimizzata per **throughput** data-parallel |
| Memoria: cache gerarchiche profonde | Memoria: **bandwidth enorme** (HBM, GDDR6X), cache piccole |
| Controllo flusso arbitrario | **SIMT**: stesso instruction stream su warp/wavefront |

> **Data center**: GPU sono *de facto* standard per AI training/inference, HPC, rendering farm.

---

## Pipeline GPU (semplificata)

```
┌─────────┐   ┌─────────┐   ┌─────────┐   ┌─────────────┐   ┌────────────┐
│ FETCH   │──▶│ DECODE  │──▶│  LOAD   │──▶│  EXECUTE    │──▶│  STORE     │
│ (istr.) │   │         │   │ (dati)  │   │  (SIMT,     │   │  (write    │
└─────────┘   └─────────┘   └─────────┘   │   multicore)│   │   back)    │
                                           └─────────────┘   └────────────┘
        ▲                                   ▲
        │                                   │
        └──────────────┬────────────────────┘
                       ▼
              Stesse unità (fetch/decode/load/store)
              → **collo di bottiglia front-end**
```

> **Warning:** Fasi 1,2,3,5 (fetch, decode, load, store) sono **condivise** tra tutti i core di un *Streaming Multiprocessor (SM)*.  
> → L'SMP può emettere **una sola istruzione per ciclo per warp** → **SIMT (Single Instruction Multiple Threads)**.  
> → **Non** "un'operazione diversa per core" come in CPU MIMD.

---

## Architettura interna: SM (Streaming Multiprocessor)

```
GPU Chip
┌─────────────────────────────────────────────────────┐
│  SM_0    SM_1    SM_2    …    SM_N                  │
│ ┌─────┐ ┌─────┐ ┌─────┐       ┌─────┐              │
│ │Core │ │Core │ │Core │  …    │Core │  (CUDA core / │
│ │(FP32│ │(FP32│ │(FP32│       │(FP32│   Stream Proc)│
│ │ INT)│ │ INT)│ │ INT)│       │ INT)│              │
│ └──┬──┘ └──┬──┘ └──┬──┘       └──┬──┘              │
│    │       │       │             │                 │
│    └───────┼───────┼─────────────┘                 │
│            ▼       ▼                               │
│      ┌─────────────────┐                           │
│      │  Warp Scheduler │  (emette 1 istr/warp/ciclo)│
│      └────────┬────────┘                           │
│               │                                    │
│      ┌────────┴────────┐                           │
│      │  Register File  │  (64–256 KB per SM)       │
│      │  Shared Memory  │  (48–228 KB, user-managed)│
│      │  L1 / Texture   │                           │
│      └─────────────────┘                           │
└─────────────────────────────────────────────────────┘
                       │
                       ▼
              ┌─────────────────┐
              │  L2 Cache       │  (condivisa tra SM, 6–50 MB)
              │  Memory Ctrl    │  → HBM / GDDR6X (TB/s)
              └─────────────────┘
```

### Concetti chiave
| Concetto | Dettaglio |
|----------|-----------|
| **Warp / Wavefront** | Gruppo di thread (32 NVIDIA, 64 AMD) eseguiti in lock-step |
| **SIMT** | Stessa istruzione, dati diversi; *divergenza* = serializzazione percorsi |
| **Shared Memory** | Scratchpad veloce (software-managed cache) per cooperazione intra-block |
| **Occupancy** | % warps attivi vs max teorico → nasconde latenza memoria |
| **Coalescing** | Accessi contigui da warp → singola transazione memoria (128 B) |

---

## Modelli di programmazione principali

| Modello | Vendor / Standard | Linguaggio | Note |
|---------|-------------------|------------|------|
| **CUDA** | NVIDIA | C++ (estensioni `<<<>>>`), PTX ISA | Più maturo, librerie ricche (cuBLAS, cuDNN, Thrust) |
| **HIP** | AMD | Quasi identico a CUDA (porting automatizzato `hipify`) | ROCm stack Linux |
| **SYCL / oneAPI** | Intel / Khronos | C++17 single-source, template | Target CPU+GPU+FPGA, portabile |
| **Metal** | Apple | Objective-C / Swift / C++ | Unified memory, tile shaders |
| **Vulkan Compute** | Khronos | SPIR-V, C/++ via glslang | Cross-vendor, verbose, basso livello |
| **OpenCL** | Khronos (legacy) | C kernel + host API | Deprecato da Apple/NVIDIA, ancora su embedded |

---

## Quando usare GPU (e quando no)

| ✅ Adatto | ❌ Non adatto |
|-----------|---------------|
| Algebra lineare densa (GEMM, SVD) | Codice seriale con branch complessi |
| Convoluzioni / stencil regolari | Strutture dati puntatore-intensive (grafo, albero) |
| Monte Carlo, particle systems | Piccoli problemi (overhead launch > gain) |
| Deep learning training/inference | Latenza singola richiesta < 1 ms (CPU meglio) |
| Elaborazione immagine/video | Logica di controllo / state machine |

---

## Riferimenti slide
- Struttura operazione GPU: sezioni "LE FASI" e warning SIMT
- SM multiple per chip: nota finale "(cose che mancano) Le gpu sono formate dalle SM…"

---

## Collegamenti
- [[Informatica industriale]] — Indice generale
- [[Programmazione parallela]] — Offloading, data parallelism, work queue → mappatura su GPU
- [[Concorrenza e sincronizzazione]] — Modello memoria GPU (coerenza rilassata, atomic, barrier `__syncthreads()`)