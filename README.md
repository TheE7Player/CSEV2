
# CSEV2
Counter Strike Event Viewer 2

> This project as of now is only supported in Windows.
> A Linux and Mac OS version will be made soon - or help by contributing to the project

![Screenshot of the application from 0.6.1](https://github.com/TheE7Player/CSEV2/blob/main/screenshot_0.6.png?raw=true)

> Now with support for many languages - By the community

![Screenshot of the languages available with the application from 0.2](https://raw.githubusercontent.com/TheE7Player/CSEV2/main/supportedLanguages.png)

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

> Update 0.4.1+ brings a new `python environment` while also having a `launcher` made in `C++` for `Windows` only at this time.
>
> Please check the [Wiki](https://github.com/TheE7Player/CSEV2/wiki) to see how to setup the environment

The project requires that you have the latest or Python version of `3.9`+ installed either natively or using an environment such as `Anaconda`

First install Python:
https://www.python.org

Or Anaconda:
https://www.anaconda.com 

## Step 1: Installation of the Packages
Once you installed either native `Python` or `Anaconda` (make sure you have the PATH set) you need to install the following:

> The Packages listed here are accurate as of version 0.6.1+

|Package Name|Package Version  |
|--|--|
| Flask | 2.0.2 |
| flaskwebgui| 0.3.3 |
| requests| 2.26.0 |
| PyYAML| 6.0 |
| psutil| 5.8.0 |

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
> Assume your python is in the C drive and you need to install it into version `3.9`

```
C:\Python39\python.exe -m pip install -r requirements.txt
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

![Screenshot of the application from 0.6.1](https://github.com/TheE7Player/CSEV2/blob/main/screenshot_0.6.png?raw=true)

