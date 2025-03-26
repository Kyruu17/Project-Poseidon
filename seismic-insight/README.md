# Project Template Applied Research Methods

## Usage:

1. **Fork the Repository**  
   - One student (repository owner) must fork this project template repository into their GitHub account.
   - The repository owner must then rename the repository according to the project name.

2. **Invite Team Members**  
   The repository owner must invite all other team members as collaborators to the forked repository.  
   - Go to the fork, then to the upper menu > **Settings** > **Access** > **Collaborators**.  
   - Add your team members' GitHub usernames or email addresses one by one.
   - All invited team members must accept the invitation to collaborate.

3. **Access the Fork via GitHub Codespaces**
   - Ensure each invited team member is logged into their own GitHub account.
   - Navigate to the project repository (no need for a fork) by including the repository URL in the address bar of the browser 
     (e.g. https://github.com/repository-owner/project-name)
   - If you see the repository in the browser, click the green **Code** button and go to the Codespaces tab.
   - First click on the **+** sign then on **Create a codespace on master** to launch a new GitHub Codespaces environment.

4. **Check Permissions**
   - Verify that you have the necessary access (e.g., write or collaborator access) to interact directly with the repository.
   - You can do this by changing some code in your Jupyter Notebook and try to commit and sync the changes.
   - If unsure, check the repository's settings or contact the repository owner.

5. **Collaborate Within Codespaces**
   - Commit and synchronize changes to your code and data with Visual Studio Code as often as possible.
   - If you have conflicts when merging, solve them with the integrated merge editor in Visual Studio Code.
   - The following video explains how this works: https://www.youtube.com/watch?v=KuB6hYoLozw
   - Use the terminal to install additional Python libraries if neccessary (don't forget to extent the requirements.txt file).

6. **Directory Structure**
```
project-name/
│
├── Data/                       # Folder with your data files
├── jupyter_notebook.ipynb      # Your Jupyter Notebook with markdown and code cells (change name if required)
├── requirements.txt            # Python libraries
├── README.md                   # Project instructions (this file)
└── .gitignore                  # Files to be ignored by Git (extent if required)
```
