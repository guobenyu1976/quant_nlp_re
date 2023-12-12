# encoding:utf-8
import re


def extract_by_re(txt_news):
    re_rule = re.compile(r'[A-Z]{3}[A-Z]?[A-Z]?[A-Z]?')
    a =re_rule.findall(txt_news)
    coin_code = a

    return coin_code

def substract_USDC(coin_code):
    re_rule = re.compile(r'USDC|USTC|BTC|RUB')
    a =re_rule.findall(coin_code)
    coin_code = a

    return coin_code


if __name__ == '__main__':
    print("start")

    txt_news = "币安新增ARKM/RUB、WLD/RUB、WLD/TRY、MEWLD/TRY交易KE对KoB"

    #find all code
    coin_code = extract_by_re(txt_news)
    print(coin_code)

    #exclude code like USDC
    for item in coin_code:
        item2 = substract_USDC(item)
        if item2==[]: print(item)

    print("over")

