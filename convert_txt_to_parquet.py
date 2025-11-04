import polars as pl
from pathlib import Path
from tqdm import tqdm
import pyarrow as pa
import pyarrow.parquet as pq
import sys

def parse_record(record: str):
    """ Parses 28 characters record"""
    record = record.strip()
    if len(record) != 28:
        print(f"Invalid record length: {len(record)} for record: {record}", file=sys.stderr)
        return None
    try:
        return {
            "uid_enrolled": record[0:8],
            "gender_enrolled": record[8],
            "ctycode_enrolled": record[9:12],
            "agegroup_enrolled": record[12],
            "uid_probe": record[12:19],
            "gender_probe": record[19],
            "ctycode_probe": record[20:23],
            "agegroup_probe": record[23],
            "matching_result": int(record[24:28])
        }
    except Exception as e:
        print(f"Error parsing record: {record} with error: {e}", file=sys.stderr)
        return None
        
    
def convert_txt_to_parquet(input_file, output_file):
    """ Converts a TXT file to a Parquet file using Polars."""
    print(f"Processing {input_file} ...")
    
    with open(input_file, 'r', encoding='utf-8') as file:
        content : str = file.read()
        records : list[str] = content.split(',')
        
    print(f"Parsing {len(records)} records...")
    
    # Parse all records
    parsed_records = [];
    for record in tqdm(records, desc="Parsing records"):
        if parse_record(record) is not None:
            parsed_records.append(parse_record(record))
    df = pl.DataFrame(parsed_records, schema={
        "uid_enrolled": pl.Utf8,
        "gender_enrolled": pl.Utf8,
        "ctycode_enrolled": pl.Utf8,
        "agegroup_enrolled": pl.Utf8,
        "uid_probe": pl.Utf8,
        "gender_probe": pl.Utf8,
        "ctycode_probe": pl.Utf8,
        "agegroup_probe": pl.Utf8,
        "matching_result": pl.Int32})
    
    #table = pa.Table.from_pandas(df.to_pandas())
    #pq.write_table(table,
    #                 output_file,
    #                 compression="gzip",
    #                 compression_level=22,
    #                 use_dictionary=True,
    #                 data_page_version="2.0",
    #                 )
    
    df.write_parquet(
        output_file, 
        compression="zstd",
        compression_level=22,
        use_pyarrow=True,
        statistics=True,
        row_group_size=100000,
        data_page_size=1024*1024
        )
    
    print(f"Parquet file saved to {output_file}")
    return len(parsed_records)
    
def batch_convert_txt_to_parquet(input_dir: str, output_dir: str):
    """ Batch converts all TXT files in a directory to Parquet files. """
    input_path = Path(input_dir)
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    txt_files = list(input_path.glob("*.txt"))
    print(f"Found {len(txt_files)} TXT files to convert.")
    total = 0
    for txt_file in tqdm(txt_files, desc="Converting files"):
        parquet_file = output_path / (txt_file.stem + ".parquet")
        count = convert_txt_to_parquet(txt_file, parquet_file)
        total += count
    print(f"Total records converted: {total}")

if __name__ == "__main__":
    if(len(sys.argv) != 3):
        print("Usage: python convert_txt_to_parquet.py <input_dir> <output_dir>")
        sys.exit(1)
    input_directory = sys.argv[1]
    output_directory = sys.argv[2]
    batch_convert_txt_to_parquet(input_directory, output_directory)


        