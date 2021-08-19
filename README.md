Monthly Stock Calculator Document

Firebase Realtime database URL: https://monthly-stock-calculator.firebaseio.com/

Firebase Realtime database Auth json: monthly-stock-calculator.json

Path to send request: /request

Path to store result: /result

Using day close data for calculation

Variable inside /request: 
* month 
  - type: int 
  -	description: The Duration of buying stock 
  -	e.g. one year, month=12
*	quantity
	- type: int
	- description: How many stocks will buy in monthly
	- e.g. one month buy 2, quantity = 2
*	Ticker
	- Type: string
	- Description: The ticker of the stock
	- E.g. AAPL,TSLA,NVDA,AMZN
*	Only US stock is available

Request Package example:
{
    'ticker' :'AAL',
    'month'  : 5,
    'quantity': 2
}


Variable inside /result: (all correct to 2 decimal places)
* Average_stock_price
  - Type: int
  - Description: The average price of the selected stock
* Cost
  - Type: int
  -	Description: Total money used during this period
*	Now_Asset
	- Type: int
	- Description: the quantity of your stock * the recent time stock price
*	Percentage
	- Type: int
	- Description: Percentage change between now asset worth and cost
*	Recent_Price
	- Type: int
	- Description: The recent price of the selected stock
*	Ticker
	- Type: string
	- Description: same as ticker in /request
*	Month_duration
	- Type: int
	- Description: same as month in /request


Result Package Example :
{
'Average_stock_price': 186.67,
 'Cost': 119468.1, 
'Now_Asset': 323897.6,
'Percentage': 171.12,
'Recent_Price': 506.09,
'Ticker': 'AAPL',
'month_duration': 64
}
