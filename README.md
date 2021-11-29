# :atm: Simple ATM Controller


> :warning: **Warning**
>
> This project was made for [Bear Robotics](https://www.bearrobotics.ai/) assessment.
> Copyright:copyright:2021 by Bear Robotics. All rights reserved.

<div id="top"></div>

## :books: Table of Contents

* [:tada: About the Project](#tada-about-the-project)
    * [Introduce](#introduce)
    * [Simplificatoin](#simplification)
    * [Fake API and Functions](#fake-api-and-functions)
    * [Diagram](#diagram)
        * [User Activity](#user-activity)
        * [System Process](#system-process)
    * [Source Directory Tree](#source-directory-tree)
* [:rocket: Usage](#rocket-usage)
    * [Requirements](#requirements)
    * [Prerequisite](#prerequisite)
    * [Test](#test)
* [:white_check_mark: To-Do](#white_check_mark-to-do)
* [:memo: Reference](#memo-reference)

## :tada: About the Project

### Introduce

*Automated Teller Machine (ATM) is an electronic telecommunications device that enalbes customers of financial instituions to perform financial transactions, such as cash withdrawals, deposits, funds transfers, balance inquiries or account information inquiries, at any time and without the need for direct interaction with bank staff.* (from [Wikipedia](https://en.wikipedia.org/wiki/Automated_teller_machine))

In this project, I built a simple ATM controller which operates limited financial transactions, seeing balance, deposit, withdrawal. I simplified some details and created some fake API or features of real world, and designed user acitivity and system process diagram for this.

### Simplification

I simplified some details which exists in real world.

* Free service fee
* Only one cash type, 1 dollor bill
* Required to insert card again to restart transaction
* Receiving amounts only with screen display, not with key pad
* Required to insert card and enter PIN number to select any transactions
* Handling error with conditional statment, not with try-exception because it used fake API and functinos

### Fake API and Functions

* Card reader machine to validate card
* Cash bin machine to withdraw and collect cash
* Bank API for financial transaction and PIN number validation
* Deposit slot to validate and spit the counterfeit cash out, collect for deposit transaction, and spit the cash out for withdrawal transaction

### Diagram

You can check more cleary and all the details of diagrams (user activity and system process) on [Figma Jam](https://www.figma.com/file/UajPEwAhq1GDH6MMGlNmMM/Simple-ATM-Controller?node-id=0%3A1).

#### Diagram Symbol

Bellow image refers to the meaning of each symbols.

![1. Diagram Symbol](/images/1-Diagram-Symbol.png)

#### User Activity

Bellow image referts to the flow of the user activity.

![2. User Activity Diagram](/images/2-User-Activity-Diagram.png)

#### System Process

Bellow image refers to the system process.

![3. System Process Diagram](/images/3-System-Process-Diagram.png)

### Source Directory Tree

Bellow tree stucuture refers to the source code directory.

You can check `ATMController` class with [atm.py](src/controller/atm.py)

```
.
├── controller
│   ├── __init__.py
│   └── atm.py
├── core
│   ├── __init__.py
│   └── config.py
├── fake
│   ├── __init__.py
│   ├── fake_account_model.py
│   ├── fake_bank_api.py
│   ├── fake_card_reader.py
│   └── fake_deposit_slot.py
└── test
    ├── __init__.py
    └── test_atm.py
```

<p align="right">⬆️ <a href="#top">Back to Top</a></p>

## :rocket: Usage

### Requirements

* Python = ^3.9
* Poetry = ^1.0
* Pydantic = ^1.8.2
* python-dotenv = ^0.19.2

I used `pydantic` and `python-dotenv` to manage [configuration](/src/core/config.py). The each ATMs `uuid`, `langitude`, and `longitude` can manage with [environment file](/.env) in this project. It cloud be managed with database in the real world.

### Prerequisite

I used [Poetry](https://python-poetry.org/) to manage Python package for separating the level, product and develop, and dependency resolving with [poetry.lock](poetry.lock) file.

You can install it with `pip`.

```sh
pip install poetry
```

Then you can install only product level packages with option, `--no-dev`.

```sh
poetry install --no-dev
```

> :information_source: **Information**
>
> The develop level packages are such as [isort](https://pycqa.github.io/isort/), [flake8](https://flake8.pycqa.org/en/latest/), [black](https://black.readthedocs.io/en/stable/) and [pre-commit](https://pre-commit.com/).


### Test

I used `unittest`, built-in module, to test.

You can check test cases with command:

```sh
python -m unittest src/test/test_atm.py
```

Then it returns a test case name like:

```sh
Balance Success Test
```

Or you can check all of test codes with [test_atm.py](src/test/test_atm.py)


<p align="right">⬆️ <a href="#top">Back to Top</a></p>


## :white_check_mark: To-do

Here are some tasks needed to do in the future.

* [ ] Middleware
    * Logging middleware to log each transaction of timestamp and result
* [ ] Create policies
    * Service fee
    * Response Template, both success and error cases
    * Maximum time to wait for transactions
    * Maximun amounts of cash to save in cash bin
    * Maximum amounts of cards to collect in card bin
    * ... Etc
* [ ] Business Logic for User Experience(UX)
    * Reapting transactions
    * Selecting transaction before inserting card
    * Checking amounts of cash in the cash bin to show the warning message if the cash exists under 10% of full
    * ... Etc
* [ ] Integrate with a real bank system API
    * To validate PIN number
    * To transact such as deposit, withdrawal, etc.
* [ ] Integrate with a real cash bin machine
    * To collect left cash
    * To transact deposit
    * To transact withdrawal
* [ ] Integrate with a real card bin machine
    * To collect left card
* [ ] Integrate with a real card reader machine
    * To vlidate a card
* [ ] Integrate with a real database or monitoring system
    * To discuss of buisness model and policy by checking timestamp and location of ATM

<p align="right">⬆️ <a href="#top">Back to Top</a></p>

## :memo: Reference

* [[ Wikipedia ] EMV](https://en.wikipedia.org/wiki/EMV#Transaction_flow)
* [[ YouTube ] How Do ATMs work](https://www.youtube.com/watch?v=rIJUFUk38Z0)
* [[ Wikipedia ] Automated teller machine](https://en.wikipedia.org/wiki/Automated_teller_machine)
* [[ National ATM systems ] How Do ATMs Work](https://www.nasatm.com/pages/how-do-atms-work)
* [[ YouTube ] How The ATM Business Works Step by Step](https://www.youtube.com/watch?v=hNBG8XvL9YI)
* [[ Vector Magnets ] How ATMs recognize counterfeit money? ](http://m.vectormagnets.com/n1856043/How-ATMs-recognize-counterfeit-money.htm)


<p align="right">⬆️ <a href="#top">Back to Top</a></p>
