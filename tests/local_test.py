from etl_scripts.metadata_etl.src.extract_clean_metadata import extract_metadata_from_aozora


def test_extract_metadata_from_aozora():
    csv_data = extract_metadata_from_aozora("https://www.aozora.gr.jp/index_pages/list_person_all_utf8.zip")
    assert csv_data is not None


