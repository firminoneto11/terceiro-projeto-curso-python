<!--Badges-->
![GitHub repo size](https://img.shields.io/github/repo-size/firminoneto11/terceiro-projeto-curso-python?style=for-the-badge)
![GitHub](https://img.shields.io/github/license/firminoneto11/terceiro-projeto-curso-python?style=for-the-badge)
![GitHub last commit](https://img.shields.io/github/last-commit/firminoneto11/terceiro-projeto-curso-python?style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/firminoneto11/terceiro-projeto-curso-python?style=for-the-badge)
![GitHub top language](https://img.shields.io/github/languages/top/firminoneto11/terceiro-projeto-curso-python?style=for-the-badge)
<br/>
<!--Title and description-->
<div align='center'><h1>third-project-python-course</br>terceiro-projeto-curso-python</h1></div>
<br/>
<h2>The third project developed in a Udemy's Python course</h2>
<hr/>
<!--About the project section-->
<div align='center'><h2>💻 About the project 💻</h2></div>
<br/>
<p>This project is the third project developed in a Udemy's Python course. This code consists in develop an application that simulates a bank system. Because it is for learning purposes, it doesn't have any real effects, but i tried to simulate as real as possible.</p>
<hr/>
<!--Technologies section-->
<div align='center'><h2>👻 Technologies 👻</h2></div>
<br/>
<p>To build this project, i used mostly Python and Tkinter. This last one is the built-in library to create Graphical User Interfaces (GUI's) from python. Also i used both HTML and CSS to create the icon for the application.<br/>
From the Python language, i used the following modules:

- Tkinter
- OS
- CSV
- Pickle
- Datetime

And to create the icon, i used the following languages:

- HTML
- CSS

The data from the users and the administrator are being stored in csv, pickle and text files. I did not used any databases because i don't know yet how to implement one in the code, but for future projects, i intend to apply them as best as i can.</p>
<hr/>
<!--How do i download the repository section-->
<div align='center'><h2>🤔 How do i download the repository? 🤔</h2></div>
<br/>
<p>To download this repository on your machine, you need the following elements installed: </p>

- [x] Python 3 or superior;
- [x] A source-code editor. I prefer using the <a href='https://www.jetbrains.com/pycharm/'>PyCharm</a> editor, but feel free to use any other from your preference;
- [x] The <a href='https://git-scm.com/download/win'>Git</a> bash terminal;

<p>Once you got all of these installed, run the following command in the git bash terminal to download this repository: </p>

```bash
git clone https://github.com/firminoneto11/terceiro-projeto-curso-python.git
```

<p>If you just want to run the code without any editing, download the 'pyinstaller' lib with the PIP - Python Index Package. Type the following command on your terminal: </p>

```pip
pip install pyinstaller
```

<p>After it's installation, go to the directory that you download this repository, open up a cmd window there, and type this line of code: </p>

```powershell
pyinstaller --onefile --noconsole --icon="valware.ico" BankSimulator.py
```

<p>This will create an '.exe' application, that you can run it without opening the source-code editor. Also, make sure that the anti-virus is not enabled, because sometimes it identifies as a threat.<br/>
Now that you are all set and good to go, the files that needs to be executed are:

- BankSimulator.py -> Execute this one if you didn't created the '.exe' file with the pyinstaller.
- BankSimulator.exe -> Execute this one if you created the '.exe' file with the pyinstaller. It will be inside a directory named 'dist'. You also have to move it to the repository folder after the creation, because it needs access to the 'valware.ico' to show the icon.
</p>
<hr/>
<!--Structure of the project section-->
<div align='center'><h2>📁 Structure of the project 📁</h2></div>
<br/>
<p>The project's presentation order are created by the screens that the GUI has. For better visualization, the functionalities will be shown in the following order:

- Main menu
- Account creation
- Accessing account
- Account info
- Deposit, withdrawal and transfer
- Administration access
- Administrator area (This one contains a client's data visualization, account removal and login/password update)
</p>
<hr/>