import requests

def main():
    base=input('Enter the base currency: ')
    other=input('Enter the second currency: ')

    res=requests.get('https://api.exchangeratesapi.io/latest', params={"base":base, "symbols":other})
    data=res.json()
    print(f" 1 {data['base']} is {data['rates'][other]} {other}")

if __name__=="__main__":
    main()
