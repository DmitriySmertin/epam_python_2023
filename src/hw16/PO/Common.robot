*** Settings ***
Documentation   This is common robot file, with necessary part for all page objects and have common keywords
Library         SeleniumLibrary

*** Variables ***
${base_url}             https://www.demoblaze.com/
${user_name}            Adonis
${password}             Pass

*** Keywords ***
open the browser and go to the home page
    ${web_driver} =  Set Variable      driver/chromedriver.exe
    Set Selenium Timeout  15
    Set Selenium Implicit Wait  15
    # Set webdriver arguments
    ${chrome_options}=    Evaluate    sys.modules['selenium.webdriver'].ChromeOptions()    sys, selenium.webdriver
    Call Method    ${chrome_options}    add_argument    --disable-extensions
    #Call Method    ${chrome_options}    add_argument    --headless
    Call Method    ${chrome_options}    add_argument    --disable-gpu
    Call Method    ${chrome_options}    add_argument    --no-sandbox
    Call Method    ${chrome_options}    add_argument    --verbose
    Call Method    ${chrome_options}    add_argument    --disable-dev-shm-usage
    ${loggin_capability}    Create Dictionary    performance=ALL
    ${capability}    Create Dictionary    goog:loggingPrefs=${loggin_capability}
    Create Webdriver    Chrome    chrome_options=${chrome_options}    desired_capabilities=${capability}
    Set Window Size    1920    1080
    Maximize Browser Window
    Go To    ${base_url}

check presense of element
    [Arguments]     ${element}
    Wait Until Element Is Visible    ${element}

go to cart
    Click Element    id:cartur
