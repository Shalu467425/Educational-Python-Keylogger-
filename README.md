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
🎯 Usage Guide
# Starting the Application
When you first run the application, sample data will be automatically added to help you get started. You can delete these sample transactions later.

### Navigating the GUI
Dashboard Tab
Displays current balance with color coding (green for positive, red for negative)

Shows quick statistics: total income, total expenses, and transaction count

Lists the 10 most recent transactions

Provides an overview of your financial health

Add Transaction Tab
Description: Enter a brief description of the transaction

Amount: Enter the amount (must be positive)

Type: Select Income or Expense

Category: Choose from 12 predefined categories

Date: Enter date in YYYY-MM-DD format or click "Today"

Click "Add Transaction" to save

View Transactions Tab
Displays all transactions in a sortable table

Filter by type: All, Income, or Expense

Delete transactions by selecting and clicking "Delete Selected"

View amounts with color coding (green for income, red for expense)

Reports Tab
Monthly Summary: Shows income, expenses, balance, and savings rate for each month

Category Breakdown: Detailed analysis of expenses by category with percentages

Export Options: Export data to JSON or CSV format for external analysis
