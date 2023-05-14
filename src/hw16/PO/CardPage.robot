*** Settings ***
Documentation   Its page objct cart of product with keywords and variables
Library         SeleniumLibrary

*** Variables ***
${add_to_cart_btn}           xpath://a[text()='Add to cart']

*** Keywords ***
add to cart
    Wait Until Element Is Visible    ${add_to_cart_btn}
    Click Element                    ${add_to_cart_btn}