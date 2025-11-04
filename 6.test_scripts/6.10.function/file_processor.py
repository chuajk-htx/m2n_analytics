import tkinter as tk
from tkinter.filedialog import askdirectory
import pandas as pd
import glob
import gc
from sqlalchemy import create_engine

class FileProcessor:
    def __init__(self):
        """Initialize variables"""
        self.folder_path = None
        self.engine = create_engine("mariadb://root:yourpassword@127.0.0.1:3306/inspectorate_implementation")
    
    def browse_button(self):
        """Allow user to select a folder and store its path in the class"""
        root = tk.Tk()
        root.withdraw()
        root.wm_attributes('-topmost', 1)
        
        self.folder_path = askdirectory(title='Select Matching Score Folder')
        if not self.folder_path:
            raise Exception("No folder selected.")
        
        print(f"Selected folder: {self.folder_path}")
    
    def processing(self):
        """Process TXT files and store results in SQL"""
        if not self.folder_path:
            raise Exception("Please select a folder first using the browse button.")
        
        all_data = []
        for file_path in glob.glob(f"{self.folder_path}/*.txt"):
            print(f"Reading: {file_path}")
            
            with open(file_path, 'r') as f:
                for line in f:
                    values = line.strip().split(',')
                    for value in values:
                        id1 = value[:7]
                        id2 = value[7:14]
                        score = float(value[14:18])  

                        all_data.append({'ID1': id1, 'ID2': id2, 'Matching Score': score})

        df_all_data = pd.DataFrame(all_data)
        df_all_data.to_sql('compiled_matching_scores', con=self.engine, index=False, if_exists='replace')

        print("Data processing complete.")
        gc.collect()

processor = FileProcessor()  # Create an instance for the object
processor.browse_button()  # Select folder, bind to button
processor.processing()  # Process files, either with second button or automatically after the browse_button has been completed