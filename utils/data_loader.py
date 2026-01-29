"""
Data loading utilities for business operations data.
Handles CSV parsing, type conversion, and basic error handling.
"""

import pandas as pd
from pathlib import Path
from typing import Tuple, Optional
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__) #name of the file 

class DataLoader:
    """Centralized data loading with error handling"""

    def __init__(self, data_dir: str = "data"):
        self.data_dir = Path(data_dir)
    
    def load_tasks(self) -> pd.DataFrame:
        """
        Load task tracker data

        Returns:
            DataFrame with tasks, or empty DataFrame if file is missing
        """

        # fetch task csv from the data dir
        tasks_path = self.data_dir/ "task.csv"
        # error handling, checking if the file exists
        try: 
            df = pd.read_csv(tasks_path)
            logger.info(f"Loaded {len(df)} tasks from {tasks_path}")

            # Convert data columns to datetime, coerce errors to NaT
            data_columns = ['due_date', 'last_followup']
            for col in data_columns:
                if col in df.columns:
                    df[col] = pd.to_datatime(df[col], errors = 'coerce')

            return  df

        except FileNotFoundError:
            logger.error(f"Tasks file not found: {tasks_path}")

            return pd.DataFrame
        
        except Exception as e:
            logger.error(f"Error loading tasks: {str(e)}")

            return pd.DataFrame()
        
    
    def load_sales(self) -> pd.DataFrame:

        """
        Loads sales data 

        if empty returns empty DataFrame 
        """
        
        sales_path = self.data_dir/"sales.csv"

        try:
            df = pd.read_csv(sales_path)
            logger.info(f"Loaded {len(df)} sales leads from {sales_path}")

            # Convert created_data to datetime
            if 'created_date' in df.columns:
                
                df['create_date'] = pd.to_datetime(df['created_date'], errors='coerce')


            # Convert value to numeric, coerce erros to Nan
            if 'value' in df:
                df['value'] = pd.to_numeric(df['value'], errors = 'coerce')

            return df
        

        except FileNotFoundError:
            logger.error(f"Sales file not found in: {sales_path}")

            return pd.DataFrame
        
        except Exception as e:
            logger.error(f"Error loading sales: {str(e)}")
            return pd.DataFrame
        

    def load_documents(self) -> str:
        """
         Load SOP documentation.
        
        Returns:
            Document content as string, or empty string if file missing
        
        """

        docs_path = self.data_dir/ "docs" / "sop.md"

        try: 
            with open(docs_path, 'r', encoding='utf-8'):
                content = f.read()

            logger.info(f"Loaded SOP document from {docs_path}")
            return content
        
        except FileNotFoundError:
            logger.error(f"File not found in {docs_path}")
            return ""

        except Exception as e:
            logger.error(f"An exeption occured: {str(e)}")

            return ""

    def load_all(self) -> Tuple[pd.DataFrame, pd.DataFrame, str]:
        """
        Load all data sources.
        
        Returns:
            Tuple of (tasks_df, sales_df, sop_content)
        """
        tasks = self.load_tasks()
        sales = self.load_sales()
        docs = self.load_documents()
        
        return tasks, sales, docs
    

def get_current_data() -> pd.Timestamp:
    """
    Get current date for business logic.
    In production, this would use datetime.now()
    For testing, we use a fixed date matching the data.
    
    Returns:
        Current date as pandas Timestamp
    """
    # Fixed date for testing (matching README current date)
    return pd.Timestamp('2026-01-20')


if __name__ == "__main__":
    # Test data loading
    loader = DataLoader()
    tasks_df, sales_df, sop = loader.load_all()
    
    print(f"\nTasks loaded: {len(tasks_df)} rows")
    print(f"Sales loaded: {len(sales_df)} rows")
    print(f"SOP loaded: {len(sop)} characters")
    
    print("\nTask columns:", tasks_df.columns.tolist())
    print("Sales columns:", sales_df.columns.tolist())
    