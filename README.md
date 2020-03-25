<h1>Covid-19 API w/ Flask</h1>
<p>La Web Api usa la libreria selenium per automatizzare l'apertura del browser ed effettuare lo scraping dei dati dalla tabella del sito https://www.worldometers.info/coronavirus/.
Prende esclusivamente i dati con colonne non vuote e le carica in un database. 
Questo processo di aggiornamento del db viene fatto alle 12:00,15:00,18:00 e 21:00 di ogni giorno.</p>

<h2>Come funziona</h2>
<p>API che ritorna i casi in tutti i paesi del mondo: <a href="http://80.211.145.147/api/v1/resources/countries">/api/v1/resources/countries</a></p>
<p>API che ritorna i casi di uno stato indicato nell’url: 
<a href="http://80.211.145.147/api/v1/resources/countries">/api/v1/resources/countries/{state}</a></p>

</br></br>

<h3 align="center">Credits</h3>
<p align="center">
@Al3xx01
</p>
<p align="center">
@SyllaAbu
</p>
