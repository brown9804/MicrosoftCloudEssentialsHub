CREATE PROCEDURE RemoveSpacesFromColumnNames
AS
BEGIN
    DECLARE @tableName NVARCHAR(255)
    DECLARE @columnName NVARCHAR(255)
    DECLARE @sql NVARCHAR(MAX)

    -- Temporary table to store table names
    CREATE TABLE #TableNames (TABLE_NAME NVARCHAR(255))
    INSERT INTO #TableNames
    SELECT TABLE_NAME
    FROM INFORMATION_SCHEMA.TABLES
    WHERE TABLE_TYPE = 'BASE TABLE' AND TABLE_SCHEMA = 'dbo'

    -- Loop through each table
    WHILE EXISTS (SELECT 1 FROM #TableNames)
    BEGIN
        SELECT TOP 1 @tableName = TABLE_NAME FROM #TableNames

        -- Print the table name for debugging
        PRINT 'Processing table: ' + @tableName

        SET @sql = 'CREATE VIEW dbo.vw' + REPLACE(@tableName, ' ', '') + ' AS SELECT '

        -- Drop the temporary table if it exists
        IF OBJECT_ID('tempdb..#ColumnNames') IS NOT NULL
            DROP TABLE #ColumnNames

        -- Temporary table to store column names
        CREATE TABLE #ColumnNames (COLUMN_NAME NVARCHAR(255))
        INSERT INTO #ColumnNames
        SELECT COLUMN_NAME
        FROM INFORMATION_SCHEMA.COLUMNS
        WHERE TABLE_NAME = @tableName

        -- Loop through each column
        WHILE EXISTS (SELECT 1 FROM #ColumnNames)
        BEGIN
            SELECT TOP 1 @columnName = COLUMN_NAME FROM #ColumnNames

            -- Print the column name for debugging
            PRINT 'Processing column: ' + @columnName

            -- Remove all spaces from column names
            IF (SELECT COUNT(*) FROM #ColumnNames) = 1
            BEGIN
                SET @sql = @sql + 'REPLACE([' + @columnName + '], '' '', '''') AS [' + REPLACE(@columnName, ' ', '') + '] '
            END
            ELSE
            BEGIN
                SET @sql = @sql + 'REPLACE([' + @columnName + '], '' '', '''') AS [' + REPLACE(@columnName, ' ', '') + '], '
            END

            DELETE FROM #ColumnNames WHERE COLUMN_NAME = @columnName
        END

        -- Remove the trailing comma and space if any
        IF RIGHT(@sql, 2) = ', '
        BEGIN
            SET @sql = LEFT(@sql, LEN(@sql) - 2)
        END

        SET @sql = @sql + ' FROM [' + @tableName + '];'

        -- Print the dynamic SQL for debugging
        PRINT 'Generated SQL: ' + @sql

        -- Execute the dynamic SQL
        BEGIN TRY
            EXEC sp_executesql @sql
        END TRY
        BEGIN CATCH
            PRINT 'Error: ' + ERROR_MESSAGE()
        END CATCH

        DELETE FROM #TableNames WHERE TABLE_NAME = @tableName
    END

    -- Clean up temporary tables
    DROP TABLE #TableNames
    DROP TABLE #ColumnNames
END