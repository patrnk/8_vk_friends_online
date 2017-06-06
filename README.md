# Watcher of Friends Online

A small script that prints your online friends on VK social network.

# Usage

The list of your online friends will be different:
```
$ python vk_friends_online.py
Login: <your login>
Password: <your password>
Here's your online friends:
* Anton Kuzmenko
* Kostya Kotikov
* Artyom Lomonosov
* Rinat Zubaidullin
```

# How to Install

Python 3 should be already installed. Then use pip (or pip3 if there is a conflict with old Python 2 setup) to install dependencies:

```bash
pip install -r requirements.txt # alternatively try pip3
```
After that, register a standalone applicaton at https://vk.com/apps?act=manage and put your "Application ID" into `VK_APP_ID` environment variable.

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
