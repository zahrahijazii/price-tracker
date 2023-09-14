import bs4
import requests
import lxml 

headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    "Accept-Language" : "en-US,en;q=0.9"
}
response = requests.get("https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1", headers=headers)

amazon_price_webpage = response.text
soup = bs4.BeautifulSoup(amazon_price_webpage, "lxml")

price = soup.find(class_="a-offscreen").get_text()
price_text = price.split("$")[1]
price_as_float = float(price_text)
