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
            


