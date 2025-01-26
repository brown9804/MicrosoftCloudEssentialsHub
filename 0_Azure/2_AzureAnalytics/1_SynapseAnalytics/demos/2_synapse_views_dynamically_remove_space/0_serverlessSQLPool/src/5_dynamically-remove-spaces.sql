-- Create a temporary table to store the dynamic SQL statements
CREATE TABLE #CreateViewStatements (SQLStatement NVARCHAR(MAX), RowNum INT);

-- Insert dynamic SQL statements for each table with a row number
INSERT INTO #CreateViewStatements (SQLStatement, RowNum)
SELECT 
    'CREATE VIEW ' + QUOTENAME(REPLACE(TABLE_NAME, ' ', '_')) + ' AS SELECT ' +
    STRING_AGG('[' + COLUMN_NAME + '] AS [' + REPLACE(COLUMN_NAME, ' ', '') + ']', ', ') +
    ' FROM ' + QUOTENAME(TABLE_NAME),
    ROW_NUMBER() OVER (ORDER BY TABLE_NAME)
FROM INFORMATION_SCHEMA.COLUMNS
GROUP BY TABLE_NAME;

-- Declare variables to hold the SQL statement and row number
DECLARE @sql NVARCHAR(MAX);
DECLARE @rowNum INT = 1;
DECLARE @maxRowNum INT;

-- Get the maximum row number
SELECT @maxRowNum = MAX(RowNum) FROM #CreateViewStatements;

-- Loop through the temporary table and execute each SQL statement
WHILE @rowNum <= @maxRowNum
BEGIN
    -- Get the next SQL statement
    SELECT @sql = SQLStatement FROM #CreateViewStatements WHERE RowNum = @rowNum;

    -- Execute the SQL statement
    EXEC sp_executesql @sql;

    -- Increment the row number
    SET @rowNum = @rowNum + 1;
END;

-- Drop the temporary table
DROP TABLE #CreateViewStatements;