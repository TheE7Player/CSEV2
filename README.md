# CSEV2
Counter Strike Event Viewer 2

![Screenshot of the application from 0.1](https://raw.githubusercontent.com/TheE7Player/CSEV2/main/screenshot.png)

Rewrite of the original CSEV made in [Java](https://github.com/TheE7Player/CSGO-Event-Viewer)

Its abilities:
- To select or view different available events that occur in `Counter-Strike: Global Offensive`
- Get the correct attributes for the events you need and with comments (if the event file has any)
- Ability to filter events to narrow down the event you need
- Updater to ensure you are on the best build of the application possible

This is made using Python and parses a `.yaml` file instead of a new type of `.json` that was used in the first edition.

This uses `Flaskwebgui` as its front-end, and - as you know - `Python` as its backend.

This application uses little `Jquery` and `JS` to allow functionality to flow

> `Flaskwebgui` is dependent on `Chrome` to be installed - please make sure you have `Chrome` installed or the program may not operate the way it should be intended to

# Installation
The project requires that you have the latest or Python version of `3.7.9`+ installed either natively or using an environment such as `Anaconda`

First install Python:
https://www.python.org

Or Anaconda:
https://www.anaconda.com 

## Step 1: Installation of the Packages
Once you installed either native `Python` or `Anaconda` (make sure you have the PATH set) you need to install the following:

> The Packages listed here are accurate as of version 0.1

|Package Name|Package Version  |
|--|--|
| Flask | 1.1.2 |
| requests| 2.25.1 |
| PyYAML| 5.3.1 |

Or you can reference the text given above from `requirements.txt` which contains the same packages from above:

> Make sure you have the PATH set before running this command
>
> If you have multiple versions installed, you need to find the pip.exe directly
>
> Change the `requirements.txt` to the correct pathing where you saved it

```
pip install -r requirements.txt
```
or if stated above, you need to install it into another version of `Python`:
> Assume your python is in the C drive and you need to install it into version `3.7.9`

```
C:\Python37\python.exe -m pip install -r requirements.txt
```
## Step 2: Running the application
Once you got all the dependencies required to run the application, select the python version you installed the dependencies above from and call the `main.py` file after `python`:

If your in the file directory of the application, you can straight up call `python` directly:
```
python main.py
```

If your are not in the same directory when calling `python`, you need to use `full pathing` instead of `relative pathing` to get the application to run:
> Replace the current path stated below with where you saved the `main.py file`

```
python C:\Users\JohnSmith\python\CSEV2\main.py
```

## Step 3: Sit back and relax
You did it. You smart cookie.

You can now use the application to find the events you need or have to remind yourself what attributes the events passes over.

Its better to setup a `.bat` file to save you for typing the command each time to load the script - but that's up you now wise one!

![Screenshot of the application from 0.1](https://raw.githubusercontent.com/TheE7Player/CSEV2/main/screenshot.png)
