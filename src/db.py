from sqlalchemy import create_engine

DB_USER = "postgres"
DB_PASSWORD = "password"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "quickcommerce"

DATABASE_URL = (
    f"postgresql://{DB_USER}:"
    f"{DB_PASSWORD}@"
    f"{DB_HOST}:{DB_PORT}/"
    f"{DB_NAME}"
)

engine = create_engine(DATABASE_URL)

print("Database Connected Successfully")