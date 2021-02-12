#!/usr/bin/env python
# coding: utf-8

# #Question 1 C#
# 
# 5 is a Value, predefined datatype (int)
# 5.0 is a Value, predefined datatype (float)
# 5 > 1 is a Value, predefined datatype (int)
# '5' is a Reference, object datatype
# 5 * 2 is a Value, predefined datatype (int)
# '5' * 2 is a Value, predefined datatype (char)
# '5' + '2' is a value predefined datatype (char)
# 5/2 is a Value predefined datatype (decimal)
# 5//2 is a Reference datatype (object)
# [5, 2, 1] is a Value, User-defined datatype (Structure)
# 5 in [1, 4, 6] is a Value, User-defined datatype (structure)
# Pi (the number) is a Value, predefined datatype (double)
# 
# 

# #Question 2 C#
# 
# a. 
# 
# using System;
# 
# namespace ConsoleApplication15 
# {     class Program
#     {         static void Main(string[] args)         
#               {           
#               string str1 = "";
#               int x = 0, c = 0;
#             
# 
#             Console.WriteLine("Insert text");
#             str1= Console.ReadLine();
# 
#             for (int i = 0; i < str1.Length; i++)             
#             {
#                 char a = str1[i];
#                 c = c + 1;
#              
#             }
#             Console.WriteLine("The text has {0} letters",c);
# 
#              }      
#         
#         
#     }
# 
# }
# 
# b. 
# using System;
# 
# public class String
# {
# 
#     public static void Main(string[] args)
# 
#     {
# 
#         string s1 = "Supercalifragilisticexpialidocious' contain";
#         string s2 = "ice";
# 
#         Console.WriteLine(s1.Contains(s2));
# 
#     }
# }
# 
# c.
#      
# 

# In[ ]:


#Question 3 C#

# Stackoverflow link: https://stackoverflow.com/questions/47255485/c-sharp-heron-triangles

using System;

namespace triangleArea
{
    class Program
    {
        static void Main(string[]args)
        {
           double sarea;
           double sidea;
           double sideb;
           double sidec;


            Console.WriteLine("enter side a of triangle");
            sidea = Convert.ToDouble(Console.ReadLine());
            Console.WriteLine("enter side b of triangle");
            sideb = Convert.ToDouble(Console.ReadLine());
            Console.WriteLine("enter side c of triangle");
            sidec = Convert.ToDouble(Console.ReadLine());


            sarea = (sidea + sideb + sidec) / 2;
            sarea = Math.Sqrt(sarea * (sarea - sidea) * (sarea - sideb) * (sarea - sidec));

            Console.WriteLine("Area = {0}", sarea);




        }
    }
}


# In[ ]:


#Question 4 C#

using System;

namespace Odd_and_Even
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] array1 = new int[5];
            array1[0] = 25;
            array1[1] = 47;
            array1[2] = 42;
            array1[3] = 56;
            array1[4] = 32;


            int[] array2 = new int[5];
            array2[0] = 25;
            array2[1] = 47;
            array2[2] = 42;
            array2[3] = 56;
            array2[4] = 32;

            int i, j = 0, b = 0;
            for (i = 0; i < 5; i++) {

                if (array1[i] % 2 == 0) { }
                array2[j] = array1[i];
                j++;
            }
            else
            {
                array2[b] = array1[i];
                b++;

            }



            
        }

    }
}


# In[ ]:


#Question 6 Python

Append = "ay"
pig = "Alien"

if len pig < 0: 
    print ("empty")
else: 
    print ("lien" + first + lst.append ("ay"))


# In[12]:


#Question 7 Python 

bld = ["AB", "AB", "B", "O", "A", "A", "AB", "O", "AB", "A", "O", "O", "A", "A", "A", "O", "O", "O", "AB", "O", "A", "A", "A", "A", "A", "AB", "AB", "A", "AB", "O", "AB", "O", "A", "O", "O", "O", "AB", "O", "AB", "AB", "AB", "A", "A", "O"]

count = bld.count ("A")
print ("The are", count, "patients of blood A")

count = bld.count ("B")
print ("There is",count,"patients of blood type B")

count = bld.count ("AB")
print ("There are",count,"patients of blood type AB")

count = bld.count ("O")
print ("There are",count,"patients of blood type O")

count = bld.count ("OO")
print ("There are",count,"patients of blood type OO")


# In[34]:


#Question 8
#AUD Australian Dollar
#CHF Swiss Franc
#CNY Chinese Yuan
#DKK Danish Krone
#EUR Euro
#GBP British Pound
#HKD Hong Kong Dollar
#INR Indian Rupee
#JPY Japanese Yen
#MXN Mexican Peso
#MYR Malaysian Ringgit
#NOK Norwegian Krone
#NZD New Zealand Dollar
#PHP Philippine Peso
#SEK Swedish Krona
#SGD Singapore Dollar
#THB Thai Baht

def curvcon(Currency, Dollar_Amount):

    CurDictionary = {
     "AUD" : 1.0345157,    
     "CHF" : 1.0237414,    
     "CNY" : 0.1550176,    
     "DKK" : 0.1651442,   
     "EUR" : 1.2296544,   
     "GBP" : 1.5550989,
     "HKD" : 0.1270207, 
     "INR" : 0.0177643,
     "JPY" : 0.01241400,
     "MXN" : 0.0751848,
     "MYR" : 0.314541,
     "NOK" : 0.1677063,
     "NZD" : 0.8003591,
     "PHP" : 0.0233234,
     "SEK" : 0.148269,
     "SGD" : 0.788871,
     "THB" : 0.0313789
    }
    
   

    if Currency in CurDictionary.keys():
        value = CurDictionary[Currency]
        amount = value * 100
        print (amount)

curvcon ('EUR', 100)
curvcon ('JPY', 100)


# In[ ]:


#Question 9 Pyhton

Trying to add incompatible variables, as in adding 6 + ‘a’= ValueError

Referring to the 12th item of a list that has only 10 items = IndexError

Using a value that is out of range for a function’s input, such as calling math.sqrt(-1.0) = IndexError

Using an undeclared variable, such as print(x) when x has not been defined = NameError

Trying to open a file that does not exist, such as mistyping the file name or looking in the wrong directory = KeyboardInterrupt


# In[ ]:


#Question 10 Python

frequencies ("Pig Latin is confusing")
letters = ["abcdefghijklmnopqrstuvwxyz"]

encode (frequencies, letters)

print encode

