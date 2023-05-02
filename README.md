# Thesis

1. index of the thesis - :white_check_mark:

- [x] definire i cuts e binning mediato per ogni monitor 
- [x] fare fit per ogni monitor
- [x] mettere gli errori statistici ai punti
- [x] ripulire programma di fit.cc e fit.h dalle schifezze
- [x] finire la averaged asymmetry nel programma
- [x] fissare riunione con Anselm per discutere se modificare modello lineare o proporre tagli 
- [x] confrontare risultati del fit con i valori ottenuti da slowvariation beam
- [x] fare stesso tipo di analisi che si è fatto su detector B anche per il detector A
- [x] Spiegato a grandi linee come funzionano i VFCs monitors
- [x] inserire i valori di Q^2
- [x] studiare la documentazione della NINO board, da quella si può dire qualcosa sul segnale
- [x] preparare documentazione su fit.cc e fit.h da consegnare ad Anselm

Introduzione 
- [] scrivere abstract/introduzione di carattere generale
- [] Iniziare ad impostare l'introduzione, dalle stelle di neutroni all'asimmetria trasversa

Capitolo sulla teoria:

- [] iniziare paragrafo contributo intermedio anelastico.
- [] completare paragrafo teoria contributo elastico.
- [] presentare i risultati della misura fatta da PREX.
- [] descrivere il modello lineare usato dopo nell'analisi.

Capitolo Setup sperimentale:
- [x] Spiegare a grandi linee come funzionano i Monitor del fascio, Resistenza di Shunt e eccitazioni nelle cavità risonanti
- [] chiedere ad Anselm documentazione sulla MasterBoard
- [] Come si stima l'errore sistematico?
- [] discutere la stabilizzazione del fascio.
- [] spiegare il funzionamento polarimetro Moller e Compton, spiegare perchè sarà utilizzato il moller in futuro.
- [] pockels cell.

Capitolo di Analisi:
- [x] migliorare l'output del programma fit.cc, inserire unit test e cambiare formato dati
- [x] controllare le run sospette senza stabilizzazione, può aiutare a capire meglio il sistematico (?)
- [x] la correlazione Asimmetria e parametri del fascio non è irrilevante, bisogna investigare
- [x] ricontrollare la procedura di autocalibration, i valori di Anselm non sembrano essere corretti. (Conteggi negativi, impossibile)
- [x] controllare le run che potrebbero non avere il fascio polarizzato.
- [x] finire l'analisi dello scan in attenuation anche per il detector A
- [x] confrontare i risultati con curve_fit di scipy
- [] completare paragrafo sui test in laboratorio dei due detector
- [] provare a vedere se c'è un test per controllare se ci sono doppi conteggi, oppure si conta di meno.
- [] vedere se è possibile estrarre almeno una stima rozza dell'incertezza associata ai monitor X25/X21 e Y25/Y21.
- [] discutere le correlazioni tra i parametri del fascio, in particolare mostrare che si può omettere nel modello xp e yp.
- [] rivedere il modello che si è usato per fare la calibrazione delle pmt.
- [] Capire perchè le asimmetrie calcolata con lo slowvariation e dal fit sono in disaccordo per svariati ordini di grandezza
- [] impostare il ricampionamento.
- [] inserire istogrammi asimmetrie per ogni pmt.
- [x] mettere il valore simulato della correlazione nel plot.
- [] correggere i cuts e completare il capitolo di analisi.

CORREZIONI FORTI

- [x] inserire uno schema dell'acceleratore e una dei detector.
- [x] cambiare la struttura della tesi, spezzare in due il capitolo analysis, la prima parte detector test and calibration, la seconda asymmetry on carbon.
- [x] introdurre prima di ogni capitolo un cappello introduttivo.
- [x] tutti i commenti nella tesi vanno definiti con un comando.
- [] i plot dei conteggi in funzione della soglia in mV vanno ricontrollati.
- [] chiedera a igors come ha ottenuto i dati di threshold vs attenuation.
- [] rivedere l'abstract
