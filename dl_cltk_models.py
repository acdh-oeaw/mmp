from cltk.dependency.stanza import StanzaWrapper
from cltk.data.fetch import FetchCorpus


def download_stanza_model(iso_code):
    StanzaWrapper(language=iso_code, interactive=False, silent=False)
    print(f"Finished downloading Stanza for '{iso_code}'.")


def download_cltk_models_repo(iso_code):
    """Download CLTK repos."""
    print(f"Going to download CLTK models for '{iso_code}'.")
    corpus_downloader = FetchCorpus(language=iso_code)
    corpus_downloader.import_corpus(corpus_name=f"{iso_code}_models_cltk")
    if iso_code == "lat":
        corpus_downloader.import_corpus(corpus_name="cltk_lat_lewis_elementary_lexicon")
    print(f"Finished downloading CLTK models for '{iso_code}'.")


if __name__ == "__main__":
    iso_code = 'lat'
    download_cltk_models_repo(iso_code)
    download_stanza_model(iso_code)
