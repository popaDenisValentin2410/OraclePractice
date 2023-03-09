import cx_Oracle

def selecteazaelevi():
    dsn_tns = cx_Oracle.makedsn('localhost', '1521') # if needed, place an 'r' before any parameter in order to address special characters such as '\'.
    conn = cx_Oracle.connect(user=r'SYSTEM', password='acasa', dsn=dsn_tns) # if needed, place an 'r' before any parameter in order to address special characters such as '\'. For example, if your user name contains '\', you'll need to place 'r' before the user name: user=r'User Name'
    c = conn.cursor()
    c.execute('Select * from Elevi') # use triple quotes if you want to spread your query across multiple lines
    rows=c.fetchall()
    #conn.close()
    conn.commit()
    conn.close()
    if rows:
        return True

print(selecteazaelevi())


def createProf():
    dsn_tns = cx_Oracle.makedsn(r'localhost',r'1521')  # if needed, place an 'r' before any parameter in order to address special characters such as '\'.
    conn = cx_Oracle.connect(user=r'SYSTEM', password=r'acasa', dsn=dsn_tns)  #
    cur=conn.cursor()
    cur.execute("CREATE TABLE PROF( CNP NUMBER,  NUME VARCHAR2(50) NOT NULL,  Prenume VARCHAR2(50) NOT NULL,  SEX VARCHAR2(50) NOT NULL ,ADRESA VARCHAR2(50) NOT NULL, PRIMARY KEY(CNP))")
    conn.commit()
    conn.close()

#createProf()

def createSTAT():
    dsn_tns = cx_Oracle.makedsn(r'localhost',r'1521')  # if needed, place an 'r' before any parameter in order to address special characters such as '\'.
    conn = cx_Oracle.connect(user=r'SYSTEM', password=r'acasa', dsn=dsn_tns)  #
    cur=conn.cursor()
    cur.execute("CREATE TABLE Stat_functiuni( IDSTAT NUMBER,  CNP NUMBER , CodMaterie NUMBER,  NRORE NUMBER,  PRIMARY KEY(IDSTAT),foreign key (CNP) references PROF(CNP),foreign key (CodMaterie) references Materie2(CodMaterie))")
    conn.commit()
    conn.close()

#createSTAT()

def ProfesoriPerMaterie(CodMaterie):
    dsn_tns = cx_Oracle.makedsn(r'localhost',r'1521')  # if needed, place an 'r' before any parameter in order to address special characters such as '\'.
    conn = cx_Oracle.connect(user=r'SYSTEM', password=r'acasa', dsn=dsn_tns)  #
    cur=conn.cursor()
    cur.execute(f"select count(*) from (SELECT DISTINCT CNP from Stat_functiuni where (CodMaterie={CodMaterie}))")
    row = cur.fetchall()
    #print(row)
    conn.commit()
    conn.close()
    return(row)

#ProfesoriPerMaterie(2)

def calculsalariu(CNP):
    dsn_tns = cx_Oracle.makedsn(r'localhost',r'1521')  # if needed, place an 'r' before any parameter in order to address special characters such as '\'.
    conn = cx_Oracle.connect(user=r'SYSTEM', password=r'acasa', dsn=dsn_tns)  #
    cur=conn.cursor()
    cur.execute(f"select 10 * sum(NRORE) from Stat_functiuni where ( CNP={CNP})")
    row=cur.fetchall()
    #print(row)
    conn.commit()
    conn.close()
    return row

def calculsalariutoti():
    dsn_tns = cx_Oracle.makedsn(r'localhost',r'1521')  # if needed, place an 'r' before any parameter in order to address special characters such as '\'.
    conn = cx_Oracle.connect(user=r'SYSTEM', password=r'acasa', dsn=dsn_tns)  #
    cur=conn.cursor()
    cur.execute("select CNP, 10 * sum(NRORE) from Stat_functiuni Group by CNP ")
    row=cur.fetchall()
    #print(row)
    conn.commit()
    conn.close()
    return row


def modificare2(var1,var2):
    dsn_tns = cx_Oracle.makedsn(r'localhost',r'1521')  # if needed, place an 'r' before any parameter in order to address special characters such as '\'.
    conn = cx_Oracle.connect(user=r'SYSTEM', password=r'acasa', dsn=dsn_tns)  #
    cur=conn.cursor()
    cur.execute(f"Update stat_functiuni set codmaterie = {var1} where cnp = {var2} ")
    row=cur.fetchall()
    #print(row)
    conn.commit()
    conn.close()
    return row
#calculsalariu(1)
calculsalariutoti()

def createMaterie():
    dsn_tns = cx_Oracle.makedsn(r'localhost',r'1521')  # if needed, place an 'r' before any parameter in order to address special characters such as '\'.
    conn = cx_Oracle.connect(user=r'SYSTEM', password=r'acasa', dsn=dsn_tns)  #
    cur=conn.cursor()
    cur.execute("CREATE TABLE Materie2(  CodMaterie NUMBER, NUMEMATERIE VARCHAR2(50) NOT NULL,  PRIMARY KEY(CodMaterie))")
    conn.commit()
    conn.close()
#createMaterie()

def AdaugareMaterie(NumeMaterie):
    dsn_tns = cx_Oracle.makedsn(r'localhost',r'1521')  # if needed, place an 'r' before any parameter in order to address special characters such as '\'.
    conn = cx_Oracle.connect(user=r'SYSTEM', password=r'acasa', dsn=dsn_tns)  #
    cur=conn.cursor()
    cur.execute(f" insert into Materie2 values (( select max(CodMaterie) from Materie2) + 1 ,'{NumeMaterie}')")
    conn.commit()
    conn.close()


# AdaugareMaterie("Baze De Date")
# AdaugareMaterie("Java")
# AdaugareMaterie("MAA")

def AdaugareStat(CNP,CodMaterie,NRORE):
    dsn_tns = cx_Oracle.makedsn(r'localhost',r'1521')  # if needed, place an 'r' before any parameter in order to address special characters such as '\'.
    conn = cx_Oracle.connect(user=r'SYSTEM', password=r'acasa', dsn=dsn_tns)  #
    cur=conn.cursor()
    cur.execute(f" insert into Stat_functiuni values (( select max(IDSTAT) from Stat_functiuni) + 1 ,{CNP},'{CodMaterie}','{NRORE}')")
    conn.commit()
    conn.close()

#AdaugareStat(5,37,25)

def AdaugareProfesor(CNP,NUME,PRENUME, SEX,ADRESA):
    dsn_tns = cx_Oracle.makedsn(r'localhost',r'1521')  # if needed, place an 'r' before any parameter in order to address special characters such as '\'.
    conn = cx_Oracle.connect(user=r'SYSTEM', password=r'acasa', dsn=dsn_tns)  #
    cur=conn.cursor()
    cur.execute(f" insert into PROF values ( {CNP},'{NUME}','{PRENUME}', '{SEX}', '{ADRESA}')")
    conn.commit()
    conn.close()

# AdaugareProfesor(12345,'Blanco','Vincente', 'M','Tenerife')
# AdaugareProfesor(1,'Candelaria','Maria', 'F','Tenerife')
# AdaugareProfesor(2,'Mara','Maria', 'F','Tenerife')
# AdaugareProfesor(3,'Henry','Ryan', 'M','Tenerife')
#AdaugareProfesor(5,'Popa','Aurelia', 'F','Tenerife')

def AfisareElev(Clasa):
    dsn_tns = cx_Oracle.makedsn(r'localhost',r'1521')  # if needed, place an 'r' before any parameter in order to address special characters such as '\'.
    conn = cx_Oracle.connect(user=r'SYSTEM', password=r'acasa', dsn=dsn_tns)  #
    cur=conn.cursor()
    cur.execute(f"Select * from Elevi where (clasa = '{Clasa}')")
    rows = cur.fetchall()
    print(rows)
    conn.commit()
    conn.close()
    return rows

#AfisareElev('7A')


def AdaugareElev(CNP,NUME,PRENUME, Clasa):
    dsn_tns = cx_Oracle.makedsn(r'localhost',r'1521')  # if needed, place an 'r' before any parameter in order to address special characters such as '\'.
    conn = cx_Oracle.connect(user=r'SYSTEM', password=r'acasa', dsn=dsn_tns)  #
    cur=conn.cursor()
    cur.execute(f" insert into ELEVI values ( {CNP},'{NUME}','{PRENUME}', '{Clasa}')")
    conn.commit()
    conn.close()

#AdaugareElev(1,'NUME','PRENUME', 'Clasa')
#AdaugareElev(1,'NUME','PRENUME', 'Clasa')
# AdaugareElev(2,'NUME','PRENUME', '7A')
#AdaugareElev(4,'Popa','PRENUME', 'A7')
# AdaugareElev(532312,'Popa','Denis', '7A')
# AdaugareElev(532432,'Popa','Mihnea', '7A')
# AdaugareElev(53452312,'Mihaila','Mihai', '7A')
# AdaugareElev(5342312,'Balaci','Alexandru', '7A')
#AdaugareElev(5342312234,'Balaci','Mario', '12B')






















