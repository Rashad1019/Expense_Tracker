# 💰 Simple Expense Tracker

> A cross-platform expense tracking application built with Python and Flet framework. Track your spending habits across desktop, mobile, and web—all from a single codebase.

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![Flet](https://img.shields.io/badge/Flet-Latest-green.svg)
![Platform](https://img.shields.io/badge/Platform-Windows%20|%20Mac%20|%20Linux%20|%20iOS%20|%20Android%20|%20Web-orange.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

---

## 📖 Overview

The Simple Expense Tracker is a practical application that helps you understand where your money goes. Built as part of a comprehensive Flet framework tutorial, this project demonstrates how Python developers can create professional, cross-platform applications without needing to learn HTML, CSS, or JavaScript.

**What makes this special:** One Python codebase runs everywhere—your Windows PC, MacBook, iPhone, Android device, or web browser. No separate codebases. No frontend frameworks. Just Python.

This tutorial project teaches you real-world application development by building something genuinely useful—a tool to track your personal spending and gain insights into your financial habits.

---

## ✨ Features

- **Quick Expense Entry**: Log amount, category, and description in seconds
- **Real-Time Totals**: See your cumulative spending update instantly
- **Organized Display**: All expenses shown in a clean, scannable data table
- **Category System**: Organize spending into Food, Transport, Entertainment, or Other
- **Easy Corrections**: Delete any expense entry with a single click
- **Smart Filtering**: View expenses by specific category to analyze patterns
- **Input Validation**: Prevents errors with built-in form validation and user feedback
- **Responsive UI**: Clean, modern interface that works on any screen size

---

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher installed on your system
- pip (Python package installer)

### Installation

1. **Clone or download this repository**
```bash
git clone https://github.com/Rashad1019/Expense_Tracker.git
cd Expense_Tracker
```

2. **Install Flet framework**
```bash
pip install flet
```

3. **Run the application**
```bash
python main.py
```

That's it! The application will launch in a new window.

---

## 📱 How to Use

1. **Add an Expense**
   - Enter the dollar amount in the "Amount" field
   - Select a category from the dropdown (Food, Transport, Entertainment, Other)
   - Type a brief description (e.g., "Lunch at Mario's", "Gas station")
   - Click "Add Expense"

2. **View Your Spending**
   - See your total expenses displayed at the top
   - All entries appear in the table below with amount, category, and description

3. **Filter by Category**
   - Use the "Filter by Category" dropdown to focus on specific spending types
   - Select "All" to see everything again

4. **Delete an Entry**
   - Click the trash icon (🗑️) next to any expense to remove it
   - Your total automatically updates

---

## 🎓 Learning Outcomes

This project teaches essential application development concepts:

- **UI Design**: Creating intuitive interfaces with input fields, buttons, dropdowns, and tables
- **Data Management**: Storing and manipulating collections of structured data
- **Event Handling**: Responding to user interactions (clicks, input changes, form submissions)
- **State Management**: Maintaining and updating application state across user actions
- **Input Validation**: Ensuring data quality with validation checks and error messages
- **Dynamic Updates**: Refreshing the UI in real-time as data changes
- **Code Organization**: Structuring code with reusable, maintainable functions

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| **Python 3.7+** | Core programming language |
| **Flet Framework** | Cross-platform UI framework |
| **Flet Widgets** | TextField, Dropdown, DataTable, Buttons, Icons |
| **Python Data Structures** | Lists and dictionaries for data storage |

---

## 📂 Project Structure

```
expense-tracker/
│
├── main.py                 # Main application code
├── README.md              # This file
└── requirements.txt       # Python dependencies
```

---

## 🎨 Application Architecture

### Core Components

**Data Layer**
- `expenses` list: Stores all expense records as dictionaries
- `total_amount` variable: Maintains running total of all expenses

**UI Layer**
- Input form with amount, category, and description fields
- Data table displaying all expenses
- Total display showing cumulative spending
- Filter dropdown for category-based viewing

**Logic Layer**
- `on_add_expense()`: Validates and adds new expenses
- `on_delete_expense()`: Removes expenses and updates totals
- `refresh_table()`: Rebuilds table display from current data
- `on_filter_change()`: Filters visible expenses by category

---

## 🌟 Why Flet?

Traditional cross-platform development is complex:
- **Native apps** require learning Swift (iOS), Kotlin (Android), C# (Windows)
- **Web apps** require HTML, CSS, JavaScript, plus a backend
- **Hybrid frameworks** like React Native still need JavaScript knowledge

**Flet changes the game:**
- Write once in Python, run everywhere
- No need to learn frontend technologies
- Modern, responsive UI out of the box
- Deploy to desktop, mobile, or web with the same code
- Perfect for Python developers who want to build full applications

---

## 🎯 Business Impact

### For Personal Use
- **Financial Clarity**: See exactly where your money goes each month
- **Pattern Recognition**: Identify spending habits and areas to reduce costs
- **Budget Awareness**: Make informed decisions based on real data
- **Quick Tracking**: Log expenses in real-time without friction

### For Developers
- **Skill Development**: Learn cross-platform app development without leaving Python
- **Portfolio Project**: Demonstrate practical application building skills
- **Foundation Building**: Understand UI/UX principles, data management, and event-driven programming
- **Time Saving**: Build functional apps in hours instead of weeks

---

## 📚 Additional Resources

- **[Flet Documentation](https://flet.dev/docs/)** - Official framework documentation
- **[Flet GitHub](https://github.com/flet-dev/flet)** - Source code and examples
- **[Flet Discord Community](https://discord.gg/dzWXP8SHG8)** - Get help and share projects
- **Tutorial Video** - [Link to original tutorial series]
- **Masterclass** - [Link to comprehensive Flet course]
- **Newsletter** - [Sign up for updates and tips]

---

## 🔧 Advanced Customization

Want to extend this project? Here are some ideas:

### Beginner Enhancements
- Add more expense categories
- Change the color scheme or theme
- Customize the window size and title
- Add date/time stamps to each expense

### Intermediate Features
- Save expenses to a file (JSON or CSV)
- Load previous expenses on startup
- Add monthly/weekly spending reports
- Create spending charts with matplotlib or plotly
- Add budget limits with alerts

### Advanced Projects
- Export data to Excel with pandas
- Add user authentication for multiple users
- Sync data to cloud storage (Firebase, AWS)
- Create mobile-specific layouts
- Add receipt photo attachments
- Implement recurring expense tracking

---

## 🤝 Contributing

This is a tutorial project, but contributions are welcome! If you've built interesting features or improvements:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👤 Contact & Support

- **Project Questions?** Email me at [Rashad12x@outlook.com](mailto:Rashad12x@outlook.com)
- **Flet Framework Help?** Join the [Discord community](https://discord.gg/dzWXP8SHG8)
- **Found a bug?** Open an issue on GitHub
- **Built something cool?** Share it with the Flet community!

---

## 🙏 Acknowledgments

- **Flet Team** - For creating an amazing Python UI framework
- **Tutorial Creator** - For the comprehensive step-by-step guide
- **Python Community** - For continuous support and inspiration

---

## 📸 Screenshots

### Application in Action

**Empty State - Ready to Track**
![Empty Expense Tracker](https://github.com/Rashad1019/Expense_Tracker/blob/main/screenshots/empty-state.png)
*Clean interface ready for your first expense entry*

**Adding an Expense**
![Adding Concert Expense](https://github.com/Rashad1019/Expense_Tracker/blob/main/screenshots/adding-expense.png)
*Entering a $120 concert ticket in the Entertainment category*

**Multiple Expenses Tracked**
![Multiple Expenses](https://github.com/Rashad1019/Expense_Tracker/blob/main/screenshots/multiple-expense.png)
*Tracking various expenses: vacation ($2700), lunch ($25), metro pass ($60), and concert ($120) - Total: $2905*

**Full Expense List**
![Complete Expense List](https://github.com/Rashad1019/Expense_Tracker/blob/main/screenshots/full-list.png)
*Complete view showing all expenses with running total of $2880*

---

## 🚦 Project Status

**Current Version:** 1.0 (Tutorial Complete)  
**Status:** ✅ Fully Functional  
**Last Updated:** November 2025

### Roadmap
- [ ] Add data persistence (save/load functionality)
- [ ] Implement export to CSV/Excel
- [ ] Create spending visualization charts
- [ ] Add budget tracking and alerts
- [ ] Mobile-optimized layout improvements

---

**Made with ❤️ and Python**

*Building practical applications doesn't require learning a dozen technologies. Sometimes, Python is all you need.*