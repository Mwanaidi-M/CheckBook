
package javaappcheckbook.java;
import java.util.*;
import java.io.*;

public class JavaAppCHECKBOOKJAVA {
    static double bal;
    static Scanner mf = new Scanner(System.in);   
    public static void accReg() //THIS METHOD IS USED TO REGISTER AN ACCOUNT.
    {
        try
        {
            String fName;
            System.out.println("Enter your account name:");
            fName = mf.next();            
            File uFile = new File(fName+".txt");            
            if((uFile.createNewFile()))
            {                
                System.out.println("Your account is empty.\nEnter the amount you wish to put in now: ");
                bal = mf.nextDouble(); 
                FileWriter fw1 = new FileWriter(uFile.getName(),true);
                BufferedWriter bf1 = new BufferedWriter(fw1);
                bf1.write("Account Holder:"+fName+ ":\n");
                bf1.newLine();
                bf1.append("\nBalance:" +bal+ " \n");
                bf1.newLine();
                bf1.close();
                fw1.close();
                System.out.println("Account Registration Successful.\n");
            }
            else
                System.out.println("Your account already exists. \n");
        }
        catch(IOException er)
        {
            System.err.println(er);
        } 
        catch(InputMismatchException er)
        {
            System.err.println("You haven't input the right format of numbers: "+er);
        }
    }
    public static void accWith() //METHOD USED TO MAKE A WITHDRAWAL
    {
        try
        {
            String fName1;
            System.out.println("Enter your account name:");
            fName1 = mf.next();

            File uFile = new File(fName1+".txt");
            if(uFile.exists())
            {
                FileWriter fw1 = new FileWriter(uFile.getName(),true);
                if(bal == 0.0)
                {
                System.out.println("Your account is empty.\n");                 
                }
                else
                {
                System.out.println("Enter the amount you wish to withdraw(between Kshs.100 and Kshs.20,000)");
                double fAppend = mf.nextDouble();
                if(bal>=fAppend && fAppend>=100 && fAppend<=20000)
                {
                bal = bal - fAppend;
                BufferedWriter bf1 = new BufferedWriter(fw1);
                bf1.write("Balance: \n" +bal);
                bf1.newLine();
                bf1.close();
                fw1.close();
                System.out.println("WITHDRAWAL SUCCESSFUL! \n");
                }
                else if(fAppend>bal)
                {
                    System.out.println("You dont enough money in your account to make a withdrawal! \n");
                }
                else
                {
                    System.out.println("Please input an amount within the limits given\n");
                }
                }
            }
             else
            {
               System.out.println("Your account does not exist.\n");
               System.out.println("Please create an account to use this service.\n"); 
            }                    
        }
        catch(IOException ei)
        {
            System.err.println(ei);
        }
        catch(InputMismatchException er)
        {
            System.err.println("You havent input the right format of numbers: "+er);
        }
    }
    public static void accDep() //METHOD USED YO MAKE A DEPOSIT.
    {
        try
        {
            String fName1;
                System.out.println("Enter your account name:");
                fName1 = mf.next();

                File uFile = new File(fName1+".txt");
            if(uFile.exists())
            {
                FileWriter fw1 = new FileWriter(uFile.getName(),true);
                System.out.println("Enter the amount you wish to Deposit");
                double fAppend = mf.nextDouble();
                bal = bal + fAppend;
                BufferedWriter bf1 = new BufferedWriter(fw1);
                bf1.write("Balance: \n" +bal);
                bf1.newLine();
                bf1.close();
                fw1.close();
                System.out.println("DEPOSIT SUCCESSFUL! \n");
            }
            else
            {
               System.out.println("Your account does not exist.\n");
               System.out.println("Please create an account to use this service.\n");
            }
                
        }

        catch(IOException ei)
        {
            System.err.println(ei);
        }
        catch(InputMismatchException er)
        {
            System.err.println("You havent input the right format of numbers: "+er);
        }
    }
    public static void accStmt() //THIS METHOD DISPLYAYS THE ACCOUNT STATEMENT.
    {
         try
        {
            String fName1;
            System.out.println("Enter your account name:");
            fName1 = mf.next();
            File mFile = new File(fName1+".txt");
            if(mFile.exists())
            {
             FileReader fr1 = new FileReader(mFile);
             BufferedReader buffr = new BufferedReader (fr1);
             int cn = 0;
                while((cn = fr1.read())!=-1)
                {
                    System.out.print((char)cn);
                }          
            fr1.close();
            buffr.close();
            }
            else
            {
               System.out.println("Your account does not exist.");
               System.out.println("Please create an account to use this service.\n");
            }
        }

        catch(FileNotFoundException fe)
        {
            System.err.println(fe);
        }
        catch(IOException er)
        {
            System.err.println(er);
            
        }
    }
    
    public static void main(String[] args) {
        // TODO code application logic here
        for(;;)
        {
            //MENU FOR THE CHECKBOOK SYSTEM
            System.out.println("WELCOME TO THE JAVA CHECKBOOK.");
            System.out.println("---------------------------------------------------------- \n");
            System.out.println("1. CREATE AN ACCOUNT.");
            System.out.println("2. WITHDRAW FROM ACCOUNT.");
            System.out.println("3. DEPOSIT TO ACCOUNT.");
            System.out.println("4. VIEW BALANCE.");
            System.out.println("5. EXIT \n");
            System.out.println("ENTER THE NUMBER OF THE TASK YOU WISH TO PERFORM:");
        
            int userInput;
            
            userInput = mf.nextInt();
            
            if(userInput == 1)
            {
                JavaAppCHECKBOOKJAVA.accReg();
            }
            else if(userInput == 2)
            {
                JavaAppCHECKBOOKJAVA.accWith();
            }
            else if(userInput == 3)
            {
                JavaAppCHECKBOOKJAVA.accDep();
            }
            else if(userInput == 4)
            {
                JavaAppCHECKBOOKJAVA.accStmt();
       
            }
            else if(userInput == 5)
            {
                System.out.println("PROGRAM CLOSED SUCCESSFULLY.\n");
                break;
                
            }
            else 
            {
                System.out.println("PLEASE INPUT A NUMBER THAT IS ON THE LIST ABOVE.\n");
            }
        }          
    }
                    
                
        
}
    

