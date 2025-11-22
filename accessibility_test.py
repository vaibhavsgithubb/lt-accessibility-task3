import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Load credentials from .env file
load_dotenv()
LT_USERNAME = os.getenv("LT_USERNAME")
LT_ACCESS_KEY = os.getenv("LT_ACCESS_KEY")
if not LT_USERNAME or not LT_ACCESS_KEY:
    raise EnvironmentError("LT_USERNAME and LT_ACCESS_KEY must be set in the .env file.")


class LambdaTestAccessibility:
    """Automated Accessibility Test Scenario 3 for LambdaTest."""

    def __init__(self):
        # 1. Define LambdaTest Grid URL
        self.hub_url = f"https://{LT_USERNAME}:{LT_ACCESS_KEY}@hub.lambdatest.com/wd/hub"
        self.driver = self._setup_driver()

    def _setup_driver(self):
        """Configures capabilities, including the mandatory accessibility settings."""
        
        # 2. Basic Browser Options
        options = Options()
        options.browser_version = 'latest'
        options.platform_name = 'Windows 10' 

        # 3. Mandatory LambdaTest Options
        lt_options = {
            "project": "LT_Accessibility_Challenge_3_Direct_URL",
            "w3c": True,
            "accessibility": True,
            "accessibility.wcagVersion": "wcag21aa",  # Task requirement: WCAG 2.1 AA
            "accessibility.bestPractice": True,       # Task requirement: Best Practices
            "accessibility.needsReview": True,        # Task requirement: Needs Review
            "name": "WCAG 2.1 AA Audit - 3 Pages" 
        }

        options.set_capability('LT:Options', lt_options)

        # Initialize Remote WebDriver
        print(f"Connecting to LambdaTest hub at: {self.hub_url}")
        driver = webdriver.Remote(
            command_executor=self.hub_url, 
            options=options
        )
        return driver

    def run_tests(self):
        """Executes the test flow covering all required pages."""
        try:
            print("Starting test execution...")
            
            # Base URLs
            homepage_url = "https://ecommerce-playground.lambdatest.io/"
            login_url = f"{homepage_url}index.php?route=account/login"
            # NEW: Use the direct URL provided for reliability
            product_detail_url = "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=42"
            
            # --- Test 1: Homepage ---
            print("Testing 1/3: Homepage...")
            self.driver.get(homepage_url)
            print(f"Successfully loaded: {self.driver.title}")

            # --- Test 2: Login Page ---
            print("Testing 2/3: Login Page...")
            self.driver.get(login_url)
            print(f"Successfully loaded: {self.driver.title}")

            # --- Test 3: Product Detail Page (Direct Navigation) ---
            print("Testing 3/3: Product Detail Page...")
            self.driver.get(product_detail_url)
            print(f"Successfully loaded Product Detail Page: {self.driver.title}")

            print("\n All required pages were visited. The automated accessibility audit is complete.")
            print(f" Test Session ID (for submission): {self.driver.session_id}")
            
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            self.driver.quit()
            print("Browser closed.")

if __name__ == "__main__":
    test = LambdaTestAccessibility()
    test.run_tests()