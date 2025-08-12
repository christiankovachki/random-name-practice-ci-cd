import os
from pathlib import Path


class FileHelper:

    @staticmethod
    def get_upload_path(file_name: str, subfolder: str = "") -> str:
        base_dir = os.getenv("UPLOAD_FILES_BASE_DIR", str(Path(__file__).parent.parent / "uploads"))
        full_path = Path(base_dir) / subfolder / file_name

        if not full_path.exists():
            raise FileNotFoundError(f"Upload file not found at: {full_path}")

        return str(full_path.resolve())
