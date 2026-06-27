# 📈 CodeAlpha - Stock Portfolio Tracker

## 📌 Project Overview

This project was developed as part of the **CodeAlpha Python Programming Internship**.

The **Stock Portfolio Tracker** is a simple Python application that allows users to manage a basic stock portfolio. Users can enter stock symbols and quantities, and the program calculates the total investment based on predefined stock prices. The application also saves the portfolio details to a text file for future reference.

---

## 🚀 Features

* View available stocks and their prices
* Add multiple stocks to the portfolio
* Enter stock quantities
* Calculate total investment value
* Input validation for stock symbols and quantities
* Save portfolio report to a `.txt` file
* Beginner-friendly and easy to understand

---

## 🛠️ Technologies Used

* Python 3
* Visual Studio Code
* File Handling
* Dictionaries
* Loops and Conditional Statements

---

## 📂 Project Structure

```text
CodeAlpha_StockPortfolioTracker/
│
├── main.py
├── portfolio.txt      # Generated automatically after running the program
└── README.md
```

---

## ▶️ How to Run

### Step 1

Install Python 3 on your computer.

### Step 2

Clone this repository or download the project.

### Step 3

Open the project folder in **Visual Studio Code**.

### Step 4

Open the integrated terminal.

### Step 5

Run the program using:

```bash
python main.py
```

or

```bash
python3 main.py
```

---

## 📊 Available Stocks

| Stock Symbol | Price (USD) |
| ------------ | ----------: |
| AAPL         |        $180 |
| TSLA         |        $250 |
| GOOGL        |        $170 |
| MSFT         |        $420 |
| AMZN         |        $195 |

---

## 💻 Sample Output

```text
==================================================
      STOCK PORTFOLIO TRACKER
==================================================

Available Stocks

AAPL : $180
TSLA : $250
GOOGL : $170
MSFT : $420
AMZN : $195

Enter Stock Symbol: AAPL
Enter Quantity: 5

Added Successfully!

Enter Stock Symbol: TSLA
Enter Quantity: 2

Added Successfully!

Enter Stock Symbol: DONE

YOUR PORTFOLIO

AAPL | Qty: 5 | Price: $180 | Total: $900
TSLA | Qty: 2 | Price: $250 | Total: $500

Total Investment = $1400
```

---

## 📁 Output File

After execution, the program automatically creates a file named:

```text
portfolio.txt
```

This file contains:

* Stock symbols
* Quantities
* Stock prices
* Individual investment values
* Total investment amount

---

## 📚 Python Concepts Used

* Variables
* Dictionaries
* Loops
* Conditional Statements
* User Input
* Functions
* Arithmetic Operations
* File Handling
* Exception Handling (`try` / `except`)

---

## 🎯 Learning Outcomes

Through this project, I learned how to:

* Use dictionaries to store and retrieve data
* Accept and validate user input
* Perform arithmetic calculations
* Work with loops and conditional statements
* Read from and write to files
* Build a simple command-line application

---

## 🔮 Future Improvements

Some features that can be added in future versions:

* CSV file export
* Graphical User Interface (GUI) using Tkinter
* Real-time stock prices using an API
* Portfolio editing (Buy/Sell stocks)
* Profit/Loss calculation
* Investment charts and graphs

---

## 👨‍💻 Author

**Your Name**

Python Programming Intern

CodeAlpha Internship Program

---

## 📜 License

This project was developed for educational purposes as part of the **CodeAlpha Python Programming Internship**.
