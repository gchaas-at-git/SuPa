
# **Survey Password Creator (SuPa)**

This is a simple app to create passwords for your online survey. Usually, survey softwares, such as, qualtrics, survey monkey, unipark etc., offer a default list of passwords to manage online survey access. However, sometimes researcher may feel the need to use costum passwords for their study. This app enables researchers to costumize their passwords to their needs without writing code. 

## Why survey passwords?
In general, survey passwords are used to control access to surveys. Surveys may be designed for a particular audience or a closed group of individuals. Passwords can be used to limit access to only those who belong to that group, such as employees of a company or members of an organization. Also, propability samples require some sort of access control, for which passwords can be used for. Assigning a unique password to each invited individual prevents multiple submissions from the same invited individual. 
Passwords may also be used for field control. A used password may indicate if an invited indivudal already responded or not. As a result, reminder do not have to be sent to the whole sample but only to non-respondents, i.e., invited individuals with an unused password.

## A short manual for the app

The app provides several inputs which settings can be change. 

**Set a seed** 
Needs a numeric input between 0 and 10,000,000,000. A seed becomes important if you want to replicate the exact same list of passwords.  

**Number of passwords to generate** 
Needs a numeric input. With an increasing number of passwords to generate, the app takes longer. If you use the web-app, the app may stop running if the number of passwords to generate is too high, e.g., 100,000. In this case, run the app [locally](#how-to-run-the-app-locally).

**Password length** 
Choose a password length between 4 and 15 for passwords. If your sample size is large, e.g., 100,000, a range of password length, e.g., 6-8, may be useful to avoid generating too many similar passwords.

**Password complexity**
Here you can decide if your password should contain at least one uppercase letters, lowercase letters, numbers and special characters (!"§$%&/()?). The special character '=' is ommitted because excel does weird things with passwords starting with an '='. The special character list comes from the german keyboard. The special charcter list from an english keyboard is not implemented yet. 

**Advanced options**
The default of the advanced options follows [recommendations from the scientific literature](#recommended-standards-by-scientific-literature). In doubt, I recommend not changing the advanced options.

**Exclude I/l/1** If this option is activated, passwords will not contain no I, l, or 1. You may deactivate this function if your password only contains uppercase letters or only lowercase letters or only numbers.

**Exclude O/0** If this option is activated, passwords will not contain no O, or 0. You may deactivate this function if your password only contains uppercase letters or only numbers.

**Edit distance/Levenshtein distance** A numeric number that provides a threshold for similarity between passwords. The default is 1 and means that if one character of a password can be changed to retrvieve another password in the list of passwords, the password is too similar. Increasing the edit distance slows the app down as more fewer passwords will be valid and more passwords need to generated and tested on similarity.  

**create passwords** A button that when clicked upon creates a list of passwords from the given setting in the main panel.

**Download data as CSV** A button that download the created password list as a csv file. Only appears after the **create passwords** button was clicked and a password list was generated.

**Download app setting** A button that downloads the settings from the main panel as a csv file. May be used for the purpose of documentation. Only appears after the **create passwords** button was clicked and a password list was generated.


## Recommended standards by scientific literature

Currently there are only a few standards recommended by the literture for survey passwords:
1. An increasing set of consecutive numbers and letters should be avoided (e.g., 'ABCDEF', '12345'; see Callegaro et al 2015, p.117). *Therefore the app only regcognizes passwords as valid if less than 50% of characters from the password have a consectutive order. For instance, an eight character long password should not have more than three characters in an consecutive order.*
2. To avoid typing errors or random guessing, pairs of passwords should differ in at least two characters (see Callegaro et al 2015, p.117). *Therefore, the app checks the similiarity between passwords with using the [editdistance package](https://pypi.org/project/editdistance/) (version 0.6.2) which uses the Levenshtein distance to evaluate the similarity between passwords. The default threshold equals 1, that is, if only one character in a password needs to be changed to retrieve a password that is already available in the list of passwords, the password will not be considered for the list. If two or more characters in a password need to be changed to retrieve a password that is already avaible in the list of passwords, the password will be considered for the list (see [How is similarity tested](#how-does-the-app-test-similarity-between-passwords) for more information).* 
3. Do not include ambiguous characters, such as, **I, 1, l** or **O, 0** (Couper et al 2001, Couper 2008). For instance, Couper et al 2001 found that passwords containing ambiguous character had a statistically significant lower response rate compared to passwords not containing such characters (43.7% vs. 50.4 %). *Therefore, ambiguous characters are excluded by default.*

## How does the app test similarity between passwords?
The app creates random passwords. Each time a random password is created, the password will be added to the list of passwords. For long passwords list and passwords list containing only short passwords, the likelyhood is high that a password is created that is similar to a password in the list. Therefore, each newly created password will be tested on similarity against the already existing passwords in the list using the [editdistance](https://pypi.org/project/editdistance/) function. At a certain length of the password list this process slows the app down substantially. Therefore, the app does not test the created password against all passwords in the list but only against a selection. That is, the app includes the password in the list, orders all passwords alphabetically and test the 1000 preceding and 1000 following passwords on similarity. For larger password lists this does not ensure that passwords are similar but at least reduces their occurence. A future version of the app may contain a more optimized method. 

## Limitations 
Streamlit has some resource limitations. Therefore, large lists of passwords (e.g., 100,000) cannot be generated with the web app. In this case, download the app from github and run it [locally](#how-to-run-the-app-locally). 

## How to run the app locally?
Before you can run the app locally, you need the following basic requirements:
1. Knowledge on how to use python
2. Knowledge on how to download a github repository.

If you fulfill the requirements, please follow the following steps:
1. Download the app from https://github.com/gchaas-at-git/supa
2. Open your command prompt and create a python enviroment and install all necessary packages from requirements.txt
```
py -3 -m venv supa_env

#depending on your operation system, the command for activating the enviroment may be different.
supa_env\scripts\activate.bat

py -m pip install -r requirements.txt

```
3. Run the app

```

streamlit run projectfolder/main.py

```

## Contact

If you have questions or suggestions, feel free to reach out to mail@georg-haas.com. I am also happy to collaborate if you have some exciting research ideas on password security for online surveys. 

## Citation

You use this app for your study, I would appreciate if you cite the app:

Haas, Georg-Christoph (2023): *Survey Password Creator (SuPa)*, Version: 1.0.0, source: https://github.com/gchaas-at-git/supa
