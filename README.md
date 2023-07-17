
# **Survey Password Creator (SuPa)**

This is a simple app for generating passwords for your online surveys. While survey software like Qualtrics, Survey Monkey, and Unipark usually provide default password lists for managing online survey access, researchers may occasionally need to use custom passwords for their studies. This app allows researchers to easily customize passwords according to their specific requirements, without the need for coding.

## Why survey passwords?
In general, survey passwords serve as a means to regulate access to surveys. Surveys may be targeted towards specific audiences or restricted to closed groups of individuals. Passwords are employed to restrict access solely to those who belong to the intended group, such as employees of a company or members of an organization.

Moreover, probability samples often require access control, which can be facilitated through the use of passwords. By assigning a unique password to each invited individual, multiple submissions from the same person can be prevented.

Passwords also play a role in field control. A used password can indicate whether an invited individual has already responded to the survey or not. Consequently, reminders need not be sent to the entire sample, but only to non-respondents, i.e., invited individuals who have not yet used their assigned password.

## A short manual for the app


The app offers multiple input options that allow users to modify various settings.

**Set a seed** 
Please enter a numeric value between 0 and 10,000,000,000. The seed is essential if you want to replicate the exact same list of passwords. 

**Number of passwords to generate** 
Please provide a numeric value. It's important to note that as the number of passwords to generate increases, the app's execution time also increases. If you are using the web app, it may stop running if the number of passwords to generate is excessively high, such as 100,000. In such cases, it is recommended to run the app locally. For instructions on how to run the app [locally](#how-to-run-the-app-locally).

**Password length** 
Select a password length between 4 and 15 characters. If your sample size is large (e.g., 100,000), using a range of password lengths (e.g., 6-8) can be beneficial to avoid generating an excessive number of similar passwords.

**Password complexity**
You can choose whether your password should include at least one uppercase letter, one lowercase letter, one number, and one special character (!"&sect;$%&/()?). The special character '=' is excluded due to compatibility issues with Excel when passwords start with that character. Please note that the current special character list is based on the German keyboard layout, and the implementation for the English keyboard layout is not yet available.

**Advanced options**
The default settings for the advanced options adhere to [recommendations from the scientific literature](#recommended-standards-by-scientific-literature). If in doubt, it is recommended not to modify the advanced options.

**Exclude I/l/1** Enabling this option ensures that passwords do not contain the characters I, l, or 1. You may deactivate this function if your password consists solely of uppercase letters, lowercase letters, or numbers.

**Exclude O/0** Enabling this option ensures that passwords do not contain the characters O or 0. You may deactivate this function if your password consists solely of uppercase letters or numbers.

**Edit distance/Levenshtein distance** This numeric value represents the threshold for similarity between passwords. The default value is 1, meaning that if a single character change can result in retrieving another password from the list, the password is considered too similar. Increasing the edit distance slows down the app as fewer passwords will meet the criteria, requiring more generation and testing for similarity..  

**create passwords** Click this button to generate a list of passwords based on the settings specified in the main panel.

**Download data as CSV** Click this button to download the generated password list as a CSV file. This option is only available after clicking the **"create passwords"** button and generating a password list.

**Download app setting** Click this button to download the main panel settings as a CSV file. This feature can be used for documentation purposes. It is available only after clicking the **"create passwords"** button and generating a password list.


## Recommended standards by scientific literature

Currently, the literature recommends a few standards for survey passwords:
1. It is advised to avoid using an increasing set of consecutive numbers and letters (e.g., 'ABCDEF', '12345'; see Callegaro et al., 2015, p.117). *Hence, the app considers passwords as valid only if less than 50% of the characters in the password are in consecutive order. For example, an eight-character password should not have more than three consecutive characters.*

2. To prevent typing errors or random guessing, pairs of passwords should differ in at least two characters (see Callegaro et al., 2015, p.117). *To ensure this, the app checks the similarity between passwords using the [editdistance package](https://pypi.org/project/editdistance/) (version 0.6.2), which utilizes the Levenshtein distance algorithm. The default threshold is set to 1, meaning that if changing a single character in a password would retrieve an existing password from the list, it is considered too similar and excluded. However, if two or more characters need to be changed to retrieve a password already in the list, it is considered valid (see [How is similarity tested](#how-does-the-app-test-similarity-between-passwords) for more information).*

3. It is recommended to avoid including ambiguous characters, such as **I, 1, l**, or **O, 0** (Couper et al., 2001; Couper, 2008). For instance, Couper et al. (2001) found that passwords containing ambiguous characters had a significantly lower response rate compared to those without such characters (43.7% vs. 50.4%). *Therefore, ambiguous characters are excluded by default.*


## How does the app test similarity between passwords?
The app generates random passwords, and each time a password is created, it is added to the list. However, in cases where the password list is long or consists mostly of short passwords, there is a higher likelihood of generating a password that is similar to an existing one. To address this issue, the app checks each newly created password for similarity against the passwords already in the list using the [editdistance](https://pypi.org/project/editdistance/) function.

As the length of the password list increases, this process significantly slows down the app. To optimize performance, the app employs a selective approach. Instead of testing the created password against all passwords in the list, it tests against a subset. Specifically, the app includes the newly created password in the list, sorts all passwords alphabetically, and then tests the 1000 preceding and 1000 following passwords for similarity. While this method does not guarantee the absence of similar passwords in larger lists, it helps reduce their occurrence.

Please note that future versions of the app may incorporate more efficient methods for handling larger password lists.

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

Haas, G.-C. (2023). Survey Password Creator (SuPa) (Version 1.0.0). Retrieved from https://github.com/gchaas-at-git/supaa


## References
Callegaro, M., Lozar Manfreda, K., & Vehovar, V. (2015). Web Survey Methodology. London: SAGE Publications. Retrieved from https://study.sagepub.com/web-survey-methodology.

Couper, M. P. (2008). Designing Effective Web Surveys. Cambridge University Press. https://doi.org/10.1017/CBO9780511499371.

Couper, M. P., Traugott, M. W., & Lamias, M. J. (2001). Web Survey Design and Administration. The Public Opinion Quarterly, 65(2), 230-253. http://www.jstor.org/stable/3078803

