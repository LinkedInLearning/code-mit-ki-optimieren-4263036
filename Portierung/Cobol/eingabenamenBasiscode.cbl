       IDENTIFICATION DIVISION.

       PROGRAM-ID. EINGABENAMEN.
      
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 WS-NAME PIC X(5).

       PROCEDURE DIVISION.
           DISPLAY "Bitte geben Sie Ihren Namen an".
           ACCEPT WS-NAME.
           DISPLAY "Hallo ", WS-NAME.
       STOP RUN.
       END PROGRAM EINGABENAMEN.
