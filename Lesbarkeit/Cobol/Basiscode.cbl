IDENTIFICATION DIVISION.
PROGRAM-ID. VerbessertesProgramm.

ENVIRONMENT DIVISION.
INPUT-OUTPUT SECTION.
FILE-CONTROL.
    SELECT EingabeDatei ASSIGN TO "input.txt"
        ORGANIZATION IS LINE SEQUENTIAL.

DATA DIVISION.
FILE SECTION.
FD  EingabeDatei.
01  DateiRecord.
    05 DateiInhalt PIC X(80).

WORKING-STORAGE SECTION.
01  AnzeigeInhalt PIC X(80).
01  DateiEnde PIC X VALUE 'N'.

PROCEDURE DIVISION.
Hauptprogramm.
    OPEN INPUT EingabeDatei
    PERFORM DateiVerarbeiten UNTIL DateiEnde = 'Y'
    CLOSE EingabeDatei
    STOP RUN.

DateiVerarbeiten.
    READ EingabeDatei INTO AnzeigeInhalt
        AT END
            MOVE 'Y' TO DateiEnde
        NOT AT END
            DISPLAY AnzeigeInhalt
    END-READ.
