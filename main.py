import flet as ft

def main(page: ft.Page):
    page.title = "Expense Tracker"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 20
    
    expenses = []
    total_amount = 0
    
    amount_input = ft.TextField(
        label="Amount ($)",
        width=150,
        input_filter=ft.NumbersOnlyInputFilter()
    )
    
    category_dropdown = ft.Dropdown(
        label="Category",
        width=150,
        options=[
            ft.dropdown.Option("Food"),
            ft.dropdown.Option("Transport"),
            ft.dropdown.Option("Entertainment"),
            ft.dropdown.Option("Other")
        ]
    )
    
    description_input = ft.TextField(
        label="Description",
        width=200
    )
    
    total_text = ft.Text(
        value="Total Expenses: $0.00",
        size=20,
        weight="bold",
        color="green"
    )
    
    expenses_table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Amount")),
            ft.DataColumn(ft.Text("Category")),
            ft.DataColumn(ft.Text("Description")),
            ft.DataColumn(ft.Text("Action"))
        ],
        rows=[]
    )
    
    filter_dropdown = ft.Dropdown(
        label="Filter by Category",
        width=150,
        options=[
            ft.dropdown.Option("All"),
            ft.dropdown.Option("Food"),
            ft.dropdown.Option("Transport"),
            ft.dropdown.Option("Entertainment"),
            ft.dropdown.Option("Other")
        ],
        value="All"
    )
    
    def on_delete_expense(index):
        def delete(e):
            nonlocal total_amount
            total_amount -= float(expenses[index]["amount"])
            expenses.pop(index)
            refresh_table_filtered(filter_dropdown.value)
        return delete
    
    def refresh_table_filtered(selected_category):
        nonlocal total_amount
        expenses_table.rows.clear()
        
        for i, expense in enumerate(expenses):
            if selected_category != "All" and expense['category'] != selected_category:
                continue
            
            delete_button = ft.IconButton(
                icon=ft.Icons.DELETE,
                on_click=on_delete_expense(i)
            )
            
            row = ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(f"${expense['amount']}")),
                    ft.DataCell(ft.Text(expense['category'])),
                    ft.DataCell(ft.Text(expense['description'])),
                    ft.DataCell(delete_button)
                ]
            )
            expenses_table.rows.append(row)
        
        total_text.value = f"Total Expenses: ${total_amount:.2f}"
        page.update()
    
    def on_filter_change(e):
        refresh_table_filtered(filter_dropdown.value)
    
    filter_dropdown.on_change = on_filter_change
    
    def on_add_expense(e):
        nonlocal total_amount
        
        if not amount_input.value or not category_dropdown.value or not description_input.value:
            page.snack_bar = ft.SnackBar(ft.Text("Please fill in all fields"))
            page.snack_bar.open = True
            page.update()
            return
        
        expense = {
            "amount": amount_input.value,
            "category": category_dropdown.value,
            "description": description_input.value
        }
        
        expenses.append(expense)
        total_amount += float(amount_input.value)
        
        amount_input.value = ""
        category_dropdown.value = None
        description_input.value = ""
        
        refresh_table_filtered(filter_dropdown.value)
    
    add_expense_button = ft.ElevatedButton(
        text="Add Expense",
        on_click=on_add_expense
    )
    
    input_row = ft.Row(
        controls=[amount_input, category_dropdown, description_input, add_expense_button],
        spacing=10
    )
    
    page.add(input_row, filter_dropdown, total_text, expenses_table)

ft.app(target=main)