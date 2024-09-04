# Made with love by RzkyO
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import pickle

used_numbers = set()

def generate_unique_random_number():
    while True:
        random_number = random.randint(4738290000000000000, 4738299999999999999)
        if random_number not in used_numbers:
            used_numbers.add(random_number)
            return random_number

driver= webdriver.Chrome()
driver.maximize_window()
driver.get("https://x.com/i/flow/login")

cookies = pickle.load(open("cookies.pkl", "rb"))

for cookie in cookies:
    driver.add_cookie(cookie)

driver.get("https://x.com/home")

counter = 0
while True:
    try:
        # Generate unique random number
        random_number = generate_unique_random_number()

        # Post the tweet
        input_message = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".public-DraftStyleDefault-block.public-DraftStyleDefault-ltr")))
        input_message.send_keys(random_number)
        
        time.sleep(1)

        # Click the post button
        driver.execute_script('document.querySelector("#react-root > div > div > div.css-175oi2r.r-1f2l425.r-13qz1uu.r-417010.r-18u37iz > main > div > div > div > div.css-175oi2r.r-kemksi.r-1kqtdi0.r-1ua6aaf.r-th6na.r-1phboty.r-16y2uox.r-184en5c.r-1c4cdxw.r-1t251xo.r-f8sm7e.r-13qz1uu.r-1ye8kvj > div > div.css-175oi2r.r-kemksi.r-184en5c > div > div.css-175oi2r.r-kemksi.r-1h8ys4a > div:nth-child(1) > div > div > div > div.css-175oi2r.r-1iusvr4.r-16y2uox.r-1777fci.r-1h8ys4a.r-1bylmt5.r-13tjlyg.r-7qyjyx.r-1ftll1t > div.css-175oi2r.r-kemksi.r-jumn1c.r-xd6kpl.r-gtdqiz.r-ipm5af.r-184en5c > div:nth-child(2) > div > div > div > button > div > span > span").click()')
        time.sleep(8)  

        counter += 1
        print("Tweet ke -", counter)
        
    except Exception as e:
        print("An error occurred:", e)
        break  
        
time.sleep(2)
driver.close()
