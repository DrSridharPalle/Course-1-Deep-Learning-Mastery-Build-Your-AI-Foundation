#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt
def plot_history(history,metric): 
    train_mae = history.history[metric]
    val_mae = history.history["val_"+metric]
    
    train_loss = history.history["loss"]
    val_loss = history.history["val_loss"]
    
    epochs = range(1, len(train_mae) + 1)
    plt.plot(epochs, train_mae, marker="o", label="Train: " + metric)
    plt.plot(epochs, val_mae, marker="*", label="Validation: " + metric)
    plt.title("Training and Validation:" + metric.upper())
    plt.legend()
    
    plt.figure()
    plt.plot(epochs, train_loss, marker="o", label="Training loss")
    plt.plot(epochs, val_loss, marker="*", label="Validation loss")
    plt.title("Training and Validation: Loss")
    plt.legend()
    plt.show()


# In[ ]:




