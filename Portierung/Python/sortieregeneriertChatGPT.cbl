IDENTIFICATION DIVISION.
PROGRAM-ID. SortNumbers.

DATA DIVISION.
WORKING-STORAGE SECTION.
01 Numbers PIC 9(2) OCCURS 6 TIMES VALUE '050209010506'.
01 Sorted-Numbers PIC 9(2) OCCURS 6 TIMES.

PROCEDURE DIVISION.
    MOVE Numbers TO Sorted-Numbers
    PERFORM VARYING I FROM 1 BY 1 UNTIL I > 5
        PERFORM VARYING J FROM I + 1 BY 1 UNTIL J > 6
            IF Sorted-Numbers(I) > Sorted-Numbers(J)
                MOVE Sorted-Numbers(I) TO TEMP
                MOVE Sorted-Numbers(J) TO Sorted-Numbers(I)
                MOVE TEMP TO Sorted-Numbers(J)
            END-IF
        END-PERFORM
    END-PERFORM
    DISPLAY "Sorted numbers: " WITH NO ADVANCING
    PERFORM VARYING K FROM 1 BY 1 UNTIL K > 6
        DISPLAY Sorted-Numbers(K) WITH NO ADVANCING
        IF K < 6 THEN DISPLAY " " WITH NO ADVANCING END-IF
    END-PERFORM
    DISPLAY "".

STOP RUN.
