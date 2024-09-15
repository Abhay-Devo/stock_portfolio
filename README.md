# Stock Portfolio Tracker

## Overview

The **Stock Portfolio Tracker** is a Python application designed to help users manage their stock investments. This tool allows users to add, remove, and track the performance of their stock portfolio. It fetches real-time stock data using Yahoo Finance and provides functionalities to view and update the portfolio effectively.

## Features

- **Add Stock**: Add new stocks to your portfolio by specifying the stock symbol and quantity.
- **Remove Stock**: Remove stocks from your portfolio.
- **View Portfolio**: Display the current stocks in your portfolio along with their real-time prices and total value.
- **List Stock Symbols**: Display a list of stock symbols and their associated companies to assist users in identifying valid symbols.

## Getting Started

### Prerequisites

- Python 3.x
- Required Python library : [yfinance](https://pypi.org/project/yfinance/)

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/stock-portfolio-tracker.git
   cd stock-portfolio-tracker

## Installation

### Install Dependencies

You can install the required libraries using pip:

```bash
pip install requests yfinance
```

# Usage
## Run the Application

### Navigate to the project directory and run the application:

```bash
python portfolio.py
```

### Interact with the Application

- **Add Stock:** Enter the stock symbol and quantity to add a stock to your portfolio.
  
- **Remove Stock:** Specify the stock symbol to remove it from your portfolio.
  
- **View Portfolio:** View all stocks in your portfolio along with their current prices and total value.
  
- **List Stock Symbols:** Display a list of stock symbols and their associated companies.

### Data Files

- **usa_companies.txt:** Contains a list of US companies and their stock symbols.

- **india_companies.txt:** Contains a list of Indian companies and their stock symbols.
  
These files help users find stock symbols when they are unsure of them.

## Example
Here is an example of how to interact with the application:

### Mathematica

Stock Portfolio Tracker
1. Add Stock
2. Remove Stock
3. View Portfolio
4. Stock Symbol by Companies
5. Exit
   
- Choose an option (1-4): 1

- Enter stock symbol: AAPL

- Enter quantity: 10

- Current price of AAPL : $150.25 per share

- Do you want to add AAPL at this price? (y/n): y

- 10 shares of AAPL added to the portfolio.

## Contributing
If you would like to contribute to this project, please follow these steps:

### Contributing to the Repository

1. **Fork the Repository**
   - On GitHub, go to the repository you want to contribute to.
   - Click the “Fork” button at the top right of the page to create a copy in your GitHub account.

2. **Clone Your Fork**
   - Copy the URL of your forked repository.
   - Open your terminal and clone the repository:

     ```bash
     git clone https://github.com/yourusername/repository.git
     ```

   - Navigate into the cloned directory:

     ```bash
     cd repository
     ```

3. **Create a New Branch**

   - Create a new branch for your feature or fix:

     ```bash
     git checkout -b feature-branch
     ```

4. **Make Your Changes**
   - Make the necessary changes to the code.

5. **Commit Your Changes**

   - Stage the changes:

     ```bash
     git add .
     ```

   - Commit the changes:

     ```bash
     git commit -m 'Add new feature'
     ```

6. **Push to Your Branch**

   - Push the changes to your fork:

     ```bash
     git push origin feature-branch
     ```

7. **Create a Pull Request**

   - Go to your forked repository on GitHub.
   - Click on “Compare & pull request”.
   - Review your changes and submit the pull request to the original repository.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements
- **Yahoo Finance:** For providing real-time stock data.
- **CodeAlpha:** For the initial guidance and support.
