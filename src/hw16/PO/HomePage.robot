*** Settings ***
Documentation   This is the page object of the home page with keywords and variables
Library         SeleniumLibrary
Library         ../helper/LoginHelper.py
Library         ../helper/ShopHelper.py

*** Variables ***
${login_btn}                 xpath://button[text()='Log in']
${logout_btn}                xpath://a[text()='Log out']
${monitor_cat}               xpath://a[text()='Monitors']

*** Keywords ***
open the login window
    Click Element                   id:login2
    Wait Until Element Is Visible   id:loginusername
    Wait Until Element Is Visible   id:loginpassword

fill the login forms
    [Arguments]    ${username}          ${password}
    Input Text     id:loginusername     ${username}
    Input Text     id:loginpassword     ${password}
    Click Button   ${login_btn}

check the welcome message
    ${actual_result} =          Get Welcome Message         ${username}
    Element Text Should Be      id:nameofuser               ${actual_result}

login setUp
    open the login window
    fill the login forms                 ${username}         ${password}
    Wait Until Element Is Not Visible    id:loginusername

click on category
    [Arguments]         ${category}
    Click Element                       ${category}

click on the product with the highest price on the page
    ${name_price} =  Get High Price And Name Item In Shop
    Open High Price Card        ${name_price}