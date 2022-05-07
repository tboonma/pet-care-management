# Pet Care Management System
Application for monitoring pet in pet care service.

## Database Example
An example of the involved with this project.

**Customer table**
| id | firstName | lastName | gender | address | email | phoneNumber |
|----|-----------|----------|--------|---------|-------|-------------|
| 1 | Tawan | Boonma | Male | Bangkok | tawan.b@mail.com | 7-845-863-4454 |

**Pet table**
| id | name | type | gender | birthyear | owner_id |
|----|-----------|----------|--------|---------|-------|
| 1 | FooFee | Scottish Fold cat | Female | 2020 | 1 |

## Project Documents
- [UML Class Diagram](../../wiki/UML%20Class%20Diagram)
- [Domain Model](../../wiki/Domain%20Model)
- [Package Diagram](../../wiki/Package%20Diagram)
- [Web Services](../../wiki/Web%20Services)

## Getting Started
### Requirements
|Name  | Recommended version(s)|   
|------|-----------------------|
|Python | 3.9 or higher |
|SQLite3 CLI | 3.33.0 or higher |

### Install Packages
1. Clone this project repository to your machine.

    ```cmd
    git clone https://github.com/tboonma/pet-care-management.git
    ```
2. Get into the directory of this repository.

    ```cmd
    cd pet-care-management
    ```
3. Create a virtual environment.

    ```cmd
    python -m venv venv
    ```
4. Activate the virtual environment.

    - for Mac OS / Linux.   
    ```cmd
    source venv/bin/activate
    ```
    - for Windows.   
    ```cmd
    venv\Scripts\activate
    ```
5. Install all required packages.

    ```cmd
    pip install -r requirements.txt
    ```
6. Create your sample database

    ```cmd
    sqlite3 sample.db < petcare.schema
    ```
7. Import CSV data into the database

    ```cmd
    $ sqlite3 sample.db
    sqlite> .mode csv
    sqlite> .import data/CustomerData.csv customers
    sqlite> .import data/PetData.csv pets
    sqlite> .quit
    ```
