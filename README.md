# PySn
Beginner Project Python <br>


Erforderlich: <br>
  Allgemeine Funktionen:  <br>
--> klassisches Snake Programm  <br>
--> Spielstände speichern <br>
--> GUI basierte Anzeige <br>

  GUI: <br>
--> Lebensanzeige (3 Leben) <br>
--> Blockbasiertes Spielfeld <br>
--> Blockbasierte Schlange <br>
--> steuerbare durch Pfeiltasten <br>
--> Farbliche Veränderung des Spielfeld / Schlange <br>
  -->GUI Menüs: <br>
    --> Highscore <br>
    --> Startscreen <br>
    --> Spielfeld <br>

Optional: <br>
--> Networking (TCP/IP?) 2 Spieler Modi <br>
--> Datenbank (Spieler,Highscore)



To do Softwarearchitektur (Julian)
Benötige Klassen:


--> WICHTUNG ZU BEACHTEN!
    MAN BEACHTE: DIE FUNKTIONEN SOLLEN SEPERIERT SEIN
        BSP:
        --> SPIELER SOLL NUR FUNKTIONEN HABE DIE FÜR SPIELER SIND
        --> SPIELER SOLL NUR ATTRIBUTE (VARIABLEN) HABE DIE FÜR SPIELER SIND!
    --> SINNVOLLE VERERBUNG
        --> WELCHE ATTRIBUTE SOLLEN DIE KINDKLASSEN AUF ZUGRIFF HABEN
        --> WELCHE ATTRIBUTE HABEN DIE KINDSKLASSEN SELBST?
    --> VERWENDEN VON GETTER / SETTER FÜR DIE SPIEL;HINDERNISSE UND SPIELER!
- Hindernisse (verschiedene Punktanzahl für verschiedene Hindernisse)
  --> Vererbung
  --> Platzierung Hindernisse


- Spiel
   --> Spiel starten
   --> Spiel beenden
   --> Spiel pausieren

- Spieler
   --> Punktestand
   --> Vererbung (für Multiplayer)
      --> Spieler der Spiel hostet
      --> Spieler der Spiel joint

