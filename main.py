from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

# Set up webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

# Get table of games from most played games chart
driver.get("https://steamdb.info/charts/")
table = driver.find_elements(By.CSS_SELECTOR, "tr.app")

# Parse data
games = []
for row in table:
    game = {
        "rank": row.find_element(By.CSS_SELECTOR, "td").text,
        "name": row.find_element(By.CSS_SELECTOR, "td:nth-of-type(3)").text,
        "current": row.find_element(By.CSS_SELECTOR, "td:nth-of-type(4)").text,
        "24h Peak": row.find_element(By.CSS_SELECTOR, "td:nth-of-type(5)").text,
        "All-Time Peak": row.find_element(By.CSS_SELECTOR, "td:nth-of-type(6)").text,
    }
    games.append(game)

# Convert to Pandas Dataframe
print("Generating CSV File, please wait.")
df = pd.DataFrame(games)
df.to_csv("top-100-games.csv", index=False)
