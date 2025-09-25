# Crypto Ticker Extractor from Text

A simple yet effective Python script designed to extract cryptocurrency ticker symbols (e.g., `BTC`, `ETH`, `ARKM`) from unstructured text, such as news articles, social media posts, or announcements.

This project demonstrates core skills in **Python programming**, **Regular Expressions (RegEx)**, and **text data processing**, which are highly valuable for data scraping, automation, and data analysis tasks.

### Overview

In the fast-paced world of cryptocurrency, news and announcements often mention new trading pairs or trending assets by their ticker symbols. This script provides a straightforward solution to automatically identify and extract these symbols from a given text, filtering out common non-target tickers like stablecoins or fiat currencies.

### Features

- **Broad Ticker Detection**: Uses a regular expression to find all potential ticker symbols (3-6 uppercase letters).
- **Exclusion Filtering**: Demonstrates a method to filter out a predefined list of unwanted symbols (e.g., `USDC`, `RUB`).
- **Lightweight & Dependency-Free**: Runs with standard Python libraries, no external packages needed.
- **Easy to Understand**: Clean, commented code that's perfect for integration into larger projects.

### How It Works

The script operates in two main steps:

1.  **Extraction (`extract_by_re`)**: It first scans the input text with the RegEx `[A-Z]{3}[A-Z]?[A-Z]?[A-Z]?`. This pattern captures any sequence of 3 to 6 consecutive uppercase letters, which is a common format for crypto tickers.
2.  **Filtering (Main Block)**: After getting a list of all potential tickers, it iterates through them and uses a secondary function (`substract_USDC`) to check against a blacklist of symbols (`USDC`, `USTC`, `BTC`, `RUB`). If a ticker is not on the blacklist, it is printed as a valid result.

### How to Use

1.  Clone the repository or save the script file .
2.  Ensure you have Python 3 installed.
3.  Run the script from your terminal:
    ```bash
    python quant_r expression v2.py
    ```
4.  Modify the `txt_news` variable inside the script to process your own text.

### Skills Demonstrated

This project showcases my proficiency in:

-   **Python Programming**: Writing clean, functional, and reusable Python code.
-   **Regular Expressions (RegEx)**: Crafting precise RegEx patterns to parse and extract specific information from unstructured text. This is a critical skill for any web scraping or data cleaning task.
-   **Text Data Processing**: Manipulating and analyzing string data to achieve a specific outcome.
-   **Problem-Solving**: Breaking down a problem (finding tickers in text) into logical, programmable steps.

### Potential Improvements

This script serves as a strong foundation. For a production environment, I would suggest the following enhancements:

-   **Dynamic Blacklist**: Move the hardcoded blacklist (`USDC`, `RUB`, etc.) to an external configuration file (e.g., `.txt` or `.json`) for easier management.
-   **Refined Filtering Logic**: The current filtering method can be made more efficient and Pythonic, for example, by using a `set` for faster lookups: `if item not in blacklist_set:`.
-   **API Integration**: Wrap the logic in a simple API (using Flask or FastAPI) to serve extraction requests over the network.
-   **Advanced Validation**: Cross-reference extracted tickers with an external API (like CoinGecko or CoinMarketCap) to validate if they are actual, existing cryptocurrencies.

---

### Hire Me on Upwork!

I am a Python developer specializing in **web scraping, data extraction, and process automation**. If you need to turn messy text into structured data, automate repetitive tasks, or build custom data pipelines, I can help.

**Let's build something great together!**

-   **[View my Upwork Profile]([Your Upwork Profile Link])**
-   **[Connect on LinkedIn / View my Portfolio]([Your LinkedIn/Portfolio Link])**

---

