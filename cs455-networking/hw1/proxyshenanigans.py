import requests


if __name__ == '__main__':
    print(requests.get('https://www.minecraft.net/').content)