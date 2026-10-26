# POSIX
I POSIX Threads sono chiamati **PTHreads**, e sono un modello di esecuzione che esiste **indipendentemente dal linguaggio di programmazione**, come **modello di esecuzione in parallelo**.

Specifica ad un Sistema Operativo un'**interfaccia** simile ai sistemi UNIX.
POSIX mantiene una differenza tra **thread** e **processi**.
Ogni processi ha almeno un thread detto **main**, tutti i thread **condividono** lo steso indirizzo di memoria, ma mantengono uno **stack privato**.
[[Lab_PThreads.pdf#page=4|Lab_PThreads, pagina 4]]