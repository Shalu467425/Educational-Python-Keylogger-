# Personal Finance Tracker

#### Video Demo: [Your YouTube Video URL Here]
#### Description:

## 📊 Project Overview

The **Personal Finance Tracker** is a comprehensive Python application designed to help users manage their personal finances effectively. This application provides both a modern Graphical User Interface (GUI) and a Command-Line Interface (CLI), allowing users to track income and expenses, categorize transactions, generate detailed financial reports, and visualize spending patterns through interactive charts.

Built as the final project for Harvard's CS50P course, this application demonstrates proficiency in Python programming, software design principles, testing methodologies, and user interface development.

## ✨ Key Features

### 1. **Dual Interface Support**
   - **GUI Mode**: Modern tabbed interface with intuitive navigation
   - **CLI Mode**: Full-featured command-line interface for terminal users

### 2. **Core Financial Management**
   - **Transaction Tracking**: Record income and expense transactions
   - **Categorization**: 12 predefined categories (Food & Dining, Transportation, Housing, etc.)
   - **Automatic Balance Calculation**: Real-time balance updates
   - **Data Persistence**: Automatic saving to CSV files

### 3. **Interactive Dashboard**
   - Current balance display with color-coded indicators
   - Quick statistics (total income, total expenses, transaction count)
   - Recent transactions view
   - Visual progress indicators

### 4. **Comprehensive Reporting**
   - **Monthly Financial Summary**: Income vs. expenses by month
   - **Category Breakdown**: Detailed expense analysis by category
   - **Date Range Filtering**: Customizable transaction period analysis
   - **Savings Rate Calculation**: Percentage of income saved

### 5. **Data Visualization**
   - **Pie Charts**: Visual expense distribution
   - **Bar Charts**: Category-wise spending comparison
   - **Interactive Charts**: Generate, customize, and save charts
   - **Real-time Updates**: Charts update with new data

### 6. **Data Management**
   - **CSV Storage**: Human-readable data format
   - **JSON Export/Import**: Backup and restore functionality
   - **Sample Data**: Auto-population for new users
   - **Transaction Deletion**: Remove unwanted entries

### 7. **User Experience**
   - **Input Validation**: Comprehensive error checking
   - **Intuitive Navigation**: Tab-based interface
   - **Responsive Design**: Adapts to window size
   - **Help System**: Built-in documentation

## 📁 Project Structure
project/
├── project.py # Main application file with GUI and CLI interfaces \
├── test_project.py # Comprehensive test suite using pytest \
├── requirements.txt # Python dependencies \
├── README.md # Project documentation (this file) \
├── finances.csv # Data storage file (auto-generated) \
├── expense_chart_*.png # Generated chart images (auto-generated) \
└── test_finances.csv # Test data file (auto-generated during testing) 

## 🚀 Installation & Setup

### Prerequisites
- Python 3.6 or higher
- pip (Python package manager)

### Step 1: Clone or Download the Project
# Clone the repository or download the project files

```bash
git clone [repository-url]
cd personal-finance-tracker
```
Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```
Step 3: Run the Application
GUI Mode (Recommended):

```bash
python project.py
```
CLI Mode:

```bash
python project.py --cli
```
Run Tests:
```bash
pytest test_project.py
```
# 🎯 Usage Guide
### Starting the Application
When you first run the application, sample data will be automatically added to help you get started. You can delete these sample transactions later.

### Navigating the GUI
**Dashboard Tab**
   - Displays current balance with color coding (green for positive, red for negative)
   - Shows quick statistics: total income, total expenses, and transaction count
   - Lists the 10 most recent transactions
   - Provides an overview of your financial health

**Add Transaction Tab**
   - **Description:** Enter a brief description of the transaction
   - **Amount:** Enter the amount (must be positive)
   - **Type:** Select Income or Expense
   - **Category:** Choose from 12 predefined categories
   - **Date:** Enter date in YYYY-MM-DD format or click "Today"
   - Click "Add Transaction" to save

**View Transactions Tab**
   - Displays all transactions in a sortable table
   - Filter by type: All, Income, or Expense
   - Delete transactions by selecting and clicking "Delete Selected"
   - View amounts with color coding (green for income, red for expense)

**Reports Tab**
   - **Monthly Summary:** Shows income, expenses, balance, and savings rate for each month
   - **Category Breakdown:** Detailed analysis of expenses by category with percentages
   - **Export Options:** Export data to JSON or CSV format for external analysis

**Charts Tab**
   - **Pie Chart:** Visual representation of expense distribution
   - **Bar Chart:** Comparison of expenses across categories
   - **Save Charts:** Export charts as PNG images for reports or presentations

### Using the CLI Mode
The CLI mode provides all core functionality through a text-based interface:
1. **Add Transaction:** Guided process for adding new transactions
2. **View Transactions:** List all transactions with details
3. **View Balance:** Display current balance
4.**Generate Reports:** Create expense reports or financial summaries
5.**Exit:** Close the application

### 🧪 Testing
The project includes comprehensive test coverage using pytest. All tests are located in test_project.py and cover:

### Test Categories:

1. Transaction Management Tests
   - Valid transaction addition
   - Invalid input handling (empty descriptions, negative amounts)
   - Category and type validation
2. Financial Calculation Tests
   - Balance calculation with various transaction combinations
   - Category summary generation
   - Monthly summary calculations
3. Data Persistence Tests
   - Save and load functionality
   - Data integrity verification
   - Export/import operations
4.Report Generation Tests
   - Expense report formatting
   - Date range filtering
   - Empty data handling
   
### Running Tests:
```bash
# Run all tests
pytest test_project.py

# Run with verbose output
pytest test_project.py -v

# Run specific test functions
pytest test_project.py::test_add_transaction_interactive_valid -v
```
**Test Coverage:**
   - 100% of required functions tested
   - Edge case coverage for invalid inputs
   - Integration tests for data persistence
   - Mock testing for user input simulation

## 🛠️ Technical Implementation
### Core Architecture
**FinanceTracker Class**
The main business logic class that handles:
   - Transaction storage and management
   - Financial calculations (balance, summaries, reports)
   - Data persistence (CSV read/write operations)
   - Data export functionality

**Transaction Data Class**
A simple data class representing individual transactions with:
   - Date, description, amount, category, and type
   - Serialization/deserialization methods for CSV/JSON

**GUI Implementation (FinanceTrackerApp Class)**
Built using Tkinter with:
   - **ttk.Notebook** for tabbed interface
   - **ttk.Treeview** for transaction tables
   - **matplotlib** integration for charts
   - **ttk.Combobox** and ttk.Radiobutton for form controls

**CLI Implementation**
Separate command-line interface that provides:
   - Interactive menu system
   - Input validation and error handling
   - Full access to core functionality

### Data Storage
   - **Primary Format:** CSV (comma-separated values)
   - **Backup Format:** JSON (JavaScript Object Notation)
   - **Auto-save:** Transactions are saved immediately after addition/deletion
   - **Sample Data:** Auto-generated for new users

### Dependencies
   - **matplotlib:** Chart generation and visualization
   - **pytest:** Testing framework (development dependency)
   - **tkinter:** GUI framework (standard library)
   - **csv & json:** Data handling (standard library)

## 🔧 Design Decisions & Challenges
### 1. Dual Interface Approach
**Decision:** Implement both GUI and CLI interfaces
**Reason:** Provides flexibility for different user preferences and demonstrates proficiency in both interface types
**Challenge:** Maintaining feature parity between interfaces while keeping code DRY

2. CSV Data Storage
Decision: Use CSV format for primary data storage
Reason: Human-readable, easy to debug, and compatible with spreadsheet software
Challenge: Implementing proper serialization/deserialization for transaction objects

3. Transaction Categorization
Decision: Predefined categories with "Other" option
Reason: Standardized categories enable consistent reporting while allowing flexibility
Challenge: Validating category inputs and handling edge cases

4. Real-time Updates
Decision: Immediate UI updates after data changes
Reason: Provides better user experience with instant feedback
Challenge: Coordinating updates across multiple UI components

5. Testing Strategy
Decision: Comprehensive unit tests with pytest
Reason: Ensures reliability and makes future development safer
Challenge: Mocking user input for interactive functions

🎨 User Interface Design
Color Scheme
Primary: Blue (#2E86AB) - Main actions and headers

Success: Green - Income and positive amounts

Danger: Red - Expenses and negative amounts

Warning: Yellow - Warnings and cautions

Info: Light Blue - Informational elements

Layout Principles
Consistency: Uniform styling across all components

Hierarchy: Clear visual hierarchy with font sizes and weights

Feedback: Immediate visual feedback for user actions

Accessibility: High contrast colors and readable fonts

🔄 Future Enhancements
Planned Features
Budget Planning: Set and track monthly budgets for categories

Recurring Transactions: Automatically add regular transactions

Multi-Currency Support: Handle different currencies and exchange rates

Cloud Sync: Synchronize data across multiple devices

Mobile App: iOS/Android companion application

Email Reports: Scheduled email delivery of financial summaries

Investment Tracking: Track stocks, bonds, and other investments

Bill Reminders: Notifications for upcoming bills

Technical Improvements
Database Integration: Replace CSV with SQLite or PostgreSQL

REST API: Web service for remote access

Web Interface: Browser-based access via Flask/Django

Data Encryption: Secure storage of sensitive financial data

Automated Backups: Regular backup to cloud storage

🐛 Troubleshooting
Common Issues & Solutions
Issue: "ModuleNotFoundError: No module named 'tkinter'"
Solution:

Ubuntu/Debian: sudo apt-get install python3-tk

Fedora/RHEL: sudo dnf install python3-tkinter

macOS: brew install python-tk or reinstall Python with Tkinter support

Windows: Should be included by default with Python installation

Issue: Charts not displaying in GUI
Solution:

bash
pip install --upgrade matplotlib
Issue: CSV file corruption
Solution:

Backup your data: Export to JSON from the Reports tab

Delete the corrupted finances.csv file

Restart the application (sample data will be added)

Import your backup from JSON

Issue: Slow performance with many transactions
Solution:

Use filtering to view subsets of transactions

Consider archiving old transactions

The application is optimized for up to 10,000 transactions

Debug Mode
To enable debug output, modify project.py:

python
import logging
logging.basicConfig(level=logging.DEBUG)
👥 Contributing
While this is a CS50P final project, suggestions and improvements are welcome:

Fork the repository

Create a feature branch

Make your changes

Add tests for new functionality

Submit a pull request

📄 License
This project is created for educational purposes as part of the CS50P course. All code is available for learning and reference.

🙏 Acknowledgments
Harvard University and CS50 for the excellent course curriculum

David J. Malan and the CS50 teaching team

Python Software Foundation for the amazing programming language

Matplotlib and Tkinter communities for documentation and examples

📊 Sample Use Cases
Student Budgeting
Track part-time job income

Monitor expenses like food, transportation, and entertainment

Generate monthly reports for financial aid applications

**Family Finance Management**
   - Track household income from multiple sources
   - Categorize expenses for tax preparation
   - Set and monitor budget goals
   - Generate year-end financial summaries

**Freelancer/Contractor**
   - Track project income and business expenses
   - Categorize expenses for tax deductions
   - Monitor cash flow and savings rate
   - Generate client billing reports

**Personal Financial Planning**
   - Monitor spending habits and identify areas for improvement
   - Track progress toward savings goals
   - Generate retirementm planning reports
   - Visualize financial trends over time

### 🏆 Learning Outcomes
This project demonstrates mastery of:
1. **Python Programming:** Object-oriented design, data structures, file I/O
2. **Software Architecture:** Modular design, separation of concerns, code organization
3. **Testing:** Unit testing, integration testing, test-driven development
4. **User Interface:** GUI design principles, event-driven programming
5. **Data Visualization:** Chart generation, data presentation
6. **Error Handling:** Comprehensive validation and user feedback
7. **Documentation:** Code comments, user guides, technical documentation

**Note:** This project was developed for Harvard's CS50P course and represents the culmination of learning from weeks of programming education. It showcases practical application of Python concepts to solve real-world problems in personal finance management.

text

## **requirements.txt** (Copy this to a separate file)

```txt
matplotlib>=3.5.0
pytest>=7.0.0
```
