# Section A

1. Give examples of different integration protocols you have come across and give example scripts in python 3 on how to achieve each one.

Integration protocols are a set of guidelines and standards that are used to facilitate communication and data transfer between different systems and applications. I will provide examples and explanations of some of the integration protocols I have come across as well sample scripts for achieving each one.
a)	Representational State Transfer (REST)
* REST is a style for building web services that use HTTP requests to POST(create), PUT(update), GET(read) and DELETE(delete) data. REST is often used to build Application Programming Interfaces that allow applications to communicate with each other over the internet.
* To use REST, you can utilize the ‘requests’ library to handle the communication.
![Alt text](Picture1.png)

* First, the ‘requests’ library is imported. This library provides the functionality used to make HTTP requests.
* A GET request is made by calling ‘response=requests.get(https://xyz.com). This sends a GET request to the URL that has been specifies and assigns the response to the ‘response’ variable.
* The status of the response i.e. 404 is printed by calling ‘print(response.status_code)’
* The content of the response is then printed by calling ‘print(response.content)’
* Next, a POST request is made by calling ‘response=requests.post(https://xyz.com). This sends a POST request to the URL specified and assigns the response to the variable ‘response’.
*Finally, both the status codes and contents are printed.


