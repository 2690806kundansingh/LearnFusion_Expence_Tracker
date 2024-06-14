from exe import Expense
import calendar
import datetime


def main():
    print("hellow hai")
    expense_file_path="expense.csv2"
    budget= 1000000


    expense=expense_kitna_hua()
    file_m_save_kro(expense,expense_file_path)


    summarise_expense(expense_file_path,budget)

def expense_kitna_hua():
   print("kitna kharcha kiya hai")
   expense_name=input("kahha khacha kiye :")
   expense_amount=float(input("kitne paise yaha pe kharch kiye hai :"))
   print(f"expense name is {expense_name},{expense_amount}")


   expense_categories=[
      "Food",
      "Home",
      "Work",
      "Fun",
      "Misc",
   ]

   while True:
      print("kis category me kharcha kar rahe ho :")
      for i ,category_name in enumerate(expense_categories):
          print(f"{i+1}.{category_name}")

      value_range=f"[1-{len(expense_categories)}]"
      select_index=int(input(f"bhai category bata do ::{value_range}"))-1
      
      if select_index in range(len(expense_categories)):
         select_category=expense_categories[select_index]
         print(select_category)

         
         new_expense=Expense(name=expense_name,category=select_category,amount=expense_amount)
         return new_expense
         

      else:
         print("Invalid category")   
      break   




def file_m_save_kro(expense :Expense,expense_file_path):
   
   print(f"kharcha file me save karna hai : {expense} to {expense_file_path}")
   with open(expense_file_path,"a") as f:
      f.write(f"{expense.name},{expense.amount},{expense.category}\n")
      



def summarise_expense(expense_file_path,budget):
   print("summary of user expenses :")
   expenses=[]
   with open(expense_file_path,'r') as f:
      lines=f.readlines()
      for line in lines:
        #  print(line)
        expense_name,expense_amount,expense_category=line.strip().split(",")
        print(f"{expense_name} {expense_amount} {expense_category}")
        line_expense=Expense(name=expense_name,amount=float(expense_amount),
        category=expense_category)
        #print(line_expense)
        expenses.append(line_expense)
        #print(expense)

   amount_by_category= {}
   for expense in expenses:
      key=expense.category

      if key in amount_by_category:
         amount_by_category[key] +=expense.amount
      else:
         amount_by_category[key]=expense.amount   

   # print(amount_by_category)

   print("ye apka category wise kharcha hai")
   for key ,amount in amount_by_category.items():
      print(f"{key}:{amount}")


      #using list comprehension
      total_Spend=sum([k.amount for k in expenses])
      print(f"itna kharcha kar liye bhai :{total_Spend:.2f}")


      remining_budget=budget - (total_Spend)
      print(f"reamining budget : {remining_budget:.2f}")


      #adding date and time and month
      now=datetime.datetime.now()
      days_in_month=calendar.monthrange(now.year,now.month)[1]
      #remaining days
      remaining_days=days_in_month - now.day
      print("remaining days iss month me bache hai :",remaining_days)



      daily_budget =  remining_budget/remaining_days
      print("daily budget :",daily_budget)

      
if __name__=="__main__":
    main()