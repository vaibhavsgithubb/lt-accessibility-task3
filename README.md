# lt-accessibility-task3
Solution for LambdaTest Accessibility Challenge - Test Scenario 3.
Submission for Test Scenario 3: Automated Accessibility Tests
This repository contains the code used to successfully execute Test Scenario 3: Run Automated Accessibility Tests on the LambdaTest platform.

Objective Summary
The goal was to set up a Selenium test suite and configure the LambdaTest automation capabilities to perform an automated accessibility audit against the WCAG 2.1 AA standard across three mandatory pages of the LambdaTest eCommerce Playground website.
Project Setup and Execution
Prerequisites
Python 3.x

Selenium and python-dotenv libraries (listed in requirements.txt)
LambdaTest Account credentials (Username and Access Key)

Repository Files
accessibility_test.py: The main Python script containing the Selenium logic and LambdaTest capability configuration.
.env: Used to securely load LambdaTest credentials (LT_USERNAME and LT_ACCESS_KEY).

key Configuration The following mandatory capabilities were set in the accessibility_test.py script to trigger the automated WCAG 2.1 AA audit on the LambdaTest grid:CapabilityValuePurposeaccessibilityTrueActivates the LambdaTest accessibility audit feature.accessibility.wcagVersion'wcag21aa'Sets the required WCAG 2.1 AA compliance level.accessibility.bestPracticeTrueIncludes a check for best practices in the report.accessibility.needsReviewTrueFlags issues requiring manual review.

Pages Covered
The script successfully navigated and triggered the accessibility audit on the following three pages:
Homepage: https://ecommerce-playground.lambdatest.io/
Login Page: .../index.php?route=account/login
Product Detail Page: .../index.php?route=product/product&product_id=42
