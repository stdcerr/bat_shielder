# bat_shielder
bat shielder helps to preserve your laptop's battery.

To preserve your laptop's battery charge over time, it is helpful to keep the number of charge cycles at a minimum which means, do not fully empty nor fully charge your battery. Bat_shiedler will warn you when the battery has reached 80% when charging by playing a sound and showing a notification. The warning will persist every minute unless the charger is unplugged.

## Installation
This application is running as a Python script and can directly use a `python` binary installed at `/usr/bin/python`.
Clone the repository and follow the instructions below:
### Python Modules
The scrip uses the following Python modules:

- subprocess
- notify2
- psutil 
- playsound

Use your Operating system's(distribution's) preferred way to install them (e.g. use `pip` for Linux)

### Cron
The suggested method is to call the script once every minute by cron, for this, add the following to your `crontab` (`crontab -e`):
`* * * * * python /path/to/bat_shielder.py`



