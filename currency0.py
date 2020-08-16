import requests
def main():
    res=requests.get('https://api.exchangeratesapi.io/latest?base=USD')
    data=res.json()
    print(f" 1 USD is {data['rates']['INR']} rupees today")

if __name__=="__main__":
    main()
