# Bank App Backend
### Built Using Django Rest Framework & React With Redux

#### [React Staging Dyno](https://react-cohort-bank.herokuapp.com/)
#### [Django Staging Dyno](test)


~#### [React Prod Dyno](https://react-cohort-bank.herokuapp.com/)~
~#### [Django Prod Dyno](test)~

#### Features:
- Email/Password Based Auth
  - Replaces The Default Django User Model 
  - Extends AbstractBaseUser Instead Of AbstractUser Because Usernames Suck.
  - Associated With Multiple Bank Accounts
  
- Bank Accounts
  - Users Can Open New Bank Accounts
  - Existing Accounts Are Read-Only For Standard Users
  - Multiple Accounts Per User
  - Accounts Can Be Checking or Savings
  - Accounts Have A Balance & A Human-Readable Name
  - Accounts Are Associated With Multiple Transactions

- Transactions
  - Transactions Represent A Change In The Balance Of An Account.
  - Transactions Can Be Deposits Or Withdrawals.
  - Transactions Have An Amount That Is Always Positive, Which Represents How Much The Balance Should Change.
  - Denominated In Cents, Not Dollars, So I Can Use Integers Instead Of Floats.

To Run Server Locally:
- Requires Pipenv & Python3
```
  pipenv install
  pipenv shell
  python manage.py runserver
```