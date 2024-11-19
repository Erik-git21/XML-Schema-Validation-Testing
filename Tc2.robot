*** Settings ***
Library    SchemaValidationLibrary.py



*** Variables ***
${XSD FILE}    schema.xsd
${XML FILE}    test.xml


*** Test Cases ***
Testovanie
    ${result}=   Validate XML    test.xml    schema.xsd
    Log    ${result}
    Should Contain    ${result}    XML is valid against XSD



*** Keywords ***




