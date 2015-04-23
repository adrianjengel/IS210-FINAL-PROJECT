
*************************************
Small Law Firm Client Administration
*************************************

---------
Persona:
---------


Mike Moneymaker, Esq.

Persona: Mike is a lawyer with a law degree from Harvard. He runs a one-man law firm in New York City.

Details: Mike’s clients are generally wealthier people who need legal advise for personal matters such as purchasing real estate, prenups and divorces, estate planning and other financial transactions. On some occasions, he also works pro-bono for underprivileged people who cannot afford legal representation otherwise. 

Goals: To keep the overhead costs of his law firm low, Mike does not want to hire a secretary, instead he would like to do all the client billing himself. Since Mike bills by the hour, he needs a software that allows him to enter the time worked for each client and any additional costs that were incurred (such as phone calls, copies and other legal fees). Mike would like to automate the billing process so that once a month an email goes out to all active clients with outstanding bills. The email has to show a detailed list of all incurred work and costs.

-------------------
Problem Scenarios:
-------------------

Problem Scenario: Mike keeps track of his work activities in a log book. Once a month he has to go back and manually calculate the hours worked for each client.  This is a very time-consuming process and often leads to errors and under- or over-billed clients.  Occasionally he gets complaints about this which of course hurts his reputation.

Current Alternative: He could hire a secretary or an accountant so he doesn’t have to do all the billing himself. However, that would incur overhead costs and hurt his bottom-line. Instead, Mike wants to save as much money as he can so he can retire early and play golf every day.

Value proposition: A software that allows Mike to enter his time and keep track of settled bills would do all the calculating thus reducing errors and inaccuracies. Since everything is done automatically, he also saves time and can instead spend more time on the golf course and improve his swing. 

-------------
User Stories:
-------------

As Mike the lawyer, I want to automate my billing so that I can reduce errors and time spent doing administrative work.

-------------------
Acceptance Stories:
-------------------

+++++++++++
Scenario 1:
+++++++++++

| Given that I have multiple client's cases I am working on at any given time,
| And those cases are all active and ongoing,
| And I have done work for a particular case in the past week,
| When I click the *Enter Time* button,
| I will be taken to a work form screen,
| Where I can enter the client and matter number, code of expense that was incurred or work in minutes that was performed.

+++++++++++
Scenario 2:
+++++++++++

| Given that I want to accurately bill my clients once a month,
| And I have done work in the past month for a particular client,
| When I click the *Create Bill* button,
| I will get a list of the work/expense for each client, showing the total work hours and amount owed by client,
| Ready to be printed and mailed to the client.

+++++++++++
Scenario 3:
+++++++++++

| Given that I want to have an accurate overview of all my work done at any given time,
| When I click the *Generate Report* button,
| I will get prompted for a time period with a start and end date,
| That will list all the work done for each client during this period, including a total of work hours and amount billed to the clients,
| Ready to be printed in a list form.
