import polars as pl
from pathlib import Path
from tqdm import tqdm
import sys

def parse_txt_to_polars(input_file_path: Path):
    """
    Reads a TXT file and converts it to a Polars DataFrame.
    Each line in the TXT file is expected to be a comma-separated record."
    
    """
    try:
        print(f"Processing {input_file_path}...")
        
        with open(input_file_path, 'r', encoding='utf-8') as file:
            content : str = file.read()
            records : list[str] = content.split(',')
        print(f"Total records found: {len(records)}")
        
        # Parse records into lists
        data = {
            "uid_probe": [],
            "gender_probe": [],
            "country_probe": [],
            "age_group_probe": [],
            "uid_enrolled": [],
            "gender_enrolled": [],
            "country_enrolled": [],
            "age_group_enrolled": [],
            "match_score": []
        }
        for record in tqdm(records, desc="Parsing records"):
            record = record.strip()
            if len(record) != 27:
                print(f"Skipping malformed record: {record}")
                continue
            
            data["uid_probe"].append(record[0:7])
            data["gender_probe"].append(record[7])
            data["country_probe"].append(record[8:11])
            data["age_group_probe"].append(int(record[11]))
            data["uid_enrolled"].append(record[12:19])  
            data["gender_enrolled"].append(record[19])
            data["country_enrolled"].append(record[20:23])
            data["age_group_enrolled"].append(int(record[23]))
            data["match_score"].append(int(record[24:28]))
        df = pl.DataFrame(data, schema={
            'uid_probe': pl.UInt32,
            'gender_probe': pl.Utf8,
            'country_probe': pl.Utf8,
            'age_group_probe': pl.UInt8,
            'uid_enrolled': pl.UInt32,
            'gender_enrolled': pl.Utf8,
            'country_enrolled': pl.Utf8,
            'age_group_enrolled': pl.UInt8,
            'match_score': pl.UInt16  
        })
        return df
    except Exception as e:
        print(f"Error reading TXT file: {e}")
        sys.exit(1)

def convert_txt_to_parquet(input_file, output_file):
    df =parse_txt_to_polars(input_file)
    output_file_path = Path(output_file)
    output_file_path.parent.mkdir(parents=True, exist_ok=True)
    df.write_parquet(
            output_file_path,
            compression='zstd',
            compression_level=7,
            statistics=True
        )
    print(f"Parquet file saved at: {output_file_path}")
    return len