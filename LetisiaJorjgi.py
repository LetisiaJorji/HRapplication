#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 4 18:15:17 2023
Προηγήθηκε όλων η εγκατaταση του mysql-connector-python
Εντολές python -m pip install mysql-connector-python

"""

class Employee:

    def __init__(self,code,name,email,tel,address,salary):
        self.code = code
        self.name = name
        self.email = email
        self.tel = tel
        self.address = address
        self.salary = salary
       
        
    def __repr__(self):
        return "\t|"+self.code+" | "+self.name+" | "+self.email+" | "+self.tel+" | "+self.address+" | "+self.salary+" | "

# =============================================================================
# #Σύνδεση με την Βάση Δεδομένων
# =============================================================================
    
def mySQLConnect():
    '''
    Returns mySql connection
    -------
    Πηγή : https://pynative.com/python-mysql-database-connection/
    '''
    import mysql.connector
    from mysql.connector import Error
    try:
        connection = mysql.connector.connect(host='localhost',database='HR',user='root',password='Pass123!@#')
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)
            return connection
    except Error as e:
        print("Error while connecting to MySQL", e)
       
# =============================================================================
# Προσθηκη Υπαλλήλου
# =============================================================================
        
def addEmployee(con):
    print("\n\t------------ Εισαγωγη νέου Υπαλλήλου -----------------")
    name =      input("\tΔώστε το όνομα του υπαλλήλου ------> ")
    email =     input("\tΔώστε το email του υπαλλήλου ------> ")
    tel =       input("\tΔώστε το τηλέφωνο του υπαλλήλου ---> ")
    address =   input("\tΔώστε την Διεύθυνση του υπαλλήλου -> ")
    salary = 0.0
    while(True):
        try:
            salary = float(input("\tΔώστε τον μισθό του υπαλλήλου -----> "))
            break
        except:
            print("Ο Μισθός είναι αριθμός με δύο δεκαδικά ψηφία. Δοκιμάστε πάλι") 
    sql = "INSERT INTO Employee (name,email,tel,address,salary) VALUES ('"+name+"','"+email+"','"+tel+"','"+address+"','"+str(salary)+"');"
    mycursor = con.cursor()
    mycursor.execute(sql)
    con.commit()
    mycursor.close()
    print("\n\t--------- H Εισαγωγη νέου Υπαλλήλου ήταν επιτυχής ------------")

# =============================================================================
# Διαγαρφη υπαλληλου
# =============================================================================

def delEmployee(mydb):
    print("\n\t------------ Διαγραφή Υπαλλήλου -----------------")
    name =      input("\tΔώστε το όνομα του υπαλλήλου ------> ")
    if findEmployee(mydb, name) == 1:
        if isOk("\tΕπιλέξατε την διαγραφή του παραπάνω υπαλλήλου")==1:
            mycursor = mydb.cursor()
            sql = "DELETE FROM Employee WHERE name = '"+name+"';"
            mycursor.execute(sql)
            mydb.commit()
            print("\n\t--------- H Διαγραφή του Υπαλλήλου "+name+" ήταν επιτυχής ------------")
        else:
            return
    else:
        print("\tΑδύνατη η διαγραφή",name)
# =============================================================================
# Προαγωγή υπαλληλου
# =============================================================================

def proEmployee(mydb):
    print("\n\t------------ Προαγωγή Υπαλλήλου -----------------")
    name =      input("\tΔώστε το όνομα του υπαλλήλου ------> ")
    if findEmployee(mydb, name) == 1:
        if isOk("\tΕπιλέξατε την προαγωγή του παραπάνω υπαλλήλου")==1:
             try:
                 salary = float(input("Δώστε τον νέο Μισθό --> "))
                 mycursor = mydb.cursor()
                 sql = "UPDATE Employee SET salary ='"+str(salary)+"' WHERE name = '"+name+"';"
                 mycursor.execute(sql)
                 mydb.commit()
                 print("\n\t--------- H Προαγωγή του Υπαλλήλου "+name+" ήταν επιτυχής ------------")
             except:
                 print("Δώστε έναν αριθμόπ με δύο δεκαδικά ψηφία")
                 return
            
        else:
            return
    else:
        print("\tΑδύνατη η προαγωγή",name)
        
# =============================================================================
# αλλαγή Στοιχείων υπαλληλου
# =============================================================================

def chaEmployee(mydb):
    print("\n\t------------ Αλλαγή Στοιχείων Υπαλλήλου -----------------")
    name =      input("\tΔώστε το όνομα του υπαλλήλου ------> ")
    if findEmployee(mydb, name) == 1:
        if isOk("\tΕπιλέξατε την αλλαγή στοιχείων του παραπάνω υπαλλήλου")==1:
            name =      input("\tΔώστε το όνομα του υπαλλήλου ------> ")
            email =     input("\tΔώστε το email του υπαλλήλου ------> ")
            tel =       input("\tΔώστε το τηλέφωνο του υπαλλήλου ---> ")
            address =   input("\tΔώστε την Διεύθυνση του υπαλλήλου -> ")
            salary = 0.0
            while(True):
                try:
                    salary = float(input("\tΔώστε τον μισθό του υπαλλήλου -----> "))
                    break
                except:
                    print("Ο Μισθός είναι αριθμός με δύο δεκαδικά ψηφία. Δοκιμάστε πάλι") 
                    return

            mycursor = mydb.cursor()
            sql = "UPDATE Employee SET name = '"+name+"', email = '"+email+"', tel = '"+tel+"', address = '"+address+"',salary ='"+str(salary)+"' WHERE name = '"+name+"';"
            mycursor.execute(sql)
            mydb.commit()
            print("\n\t--------- H αλλαγή στοιχείων του Υπαλλήλου "+name+" ήταν επιτυχής ------------")
              
        else:
            return
    else:
        print("\tΑδύνατη η αλλαγή στοιχείων ",name)
        
# =============================================================================
# Ευρεση Υπαλλήλου
# =============================================================================
        
def findEmployee(mydb,name):
    mycursor = mydb.cursor()
    sql = "SELECT * FROM Employee WHERE name = '"+name+"';"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    if len(myresult)>=1:
        for x in myresult:
            print("\t",x)
        return 1
    else:
        print("\tΔεν βρέθηκε",name)
        return 0
    
# =============================================================================
# Εμφάνιση όλων των υπαλληλων 
# =============================================================================

def displayAll(con):
    mycursor = con.cursor()
    mycursor.execute("SELECT * FROM Employee")
    myresult = mycursor.fetchall()
    print("\t+------+-------+-----------------+------------+------------------+---------+")
    print("\t| code | name  | email           | tel        | address          | salary  |")
    print("\t+------+-------+-----------------+------------+------------------+---------+")
   
    for x in myresult:
      print("\t|   ",x[0],"|",x[1],"|",x[2],"|",x[3],"|",x[4],"|",x[5],"|")
    print("\t+------+-------+-----------------+-----------+------------------+---------+")
    mycursor.close()

# =============================================================================
# Επιβεβαίωση Ναι Οχι
# =============================================================================
def isOk(message):
    print(message)
    ch = input("Είστε βέβαιοι (Yy/Nn) ")
    if ch.capitalize() == 'Y':
        return 1
    return 0

# =============================================================================
# Κυριως Πρόγραμμα    
# =============================================================================

if __name__=="__main__":
    con = mySQLConnect()
    while(True):
        print("            M E N U ")
        print("==============================")
        print("1. Προσθήκη Υπαλλήλου")
        print("2. Προβολή Στοιχείων Υπαλλήλου")
        print("3. Επεξεργασία Υπαλλήλου")
        print("4. Προαγωγή Υπαλλήλου")
        print("5. Διαγραφή Υπαλλήλου")
        print("6. Αναζήτηση Υπαλλήλου")
        print("0. Έξοδος")
        ch = int(input("Δώστε την επιλογή σας --> "))
        if ch ==1:
            addEmployee(con)
        elif ch ==2:
            displayAll(con)
        elif ch ==3:
            chaEmployee(con)
            
        elif ch ==4:
            proEmployee(con)
    
        elif ch ==5:
            delEmployee(con)
    
        elif ch ==6:
            print("\n\t------------ Αναζήτηση Υπαλλήλου -----------------")
            name =      input("\tΔώστε το όνομα του υπαλλήλου ------> ")
            findEmployee(con, name)
            
        elif ch ==0:
            if isOk("Επιλέξατε να βγείτε από το πρόγραμμα") ==1:
                con.close()
                print("MySQL connection is closed")
                break
    
    
   
 
