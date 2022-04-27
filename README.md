This is the read me file for the PaymentGateway API.

The API sends payment data to the server.

The payment request contains the following data:
1) amount
2) currency
3) card_type
4) card number
5) card expiration month
6) card expiration year
7) card CVV number

On sending the payment request, client side validation is done. This involves checking the presence of all the fields in the request. Client side error is raised if any field is absent.

If the request passes client side validation, it is processed by the API. The payment data is stored in the database. Based upon the request data, additional fields viz. authorization_code, status and time are also added to the data.

The payment request may lead to a 'failure' status under the following cases:
1) Amount is negative.
2) card_type is neither credit-card or debit-card.
3) Length of card number is not equal to 12.
4) Card is expired i.e. today's date is larger than card expiration month and year.
5) CVV number is non-numeric.

In other cases, the status of payment is set to 'success'.


INSTALLING & RUNNING the API:
1) Open the terminal and move to the PaymentGateway directory
2) Create a virtual environment:
	</python -m venv venv>
3) Install the dependencies:
	</pip install -r requiremets.txt>
4) Initialise the database, migrate and upgrade.
	</flask db init>
	</flask db migrate>
	</flask db upgrade> 
5) Run the flask app:
	</flask run>

CHECKING API FUNCTIONALITY:
1) Install Insomnia (for sending requests and checking responses)):
	https://insomnia.rest/download
2)  (a) For POST request type in the URL:
	</http:localhost:5000/api/payments>
	
	(b) Select JSON in the Body drop down menua and enter the JSON text:
	{
	"amount": "100",
	"currency": "USD",
	"card_type": "credit-card",
	"card": {
		"number": "4111111111111111",
		"expiration_month": "2",
		"expiration_year": "2020",
		"cvv": "111"
		}
	}
	
	(c) Click Enter.
	(d) Verify the response.

3) 	(a) For GET request type in the URL:
	</http:locahost:5000/api/payments/1>
	(b) Click Enter.
	(c) Verify the response. 