import pandas as pd
from sqlalchemy import create_engine
from faker import Faker
import random

fake = Faker()
# Conexão com PostgreSQL (localhost:5432)
engine = create_engine('postgresql://superset_user:superset_password@localhost:5432/generic_pilot_db')

def generate_sample_data(n=300):
    categories = ['Hardware', 'Software', 'Cloud', 'Support']
    statuses = ['Success', 'Warning', 'Error', 'Pending']
    
    data = [{
        'id': i,
        'item_name': f"Resource_{i:03d}",
        'category': random.choice(categories),
        'status': random.choice(statuses),
        'value': round(random.uniform(10.0, 1000.0), 2),
        'load_percentage': random.randint(0, 100),
        'created_at': fake.date_time_between(start_date='-30d', end_date='now')
    } for i in range(1, n + 1)]
    
    return pd.DataFrame(data)

try:
    df = generate_sample_data()
    df.to_sql('pilot_metrics', con=engine, if_exists='replace', index=False)
    print("✅ Sample data successfully inserted into PostgreSQL!")
except Exception as e:
    print(f"❌ Error inserting data: {e}")