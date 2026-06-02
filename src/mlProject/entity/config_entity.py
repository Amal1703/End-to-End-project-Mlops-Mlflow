from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True) # frozen=True signifie que les instances de la dataclass devient immutable (en lecture seule après sa création, modification des instance non autorisé)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path
    
@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    unzip_data_dir: Path
    STATUS_FILE: str
    all_schema: dict # read the file schema.yaml and save it in a dictionary format

@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_path: Path
    all_schema: dict # read the file schema.yaml and save it in a dictionary format   