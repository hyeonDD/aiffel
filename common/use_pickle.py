import pickle
import gzip


def save_pikle_gzip(obj: object, file_name: str):
    """
    obj -> pickle gzip 저장용
    """
    with gzip.open(f'{file_name}.pickle.gz', 'wb') as f:
        pickle.dump(obj, f)


def load_pikle_gzip(file_name: str):
    """
    pickle gzip -> obj load용
    """
    with gzip.open(f'{file_name}.pickle.gz', 'rb') as f:
        load_pickle = pickle.load(f)
    return load_pickle
