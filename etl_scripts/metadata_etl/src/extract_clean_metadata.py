import oci
import io
import zipfile
import requests

def extract_metadata_from_aozora(url: str):
    try:
        print("Extracting metadata from Aozora...")
        response = requests.get(url, timeout=60)
        response.raise_for_status()

        # Open ZIP without writing it to disk
        with zipfile.ZipFile(io.BytesIO(response.content)) as z:

            # Find CSV inside ZIP
            csv_files = [
                name for name in z.namelist()
                if name.lower().endswith(".csv")
            ]

            if not csv_files:
                raise ValueError("No CSV file found inside ZIP")

            csv_name = csv_files[0]

            print(f"Found CSV: {csv_name}")

            # Read CSV as raw bytes
            csv_data = z.read(csv_name)

            return csv_data

    except Exception as e:
        print(f"Error extracting metadata: {e}")
        return None

    finally:
        print("Finished extracting metadata.")
        

def load_metadata_into_bucket(csv_data: bytes, bucket_name: str, namespace: str, object_name: str):
    try:
        print(f"Loading metadata into bucket: {bucket_name}...")

        config = oci.config.from_file()
        object_storage = oci.object_storage.ObjectStorageClient(config)

        object_storage.put_object(
            namespace,
            bucket_name,
            object_name,
            csv_data
        )

    except Exception as e:
        print(f"Error loading metadata into bucket: {e}")
        raise

    finally:
        print("Finished loading metadata into bucket.")

def clean_load_metadata_into_supabase(df):
    pass
