# COVID-19 News Bot

The **COVID-19 News Bot** is an automated bot developed using Python, designed to send news updates about COVID-19 to a WhatsApp group. It utilizes web scraping techniques with BeautifulSoup and requests to fetch official news on Coronavirus cases, lockdowns, and related information. The bot also employs Selenium to control the WhatsApp Web interface, enabling automatic news sharing with the group.

## Features

- Automated news updates: The bot automatically fetches the latest news on COVID-19 from reliable sources.
- WhatsApp integration: It shares the collected news updates with a specified WhatsApp group.
- Efficient web scraping: BeautifulSoup and requests are used to scrape and process information from the internet.
- Selenium integration: The bot controls the WhatsApp Web interface using Selenium, allowing seamless message sharing.

## Installation

To set up and run the COVID-19 News Bot, follow these steps:

1. Clone the repository to your local machine.
2. Install the required Python packages:

   - selenium
   - requests
   - beautifulsoup4
   - webdriver_manager
   - Crypto

3. Download the appropriate Chrome WebDriver for your system and place it in the project directory. (The code provided uses the Chrome WebDriver).
   - You can download the WebDriver here: [https://sites.google.com/a/chromium.org/chromedriver/downloads](https://sites.google.com/a/chromium.org/chromedriver/downloads)

4. Run the bot using the provided Python script.

5. Scan the QR code with your WhatsApp account to log in and allow the bot to access WhatsApp Web.

6. The bot will start sharing COVID-19 news with the specified WhatsApp group automatically.

## Usage

The COVID-19 News Bot automatically fetches news updates and sends them to a WhatsApp group. The bot uses web scraping techniques to gather data from reliable sources, ensuring that the information shared is accurate and up-to-date.

## Contributing

We welcome contributions to the COVID-19 News Bot project. To contribute, follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and test thoroughly.
4. Submit a pull request, explaining the changes you've made.

## License

This project is licensed under the [MIT License](LICENSE).
