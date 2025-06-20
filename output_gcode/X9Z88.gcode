G21 ; set units to mm
G90 ; use absolute positioning
G0 X0.00 Y-0.12 ; move to start of X
M3 ; pen down
G1 X10.00 Y15.24 ; draw X
M5 ; pen up
G0 X15.00 Y0.28 ; move to start of 9
M3 ; pen down
G1 X25.00 Y15.62 ; draw 9
M5 ; pen up
G0 X30.00 Y-0.12 ; move to start of Z
M3 ; pen down
G1 X40.00 Y14.85 ; draw Z
M5 ; pen up
G0 X45.00 Y-0.87 ; move to start of 8
M3 ; pen down
G1 X55.00 Y14.34 ; draw 8
M5 ; pen up
G0 X60.00 Y-0.57 ; move to start of 8
M3 ; pen down
G1 X70.00 Y14.31 ; draw 8
M5 ; pen up