import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

csv_file = "./history_01_01.csv"
history_df = pd.read_csv(csv_file)

history_df[['train_loss', 'val_loss']].plot()
plt.grid()
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.savefig('loss_01_01')

plt.close()
history_df[['train_accuracy', 'val_accuracy']].plot()
plt.grid()
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.savefig('acc_01_01')
