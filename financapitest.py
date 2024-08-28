import requests
import matplotlib.pyplot as plt

api_key = open('api_key.txt', 'r').read()

company = "META"

years = 10

income_statement = requests.get(f"https://financialmodelingprep.com/api/v3/income-statement/{company}?limit={years}&apikey={api_key}")

income_statement = income_statement.json()

# print(income_statement[0]['revenue'])
# print(income_statement[0]['grossProfit'])
# print(income_statement[0]['eps'])
# print(income_statement[0]['ebitda'])

revenues = list(reversed([income_statement[i]['revenue'] for i in range(len(income_statement))]))
gross_profits = list(reversed([income_statement[i]['grossProfit'] for i in range(len(income_statement))]))

print(revenues, gross_profits)

plt.plot(revenues, label="Revenue")
plt.plot(gross_profits, label="Gross Profit")
plt.legend(loc="upper left")
plt.show()
