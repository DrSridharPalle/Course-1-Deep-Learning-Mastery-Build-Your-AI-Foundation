#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt
def plot_history(history): 
    train_accuracy = history.history["accuracy"]
    val_accuracy = history.history["val_accuracy"]
    
    train_loss = history.history["loss"]
    val_loss = history.history["val_loss"]
    
    epochs = range(1, len(train_accuracy) + 1)
    plt.plot(epochs, train_accuracy, "b*", label="Training accuracy")
    plt.plot(epochs, val_accuracy, "b", label="Validation accuracy")
    plt.title("Training and Validation accuracy")
    plt.legend()
    
    plt.figure()
    plt.plot(epochs, train_loss, "r*", label="Training loss")
    plt.plot(epochs, val_loss, "r", label="Validation loss")
    plt.title("Training and Validation loss")
    plt.legend()
    plt.show()


# In[ ]:




