# Simple Token Scanner Multi Blockchain 
**Tested On:** ![python](https://badgen.net/badge/python/3.10/blue?icon=pypi&cache=500)

Hello there today I create simple tools that can `check` available all token on your `wallet` with multi blockchain such as: 

- [Ethereum](https://ehterscan.io/)
- [Binance Smartchain](https://bscscan.com/)
- [Polygon](https://polygonscan.com/) (`This chain error due that network behind Cloudflare network in Under Attack Mode`)
- [AVAX Chain](https://snowtrace.com/)
- [Fantom](https://ftmscan.com/)

This script grabbing from their block explorer, may some request are limited access.<br>
And on this script doesnt not use **threading** due access  limited requests, So this script running may slowing if your have a lot wallet in file list :v<br>
# Installations
Click this -> [![v1.0](https://badgen.net/badge/release/v.1.0/blue?icon=git&cache=500)](https://github.com/dbgid/SimpleTokenScannerMultiChain/releases/download/v.1.0/multitoken.py) button to start download from release this repo.
or you can also clone this by following command
```shell
git clone https://github.com/dbgid/SimpleTokenScannerMultiChain
cd SimpleTokenScannerMultiChain
```
Make sure you has install dependency module below
- ![requests](https://badgen.net/badge/requests/2.28.1/blue?icon=pypi&cache=500)
- ![bs4](https://badgen.net/badge/bs4/0.0.1/blue?icon=pypi&cache=500)
- ![colorama](https://badgen.net/badge/colorama/0.4.5/blue?icon=pypi&cache=500)

install them on your linux manchine by following command in ![terminal](https://badgen.net/badge/icon/terminal?icon=terminal&label&cache=500)

```shell
pip install requests==2.28.1 bs4==0.0.1 colorama==0.4.5
```
in the above for `termux in android` in other linux manchine use following command
```shell
pip3 install requests==2.28.1 bs4==0.0.1 colorama==0.4.5
```
# Usage
- Termux Android
```shell
python multitoken.py -c <blockchain> -f <wallet.txt>
```
- Other Linux Manchine
```shell
python3 multitoken.py -c <blockchain> -f <wallet.txt>
```
> List Other Command Options
- Get Blockchain Id
> --blockchain
- Clear Saved Token Data (listoken.txt)
> --clear
- See full help usage
> -h
# Note
Sorry for `Polygon` chain currently is not working.
Due their behind in **Cloudflare** network, I can't bypass them.
The `Under Attack Mode` can be solved with headless browser.
But this script only grabbing the html element of their website.
Maybe next time Ill release on the headless version.
So you guys if you like with this repo, don't hesitate to fork and clone this repo :)

regards,

**DBG ID**
