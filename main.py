from datasets import load_dataset

ds = load_dataset("ag_news")

# Filter to SPORTS only (label == 1)
sports_train = ds["train"].filter(lambda x: x["label"] == 1)
sports_test  = ds["test"].filter(lambda x: x["label"] == 1)

print("Sports train rows:", len(sports_train))
print("Sports test rows:", len(sports_test))

print("\nSample:")
print(sports_train[0])