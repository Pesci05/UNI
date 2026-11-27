---
title: IIOT - Indice di Studio
tags:
  - iiot
  - iot
  - indice
  - studio
aliases:
  - IIOT
  - Indice IoT
---

# IIOT — Indice di Studio

> [!info] Come usare questo indice
> Questa nota organizza tutti gli argomenti presenti nella cartella `IOT/lectures`.
> Per ogni lezione trovi:
> - **Checkbox** (`- [ ]`) per tracciare l'avanzamento dello studio
> - **Dispensa**: collegamento diretto alla lezione originale in `lectures`
> - **Appunti**: collegamento alla nota personale da creare e compilare per quell'argomento
> - **Argomenti chiave**: i concetti principali da approfondire durante lo studio

---

## 1. Cyber-Physical Systems & Internet of Things

- [ ] **Introduction to Cyber-Physical Systems & IoT**
  - Dispensa: [[cps_introduction|Introduction to Cyber-Physical Systems & IoT]]
  - Appunti: [[Appunti - CPS e IoT]]
  - Argomenti chiave: Internet e dispositivi connessi, evoluzione IoT, Smart Objects, M2M vs IoT, stack IoT, Cyber-Physical Systems (CPS).

---

## 2. Programming & Software Engineering (Python)

- [ ] **Python Best Practices & Object-Oriented Programming**
  - Dispensa: [[python_best_practices_and_oop|Python Best Practices & OOP]] (moduli: [[python_best_practices|Python Best Practices]], [[python_oop|Python OOP & Use Case Modelling]])
  - Appunti: [[Appunti - Python Best Practices e OOP]]
  - Argomenti chiave: `if __name__ == "__main__"`, gestione eccezioni, type hints, configurazioni ed environment variables, logging, virtual env e `uv`, struttura progetto/moduli, principi OOP e modellazione di casi d'uso Smart Home.

- [ ] **Python Advanced Topics — Panoramica**
  - Dispensa: [[python_advanced_topics|Python Advanced Topics]]
  - Appunti: [[Appunti - Python Advanced Topics]]
  - Argomenti chiave:
    - [ ] [[concurrency_and_threading|Concurrency & Threading]] → [[Appunti - Concurrency e Threading]] *(GIL, `threading`, race condition, lock, primitive di coordinamento, graceful shutdown)*
    - [ ] [[thread_pools_and_futures|Thread Pools & Futures]] → [[Appunti - Thread Pools e Futures]] *(`ThreadPoolExecutor`, `Future`, `ProcessPoolExecutor`, timeout ed eccezioni)*
    - [ ] [[asyncio|Asyncio]] → [[Appunti - Asyncio]] *(coroutine, `TaskGroup`, timeout, codice bloccante, primitive di sincronizzazione)*
    - [ ] [[queues|Thread-Safe Queues]] → [[Appunti - Queues]] *(modulo `queue`, pattern Producer-Consumer, backpressure, pipeline multi-stage)*
    - [ ] [[event_driven_architecture|Event-Driven Architecture in Python]] → [[Appunti - Event-Driven in Python]] *(Observer pattern, Event Bus sincrono/asincrono con thread e `asyncio`)*
    - [ ] [[testing|Testing in Python]] → [[Appunti - Testing in Python]] *(`unittest`, `pytest`, test doubles/mock, testing di codice concorrente, `asyncio` e code, coverage)*

---

## 3. Communication Protocols & Patterns

- [ ] **IoT Protocols Overview**
  - Dispensa: [[iot_protocols_overview|IoT Protocols Characteristics & Overview]]
  - Appunti: [[Appunti - Panoramica Protocolli IoT]]
  - Argomenti chiave: stack Internet tradizionale vs stack IoT, protocolli di livello applicativo, modelli di interazione, standardizzazione e interoperabilità.

- [ ] **The HTTP Protocol & RESTful Architectural Style**
  - Dispensa: [[http_protocol_and_rest|The HTTP Protocol & RESTful Architectural Style]]
  - Appunti: [[Appunti - HTTP e REST]]
  - Argomenti chiave: approccio Web-based per IoT, messaggi HTTP (GET, POST, PUT, DELETE, status code), stile architetturale REST, livello di maturità REST, nuovo metodo HTTP `QUERY`.

- [ ] **Publish/Subscribe Pattern & MQTT Protocol**
  - Dispensa: [[pubsub_mqtt_protocol|Pub/Sub Introduction & MQTT Protocol]]
  - Appunti: [[Appunti - Pub-Sub e MQTT]]
  - Argomenti chiave: pattern Pub/Sub, broker e code, confronto con ZeroMQ/DDS/Kafka/AMQP, protocollo MQTT, topic e wildcard (`+`, `#`), QoS (0, 1, 2), Persistent Sessions, Retained Messages, Last Will and Testament (LWT), Bridge Mode.

- [ ] **The Constrained Application Protocol (CoAP)**
  - Dispensa: [[coap_protocol|The Constrained Application Protocol (CoAP)]]
  - Appunti: [[Appunti - CoAP]]
  - Argomenti chiave: reti IoT constrained (LLN), perché HTTP/TCP non bastano, architettura a due livelli (Messaging e Request/Response su UDP), affidabilità (CON/NON/ACK/RST), formato messaggio e opzioni, funzionalità IoT (Observe, Blockwise), confronto CoAP vs HTTP vs MQTT.

- [ ] **Resource & Service Discovery**
  - Dispensa: [[resource_and_service_discovery|Resource & Service Discovery]]
  - Appunti: [[Appunti - Resource e Service Discovery]]
  - Argomenti chiave: Resource Discovery, Web Linking e CoRE Link Format (RFC 6690), discovery unicast/multicast, CoRE Interfaces, CoRE Resource Directory, Service Discovery (mDNS/DNS-SD, UPnP, Physical Web / URI Beacons).

- [ ] **IoT Smart Object Design**
  - Dispensa: [[iot_smart_object_design|IoT Smart Object Design]]
  - Appunti: [[Appunti - Smart Object Design]]
  - Argomenti chiave: progettazione di Smart Object, modellazione risorse CoAP (caso d'uso Smart Home), modellazione topic MQTT (caso d'uso Fleet Monitoring), librerie software e confronto design CoAP vs MQTT.

---

## 4. Data Formats

- [ ] **Classic Data Formats: JSON, YAML, TOML & CSV**
  - Dispensa: [[data_formats_classic|Classic Data Formats: JSON, YAML, TOML & CSV]]
  - Appunti: [[Appunti - Formati Dati Classici]]
  - Argomenti chiave: rappresentazione dati in IoT/CPS, sintassi e casi d'uso di JSON, YAML, TOML e CSV, validazione dei dati e confronto tra formati.

- [ ] **IoT Data Formats — Sensor Measurement Lists (SenML)**
  - Dispensa: [[data_formats_iot_senml|Sensor Measurement Lists (SenML)]]
  - Appunti: [[Appunti - SenML]]
  - Argomenti chiave: struttura e semantica SenML, Base Fields e Regular Fields, risoluzione di un SenML Pack, Labels e Units, attuazione, estensibilità, SenML-CBOR, creazione e parsing in Python.

- [ ] **IoT Data Formats — Concise Binary Object Representation (CBOR)**
  - Dispensa: [[data_formats_iot_cbor|Concise Binary Object Representation (CBOR)]]
  - Appunti: [[Appunti - CBOR]]
  - Argomenti chiave: motivazioni dei formati binari, modello dati e tipi, struttura di encoding, uso in IoT (CoAP/SenML), libreria Python `cbor2`, confronto dimensioni rispetto a JSON.

---

## 5. Software Architectures

- [ ] **Software Architecture — Monolithic Approaches**
  - Dispensa: [[soft_arch_monolithic_approaches|Software Architectures Monolithic Approaches]]
  - Appunti: [[Appunti - Architetture Monolitiche]]
  - Argomenti chiave: definizione e caratteristiche architetturali (operazionali, strutturali, cross-cutting), anti-pattern (Big Ball of Mud), pattern semplici (Client-Server, Three-Tier), architettura Layered, Pipeline / ETL in IoT, Microkernel.

- [ ] **Software Architecture — Distributed Approaches**
  - Dispensa: [[soft_arch_distributed_approaches|Software Architectures Distributed Approaches]]
  - Appunti: [[Appunti - Architetture Distribuite]]
  - Argomenti chiave: le 8 Fallacies of Distributed Computing (incluso Stamp Coupling), transazioni distribuite, Service-Based Architecture, Event-Driven Architecture (Broker vs Mediator topology), Serverless Architecture.

- [ ] **Software Architecture — Microservices**
  - Dispensa: [[soft_arch_microservices|Microservices Software Architectures]]
  - Appunti: [[Appunti - Microservizi]]
  - Argomenti chiave: definizione, pro/contro rispetto al monolite, gestione dati, API Gateway e BFF, esempio IoT a microservizi, Scalability Cube (assi X, Y, Z), VM vs container, pattern Sidecar e Load Balancer.

---

## 6. Cloud & Edge Computing

- [ ] **Edge Computing for the IoT**
  - Dispensa: [[edge_computing_for_the_iot|Edge Computing for the IoT]]
  - Appunti: [[Appunti - Edge Computing e IoT Hub]]
  - Argomenti chiave: Cloud Computing e IoT, il problema della Cloud "Addiction", visione Edge/Fog Computing, applicazioni IoT distribuite, IoT Hub come Fog Node (protocol stack e application layer), sincronizzazione Cloud-Edge e Virtual Replication.

---

## 7. End-to-End System Design

- [ ] **End-2-End Architecture Design**
  - Dispensa: [[end2end_architecture_design|End-2-End Architecture Design]]
  - Appunti: [[Appunti - End-to-End System Design]]
  - Argomenti chiave: progettazione end-to-end su casi d'uso reali (Personal Health Device, Health & Sport, Industrial Remote Telemetry), modelli dati, scelta protocolli e comunicazione, Dual-Broker Architecture.

---

## Piano di Studio (2 Settimane)

> [!tip] Obiettivo del piano
> Distribuzione consigliata su **14 giorni** per coprire teoria, stesura degli appunti e laboratori pratici. Puoi adattare i giorni in base alla tua dimestichezza con Python e le reti.

### Settimana 1 — Fondamenti, Python e Protocolli IoT

- [ ] **Giorno 1 — Introduzione e Python Base**: [[cps_introduction|CPS & IoT]] + [[python_best_practices|Python Best Practices]]
- [ ] **Giorno 2 — OOP e Concorrenza**: [[python_oop|Python OOP & Use Case Modelling]] + [[concurrency_and_threading|Concurrency & Threading]]
- [ ] **Giorno 3 — Programmazione Asincrona e Code**: [[thread_pools_and_futures|Thread Pools & Futures]] + [[asyncio|Asyncio]] + [[queues|Thread-Safe Queues]]
- [ ] **Giorno 4 — Eventi, Testing e Pratica**: [[event_driven_architecture|Event-Driven Architecture]] + [[testing|Testing in Python]] *(+ codice `smart-factory`)*
- [ ] **Giorno 5 — Stack IoT, HTTP e REST**: [[iot_protocols_overview|IoT Protocols Overview]] + [[http_protocol_and_rest|HTTP & REST]] *(+ lab `laboratory-python-http-rest-api`)*
- [ ] **Giorno 6 — MQTT e CoAP**: [[pubsub_mqtt_protocol|Pub/Sub & MQTT]] + [[coap_protocol|CoAP]] *(+ lab `laboratory-python-coap-main`)*
- [ ] **Giorno 7 — Discovery, Smart Object e Ripasso**: [[resource_and_service_discovery|Resource & Service Discovery]] + [[iot_smart_object_design|IoT Smart Object Design]] + consolidamento appunti Settimana 1

### Settimana 2 — Formati Dati, Architetture, Edge e System Design

- [ ] **Giorno 8 — Formati Dati Classici**: [[data_formats_classic|JSON, YAML, TOML & CSV]]
- [ ] **Giorno 9 — Formati Dati IoT**: [[data_formats_iot_senml|SenML]] + [[data_formats_iot_cbor|CBOR]]
- [ ] **Giorno 10 — Architetture Monolitiche**: [[soft_arch_monolithic_approaches|Monolithic Approaches]]
- [ ] **Giorno 11 — Architetture Distribuite**: [[soft_arch_distributed_approaches|Distributed Approaches]]
- [ ] **Giorno 12 — Microservizi**: [[soft_arch_microservices|Microservices Software Architectures]]
- [ ] **Giorno 13 — Cloud & Edge Computing**: [[edge_computing_for_the_iot|Edge Computing for the IoT]]
- [ ] **Giorno 14 — Design End-to-End e Ripasso Finale**: [[end2end_architecture_design|End-2-End Architecture Design]] + revisione completa di tutti gli appunti

---

## Note e Laboratori Correlati

- Promemoria corso: [[2026-10-22]]
- Progetti/Laboratori Python nella cartella `IOT/python/`:
  - `IOT/python/smart-factory`
  - `IOT/python/laboratory-python-http-rest-api`
  - `IOT/python/laboratory-python-coap-main`
