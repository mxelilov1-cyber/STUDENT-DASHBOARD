# SQL Server bağlantı parametrləri
SERVER_NAME = "localhost"  # Və ya kompüterinizdəki SQL Server adı
DATABASE_NAME = "UniversityDB"
DRIVER_NAME = "{ODBC Driver 17 for SQL Server}"

DB_CONNECTION_STRING = (
    f"DRIVER={DRIVER_NAME};"
    f"SERVER={SERVER_NAME};"
    f"DATABASE={DATABASE_NAME};"
    f"Trusted_Connection=yes;"
)
