
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

# Konfigurasi Chrome
options = Options()
options.add_argument("--start-maximized")

# Ganti path chromedriver kamu kalau perlu
driver = webdriver.Chrome(options=options)

# 1. Buka halaman Oroswap
driver.get("https://testnet.oroswap.org/pools")
time.sleep(5)

while True:
    try:
        # 2. Klik tombol "Deposit" pertama (yang diinginkan)
        deposit_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Deposit')]")
        deposit_button.click()
        time.sleep(3)

        # 3. Input nominal "0.01" ke kolom ORO
        oro_input = driver.find_element(By.XPATH, "//input[@placeholder='0.0' and contains(@class, 'number')]")
        oro_input.clear()
        oro_input.send_keys("0.01")
        time.sleep(1)

        # 4. Klik tombol "Add Liquidity"
        add_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Add Liquidity')]")
        add_button.click()
        time.sleep(5)

        # 5. Klik tombol "Approve" di Keplr (tidak bisa dikontrol langsung oleh Selenium)
        print("\n❗Silakan klik Approve secara manual jika tidak otomatis.")

        # Tunggu proses selesai
        time.sleep(6)

        # 6. Kembali ke halaman awal
        driver.get("https://testnet.oroswap.org/pools")
        time.sleep(5)

    except Exception as e:
        print("Terjadi error:", e)
        break

driver.quit()
