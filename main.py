import datetime
import json
import asyncio
import time
import ast
import asyncpg
from playwright.async_api import async_playwright
from connect import *

data_1 = []
class SupperParserVita():
    async def making_a_request(self, page, urlss):
        print(urlss)
        js = f'''() => {{return fetch("{urlss}").then(response => {{return response.text();}})}}'''
        a = await page.evaluate(js)
        e = a.split(r'"products": [')[1].split(r']')[0]
        res = json.loads(e)
        g_id = res['id']
        main_id_name_price = ([res['id'], res['name'], res['price']])

        print(main_id_name_price)
        js_city = f'''() => {{return fetch("указать аджакс={g_id}").then(response => {{return response.json();}})}}'''
        main_address = await page.evaluate(js_city)

        day = []
        for i in main_address['TODAY_RESULT']['RESULT']:
            main_address_g = i['address']
            day.append(main_address_g)

        # id name price and address
        address_and_inp = day + main_id_name_price
        #print(address_and_inp)

        #print(data_info_in_json)

            #Сохранить через картеж
    async def start_parser(self, urlss):
        async with async_playwright() as p:
            browser = await p.firefox.launch(headless=False)
            context = await browser.new_context(base_url="")
            page = await context.new_page()
            await page.goto("")

            await asyncio.gather(
                asyncio.create_task(self.making_a_request(page, urlss)),
            )


if __name__ == "__main__":
    r = SupperParserVita()
    start = datetime.datetime.now()
    asyncio.run(r.start_parser())
    print(datetime.datetime.now() - start)






        # l = list(self.headers.keys())
            # #print(l)
            # new_header = {}
            # random.shuffle(l)
            # for n in l:
            #     new_header.update({n: self.headers[n]})
            #     #new_header.update({'Referer': 'https://www.google.com'})
            # print(new_header)
            # self.cookie = await page.context.cookies()
            #
            # a = map(dict, self.cookie)
            #my_tuple = tuple(a)
            # print(a)
            # print(my_tuple)
            #cookie_dict = {}
            #fetch("https://vitaexpress.ru/")
            #{{"headers": {{"Accept": "application/json"}},"method": "GET"}})

            # cookies = httpx.Cookies()
            # for cook in my_tuple:
            #     cookies.set(name=cook['name'], value=cook['value'], domain=cook['domain'], path=cook['path'])
            # ssl_config = httpx._config.SSLConfig()
            # ssl_context = ssl_config.load_ssl_context()
            # ssl_context.options |= getattr(ssl, "PROTOCOL_TLS_CLIENT_v1_3", 0)
            # async with httpx.AsyncClient(cookies=cookies, headers=new_header,
            #                              verify=ssl_context,
            #                              follow_redirects=True) as client:
            #     r = await client.get("https://vitaexpress.ru")
            #     print(r.status_code)
