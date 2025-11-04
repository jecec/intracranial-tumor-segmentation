from args import get_args
from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split, StratifiedKFold

args = get_args()
images = []
masks = []


for split in Path(args.data_dir).iterdir():
    if Path(args.output_dir, f'{split.name}.csv').exists():
        print(f"Skipping metadata creation for split {split.name}")
        continue
    data = []
    for directory in split.iterdir():
        for file in directory.iterdir():
            if file.suffix == '.jpg':
                images.append(str(file))
            elif file.suffix == '.png':
                masks.append(str(file))
        for image, mask in zip(images, masks):
            data.append([image, mask])
        df = pd.DataFrame(data, columns=['image', 'mask'])
        df.to_csv(Path(args.output_dir, f'{split.name}.csv'), index=False)



# TODO: Create SKF splits
df = pd.read_csv(Path(args.output_dir, 'train.csv'))
train, val = train_test_split(df, test_size=0.2, random_state=args.seed)

skf = StratifiedKFold(n_splits=args.folds, random_state=args.seed)

