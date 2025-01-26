CREATE EXTERNAL TABLE [Employee Data Test Brown] (
    [Employee ID] INT,
    [Employee Name] NVARCHAR(50),
    [Hire Date] DATE
)
WITH (
    LOCATION = 'employee data with spaces.csv',
    DATA_SOURCE = MyDataSourceNameTest,
    FILE_FORMAT = MyFileFormat
);

CREATE EXTERNAL TABLE [Product Data Test Brown] (
    [Product ID] INT,
    [Product Name] NVARCHAR(50),
    [Release Date] DATE
)
WITH (
    LOCATION = 'product data with spaces.csv',
    DATA_SOURCE = MyDataSourceNameTest,
    FILE_FORMAT = MyFileFormat
);