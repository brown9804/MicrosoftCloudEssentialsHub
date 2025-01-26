USE MyUserDatabase;

CREATE EXTERNAL DATA SOURCE MyDataSourceNameTest
WITH (
    LOCATION = 'https://brownteststorage.dfs.core.windows.net/sample-tables-container/'
);
