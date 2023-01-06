# Scrapy on Raspberry Pi scheduled with Cron

## Project Overview

A Raspberry Pi 3B with Raspbian OS, Debian version: 11 (bullseye) is used to run the Scrapy webcrawler. The crawler is sheduled using a crontab.

## Use Case

The Boulderbar, a bouldering indoor climbing hall, has a visualization on their website showing the current capacity utilization in percentage. To find out the best times to go climbing, the capacity utilization and a unux timestamp are logged every 15 minutes during the opening hours.

## Setup

### Virtual Environment

To setup a virtual Environment (venv) `cd` to your project directory and run the following commands.

```
python3 -m venv ./venv
source ./venv/bin/activate
```

further explanation of this step can be found [here](https://geektechstuff.com/2019/01/14/creating-a-virtual-python-environment-python/).

### Install Scrapy

Run `sudo pip3 install scrapy` in your venv environment.

### Create a Web Crawler

Scrapy is a fast high-level web crawling and web scraping framework, used to crawl websites and extract structured data from their pages.

#### Spider

A so called spider is used to extract the data from the webpage.
The information can be found on `https://shop.boulderbar.net:8080/modules/bbext/CustomerCapacity.php?gym=hbf`. Using CSS Selectors and html tags a string (for example "35%") is selected via `div.capacity_auslastung center h2::text`.

#### Processing the Data

An `item.py`, an `itemloader.py` and `pipelines.py` are used to process the data and convert it to a float number.
Further information regarding this process can be found at the [official documentation](https://docs.scrapy.org/en/latest/intro/tutorial.html) and in this [tutorial from scrapeops.io](https://scrapeops.io/python-scrapy-playbook/scrapy-beginners-guide/)

### run the crawler manually

To run the crawler you can go to the top level directory of the project and use the command `scrapy crawl boulderbarhbf`.

### Schedule the crawler

To run the crawler on schedule, a shell file (getdata.sh) is created. Always using full path directories here (including /home/username/etc..).

```
#!/bin/bash
#activate virtual environment
source "/full/path/to/project/venv/bin/activate"

#move to the project directory
cd /full/path/to/project/

#start spider
scrapy crawl boulderbarhbf -o boulderbar.jsonl
```

Schedule the spider in crontab using the following line in `crontab -e`:

```
 */15 8-23 * * * /full/path/to/shfile/getdata.sh
```

To check if cron is running properly, run `grep CRON /var/log/syslog`.

This crontab runs the `getdata.sh`-file every 15 minutes from 8am to 23pm and appends a new line with the scraped data to the file `boulderbar.jsonl`.
