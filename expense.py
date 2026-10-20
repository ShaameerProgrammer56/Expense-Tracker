#EXPENSE TRACKER

print("Welcome to our expense tracker program ! ")
print("How may we assit u today?")
expenses = {
    "Food" : 500,
    "Car" : 1000 ,
    "House" : 15000 ,
    "Groceries" : 1200, 
    "Bills" : 400

}


while True : 
   user = input("Please Enter What u want to begin with , 1.Add Expense 2. View Expense 3. Remove Expense 4.Add a new Expense Category")

   if user == "1" : 
     print("Great! Please Enter the amount and the category your going to add your expense in!")
     category = input("Please Enter a Category!")
     amount = int(input("Please Enter a Amount!"))
     if category in expenses :
        expenses[category] += amount
        print(f"Successfully added {amount} into {category}, Total expense now {expenses[category]}")
     else : 
       print("Please Enter a valid category")

     cont = input("Would You Like to Continue? (y/n)")
     if cont == "y" :
       continue 
     else :
       break
   elif  user == "2" : 
     print(f"Here Are all of your Expenses that you recorded! {expenses}")
     conti_nue = input("Would You Like to Continue? (y/n)")
     if conti_nue == "y" :
       continue 
     else :
       break 
   elif user == "3" : 
     exp_remove = input("Please Enter The category from which you want to remove your Expense from")
     amount_remove = int(input("Please Enter the amount u want to remove"))
     if exp_remove in expenses :
       expenses[exp_remove] -= amount_remove 
       print(f"Successfully Removed {amount_remove} from {exp_remove}, Remaining : {expenses}")
     else :
       print("Enter a valid category!")
     choice = input("Would You like to continue? (y/n)")
     if choice == "y" :
       continue 
     else : 
       break
   elif user == "4" : 
     name = input("Please enter the name of the category : ")
     new_am = int(input("Please enter the amount You would like to enter in the category"))
     if name in expenses :
        print("There is already a category !")
     else :
        expenses[name] = new_am 
        print(f"Updated Your expenses Updated version : {expenses}")
     choice2 = input("Would You like to continue? (y/n)")
     if choice2 == "y" :
            continue 
     else : 
            break