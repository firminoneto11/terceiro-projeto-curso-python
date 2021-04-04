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

- [x] Main menu
- [x] Account creation
- [x] Accessing account
- [x] Account info
- [x] Deposit, withdrawal and transfer
- [x] Administration access
- [] Administrator area (This one contains a client's data visualization, account removal and login/password update)
</p>
<hr/>
<!--Main Menu Section-->
<div align='center'><h2>💎 Initial Screen / Main Menu 💎</h2></div>
<br/>
<p>When the user executes the program, the first screen that is shown is this one: </p>
<img src='https://github.com/firminoneto11/terceiro-projeto-curso-python/blob/main/assets/ss1.PNG' alt='A screenshot of the main menu screen'>
<p>As you can see, there are four options: </p>

- Entrar na conta / Login account
- Criar conta / Create account
- Administrador / Admin
- Sair / Quit

<p>Each of these buttons leads to differents screens and the navigation among them is pretty simple and intuitive.</p>
<hr/>
<!--Account creation section-->
<div align='center'><h2>💎 Account Creation 💎</h2></div>
<br/>
<p>If the user chooses to create an account, the following screen is presented: </p>
<img src='https://github.com/firminoneto11/terceiro-projeto-curso-python/blob/main/assets/ss2.PNG' alt='A screenshot of the account creation screen'>
<p>Here we have five fields to be filled and they are necessary for identification of the users. Also, the system generates an account number automatically, which starts in 1001 and gets incremented everytime a new user is registered.</br>
The 'Criar conta' button means 'Create account', which is to finish the registration and create the account and the 'Voltar' button is just a back button to cancel all the changes and go back to the main menu.<br/>
If any of these fields is left empty and the user tries to create the account, an error window will pop up, showing that in order to create an account, all the fields can not be left in blank.<br/>
The fields in respective order and it's meanings:

- Nome / Name
- CPF / This one is like a social security number. Also it HAS to be only numbers, otherwise an error window will pop up, showing that this field is to be filled with numbers only.
- Data de Nascimento / Birth date (dd/mm/yyyy). The birth date has to be in this format, because the system will convert it to the standard format.
- Login
- Senha / Password

Once again, these fields can not be left empty or it won't create the account with the given data.<br/>
After a successfully account creation a pop up window will be displayed notifying the user that his account was created succesfully and also will inform his account number, which is necessary to log into his account.
</p>
<hr/>
<!--Accessing account section-->
<div align='center'><h2>💎 Accessing account 💎</h2></div>
<br/>
<p>If at least one account is registered in the system, the user can access it in the 'Entrar na conta' button. When he selects it, this screen will be displayed: </p>
<img src='https://github.com/firminoneto11/terceiro-projeto-curso-python/blob/main/assets/ss3.PNG' alt='Screenshot of the accessing acount section'>
<p>Here, we have three fields to be filled: 

- Número da conta / Account number
- Login
- Senha / Password

If any of these fields are left empty, the pop window will be shown, informing that all fields must be filled.<br/>
To access the account, just needs the account number, which is displayed right after the account creation and the login/password chosen as well.<br/>
Also, there are two buttons. The 'Acessar conta' button should be pressed after typing the right data in the entry boxes and the 'Voltar' button returns to the main menu.
</p>
<hr/>
<!--Account info section-->
<div align='center'><h2>💎 Account info 💎</h2></div>
<br/>
<p>After a successfully login, the following screen will be shown to the user: </p>
<img src='https://github.com/firminoneto11/terceiro-projeto-curso-python/blob/main/assets/ss4.PNG' alt='A screenshot of the account info section'>
<p>When an account is created, the initial balance amount is zero (R$00,00) reais. It can be changed by transfering from another account or depositing.<br/>
The data that are being displayed are:

- Número da conta / Account number
- Saldo / Current balance
- Nome / Name
- CPF / Social Security Number
- Data de nascimento / Birth date
- Login
- Senha / Password

Here we have an exemple of what and how will be displayed the data from a account. And also, we have four buttons that will do different actions. Here's them: 

- Depositar / Deposit
- Sacar / Withdrawal
- Transferir / Transnfer
- Voltar ao menu inicial / Back to the main menu

If the user presses the 'Voltar ao menu inicial' button, the user's session is closed, returns to the main menu and needs to login again to access the account info section.
</p>
<hr/>
<!--Deposit, withdrawal and transfer section-->
<div align='center'><h2>💎 Deposit, withdrawal and transfer 💎</h2></div>
<br/>
<p>Still on the account info screen, the user is presented with the four buttons bellow the account's info. The 'Voltar ao menu principal' is the back button and it works for canceling the session and going back to the main menu, but what about the other three? Let's talk about them.</p>
<h3>* Deposit</h3>
<img src='https://github.com/firminoneto11/terceiro-projeto-curso-python/blob/main/assets/ss5.PNG' alt='A screenshot of the deposit area'>
<p>As you can see, the deposit area only has one input box and two buttons. The 'Depositar' button is the one that does the actual action and the 'Cancelar' button closes the deposit window.<br/>
If the user presses the deposit button without any value typed in the input box, a pop up  window will be displayed informing that he needs to insert any value in there and also it has to be valid number values. After that is correctly done, the deposit is completed and a nice pop up window will be displayed showing that the deposit was successfully made.
</p>
<h3>* Withdrawal</h3>
<img src='https://github.com/firminoneto11/terceiro-projeto-curso-python/blob/main/assets/ss6.PNG' alt='A screenshot of the withdrawal area'>
<p>The withdrawal area works quite similar to the deposit area, but there are some minor differences beetween them. The 'Sacar' button is now the withdrawal button and the input box also doesn't accept any invalid numbers or empty entry, but the amount to be withdrawaled HAS to be equal or less than the user's current balance, otherwise, an error (pop up window) will be displayed.</p>
<h3>* Transfer</h3>
<img src='https://github.com/firminoneto11/terceiro-projeto-curso-python/blob/main/assets/ss7.PNG' alt='A screenshot of the transfer area'>
<p>Now, about the transfer. This one now has two input boxes and two buttons. This time, the 'Transferir' button is the transfer button and before pressing it, the two input boxes needs to be filled.<br/>
The first input box is asking the amount of money/credit that the user wants to transfer. It also follows the rules of the withdrawal area, the amount to be transfered HAS to be equal or less than the user's current balance, otherwise, an error (pop up window) will be displayed.<br/>
The second input box asks the destiny account number of the transfer, then again, if the destiny account number is invalid, a pop up window will be shown, saying that the account number typed is not valid.</p>
<hr/>
<!--Administration access section-->
<div align='center'><h2>💎 Administration access 💎</h2></div>
<br/>
<p>If the user/administrator clicks the 'Administração' button in the main menu area, the following screen is shown: </p>
<img src='https://github.com/firminoneto11/terceiro-projeto-curso-python/blob/main/assets/ss8.PNG' alt='A screenshot of the admin access area'>
<p>There are two input boxes and two buttons. The first input box is for the login and the second input box (senha) is the password. By default, both login and password are 'admin'. That can be changed afterawards.<br/>
Like the previous inputs boxes, if the 'Acessar Administração' button is pressed and any of the input boxes is empty, a pop up error will be displayed, showing that the administrator needs to fill the boxes.<br/>
The 'Voltar' button works like the others and returns to the main menu screen.
</p>
<hr/>
<!--Administrator area section-->
<div align='center'><h2>💎 Administration area 💎</h2></div>
<br/>
<p>Area in construction...</p>
<hr/>
<!--Author section-->
<div align='center'><h2>👾 Author 👾</h2></div>
<p>Made with ❤ by <a href='https://github.com/firminoneto11'>Firmino Neto</a>.</p>