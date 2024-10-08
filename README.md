[![Python Application Test with Github Actions by Peter](https://github.com/cpyang123/DE-W5/actions/workflows/test.yml/badge.svg)](https://github.com/cpyang123/DE-W5/actions/workflows/test.yml)


# Command Line Tool for Managing House Price Records

## Overview

This project provides a command-line interface (CLI) for managing house price records stored in a SQLite database. The tool allows users to create, read, update, and delete records in a database, as well as initialize the database with a predefined dataset.

## Features

1. **Initialize the Database**:
   - Loads a CSV file (`train.csv`) containing house price data and stores it in a SQLite database.
   - Command: `init`
   
2. **Create a New Record**:
   - Allows users to insert a new house price record into the database with specified details such as median income, house age, and median house value.
   - Command: `create_record`
   - Required Arguments:
     - `MedInc` (Median Income)
     - `HouseAge`
     - `AveRooms` (Average Rooms)
     - `AveBedrms` (Average Bedrooms)
     - `Population`
     - `AveOccup` (Average Occupants)
     - `Latitude`
     - `Longitude`
     - `MedHouseVal` (Median House Value)

3. **Update an Existing Record**:
   - Updates an existing house price record identified by an ID. All the attributes of the record can be modified.
   - Command: `update_record`
   - Required Arguments:
     - `id` (ID of the record)
     - `MedInc` (Median Income)
     - `HouseAge`
     - `AveRooms` (Average Rooms)
     - `AveBedrms` (Average Bedrooms)
     - `Population`
     - `AveOccup` (Average Occupants)
     - `Latitude`
     - `Longitude`
     - `MedHouseVal` (Median House Value)

4. **Read Records**:
   - Retrieves house price records from the database. Users can either retrieve all records or specify an ID to fetch a single record.
   - Command: `read`
   - Optional Argument:
     - `--id` (ID of the record to read; if not provided, all records are displayed)

5. **Delete a Record**:
   - Deletes a house price record from the database based on a provided ID.
   - Command: `delete_record`
   - Required Argument:
     - `--id` (ID of the record to delete)

## Getting Started

### Prerequisites

- Python 3.x
- SQLite3
- A CSV file (`train.csv`) with the following structure:
  - `MedInc`: Median income in the area
  - `HouseAge`: Age of the house
  - `AveRooms`: Average number of rooms in houses
  - `AveBedrms`: Average number of bedrooms in houses
  - `Population`: Population of the area
  - `AveOccup`: Average occupancy
  - `Latitude`: Latitude coordinate
  - `Longitude`: Longitude coordinate
  - `MedHouseVal`: Median house value

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
    ```

2. Run make all:
    This will install all requirements and make sure everything is running right
    ```bash
    make all
    ```

### Usage

1. **Initialize the Database**:
   ```bash
   python main.py init
   ``` 

2. **Create a New Record**:
    ```bash
    python main.py create_record <MedInc> <HouseAge> <AveRooms> <AveBedrms> <Population> <AveOccup> <Latitude> <Longitude> <MedHouseVal>
    ```
3. **Update Existing Record**:
    ```bash
    python main.py update_record <id> <MedInc> <HouseAge> <AveRooms> <AveBedrms> <Population> <AveOccup> <Latitude> <Longitude> <MedHouseVal>
    ```
4. **Read Records**:
    Read all records:
    ```bash
    python main.py read
    ```

    To read a specific record by ID:
    ```bash
    python main.py read --id <id>
    ```

5. **Delete a Record**:
    ```bash
    python main.py delete_record --id <id>
    ```

### File Structure
```
Root Directory
├── .devcontainer
│   ├── devcontainer.json
│   └── Dockerfile
├── .github
│   └── workflows
│       └── test.yml
├── .pytest_cache
├── database
│   └── demo.db
├── mylib
│   ├── __pycache__
│   ├── __init__.py
│   ├── lib.py
├── .gitignore
├── main.py
├── Makefile
├── README.md
├── requirements.txt
├── test_main.py
└── train.csv
```
