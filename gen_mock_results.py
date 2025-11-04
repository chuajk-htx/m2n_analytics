import os
import random
from tqdm import tqdm


def get_padded_int_str(min: int, max : int):
    if min < 0 or max < 0:
        error_msg = f"min and max values must be more than 0"
        return error_msg
    else:
        random_int = random.randint(min,max)
        width : int = len(str(max))
        value : str = f"{random_int:0{width}d}"
        return value

def get_uid() -> str:
    min : int = 1
    max : int = 1500000
    return get_padded_int_str(min, max)

def get_biographics() -> str:
    genders : list[str] = ["M","F"]
    gender = random.choice(genders)
    nationalities : list[str] = ["MYS","SGD","IND","THA"]
    nationality = random.choice(nationalities)
    age_groups : list[int] = [1,2,3,4,5]
    age_group = random.choice(age_groups)
    return f"{gender}{nationality}{age_group}"

def get_matching_results() -> str:
    min : int = 0
    max : int = 9999
    return get_padded_int_str(min, max)

def create_mock_data(delimiter: str = ",", filepath: str = "mock_matching_results.txt") -> None:
    max_bytes_size : int = 10*10**6  # 10 MB
    if os.path.exists(filepath):
        os.remove(filepath)
    try:
        total_bytes_size = 0
        progress_bar = tqdm(total=max_bytes_size, unit="B", unit_scale=True, desc="Generating mock data")
        with open(filepath,'a') as file:
            while total_bytes_size < max_bytes_size:
                uid_probe = get_uid()
                biographics_probe = get_biographics()
                uid_enrolled = get_uid()
                biographics_enrolled = get_biographics()
                match_result = get_matching_results()
                record = f"{uid_probe}{biographics_probe}{uid_enrolled}{biographics_enrolled}{match_result}"
                entry =  f"{delimiter}{record}" if total_bytes_size > 0 else record
                file.write(entry)
                total_bytes_size += len(entry.encode('utf-8'))
                progress_bar.update(len(entry.encode('utf-8')))
        #progress_bar.close()
        print(f"Mock data generation completed. File saved at: {filepath}")

    except FileNotFoundError as filepath_error:
        print(f"filepath not defined: {filepath_error}")
    except Exception as e:
        print(f"Exception: {e}")

if __name__ == "__main__":
    delimiter = ","
    create_mock_data(delimiter=delimiter, filepath="../mock_matching_scores.txt")
    


    





