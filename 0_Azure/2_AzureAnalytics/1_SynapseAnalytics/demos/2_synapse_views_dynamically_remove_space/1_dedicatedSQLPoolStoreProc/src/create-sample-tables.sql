 -- Create sample tables with spaces in names
    CREATE TABLE [Employee Records] (
        [Employee ID] INT,
        [Employee Name] NVARCHAR(255),
        [Employee Address] NVARCHAR(255)
    );

    CREATE TABLE [Sales Data] (
        [Sale ID] INT,
        [Sale Date] DATE,
        [Employee ID] INT,
        [Sale Amount] DECIMAL(10, 2)
    );

    CREATE TABLE [Inventory Details] (
        [Item ID] INT,
        [Item Name] NVARCHAR(255),
        [Item Category] NVARCHAR(255),
        [Item Price] DECIMAL(10, 2)
    );

    -- Insert sample data into the tables
    INSERT INTO [Employee Records] ([Employee ID], [Employee Name], [Employee Address])
    VALUES (1, 'Alice Johnson', '789 Pine St');

    INSERT INTO [Employee Records] ([Employee ID], [Employee Name], [Employee Address])
    VALUES (2, 'Bob Brown', '101 Maple St');

    INSERT INTO [Sales Data] ([Sale ID], [Sale Date], [Employee ID], [Sale Amount])
    VALUES (1, '2023-02-01', 1, 200.00);

    INSERT INTO [Sales Data] ([Sale ID], [Sale Date], [Employee ID], [Sale Amount])
    VALUES (2, '2023-02-02', 2, 250.00);

    INSERT INTO [Inventory Details] ([Item ID], [Item Name], [Item Category], [Item Price])
    VALUES (1, 'Gadget', 'Electronics', 49.99);

    INSERT INTO [Inventory Details] ([Item ID], [Item Name], [Item Category], [Item Price])
    VALUES (2, 'Tool', 'Hardware', 29.99);