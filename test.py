import requests

headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
}
cookies = {
    'cookie': 'visid_incap_1101384=Qy35wsk8QW+LoLaPHm2DkeNLDmEAAAAAQUIPAAAAAAC0voE+SwVn9TjUpuVd4Gds; nlbi_1101384=6OpWSCxq6V1AXwMQyZtWRQAAAABa2edYPNa9l6f1bvImbL+E; __Secure-ab-group=19; __Secure-user-id=0; xcid=e7060b61846e9af8508248dafdf88e67; __Secure-ext_xcid=e7060b61846e9af8508248dafdf88e67; _gcl_au=1.1.2063103561.1628326888; cnt_of_orders=0; isBuyer=0; tmr_lvid=f8b40971a5890b1b85a52832106329a1; tmr_lvidTS=1628326888835; _fbp=fb.1.1628326889201.167900671; __exponea_etc__=6943a77d-d5f1-49fc-aec8-fac373b8b18d; visid_incap_2317293=c5SO1DF9T/q/2mbp/ia80tFrD2EAAAAAQUIPAAAAAAA1Jv3CiC1zlPfv6Yri0dXQ; nlbi_2317293=BEskWIMXbyn1im2dQ1ZdBQAAAACh8vTYngc+eld8/b4d09Tm; incap_ses_379_1101384=gQyqQ0wIChHilUD8C3tCBY6/HGEAAAAATu+VuzqTgHsXrojp0WSUFQ==; incap_ses_1339_1101384=ZHA4J3xFTFAxFWikyRWVEkHIHGEAAAAAGeJJ4aVPvQKY5vRk+ajjnA==; incap_ses_631_1101384=85svXuBOQlgx2RyanMPBCKrYHWEAAAAAYiJ0beHjcaOsgm9lqlt/vw==; __Secure-access-token=3.0.LMKZNelrR9OtsmtEhpn1zA.19.l8cMBQAAAABhDkvkHbPLwqN3ZWKgAICQoA..20210821190430.Gj_FlWe7odY4aPIvVOUM3gp3EF4AlhqtE3lV8LioXR0; __Secure-refresh-token=3.0.LMKZNelrR9OtsmtEhpn1zA.19.l8cMBQAAAABhDkvkHbPLwqN3ZWKgAICQoA..20210821190430._PVCQhctPdADViIfLrvlxuLAWmDskes8fJqKbHPpzrk; incap_ses_584_1101384=5QMTAVfG3mvB66Pbn8kaCB4yIWEAAAAAukJEZjrrf0pziqWHD00+PA==; _ga_JNVTMNXQ6F=GS1.1.1629565474.16.0.1629565475.0; _ga=GA1.2.1654334305.1628326888; _gid=GA1.2.949092585.1629565476; _dc_gtm_UA-37420525-1=1; _gat_UA-37420525-1=1; cto_bundle=LQkgIV9yRXJKbW5ZekVJSGxPSXdqTU9JWlJQRnFUNzFHcWpVOHY5TW9SZXBUWElzbHdyRWxtYXolMkJYb1lKMUg2bUJlS29qMXRyMGI2N0NjY3JsU3ZPSGMwNmhSQnd6bkt0Q0FqQWNaYVZwVGxYM1NrVnplN3lsVzJFa2xhZGg4M3hmZFljUmNpbnBwS01HWWVEVFR4U01WNFRaQSUzRCUzRA; tmr_detect=0%7C1629565479228; __exponea_time2__=0.15027666091918945; RT="z=1&dm=ozon.ru&si=7b3f7d31-800f-48d5-96fb-37c883bb9ae5&ss=ksm17fzs&sl=0&tt=0&bcn=%2F%2F6852bd11.akstat.io%2F&ul=kw4"; tmr_reqNum=293'
}
response = requests.get('https://www.ozon.ru/product/mobilnyy-telefon-philips-xenium-e212a-chernyy-258374791/features/',
                        headers=headers, 
                    )
with open('features.html', 'w') as fl:
    fl.write(response.text)