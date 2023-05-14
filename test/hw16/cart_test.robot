*** Settings ***
Suite Setup     Open The Browser And Go To The Home Page
Test Setup      Login SetUp
Resource        src/hw16/PO/Common.robot
Resource        src/hw16/PO/HomePage.robot
Resource        src/hw16/PO/CardPage.robot

*** Test Cases ***
Added to Cart test
    HomePage.click on category           ${monitor_cat}
    HomePage.click on the product with the highest price on the page
    CardPage.add to cart
    go to cart