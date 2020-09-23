import os
import wget

bs_cache_home = os.path.expanduser(
    os.getenv("BS_HOME", os.path.join(os.getenv("XDG_CACHE_HOME", "~/.cache"), "bertserini"))
)

default_datasets_cache_path = os.path.join(bs_cache_home, "datasets")

try:
    from pathlib import Path

    BS_DATASETS_CACHE = Path(os.getenv("BS_DATASETS_CACHE", default_datasets_cache_path))
except (AttributeError, ImportError):
    BS_DATASETS_CACHE = os.getenv(os.getenv("HF_DATASETS_CACHE", default_datasets_cache_path))

dataset_dict = {
    "squad" : {"_URL": "https://rajpurkar.github.io/SQuAD-explorer/dataset/",
               "_DEV_FILE": "dev-v1.1.json",
               "_TRAINING_FILE": "train-v1.1.json"},
    "cmrc2018" : {"_URL": "https://github.com/ymcui/cmrc2018",
               "_DEV_FILE": "https://worksheets.codalab.org/rest/bundles/0x72252619f67b4346a85e122049c3eabd/contents/blob/",
               "_TRAINING_FILE": "https://worksheets.codalab.org/rest/bundles/0x15022f0c4d3944a599ab27256686b9ac/contents/blob/",
               "_TEST_FILE": "https://worksheets.codalab.org/rest/bundles/0x182c2e71fac94fc2a45cc1a3376879f7/contents/blob/"},
    }

def get_urls_to_download(data_name):
    url_dict = dataset_dict.get(data_name)
    if data_name == "squad":
        urls_to_download = {
            "train": os.path.join(url_dict.get("_URL"), url_dict.get("_TRAINING_FILE")),
            "dev": os.path.join(url_dict.get("_URL"), url_dict.get("_DEV_FILE")),
        }
    elif data_name == "cmrc2018":
        urls_to_download = {"train": url_dict.get("_TRAIN_FILE"), "dev": url_dict.get("_DEV_FILE"), "test": url_dict.get("_TEST_FILE")}
    return urls_to_download

#return file address
def url_download(data_name, split, force=False):
    urls_to_download = get_urls_to_download(data_name)
    split_url = urls_to_download[split]
    cache_dir = str(BS_DATASETS_CACHE)
    split_name = "{}_{}.json".format(data_name, split)
    split_file = os.path.join(cache_dir, split_name)
    #check if in cache
    if not os.path.isdir(cache_dir):
        os.makedirs(cache_dir)

    if force:
        os.remove(split_file)

    if not os.path.isfile(split_file):
        wget.download(split_url, split_file)

    return split_file


def download(file_or_name):
    if (file_or_name is not None) and (not os.path.exists(file_or_name)):
        data_name, split = file_or_name.split("-")
        url_download(data_name, split)

