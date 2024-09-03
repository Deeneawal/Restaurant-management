#THE RIGHT OF THIS PROGRAM,EITHER TO ALTER OR MODIFY THE PROGRAM AS WELL AS THE DISTRIBUTION RIGHT, STILL REMAINS IN THE HANDS OF
#ZUHAIB AHMAD KHAN
#####################################################################################################################################


#                                        PROJECT ON RESTAURANT MANAGEMENT SYSTEM
#                                         *************************************
'''                                           _____________________________
                                             |          MADE BY:~          |
                                             |                             |
                                             |      ZUHAIB AHMAD KHAN      |
                                             |_____________________________|                         '''
print()
print('\t\t\t\t        Project on Restaurant Management System \n \t\t\t\t\t  ******************************** \n \t\t\t\t\t   _______________________________ \n \t\t\t\t\t  |           MADE BY:~           |\n \t\t\t\t\t  |                               |\n \t\t\t\t\t  |      ZUHAIB AHMAD KHAN\t  |\n \t\t\t\t\t  |_______________________________|')
print()
print()
print('\t\t\t\t\t     WELCOME TO FOODIES UNITES !!!')
print('\t\t\t\t\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print()
print('\t\t\t\"Its our pleasure to serve you, hope our service won\'t let you down....\"')
print()
print()
input("press any enter to continue................!")
######################################################################################################################################
#                            MODULES USED IN PYTHON                                                                           #
######################################################################################################################################
import pickle
import os
import math
import getpass
######################################################################################################################################
#                            FUNCTION TO GENERATE SERIAL NUMBER                                                                           #
######################################################################################################################################

def gen_serial():
  try:
    if os.path.exists("Serial.txt")==False:
        f=open("Serial.txt",'w')
        f.write('0')
        f.close()

        

    number=open("Serial.txt",'r')
    lis=number.readlines()
    le=len(lis)
    n=int(lis[le-1])
    n=n+1
    number.close()
    number=open("Serial.txt",'w')
    number.write(str(n))
    number.close()
    #this will return pin for each customer. 
    return(n)

  except Exception as e:
        print (f"I/O error {e}")
######################################################################################################################################
#                            FUNCTION TO GENERATE BILL NUMBER                                                                          #
######################################################################################################################################

def gen_billno():
  try:
    if os.path.exists("billno.txt")==False:
        f=open("billno.txt",'w')
        f.write('0')
        f.close()

    number=open("billno.txt",'r')
    lis=number.readlines()
    le=len(lis)
    n=int(lis[le-1])
    n=n+1
    number.close()
    number=open("billno.txt",'w')
    number.write(str(n))
    number.close()
    #this will return pin for each customer. 
    return(n)
  except Exception as e:
        print (f"error is {e}")
######################################################################################################################################
#                            CLASS USED IN PROJECT                                                                           #
######################################################################################################################################
        
class restaurant(object):
    def __init__(r):
        #r.name=''
        #r.phone=''
        r.sno=0
        r.item=''
        r.price=0
        
    def addItem(r):
         r.sno=gen_serial()
         r.item=input('\t\tInput the dish name :').upper()
         r.price=int(input('\t\tInput the price: '))
         
    def retsno(r):
        return r.sno
      
    def retprice(r):
        return r.price
      
    def retitem(r):
        return r.item
      
    def show_item(r):
         print( "\nSerial No. :", r.sno)
         print( "\nItem name: ", r.item)
         print( "\nPrice: ", r.price)
    def out(r):
        print("%-10s"%" ",'%-15s'%r.sno,'%-52s'%r.item,'%-10s'%r.price)

    def modify(r):          #function to get new data from user
        print( "\nSerial No. : ", r.sno)
        r.item=input("\n\nEnter the Item name: ").upper()
        r.price=int(input("\nEnter the price: "))
################################################################################################################################
#                            class order                                                                         #
################################################################################################################################

class order(object): 
   def _init_(o):
        o.billno=0
        o.sno=0
        o.item=''
        o.price=0
        o.qty=0
        o.amt=0
        o.grand_total=0
        
   def retamt(o):
      return o.amt

   def retbillno(o):
      return o.billno
    
   def bill_report(o):
        print("%-10s"%" ","%-10s"%o.billno,'%-15s'%o.sno,'%-52s'%o.item,'%-10s'%o.price,'%-10s'%o.qty,'%-10s'%o.amt)

######################################################################################################################################
#                            FUNCTION TO CALCULATE BILL AMOUNT                                                                           #
######################################################################################################################################    

def bill_generate():
        ac=order()
        outFile=open("bill.dat","rb")
        ac=pickle.load(outFile)
        g=g+ac.retamt()
        print(g)

def calculate():
  found=0
  ac=order()
  it=restaurant()
  ac.billno=gen_billno()
  while True:
      print()
      a=int(input('Enter the Item no. to order:'))
      try:
        #inFile=open("bill.dat","rb")
        infile=open('items.dat','rb')
        outFile=open("bill.dat","ab")
        while True:
          it=pickle.load(infile)
          if it.retsno()==a:
            m=int(input('Enter the quantity: '))
            ac.sno=a
            ac.item=it.item
            ac.qty=m
            ac.price=it.retprice() 
            ac.amt=ac.price*ac.qty
            pickle.dump(ac,outFile)
            found=1
            print( "\n\n\tItem Ordered")
                
      except EOFError:
          infile.close()
          outFile.close()
          if found==0:
            print( "\n\nItem Not Found")
          else:
            print( "\n\n\tItems Ordered")
            print( "\n\n\tYour Bill Number is : ",ac.retbillno())
      
      except IOError:
        print( "File could not be open !!")
      print()
      n=input('Want to Order more? [Y/N]: ')
      if n=='n' or n=='N':
        break
      
def saveitem():
    try:
        it=restaurant()
        outFile=open("items.dat","ab") 
        it.addItem()
        pickle.dump(it,outFile)
        outFile.close()
        print( "\n\n Item Created Successfully")
        
    except:
        pass

def display_all():
    print( "\n\n","%-46s"%" ","ITEM LIST")
    print("%-44s"%" ","**************\n\n")
    print( "%-8s"%" ",90*"=")
    print("%-10s"%" ","%-15s"%"Item No.","%-50s"%"Item Name","%-10s"%"Price")
    print( "%-8s"%" ",90*"=","\n")
    try:
        inFile=open("items.dat","rb")
        while True:
            it=pickle.load(inFile)
            it.out()
            
    except EOFError:
        inFile.close()
        
    except IOError:
        print( "File could not be open !! Press any Key...")

def display_bill(n):
    gt=0
    print( "\n\n","%-46s"%" ","CUSTOMER BILL")
    print("%-44s"%" ","  ***************\n\n")
    print( "%-8s"%" ",110*"=")
    print("%-10s"%" ","%-10s"%"Bill No.","%-15s"%"Item No.","%-50s"%"Item Name","%-10s"%"Price","%-10s"%"Quantity","%-10s"%"Amount")
    print( "%-8s"%" ",110*"=","\n")
    try:
        inFile=open("bill.dat","rb")
        while True:
            it=pickle.load(inFile)
            if it.retbillno()==n:
              it.bill_report()
              gt=gt+it.retamt()
            
    except EOFError:
        inFile.close()
        print( "%-8s"%" ",110*"=","\n")
        print( "\t\t\t\t\t\tGrand Total : ",gt)
    except IOError:
        print( "File could not be open !! Press any Key...")

def display_allbill():
    gt=0
    print( "\n\n","%-46s"%" ","CUSTOMER BILL")
    print("%-44s"%" ","******************\n\n")
    print( "%-8s"%" ",110*"=")
    print("%-10s"%" ","%-10s"%"Bill No.","%-15s"%"Item No.","%-50s"%"Item Name","%-10s"%"Price","%-10s"%"Quantity","%-10s"%"Amount")
    print( "%-8s"%" ",110*"=","\n")
    try:
        inFile=open("bill.dat","rb")
        while True:
            it=pickle.load(inFile)
            it.bill_report()
            gt=gt+it.retamt()
            
    except EOFError:
        inFile.close()
        print( "%-8s"%" ",110*"=","\n")
        print( "\t\t\t\t\t\tGrand Total : ",gt)
        
    except IOError:
        print( "File could not be open !! Press any Key...")

        
def modify_item(n):
    found=0
    try:
        inFile=open("items.dat","rb")
        outFile=open("temp.dat","wb")
        while True:
            it=pickle.load(inFile)
            if it.retsno()==n:
                print( 100*"-")
                it.show_item()
                print( 100*"-")
                print( "\n\nEnter The New Details of Serial no.: ",n)
                it.modify()
                pickle.dump(it,outFile)
                print( "\n\n\tRecord Updated")
                found=1
            else:
                pickle.dump(it,outFile)
             
    except EOFError:
        inFile.close()
        outFile.close()
        if found==0:
            print( "\n\nRecord Not Found ")

    except IOError:
        print( "File could not be open !! Press any Key...")

    os.remove("items.dat")
    os.rename("temp.dat","items.dat")

def delete_item(n):
    found=0

    try:
        inFile=open("items.dat","rb")
        outFile=open("temp.dat","wb")
        while True:
            it=pickle.load(inFile)
            if it.retsno()==n:
                found=1
                print( "\n\n\tRecord Deleted ..")
            else:
                pickle.dump(it,outFile)

    except EOFError:
        inFile.close()
        outFile.close()
        if found==0:
            print( "\n\nRecord Not Found")

    except IOError:
        print( "File could not be open !! Press any Key...")

    os.remove("items.dat")
    os.rename("temp.dat","items.dat")

def search_item(n):
    found=0

    try:
        inFile=open("items.dat","rb")
        outFile=open("temp.dat","wb")
        while True:
            it=pickle.load(inFile)
            if n in it.retitem():
                found=1
                print( 100*"-")
                print( "\n\n\tItem Found......!!")
                it.show_item()
                print( 100*"-")
                pickle.dump(it,outFile)
            else:
                pickle.dump(it,outFile)

    except EOFError:
        inFile.close()
        outFile.close()
        if found==0:
            print( "\n\nRecord Not Found")

    except IOError:
        print( "File could not be open !! Press any Key...")

    os.remove("items.dat")
    os.rename("temp.dat","items.dat")    


  

while True:
    ac=order()
    print()
    print('\t\t     MAIN MENU')
    print('\t\t   ************\n')
    print('\t\t1. Administration Menu')
    print('\t\t2. Display All Items')
    print('\t\t3. Search the Food')
    print('\t\t4. Order')
    print('\t\t5. Bill')
    print('\t\t6. Exit')
    print()
    f=input('Enter your choice: ')
    print()
    if f=='1':
        # Prompt the user for a password without displaying it
        password = getpass.getpass("Enter your password: ")
        if password=='123':
            while True:
                print('\n\n')
                print('\t\t    Administration Menu')
                print('\t\t     *****************  \n')
                print('\t\t1. Add items to Existing List')
                print('\t\t2. Modify the particular item ')
                print('\t\t3. Delete the Item from the List')
                print('\t\t4. Display Current List')
                print('\t\t5. Display all orders')
                print('\t\t6. Exit Administration Menu')
                print()
                m=input('Enter Your Choice: ')
                if m=='1':
                    saveitem()
                elif m=='2':
                    display_all()
                    print('\n\n\n\n')
                    num=int(input('Enter the Item no. to be modified: '))
                    modify_item(num)
                elif m=='3':
                    display_all()
                    print()
                    num=int(input('Enter the Item no. to be Deleted: '))
                    delete_item(num)
                elif m=='4':
                    display_all()
                    print()
                    input('Press Enter to continue.....................!!')
                    print('\n\n\n\n')
                elif m=='5':
                    display_allbill()
                    print()
                    input('Press Enter to continue.....................!!')
                    print('\n\n\n\n')
                elif m=='6':
                    break
                else:
                    print('INVALID CHOICE')
        else:
                print('Wrong Password!!!\n Retry')
    elif f=='2':
        display_all()
        print()
        input('Press Enter to continue.....................!!')
        print('\n\n\n\n')

    elif f=='3':
        item=input('Enter the Item Name: ')
        search_item(item.upper())

    elif f=='4':
        print('\n\t\t\t\tWelcome to Order Section\n\t\t\t\t  *****************')
        print('\t\tOur Food Services are unique and exciting, \n\t\tfilled with delicious & hygenic foods')
        display_all()
        print()
        calculate()
        print()
        print('Ordered successfully....!!!')
        print('\n\n\n\n')
    elif f=='5':
        num=int(input("enter bill number : "))
        display_bill(num)
        print()
        input('Press Enter to continue.....................!!')
        print('\n\n\n\n')
      
    elif f=='6':
        break
    else:
        print('Invalid Choice')
    print()
print()
print()
print('\t\t\t\t~Thanks for coming to Foodies Unites!!~')
print('\t\t\t\t    ~Your Pleasure Our Comfort!!!~')
print('\t\t\t\t            ~Visit Again~')
input('\nPress Enter to exit...............')

########################################################################################################################################
########################################################################################################################################



"""                                                       END
                                                          OF
                                                       PROGRAM                                                                      """  


########################################################################################################################################
########################################################################################################################################

'''THIS PROGRAM WAS INITIALLY DESIGNED AND TYPED BY ZUHAIB AHMAD KHAN
AND ABHINAV PRAMANIK. THIS PROJECT WAS ADVANCED WITH THE HELP OF OUR
COMPUTER TR. MANINDER SINGH WHO WAS OUR CLASS TEACHER AS WELL.'''
