# :computer: Instagram-Message-Bot :robot:   ![Followers](https://img.shields.io/github/followers/MB557?label=Followers&style=social) ![](https://img.shields.io/maintenance/yes/2020)
A bot that efficiently handles message sending on Instagram. <br> 

# About :question:

I have programmed a message bot that works specifically for Instagram. The bot was designed in _Python 3.7.6_ making use of 
webscraping techniques. The objective of this bot is to automate the process of sending a message (text/image) to a receiver without the
involvement of the user/host. <br>
Link to code: [Instagram_Message_Bot.py](Instagram_Message_Bot.py)

# Requirements :clipboard:

### System Requirements
The following system requirements must be met. To install a requirement, you can download from the link mentioned on the side.
- **Python 3 and above.**            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Download Python](https://www.python.org/downloads/)
- **PIP for Python in Windows**      &nbsp;&nbsp;&nbsp;&nbsp;[PIP Installation Guide](https://phoenixnap.com/kb/install-pip-windows)
- **Chrome Webdriver**               &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Chrome Webdriver Installation](https://chromedriver.chromium.org/downloads) <br> <br>

### Python Module Requirements
This bot works on the concept of webscraping. Thus, to run this bot, certain modules will have to be installed.
- **selenium**
- **PIL**
- **tkinter**

To install these modules, open up CMD and type in: ```pip3 install <modulename>```
<br>

# Implementation :spades:

After the requirements have been met, follow the below steps to run the program.
- Open CMD (command-prompt), navigate to the working directory. Type in:  ```python Instagram_Message_Bot.py``` <br>
- If you're getting an error, check the python version you're using by typing ```python --version``` in CMD. Make sure you are using python
	3 and above. If the error still pops up, check if the modules were installed correctly.
- After the program executes, it will ask for certain necessary details such as **host account details, Instagram ID of the receiver 
and the message (text/image)** to be sent as shown below. <br> <br>
	<img align="center">![CMD](https://user-images.githubusercontent.com/55105941/86123011-63f5dd80-baf6-11ea-976f-379e81d8a9aa.JPG) <br>
- If the message type is Text, you will be required to type in the message.
- However, if you choose to send an image, a dialog box will open from where you can choose your image.

# Notes :pushpin:

- This bot **only works in _Windows_** (due to directory address configurations which differ in other OS'es.)
- This bot contains 2 .py files. It is necessary to **keep these files in the _same directory_.**
- After the installation of the Chrome Webdriver, it is important to **_replace the driver address in line number 13_ in [Instagram_Message_Bot.py](Instagram_Message_Bot.py) with the address of your Webdriver's location address.** Line 13: <br>
	<img align = "center"> ![Line13](https://user-images.githubusercontent.com/55105941/86123326-e5e60680-baf6-11ea-8a91-ba9efcf3db8a.JPG) <br>
- The password **will not be _visible (and won't be stored)_ when being typed.**

After the provision of these details, the bot takes over and the **user can go away from keyboard.**
