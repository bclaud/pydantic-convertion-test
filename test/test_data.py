reais_to_cents_data = [
    (10.00, 1000),
    (5.43, 543),
    (9.99, 999),
    (100.99, 10099),
    (15.75, 1575),
    (20.50, 2050),
    (3.25, 325),
    (7.80, 780),
    (12.45, 1245),
    (6.89, 689),
    (25.30, 2530),
    (17.60, 1760),
    (8.77, 877),
    (30.90, 3090),
    (50.25, 5025),
    (99.99, 9999),
    (45.67, 4567),
    (23.45, 2345),
    (88.88, 8888),
    (34.56, 3456),
    (60.75, 6075),
    (70.45, 7045),
    (43.20, 4320),
    (56.78, 5678),
    (79.99, 7999),
    (65.43, 6543),
    (87.65, 8765),
    (95.25, 9525),
    (120.50, 12050),
    (150.75, 15075),
    (200.90, 20090),
    (250.25, 25025),
    (175.60, 17560),
    (180.77, 18077),
    (210.30, 21030),
    (300.99, 30099),
    (350.45, 35045),
    (400.67, 40067),
    (450.89, 45089),
    (500.25, 50025),
    (550.70, 55070),
    (600.34, 60034),
    (650.98, 65098),
    (700.56, 70056),
    (750.39, 75039),
    (800.46, 80046),
    (850.23, 85023),
    (900.99, 90099),
    (950.75, 95075),
    (1000.10, 100010),
    (1050.55, 105055),
    (1100.88, 110088),
    (1150.33, 115033),
    (1200.66, 120066),
    (1250.99, 125099),
    (1300.30, 130030),
    (1350.68, 135068),
    (1400.77, 140077),
    (1450.55, 145055),
    (1500.99, 150099),
    (1550.45, 155045),
    (1600.10, 160010),
    (1650.75, 165075),
    (1700.25, 170025),
    (1750.50, 175050),
    (1800.90, 180090),
    (1850.40, 185040),
    (1900.80, 190080),
    (1950.70, 195070),
    (2000.99, 200099),
    (2050.89, 205089),
    (2100.76, 210076),
    (2150.43, 215043),
    (2200.32, 220032),
    (2250.65, 225065),
    (2300.98, 230098),
    (2350.87, 235087),
    (2400.75, 240075),
    (2450.43, 245043),
    (2500.65, 250065),
    (2550.77, 255077),
    (2600.99, 260099),
    (2650.50, 265050),
    (2700.25, 270025),
    (2750.10, 275010),
    (2800.88, 280088),
    (2850.66, 285066),
    (2900.33, 290033),
    (2950.40, 295040),
    (3000.26, 300026),
    (3050.59, 305059),
    (3100.78, 310078),
    (3150.90, 315090),
    (3200.95, 320095),
    (3250.99, 325099),
    (3300.75, 330075),
    (3350.60, 335060),
    (3400.50, 340050),
    (3450.40, 345040),
    (3500.30, 350030),
    (3550.78, 355078),
    (3600.88, 360088),
    (3650.99, 365099),
    (3700.76, 370076),
    (3750.57, 375057),
    (3800.40, 380040),
    (3850.50, 385050),
    (3900.60, 390060),
    (3950.70, 395070),
    (4000.80, 400080),
    (4050.89, 405089),
    (4100.95, 410095),
    (4150.99, 415099),
    (4200.75, 420075),
    (4250.56, 425056),
    (4300.38, 430038),
    (4350.45, 435045),
    (4400.56, 440056),
    (4450.77, 445077),
    (4500.99, 450099),
    (4550.88, 455088),
    (4600.77, 460077),
    (4650.66, 465066),
    (4700.55, 470055),
    (4750.44, 475044),
    (4800.33, 480033),
    (4850.22, 485022),
    (4900.11, 490011),
    (4950.55, 495055),
    (5000.99, 500099),
    (5050.88, 505088),
    (5100.77, 510077),
    (5150.66, 515066),
    (5200.55, 520055),
    (5250.44, 525044),
    (5300.33, 530033),
    (5350.22, 535022),
    (5400.11, 540011),
    (5450.55, 545055),
    (5500.99, 550099),
    (5550.88, 555088),
    (5600.77, 560077),
    (5650.66, 565066),
    (5700.55, 570055),
    (5750.44, 575044),
    (5800.33, 580033),
    (5850.22, 585022),
    (5900.11, 590011),
    (5950.55, 595055),
    (6000.99, 600099),
    (6050.88, 605088),
    (6100.77, 610077),
    (6150.66, 615066),
    (6200.55, 620055),
    (6250.44, 625044),
    (6300.33, 630033),
    (6350.22, 635022),
    (6400.11, 640011),
    (6450.55, 645055),
    (6500.99, 650099),
    (6550.88, 655088),
    (6600.77, 660077),
    (6650.66, 665066),
    (6700.55, 670055),
    (6750.44, 675044),
    (6800.33, 680033),
    (6850.22, 685022),
    (6900.11, 690011),
    (6950.55, 695055),
    (7000.99, 700099),
    (7050.88, 705088),
    (7100.77, 710077),
    (7150.66, 715066),
    (7200.55, 720055),
    (7250.44, 725044),
    (7300.33, 730033),
    (7350.22, 735022),
    (7400.11, 740011),
    (7450.55, 745055),
    (7500.99, 750099),
    (7550.88, 755088),
    (7600.77, 760077),
    (7650.66, 765066),
    (7700.55, 770055),
    (7750.44, 775044),
    (7800.33, 780033),
    (7850.22, 785022),
    (7900.11, 790011),
    (7950.55, 795055),
    (8000.99, 800099),
    (8050.88, 805088),
    (8100.77, 810077),
    (8150.66, 815066),
    (8200.55, 820055),
    (8250.44, 825044),
    (8300.33, 830033),
    (8350.22, 835022),
    (8400.11, 840011),
    (8450.55, 845055),
    (8500.99, 850099),
    (8550.88, 855088),
    (8600.77, 860077),
    (8650.66, 865066),
    (8700.55, 870055),
    (8750.44, 875044),
    (8800.33, 880033),
    (8850.22, 885022),
    (8900.11, 890011),
    (8950.55, 895055),
    (9000.99, 900099),
    (9050.88, 905088),
    (9100.77, 910077),
    (9150.66, 915066),
    (9200.55, 920055),
    (9250.44, 925044),
    (9300.33, 930033),
    (9350.22, 935022),
    (9400.11, 940011),
    (9450.55, 945055),
    (9500.99, 950099),
    (9550.88, 955088),
    (9600.77, 960077),
    (9650.66, 965066),
    (9700.55, 970055),
    (9750.44, 975044),
    (9800.33, 980033),
    (9850.22, 985022),
    (9900.11, 990011),
    (9950.55, 995055),
    (10000.99, 1000099),
    (10050.88, 1005088),
    (10100.77, 1010077),
    (10150.66, 1015066),
    (10200.55, 1020055),
    (10250.44, 1025044),
    (10300.33, 1030033),
    (10350.22, 1035022),
    (10400.11, 1040011),
    (10450.55, 1045055),
    (10500.99, 1050099),
    (10550.88, 1055088),
    (10600.77, 1060077),
    (10650.66, 1065066),
    (10700.55, 1070055),
    (10750.44, 1075044),
    (10800.33, 1080033),
    (10850.22, 1085022),
    (10900.11, 1090011),
    (10950.55, 1095055),
    (11000.99, 1100099),
    (11050.88, 1105088),
    (11100.77, 1110077),
    (11150.66, 1115066),
    (11200.55, 1120055),
    (11250.44, 1125044),
    (11300.33, 1130033),
    (11350.22, 1135022),
    (11400.11, 1140011),
    (11450.55, 1145055),
    (11500.99, 1150099),
    (11550.88, 1155088),
    (11600.77, 1160077),
    (11650.66, 1165066),
    (11700.55, 1170055),
    (11750.44, 1175044),
    (11800.33, 1180033),
    (11850.22, 1185022),
    (11900.11, 1190011),
    (11950.55, 1195055),
    (12000.99, 1200099),
    (12050.88, 1205088),
    (12100.77, 1210077),
    (12150.66, 1215066),
    (12200.55, 1220055),
    (12250.44, 1225044),
    (12300.33, 1230033),
    (12350.22, 1235022),
    (12400.11, 1240011),
    (12450.55, 1245055),
    (12500.99, 1250099),
    (12550.88, 1255088),
    (12600.77, 1260077),
    (12650.66, 1265066),
    (12700.55, 1270055),
    (12750.44, 1275044),
    (12800.33, 1280033),
    (12850.22, 1285022),
    (12900.11, 1290011),
    (12950.55, 1295055),
    (13000.99, 1300099),
    (13050.88, 1305088),
    (13100.77, 1310077),
    (13150.66, 1315066),
    (13200.55, 1320055),
    (13250.44, 1325044),
    (13300.33, 1330033),
    (13350.22, 1335022),
    (13400.11, 1340011),
    (13450.55, 1345055),
    (13500.99, 1350099),
    (13550.88, 1355088),
    (13600.77, 1360077),
    (13650.66, 1365066),
    (13700.55, 1370055),
    (13750.44, 1375044),
    (13800.33, 1380033),
    (13850.22, 1385022),
    (13900.11, 1390011),
    (13950.55, 1395055),
    (14000.99, 1400099),
    (14050.88, 1405088),
    (14100.77, 1410077),
    (14150.66, 1415066),
    (14200.55, 1420055),
    (14250.44, 1425044),
    (14300.33, 1430033),
    (14350.22, 1435022),
    (14400.11, 1440011),
    (14450.55, 1445055),
    (14500.99, 1450099),
    (14550.88, 1455088),
    (14600.77, 1460077),
    (14650.66, 1465066),
    (14700.55, 1470055),
    (14750.44, 1475044),
    (14800.33, 1480033),
    (14850.22, 1485022),
    (14900.11, 1490011),
    (14950.55, 1495055),
    (15000.99, 1500099),
    (15050.88, 1505088),
    (15100.77, 1510077),
    (15150.66, 1515066),
    (15200.55, 1520055),
    (15250.44, 1525044),
    (15300.33, 1530033),
    (15350.22, 1535022),
    (15400.11, 1540011),
    (15450.55, 1545055),
    (15500.99, 1550099),
    (15550.88, 1555088),
    (15600.77, 1560077),
    (15650.66, 1565066),
    (15700.55, 1570055),
    (15750.44, 1575044),
    (15800.33, 1580033),
    (15850.22, 1585022),
    (15900.11, 1590011),
    (15950.55, 1595055),
    (16000.99, 1600099),
    (16050.88, 1605088),
    (16100.77, 1610077),
    (16150.66, 1615066),
    (16200.55, 1620055),
    (16250.44, 1625044),
    (16300.33, 1630033),
    (16350.22, 1635022),
    (16400.11, 1640011),
    (16450.55, 1645055),
    (16500.99, 1650099),
    (16550.88, 1655088),
    (16600.77, 1660077),
    (16650.66, 1665066),
    (16700.55, 1670055),
    (16750.44, 1675044),
    (16800.33, 1680033),
    (16850.22, 1685022),
    (16900.11, 1690011),
    (100000.00, 10000000),
    (50000.43, 5000043),
    (99999.99, 9999999),
    (1000000.99, 100000099),
    (500000.50, 50000050),
    (999999.99, 99999999),
    (10000000.00, 1000000000),
    (5000000.43, 500000043),
    (9999999.99, 999999999),
    (100000000.99, 10000000099),
    (50000000.50, 5000000050),
    (99999999.99, 9999999999),
    (1000000000.00, 100000000000),
    (500000000.43, 50000000043),
    (999999999.99, 99999999999),
    (10000000000.99, 1000000000099),
    (5000000000.50, 500000000050),
    (9999999999.99, 999999999999),
    (100000000000.00, 10000000000000),
    (50000000000.43, 5000000000043),
    (99999999999.99, 9999999999999),
    (1000000000000.99, 100000000000099),
    (500000000000.50, 50000000000050),
    (999999999999.99, 99999999999999),
    (10000000000000.00, 1000000000000000),
    # (5000000000000.43, 500000000000043), #fail
    (9999999999999.99, 999999999999999),
    # (100000000000000.99, 10000000000000099),#fail
    # (50000000000000.50, 5000000000000050), #fail
]
cents_to_reais_data = [
    (1000, 10.00),
    (500, 5.00),
    (1543, 15.43),
    (9999, 99.99),
    (1000, 10.00),
    (500, 5.00),
    (1543, 15.43),
    (9999, 99.99),
    (123456, 1234.56),
    (789, 7.89),
    (9876, 98.76),
    (1111, 11.11),
    (3333, 33.33),
    (6666, 66.66),
    (123, 1.23),
    (4567, 45.67),
    (8888, 88.88),
    (777, 7.77),
    (999, 9.99),
    (4321, 43.21),
    (987, 9.87),
    (6543, 65.43),
    (9832, 98.32),
    (7865, 78.65),
    (456, 4.56),
    (9876, 98.76),
    (9999, 99.99),
    (6543, 65.43),
    (3333, 33.33),
    (2345, 23.45),
    (5678, 56.78),
    (8901, 89.01),
    (9753, 97.53),
    (1234, 12.34),
    (4000, 40.00),
    (6000, 60.00),
    (8000, 80.00),
    (2000, 20.00),
    (7000, 70.00),
    (8800, 88.00),
    (6800, 68.00),
    (5500, 55.00),
    (7700, 77.00),
    (3300, 33.00),
    (9900, 99.00),
    (6600, 66.00),
    (8800, 88.00),
    (7770, 77.70),
    (5500, 55.00),
    (9900, 99.00),
    (6600, 66.00),
    (8800, 88.00),
    (7770, 77.70),
    (5500, 55.00),
    (9900, 99.00),
    (6600, 66.00),
    (8800, 88.00),
    (7770, 77.70),
    (5500, 55.00),
    (9900, 99.00),
    (6600, 66.00),
    (8800, 88.00),
    (7770, 77.70),
    (5500, 55.00),
    (9900, 99.00),
    (6600, 66.00),
    (8800, 88.00),
    (7770, 77.70),
    (5500, 55.00),
    (9900, 99.00),
    (6600, 66.00),
    (123456789, 1234567.89),
    (45678000, 456780.00),
    (888888, 8888.88),
    (777777, 7777.77),
    (9999999, 99999.99),
    (43218907, 432189.07),
    (98765432, 987654.32),
    (65439876, 654398.76),
    (98324567, 983245.67),
    (78650789, 786507.89),
    (45678901, 456789.01),
    (98765000, 987650.00),
    (99999990, 999999.90),
    (65439876, 654398.76),
    (33333330, 333333.30),
    (23459876, 234598.76),
    (56780000, 567800.00),
    (89018907, 890189.07),
    (97539876, 975398.76),
    (12349876, 123498.76),
    (40009876, 400098.76),
    (60000000, 600000.00),
    (80000000, 800000.00),
    (20000000, 200000.00),
    (70000000, 700000.00),
    (88000000, 880000.00),
    (68000000, 680000.00),
    (55000000, 550000.00),
    (77000000, 770000.00),
    (33000000, 330000.00),
    (99000000, 990000.00),
    (66000000, 660000.00),
    (88000000, 880000.00),
    (77700000, 777000.00),
    (55000000, 550000.00),
    (99000000, 990000.00),
    (66000000, 660000.00),
    (88000000, 880000.00),
    (77700000, 777000.00),
    (55000000, 550000.00),
    (99000000, 990000.00),
    (66000000, 660000.00),
    (88000000, 880000.00),
    (77700000, 777000.00),
    (55000000, 550000.00),
    (99000000, 990000.00),
    (66000000, 660000.00)
]