## Quiz game
Lo scopo del progetto e' installare una VM (alpine-slim) minimale con pre-caricata l'immagine di un container.  
La VM garantisce la connessione verso un server (posto nella sottorete 172.20.125.0/24), l'applicazione e' sviluppata su Docker e realizza un'architettura client/server.  

## Istruzioni

1. Scaricare dal sito 'https://storage.to/c/HxwJ6BLDt' in una sola cartella locale i 3 file della VM in formato OVF (.ovf .vmdk .mf).  

2. Su host client ESXi installare la VM, configurando la connettivita' per raggiungere la sottorete 172.20.125.0/24.Username = root, password = root.  
3. Verificare che la VM abbia indirizzo IP appartenente alla sottorete, quindi 172.20.125.X.

4. Sulla VM e' presente una cartella 'game-client' ed e' gia disponibile l'immagine Docker del client del gioco.  
5. Creare il relativo container e seguire le istruzioni a video.

6. Il container termina selezionata la risposta corretta.  

Il gioco consiste nel rispondere ad una domanda: vince chi risponde per primo!
