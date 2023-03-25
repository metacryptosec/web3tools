'''
生成以太坊账户地址
使用方法：
1. 安装python3
2. 安装python package： pip install eth_account
3. python3 create.py --count number
4. 如果不指定--count number,默认生成10个地址
'''

from eth_account import Account
import argparse
# 生成一个新的私钥
def generate_accounts(num=10):
    for i in range(num):
        private_key = Account.create().privateKey.hex()
        account = Account.privateKeyToAccount(private_key)
        print("Private key:", private_key)
        print("Address:", account.address)

def setting():
    parser = argparse.ArgumentParser()
    parser.add_argument('--count', type=int, default=10, help='the number of lines to print')
    args = parser.parse_args()
    generate_accounts(args.count)

setting()