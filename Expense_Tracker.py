# Welcome to Expense Tracker 💸
# ======= MENU =======
# 1️⃣Add Expense
# 2️⃣View All Expenses
# 3️⃣View Total Spending
# 4️⃣View Spending by Category
# 5. Exit
# =====================
print("====Welcome to the Expense Tracker====")
expenses=[]
while (True):
    print("=== MENU ===")
    print("1. Add expense")
    print("2. View all expenses")
    print("3. View total spending")
    print("4. View spending by category")
    print("5. Exit")
    choice = int(input("Enter the choice from menu (1-5)-> "))

# Add expenses
    if choice == 1:
        date = input("Enter the date (DD/MM/YYYY) : ")
        category = input("Enter the category(Food, Travel, Shopping, Movie, etc.) : ")
        desc = input("Enter the short description about your expense : ")
        amount = float(input("Enter the amount(₹) : "))
        expense = {
            "date" : date,
            "category" : category,
            "description" : desc,
            "amount" : amount
        }
        expenses.append(expense)
        print("Your expense are added successfully.")
        print("To check your expenses record press 2 ")

# View expenses  
    elif choice == 2:

        if len(expenses)==0:
            print("No expenses are added yet.")
        else :
            print("=== Your all expenses ===")
            i =1
            for j in (expenses):
                print(f"{i}. Date: {j['date']} || Category: {j['category']} || Description: {j['description']} || Amount(₹): {j['amount']} ")
                i+=1
            print("---------------------")


    # view total spendings
    elif choice == 3:
        total = 0
        for j in (expenses):
            total += j["amount"]
        print("Your total spending is ₹:",total)


# view spending by category
    elif choice == 4:
        if len(expenses) == 0:
            print("No expenses are recorded yet.")
        else : 
            summary= {}
            for c in expenses:
                cat = c["category"]
                if cat in summary:
                    summary[cat] += c["amount"]
                else:
                    summary[cat] = c["amount"]

            print("=== Your spending by category ===")
            for cat, amt in summary.items():
                print(f"Category : {cat} -> Amount : {amt}")

    # Exit
    elif choice == 5:
        print("\n Thanks for using Expense Tracker!")
        break
    else:
        print("\n❌ 404 Invalid choice. Please try again.")
        print("Please enter the number accoding to Menu (1-5)")


