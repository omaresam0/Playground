import os
import calendar
import sys

import expense
import csv
from datetime import datetime
from text_styling import Colors

# List of categories
categories = [
        "🍔 Food",
        "🏠 Home",
        "💼 Work",
        "🎉 Fun",
        "✨ Misc",
 ]
def main():
    budget = get_budget()
    path = 'expenses.csv'
    welcome_message_displayed = False
    # Displaying welcome Message only once when the app starts
    while True:
        if not welcome_message_displayed:
            welcome_message()
            welcome_message_displayed = True
        print_menu()
        try:
            choice = int(input("Enter your choice\t"))
            match choice:
                case 1:
                    expense_result = add_item()
                    save_item(expense_result, path)
                case 2:
                    view_expenses(path, budget)
                case 3:
                    modify_expense(path)
                case 4:
                    remove_expense(path)
                case 5:
                    clear_expenses(path)
                case 6:
                    print(Colors.colored_text("Goodbye!", "cyan"))
                    break
                case other_choice: # Input is a number but out of range (1-4)
                    print("Invalid input. Please enter a valid number.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")
        #print(expense_result) # Expense inserted <obj>

        quit_input = input("Press 'q' to quit, or any other key to return to the menu:")
        if quit_input.lower() == 'q':
            print(Colors.colored_text("Exiting, Goodbye!", "cyan"))
            break


# Welcoming the user
def welcome_message():
    print(Colors.colored_text("Welcome to the Expense Tracker App!", "cyan"))
    budget = modify_budget()

def print_menu():
    print(Colors.colored_text("\nChoose from the following prompts", "cyan"))
    print(Colors.colored_text(
    """    1 - Add Expense 
    2 - View All Expenses 
    3 - Modify Expenses
    4 - Remove Expense
    5 - Clear Expenses
    6 - Quit"""
    ,"cyan"))


# User entering the expenses
def add_item():

    while True:
        expense_name = input("Enter expense name: ")
        # If not empty or consists of only digits
        if not expense_name or expense_name.isdigit():
            print("Invalid input! Please enter a valid expense")
        else:
            break

    while True:
        try:
            expense_price = float(input("Enter the cost: "))
            break
        except ValueError:
            print("Invalid input! Please Enter a number")

    while True:
        print("Choose a category:")
        for i, category in enumerate(categories):
            print(f'{i+1}. {category}')
        category_range = f'[1-{len(categories)}]'

        # User entering the expense category
        try:
            choice = int(input(f"Choose a category {category_range} ")) -1
            if choice in range(0,len(categories)): # if input number doesn't exceed the length of the list
                expense_category = categories[choice] # taking the equivalent category from the list
                new_expense = expense.Expense(expense_name, expense_category, expense_price) # creating an expense object
                return new_expense
            else:
                print("Invalid input! Please choose from the list")
        except ValueError: # raise ValueError if User entered word instead of a number
            print("Invalid input! Please Enter a number")

# Saving the expense details in an excel file
def save_item(expense_result: expense.Expense, path): # expense object and csv file
    with open(path, 'a', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow([expense_result.name, expense_result.category, expense_result.cost])

def view_expenses(path, budget):
    expenses_list = [] # Store all expenses
    with open(path, encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            #print(','.join(row))

            name,category,cost = row
            expenses_list.append({'name': name, 'category': category, 'cost': float(cost)})

        # Check if the file is empty
        with open(path, 'r', newline='', encoding='utf-8') as csvfile:
            file_content = csvfile.read().strip()
            if not file_content:
                print(Colors.colored_text("No expenses to be viewed.", "yellow"))
                return # break

        # Now, since the file is not empty, you can use csv.reader
        with open(path, encoding='utf-8') as csvfile:
            csvreader = csv.reader(csvfile)
            print(Colors.colored_text("**ALL EXPENSES**", "magenta"))
            for i, row in enumerate(csvreader):
                name, category, cost = row
                print(f"{i + 1}. Name: {name}, Category: {category}, Cost: ${float(cost):.2f}")

    # Summary of each category and how much expenses it has ... e.g: Food : 500
    category_with_cost = {} # Dict for category along with the cost {'category':cost}
    for expense in expenses_list: #
        category = expense['category'] # Taking category and cost from the expenses list to use them
        cost = expense['cost']
        # if category not in the new dict (user didn't buy anything under that category until now)
        if category not in category_with_cost:
            category_with_cost[category] = cost # Add the category and assign its value as the cost the user entered
        else: # Category exists
            category_with_cost[category]+=cost # Increment the cost the user entered
    print(Colors.colored_text("**Expenses by category**", "yellow"))
    for category, cost in category_with_cost.items():
        print(f'{category}: ${cost:.2f}')

    # Total spent
    total_spent = sum(category_with_cost.values())
    print(Colors.colored_text(f'Total Expenses: ${total_spent:.2f}', "red"))

    # Remaining money off the budget
    remaining = budget - total_spent
    print(Colors.colored_text(f"You've ${remaining:.2f} left from your budget","blue"))

    now = datetime.now()
    days_in_month = calendar.monthrange(now.year, now.month)[1]  # [1] extracts second element which is the number of days in month
    remaining_days = days_in_month - now.day
    # print(remaining_days)
    daily_budget = remaining / remaining_days
    #print(green(f"Budget Per Day: ${daily_budget:.2f}"))
    print(Colors.colored_text(f"Budget Per Day: ${daily_budget:.2f}", "green")) # Budget per day till the budget spent

def save_expenses(expenses_list, path):
    with open(path, 'w', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)
        for expense in expenses_list:
            csvwriter.writerow([expense['name'], expense['category'], expense['cost']])
def load_expenses(path):
    try:
        with open(path, 'r', newline='', encoding='utf-8') as csvfile:
            csvreader = csv.reader(csvfile)
            expenses_list = []
            for row in csvreader:
                name, category, cost = row
                expenses_list.append({'name': name, 'category': category, 'cost': float(cost)})
            return expenses_list
    except FileNotFoundError:
        return []

def remove_expense(path):
    expenses_list = load_expenses(path)
    if not expenses_list:
        print(Colors.colored_text("No expenses available to remove.", "yellow"))
        return

    print(Colors.colored_text("**AVAILABLE EXPENSES**", "magenta"))
    for i, expense in enumerate(expenses_list):
        print(f"{i + 1}. Name: {expense['name']}, Category: {expense['category']}, Cost: ${expense['cost']:.2f}")

    while True:
        try:
            choice = int(input("Enter the number of the expense to remove (0 to cancel): "))
            if choice == 0:
                print("Operation cancelled.")
                return
            elif 1 <= choice <= len(expenses_list):
                # Remove the selected expense
                removed_expense = expenses_list.pop(choice - 1)
                save_expenses(expenses_list, path)
                print(Colors.colored_text(f"Expense '{removed_expense['name']}' removed successfully.", "green"))
                return
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")



def modify_expense(path):

    # Load expenses from the file
    expenses_list = load_expenses(path)

    # Display existing expenses with their indices
    print("Existing Expenses:")
    for i, expense in enumerate(expenses_list):
        print(f"{i + 1}. {expense['name']} - {expense['category']} - ${expense['cost']}")

    # Ask the user to select an expense to modify
    try:
        index = int(input("Enter the expense number to modify: ")) - 1
        if 0 <= index < len(expenses_list):
            # Prompt the user to enter new details for the expense
            new_name = input("Enter the new name for the expense: ")

            # Display available categories
            print("Choose a category:")
            for i, category in enumerate(categories):
                print(f"{i + 1}. {category}")

            # Ask the user to choose a category
            while True:
                category_choice = input("Choose a category (1-5): ")
                if category_choice.isdigit():
                    category_index = int(category_choice) - 1
                    if 0 <= category_index < len(categories):
                        new_category = categories[category_index]
                        break
                print("Invalid category choice. Please enter a number between 1 and 5.")

            new_cost = float(input("Enter the new cost for the expense: "))

            # Update the selected expense with the new details
            expenses_list[index]['name'] = new_name
            expenses_list[index]['category'] = new_category
            expenses_list[index]['cost'] = new_cost

            # Save the modified list of expenses back to the file
            save_expenses(expenses_list, path)
            print("Expense modified successfully.")
        else:
            print("Invalid expense.")
    except ValueError:
        print("Invalid input. Please enter a valid expense.")
def clear_expenses(path):
    load_expenses(path)
    # Asking for confirmation before clearing all expenses
    while True:
        confirm = input("Are you sure you want to clear all expenses? (Y/N): ").lower()
        if confirm == "y":
            # Clear the file by opening it in write mode
            with open(path, 'w', newline='', encoding='utf-8') as csvfile:
                csvfile.truncate(0)  # Truncate the file to remove all content
            print(Colors.colored_text("All expenses cleared!", "red"))
            break
        elif confirm == "n":
            print("No expenses were cleared.")
            break
        else:
            print("Invalid input. Please enter 'Y' or 'N'.")

def get_budget():
    if os.path.exists("budget.txt"):
        # if file exists, read the budget from it
        with open("budget.txt", "r") as file:
            budget = float(file.read())
    else:
        # if file doesn't exist, prompt user to enter the budget
        budget = float(input("Enter your budget:"))
        # saving the budget
        with open("budget.txt", "w") as file:
            file.write(str(budget))
        return budget;
    return budget

def modify_budget():
    budget = get_budget()
    modify_budget = input(
        Colors.colored_text("Do you want to modify your budget? ", "cyan") + Colors.colored_text("(yes/no) ",
                                                                                                 "green")).lower()

    if modify_budget == "yes":
        new_budget = float(input("Enter your new budget: "))
        budget = new_budget

        #update the file
        with open("budget.txt", "w") as file:
            file.write(str(new_budget))
        print("Your budget has been updated to.",budget)
        return budget
    return budget
if(__name__ == '__main__'):
    main()