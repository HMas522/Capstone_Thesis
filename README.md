# Continuous Intelligence App

- Repository: [Hmass522 GitHub](https://github.com/HMas522/Capstone_Thesis)
- Overleaf Report [Hmassey Overleaf](https://www.overleaf.com/read/czmjjqvmpcjy#18f9b6)
- Shiny Website: [Shiny Website](https://hmas522.shinyapps.io/capstone_thesis/)
- Author: [Hayley Massey](https://github.com/HMas522)

-----

## Customize Your Web_App

### Get the Code to your Local Machine
    
1. Open VS Code and from the menu, select **View** / **Command Palette**.
1. Type "Git: Clone" in the command palette and select it.
1. Enter the URL (web address) of your forked GitHub repository (make sure it contains your GitHub username - not denisecase).
1. Choose a directory on your local machine (e.g., Documents folder) to store the project. 
1. Avoid spaces in your directory and file names. If you have spaces, you'll need to use double quotes to keep the entire path recognized as a single string.
1. If prompted, sign in to GitHub from VS Code.

### Make Changes in VS Code

With your respository folder open in VS Code:

1. Click on this README.md file for editing.
1. Update the README.md file by changing your name in the author link above.
1. Update the links in the README.md file to your username instead of denisecase.

### Save Your Changes

1. After making changes, you want to send them back to GitHub.
1. In VS Code, find the "Source Control" icon and click it.
1. Important: Enter a brief commit message describing your changes.
1. Change the "Commit" button dropdown to "Commit and Push" to send your changes back to GitHub.

-----

## Create a Local Virtual Environment

Open a PowerShell terminal in this Capstone Thesis folder on your machine. 
Create a virtual environment named .venv in the current directory. 
Verify that a .venv folder was created after running the command. 

```shell
python -m venv .venv
```

If VS Code asks to use it as the workspace folder, select Yes.

## Activate the Environment

Run the following command to activate the virtual environment we just created.
Verify that the PowerShell prompt now shows (.venv) at the beginning of the line.

```shell
.venv\Scripts\activate
```

## Prepare the Environment

Run the following commands to upgrade pip and install required packages.
Rerun as needed until everything is successfully installed.

```shell
python -m pip install --upgrade pip wheel pyodide-py
python -m pip install --upgrade -r requirements.txt
```

Read the requirements.txt file to see the packages we are installing.

Additional information can be found in our first Shiny repo: 
[cintel-02-app/SHINY.md](https://github.com/denisecase/cintel-02-app/blob/main/SHINY.md#step-2-prepare-virtual-environment)

-----

## Run the App

Verify your virtual environment is activated and packages have been installed. 
Run the following PowerShell command to start the app.

```shell
shiny run app.py
```

You may use `shiny run app.py --reload` but it can be harder to stop the app during development.
Open the app by following the instructions provided in the terminal. 
For example, try CTRL CLICK (at the same time) on the URL displayed (http://127.0.0.1:8000).

Hit CTRL c (at the same time) to quit the app. 
If it won't stop, close the terminal window.
Reopen the terminal window and be sure the virtual environment is activated
before running the app again.

## Deploy the App

Add and customize .github/workflows/deploy.yml.
Login to [shinyapps.io](https://www.shinyapps.io/) then Account / Tokens and add 3 repo secrets.
See the earlier [SHINYAPPS.md](https://github.com/denisecase/cintel-02-app/blob/main/SHINYAPPS.md) for details.

- Name: SHINYAPPS_ACCOUNT, Secret: Paste shinyapps.io account name
- Name: SHINYAPPS_TOKEN, Secret: (paste token )
- Name: SHINYAPPS_SECRET, Secret: (paste secret)

-----

## ⚠️ Delete Hosted App Before Pushing to GitHub

Reminder: The GitHub action deploy.yml may not automatically delete an existing app from shinyapps.io so we can redeploy.

Before pushing to GitHub, login to [shinyapps.io](https://www.shinyapps.io/) and view the list of applications. 

- First archive the app.
- Then delete the archived app.

## Top Down or Bottom Up Approach?

### Top Down 

Shiny is a very complex python package that can be an easy way to build an app (interactive web application). 
Shiny has several examples with starter code. In a previous course, the author executed code with the professor's help. 
A website with continous stocks and continous airline flights were deployed using the Shiny app. 
Shiny has multiple different functions that all interact with one another. 
One cannot modify a few lines of code and have it completely alter the function. 

![Complex Shiny Display](images/Shinyexp1.png)

Shiny has server, session, input, and outputs that all delicately work with one another.

### Bottom Up

The author decided to take the Bottom Up approach. Breaking down the goals peace wise and execute them separately.
Then once all the pieces execute sucessfully on their own, the code can be carefully intertwined to execute a final product. 

A website that hosted and displays data is pretty obsolete if there is no data to display.

# Using API to collect the data

There are a lot of free API's out there that user's can fetch data for their own use for free.
Caveat of API's is that they limit the user to how many times the user can contact the API.
If the limit is over used, then the API might start charging a month fee based on the rate contacted.

The Sports API basic plan limits the user to only contact the API 100 times per day.
Seems like a lot until it is actually applied. The user trying to deploy the code contacted the API, 30 times in one day.

![API tracking](images/API-Tracking.png)

The 2nd object was to use a deque for the data to be live on the Shiny app, but with the limiations of the API's basic plan, this might be no longer in scope.
This relates to a real life problem for companies using API's for apps they may develop. Companies might or cannot afford a monthly cost of $40 a month for 150,000 requests a day.

# API code

Use requests.get to contact the API url's host site to recieve the json response from the API
Create a data dictionary based on the API's json stucture. This will be loaded into a data frame.
The data cannot be viewed unless a print() statement is used or a csv is written to the local destination.
Shiny can work with csv files. The data is now captured and can be used with Shiny.

![API code 1](images/fetchcode1.png)

![API code 2](images/fetchcode2.png)

# Shiny Display

Shiny is unique because of how customizable it is.
The code to display a dataframe is fairly simple but kind of boring. 

![Shiny local deploy](images/local-shiny-deploy.png)

Also, this is hosted on a local server. The object is to have Shinyapps.io host it on a url (https).

The deploy.yml workflow code was leverage from Professor Dr. Denise Case. 
This file will automatically deploy the app.py to the Shinyapps.io, use the correct Python version, install requirements.txt, when changes are pushed to Github.

Shiny account, secrets, and token are what connect my github repo and shiny app together. 

![worflow 1](images/workflow.png)

![workflow 2](images/workflowgit.png)

![worflow 3](images/workflow2.png)

# Shiny Deployed Website

After following the requirements listed at the beginning of this README and activating the virtual environment.
The Shiny app was deployed with shiny run app.py

![Shiny app just dataframe](images/simple-code.png)

![Shiny website deploy](images/Shiny-website-deployed.png.png)

A separate repository was created to design a simple template that is more inviting to the audience. 

Repository Sandbox: [Hmass522 GitHub](https://github.com/HMas522/Capstone_sandbox)

![Basic Shiny Template](images/basic-temp.png)

The code was mixed together so the basic template and Soccer Standings will be displayed

![Mixed Code](images/mixedappcode.png)

# Objective 1 complete!

![Draft 1 Website](images/draft1app.png)

# Archive and Delete the Shinyapp.io

The app must be archived and deleted any time updates are made or multiple versions of the app will be launched and will not match the original url. 


## Future Work if Time Permits

Would like to add a matplotlib graph like in the EDA repo.

Also add another tab to include 2023 standings