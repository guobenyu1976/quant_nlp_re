# High-Speed Crypto Trading Signal Extractor
### A Proof-of-Concept for an Event-Driven Trading Strategy

![Python Version](https://img.shields.io/badge/Python-3.7%2B-blue.svg)
![Strategy](https://img.shields.io/badge/Strategy-Event--Driven-orange.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

This project demonstrates the core logic of a **high-speed, event-driven trading strategy**. It's designed to instantly capture potential trading signals, like cryptocurrency tickers, from real-time text data such as news headlines, social media posts (e.g., a tweet from Elon Musk), or official announcements.

While simple, this approach is **powerful and effective** because in algorithmic trading, **speed is alpha**. The goal is not complex linguistic analysis, but the immediate identification of an asset being mentioned, allowing a trading bot to act nanoseconds ahead of the market.

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

