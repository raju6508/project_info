# project_info_database

## Overview
This repository contains the database information for the `project_info` application. It includes multiple tables that represent project information and statuses.

## MySQL Versions Used
- **MySQL Workbench:** 8.0.31  
  [Installation Guide](https://dev.mysql.com/doc/workbench/en/wb-installing-mac.html)
- **MySQL Server:** 8.0.31  
  [Installation Guide](https://dev.mysql.com/doc/refman/8.0/en/macos-installation-pkg.html)

## Folder Structure
### 1. `schemas`
Contains SQL files that create the database. These scripts define the structure and relationships within the database schema.

### 2. `tables`
Includes SQL files that create the individual tables used in the database. Each file corresponds to a specific table, with details about columns, data types, and constraints.

### 3. `seed-data`
Holds SQL files that insert dummy data into the tables. This data can be used for testing and development purposes.

## Getting Started

### Prerequisites
Ensure you have the following installed on your system:
- MySQL Server and Workbench (versions mentioned above)
- A code editor (e.g., Visual Studio Code) or terminal for running SQL scripts

### Steps to Set Up the Database
1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd project_info_database
   ```
2. Open MySQL Workbench and connect to your MySQL server.
3. Run the SQL files in the following order:
   - Navigate to the `schemas` folder and execute the database creation script.
   - Move to the `tables` folder and execute each table creation script in sequence.
   - Finally, execute the scripts in the `seed-data` folder to populate the database with sample data.

### Example Commands
- **To execute a script in MySQL Workbench:**
  1. Open the Workbench.
  2. Select your database connection.
  3. Open the desired SQL file and click the lightning bolt icon to run the script.

- **To execute a script via the command line:**
   ```bash
   mysql -u <username> -p < database_name> < /path/to/script.sql
   ```

## Contribution Guidelines
- **Schema Modifications:**
  Add or update files in the `schemas` folder if you are modifying the database structure.
- **Table Updates:**
  Include any table-related changes in the `tables` folder.
- **Seed Data:**
  If adding new seed data, ensure the data integrity and provide descriptive comments in the SQL files.

## Additional Information
- **Testing:** Use dummy data from the `seed-data` folder to test database functionality.
- **Documentation:** Keep the SQL files well-commented and updated to ensure ease of understanding for new team members.
- **Backup:** Regularly back up the database and commit changes to the repository to maintain version history.

## Contact
For queries or support, reach out to the database team or the repository maintainer.

