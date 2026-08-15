from etl_scripts.metadata_etl.src.extract_clean_metadata import extract_metadata_from_aozora


def test_extract_metadata_from_aozora():
    csv_data = extract_metadata_from_aozora("https://www.aozora.gr.jp/index_pages/download_zip.php")
    assert csv_data is not None


