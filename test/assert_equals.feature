Feature: Assert Equals

  Scenario: As a dev I want to display custom messages when assertion fails so that I have better information on failing cases
    Given a custom message and to objects that are not equal
    When assert_equals is executed with the given parameters
    Then the exception message should start with the custom message


  Scenario: As a dev I want to format subjects under test when assertion fails so that I have better information on failing cases
    Given a custom format method and to objects that are not equal
    When assert_equals is executed with the given parameters
    Then the parameters in the exception message should be formatted accordingly