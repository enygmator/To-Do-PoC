# To Do App (Proof of Concepts)

>NOTE: This project is no longer in active development. This was a semester project, as a proof of concept **(intending to use multiple components rather that a framework, which is a not a good idea, thus making this more of a proof of bad concepts)** and thus cannot be developed into something which is better that other products on the market

![Python Style Check](https://github.com/enygmator/To-Do-PoC/workflows/Python%20Style%20Check/badge.svg)

This app will help you to stay on top of your daily tasks. It shows you what you have to do and at the same time 
classifies the tasks for you to manage your responsibilities, work or just your wish to do something.

This app was created, not to be used in production, but far from it; it was made to show a proof of concept, which was to achieve the following:
- Make a webserver to run the app using only `http.server` and no other web framework (to learn concepts related to webservers)
- Upload the python code as a package to PyPI.org (to learn python packaging)
- Use Azure DevOps (now migrated to github) and learn team collaboration using DevOps methods
- Use Github for open-sourcing the project and learn concepts related to workflows on Github.
- Using Git as a VCS (version control system) to effectively manage the repository's history and the development of the app
- To use SQLite3 on the backend (to learn DBMS)
- Implement various features of python in a single project.
- Implement a model similar to the MVC (model-view-controller) architecture.
- Learn web development (we used HTML, CSS and extensive Javascript)

>NOTE: You will notice that a lot of code is unnecessarily lengthy, redundant, and abnormal (as compared to normal coding practices). The reason for most of these situations is that, this project was made as part of a 1st semester CSE engg. project and thus had to incorporate various features and explore situations in code which are not normal, that is, try out various possibilities.  
So, this project does not aim to write good code, rather it intends to show a proof of concept, where multiple components come together to make what could actually be replaced by a single (web) framework

## More Information
To get to know more details of the project, check out the WIKI, which has documented the code pretty well, with a lot of explanation. You may also open issues to intimate of any errors/problems/warnings, or just to get in touch with the developer.

# Installation / Build
>Note that you must have `pip3` and `python3` installed.

### Direct installation from PyPI
This app can be installed directly from the PyPI repo by just running the command `pip3 install todopoc` in a CLI.

### Cloning the Repo and installing it
You can clone the repo and open the CLI with the path set to the main project folder (containing `run.ps1` and `run.sh`). Now, in linux/WSL, run `./run.sh` in bash and/or in windows, run `.\run.ps1` in powershell **AS ADMIN**. Choose the appropriate options, and you are done installing it.

### Install from Release
You can download the ZIP file from the Release section and install it from there by executing: `pip install todopoc.zip` (Not working at the moment)

# Usage
After installing the package, you can run the app from any python interactive terminal or code file like this:
```py
import todopoc as app
app.Start()
```
>This starts the app. the server and port number are mentioned as the output. By default, it is set to http://localhost:8182

you can use Ctrl+C to stop the app

# Development
If you want to develop or debug it, you need to clone the source code, and install it using the above instruction, and make sure you choose `"Y"` when asked, if you want to install it in development mode.
While developing it, you can use the app usual, the way it is mentioned in [USAGE](#Usage), except for the fact that, you will have to import it every single time after making changes.  

A simpler method would be to run the `WebServer.py` file directly using python, but beware, you will have to temporarily change some import statements in files such as `MasterControl.py`.

# LICENSE
This project has been open-sourced on github with the Apache License, Version 2.0, January 2004. Read the License file for further details.

# Contributions
This project has no intention of being developed. But, developers are free to use this code for their own purposes according to the license.

If you want to contribute, then you can open a PR and I will gladly look into it.

Feel free to contact the developers!

# Project Details:

Created by GROUP 10:
1. Moyank Giri
2. Vaibhava Krishna D
3. T Tarun Aditya (Lead developer and project manager)

"A Python Project"  
Semester 1 of batch 2019-23  
"UE19CS102" (Introduction to computing using python Lab) - Section M  
PES University, Bengaluru, Karnataka, India
