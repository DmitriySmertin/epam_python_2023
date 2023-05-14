*** Settings ***
Library         helper/LoginHelper.py
Suite Setup     Open The Browser And Go To The Home Page
Resource        src/hw16/PO/Common.robot
Resource        src/hw16/PO/HomePage.robot

*** Test Cases ***
Login test
    HomePage.open the login window
    HomePage.fill the login forms        ${username}     ${password}
    check presense of element            ${logout_btn}
    HomePage.check the welcome message