# SQL Management Tools - Overview 

Costa Rica

[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/)
[brown9804](https://github.com/brown9804)

Last updated: 2024-09-05

----------

## Wiki 

- [Try Azure SQL Managed Instance for free (preview)](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/free-offer?view=azuresql)
- [Try the Next-gen GP Azure SQL Managed Instance for free](https://techcommunity.microsoft.com/t5/azure-sql-blog/try-the-next-gen-gp-azure-sql-managed-instance-for-free/ba-p/4136933)

| **Category**           | **Tool**                         | **Description**                                                                                   |
|------------------------|----------------------------------|---------------------------------------------------------------------------------------------------|
| **On-Premises**        | SQL Server Management Studio (SSMS) | Comprehensive tool for managing Microsoft SQL Server components.                                  |
|                        | DBeaver                          | Universal database management tool supporting various databases with a user-friendly interface.   |
| **Third-Party Clouds** | Adminer                          | Lightweight, full-featured database management tool deployable as a single PHP file.              |
|                        | HeidiSQL                         | Open-source tool for managing MySQL, MariaDB, and SQL Server databases.                           |
| **Azure**              | Azure Data Studio                | Cross-platform database tool with modern editor experience and integrated terminal.               |
|                        | Azure SQL Managed Instance       | Fully managed PaaS database offering with a free trial for 12 months.                             |

## On-Premises Tools

### **SQL Server Management Studio (SSMS)**
**Description:** A comprehensive tool for managing Microsoft SQL Server components.
**Step-by-Step Instructions:**
1. **Download and Install:**
   - Go to the [SQL Server Management Studio download page](https://docs.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms).
   - Click on the download link and run the installer.
   - Follow the installation prompts to complete the setup.
2. **Connect to a Server:**
   - Open SSMS and click on "Connect" in the Object Explorer.
   - Enter your server name and authentication details.
3. **Manage Databases:**
   - Use the Object Explorer to navigate and manage your databases.
   - Right-click on databases to create new ones, run queries, or perform other management tasks[^20^]²¹.

### **DBeaver**
**Description:** A universal database management tool supporting various databases with a user-friendly interface.
**Step-by-Step Instructions:**
1. **Download and Install:**
   - Visit the [DBeaver download page](https://dbeaver.io/download/).
   - Choose the appropriate version for your operating system and install it.
2. **Create a Database Connection:**
   - Open DBeaver and click on "New Database Connection."
   - Select your database type and enter the connection details.
3. **Run SQL Queries:**
   - Use the SQL Editor to write and execute queries.
   - View results in the results pane²⁴²⁵.

## Third-Party Clouds

### **Adminer**
**Description:** A lightweight, full-featured database management tool deployable as a single PHP file.
**Step-by-Step Instructions:**
1. **Download Adminer:**
   - Download the latest version from the [Adminer website](https://www.adminer.org/).
2. **Deploy Adminer:**
   - Upload the PHP file to your web server.
   - Access it via your web browser.
3. **Connect to a Database:**
   - Enter your database connection details on the Adminer login page.
   - Manage your database through the Adminer interface¹⁴¹⁵.

### **HeidiSQL**
**Description:** An open-source tool for managing MySQL, MariaDB, and SQL Server databases.
**Step-by-Step Instructions:**
1. **Download and Install:**
   - Go to the [HeidiSQL download page](https://www.heidisql.com/download.php).
   - Download and run the installer.
2. **Create a New Session:**
   - Open HeidiSQL and click on "New" to create a new session.
   - Enter your database connection details.
3. **Manage Databases:**
   - Use the interface to browse, query, and manage your databases⁵⁶.

## Azure Tools

### **Azure Data Studio**
**Description:** A cross-platform database tool with a modern editor experience and integrated terminal.
**Step-by-Step Instructions:**
1. **Download and Install:**
   - Download Azure Data Studio from the [official website](https://docs.microsoft.com/en-us/sql/azure-data-studio/download-azure-data-studio).
   - Follow the installation instructions for your operating system.
2. **Connect to a Database:**
   - Open Azure Data Studio and click on "New Connection."
   - Enter your database connection details.
3. **Use the Editor:**
   - Write and execute SQL queries in the editor.
   - View results and manage your database[^20^].

### **Azure SQL Managed Instance**
**Description:** A fully managed PaaS database offering with a free trial for 12 months.
**Step-by-Step Instructions:**
1. **Create an Azure Account:**
   - Sign up for a free Azure account at [Azure Free Account](https://azure.microsoft.com/en-us/free/).
2. **Create a SQL Managed Instance:**
   - Go to the Azure portal and navigate to "SQL Managed Instances."
   - Click on "Create" and follow the prompts to set up your instance.
3. **Connect and Manage:**
   - Use Azure Data Studio or SSMS to connect to your managed instance.
   - Perform database management tasks as needed[^20^].



(1) Your Step-by-Step Guide to SQL Server Management Studio (SSMS). https://adamtheautomator.com/sql-server-management-studio/.
(2) SQL Server Management Studio - A step-by-step installation guide. https://www.sqlshack.com/sql-server-management-studio-step-step-installation-guide/.
(3) DBeaver Tutorial - How to Use DBeaver (SQL Editor). https://www.youtube.com/watch?v=LEx96-CkB1Q.
(4) How to Download and Install DBeaver on Windows | Step-by-Step Guide 📥. https://www.youtube.com/watch?v=BMGdkmWOvNY.
(5) How to Install Adminer on Your Synology NAS – Marius Hosting. https://mariushosting.com/how-to-install-adminer-on-your-synology-nas/.
(6) How to Use Adminer to Manage Databases Easily with a Single ... - Kinsta. https://kinsta.com/blog/adminer/.
(7) HeidiSQL Tutorial 02 :- How to install HeidiSQL. https://www.youtube.com/watch?v=qo0XTfq52cU.
(8) Tutorial HeidiSQL with MariaDB and MySQL Part 1 Installation. https://www.youtube.com/watch?v=11vhRYEfHNE.
(9) 17 Best Step-By-Step Guide Creation Tools for 2024 - Paperform Blog. https://paperform.co/blog/best-step-by-step-guide-creation-tools/.
(10) How to Create Step-by-Step Instructional Guides (2024) - Whatfix. https://whatfix.com/blog/step-by-step-instructions/.
(11) How to Create Step-By-Step Instructions? - TechSmith. https://www.techsmith.com/blog/create-instructions-using-visuals/.
(12) HeidiSQL: Step by Step Guide to Exporting a Database. https://www.youtube.com/watch?v=J4VgnoWHFo4.
(13) Technical help document - HeidiSQL. https://www.heidisql.com/help.php.
(14) How to Use HeidiSQL to Connect to a MySQL Database - Hostinger. https://www.hostinger.com/tutorials/heidisql-remote-mysql-connection.
(15) How to use HeidiSQL on Hypernode — Docs dev documentation. https://docs.hypernode.com/best-practices/database/how-to-use-heidisql-on-hypernode.html.
(16) Getting set up with Heidi SQL for Windows - wiki.ice-d.org. https://wiki.ice-d.org/_media/applications:heidisql_set_up.pdf.
(17) How to install Adminer (Database Administration Tool) on Ubuntu 22.04 | VPS Tutorial. https://www.youtube.com/watch?v=r4keak825B4.
(18) How To Make Yourself An Administrator In Windows 10. https://www.youtube.com/watch?v=9ookuz2fCns.
(19) How to open database in Adminer | Database management in a single PHP file.. https://www.youtube.com/watch?v=Q-gkCjcNaX0.
(20) How to Give Administrator Permission in Windows 10: A Step-by-Step Guide. https://www.supportyourtech.com/articles/how-to-give-administrator-permission-in-windows-10-a-step-by-step-guide/.
(21) Step-by-Step Guide: Installing SQL Server 2022 and SQL Server Management Studio (SSMS) 19. https://www.youtube.com/watch?v=UnG2UPl8t-4.
(22) SSMS Tutorial (SQL Server Management Studio) - Feature Demonstration. https://www.youtube.com/watch?v=2VQMI4ZvtA4.
(23) How to Install SQL Server Management Studio (SSMS) Step by Step -SQL Server / T-SQL Tutorial Part 1. https://www.youtube.com/watch?v=SUcC4DZWwKY.
(24) How to Use Microsoft SQL Server Management Studio (SSMS) - Process Street. https://bing.com/search?q=step+by+step+instructions+for+SQL+Server+Management+Studio+%28SSMS%29.
(25) SSMS components and configuration - SQL Server Management Studio (SSMS .... https://learn.microsoft.com/en-us/sql/ssms/tutorials/ssms-configuration?view=sql-server-ver16.
(26) How to use SQLite on DBeaver - Step by Step -. https://www.youtube.com/watch?v=aBRmQlQu5qw.
(27) DBeaver user guide. https://dbeaver.com/wp-content/uploads/wikidocs_archive/dbeaver_v_21_2.pdf.
(28) DBeaver Documentation. https://dbeaver.com/docs/dbeaver/.
(29) Getting started · dbeaver/dbeaver Wiki - GitHub. https://github.com/dbeaver/dbeaver/wiki/Getting-started/Installation.
(30) Connect PostgreSQL Database with DBeaver: Step-by-Step Guide - Toolify. https://www.toolify.ai/ai-news/connect-postgresql-database-with-dbeaver-stepbystep-guide-924307.
(31) undefined. https://dbeaver.io/download/.
(32) undefined. https://github.com/vrana/adminer/releases/download/v4.7.8/adminer-4.7.8.php.
(33) undefined. https://www.heidisql.com/download.php.



