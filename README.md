# telebot-for-google-trend

## Introduction
Hi, I am Laddie and this is my first Telegram bot. The steps below will teach you how to run the bot. I will be happy to receive any feedback from the SGAG team to help me improve on my Telegram bot skills.

## Check your Google Chrome Version
I am using Selenium to scrape from Google Trend website and running it on headless mode. A chrome.exe file is needed according to your Google Chrome version. 

Here are the steps to check your Chrome Version:

1. Top right of your Google Chrome Browser click on the three vertical button.
2. Go to help and then click on About Google Chrome

The version is located beside the blue tick. In this case the version will be 111
![image](https://user-images.githubusercontent.com/103995451/226516647-58daa532-dac5-4d6c-889a-99fa2bc824b3.png)


Go to the following link to download the Chrome.exe for your Google Chrome browser:

- [Version 112](https://chromedriver.storage.googleapis.com/index.html?path=112.0.5615.28/)
- [Version 111](https://chromedriver.storage.googleapis.com/index.html?path=111.0.5563.64/)
- [Version 110](https://chromedriver.storage.googleapis.com/index.html?path=110.0.5481.77/)

After the file is downloaded, save it in the same folder that contains the Python files.


## Running Flask to scrape the Google Trend 
I did not host the web application, so the `webscraping.py` needs to be run locally before the scraping can be done. 

If you are using *VScode*, right click on `webscraping.py` and click on *run Python file on terminal*.  Else you just need to run the code using any IDE.

![Untitled](https://user-images.githubusercontent.com/103995451/226541563-c26d97e5-f550-4382-839d-ab3e6efb6101.png)



After running, go to the terminal and make sure you are running on http://127.0.0.5000. As shown in the image below, the red bounding box.

![tempsnip](https://user-images.githubusercontent.com/103995451/226541346-d88ba92a-17aa-4c96-a5e9-8e985a31c16f.png)

If you are not running on http://127.0.0.5000, Please do the following:

1. Go to `telegram-bot.py` and look at line 24 as shown in the image below.
![1](https://user-images.githubusercontent.com/103995451/226542048-5a40c9dd-a6a9-435f-a4e4-4222f72958d2.png)
2. Change the `BASE` to the local link that you are running.

## Running Telegram bot
Now for the final step, you need you run the `telegram-bot.py` and `webscraping.py` simultaneously.

Go to Telegram and scan this QR code for the bot.

![photo_2023-03-21_15-34-31](https://user-images.githubusercontent.com/103995451/226542848-d00f1c8c-9c5a-46e2-8379-f991a21fad71.jpg)

## Marking Scheme
To access level four and five answers, type /level4 or /level5 and send it to the Telegram bot to see my answers.
