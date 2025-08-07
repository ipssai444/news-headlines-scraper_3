\# 📰 News Headlines Scraper - Day 3 Task (Elevate Labs Internship)



This is a simple Python-based web scraping project developed as part of the Elevate Labs Internship program – Day 3 task.



The goal of this project is to fetch and display the latest news headlines from a public news website (BBC News), and save them to a local text file using web scraping techniques.



---



\## 📌 Objective



The objective of this project is to:

\- Practice real-world web scraping using Python

\- Extract dynamic content (headlines) from a live website

\- Understand HTML parsing with BeautifulSoup

\- Write structured code that can be reused or extended



---



\## ✅ Features Implemented



\- ✅ Sends an HTTP GET request to the \*\*BBC News\*\* website

\- ✅ Parses the HTML content using \*\*BeautifulSoup\*\*

\- ✅ Extracts all `<h2>` tags that contain the `data-testid="card-headline"` attribute

\- ✅ Iterates through each headline and displays them on the console

\- ✅ Saves all the scraped headlines into a file named `headlines.txt`



---



\## 🛠️ Technologies Used



| Tool/Library      | Purpose                                |

|------------------|----------------------------------------|

| Python 3.x        | Core programming language              |

| `requests`        | To make HTTP requests to websites      |

| `beautifulsoup4`  | To parse and navigate HTML content     |

| VS Code / Terminal | Development \& execution environment   |



---



\## 🧾 How to Run the Project Locally



Follow these steps to run the project on your local machine:



\### 🔧 Step 1: Install Required Libraries



Make sure `requests` and `beautifulsoup4` are installed.  

Run this command in the terminal:



```bash

pip install requests beautifulsoup4



