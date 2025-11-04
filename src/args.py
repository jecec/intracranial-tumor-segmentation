import argparse

def get_args():
    parser = argparse.ArgumentParser(description='Argument Parser for global arguments')
    parser.add_argument('-data_dir', type=str, default="data/raw/segmentation_task")
    parser.add_argument('-output_dir', type=str, default="output/CSVs")

    parser.add_argument('-folds', type=int, default=5)
    parser.add_argument('-train_size', type=float, default=0.8)

    parser.add_argument('-seed', type=int, default=28)
    args =parser.parse_args()

    return args