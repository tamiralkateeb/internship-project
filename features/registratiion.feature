
Feature: User Registration

Scenario: User can enter information into the input fields on the registration page
  Given the user is on the registration page
  When the user enters "ALEX" into the Full Name field
  And the user enters "+971 + test + careerist" into the Phone Number field
  And the user enters "ALEX@GMAIL.COM" into the Email field
  And the user enters "test" into the Company Website field
  And the user enters "USA3241" into the Password field
  Then the entered information should be present in the respective fields
