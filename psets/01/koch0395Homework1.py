# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: hydrogen
#       format_version: '1.3'
#       jupytext_version: 1.18.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown] id="ZwHNjZGMqoLW"
# # CSCI 2033: Introduction to Google Colab!
#
# *Inspired by the notebook created by Ryan Diaz (Former TA - Fall 2023)*
#
# This notebook will give you a quick introduction to Google Colab, the services it provides, and some cool things you can do to enhance your coding experience (both in assignments in this class and on your own projects)!
#
# ## **BEFORE YOU BEGIN:**
#
# Save a copy of this notebook by going to `File` -> `Save a copy in Drive` in the top menu bar. You can find the copy in a folder titled `Colab Notebooks` within your Drive (which will be created for you if you don't have one already).
#

# %% [markdown] id="Gv5Ke-cRq_eO"
# # 1. Introduction to Python Notebooks
#
# Colab notebooks are written entirely in the format of Python notebooks, which are a special way of displaying Python code in a more readable and interactive format. Python notebooks aren't unique to Colab (you may have heard of [Jupyter Notebooks](https://jupyter.org/) before), but they are the main format of a Colab notebook, so it is important to know how to use them. In this section, you will learn more about the basics of Python notebooks, how to create content within them, and some helpful tips when it comes to working with Python notebooks.

# %% [markdown] id="FCqT6pNVrWFX"
# ### 1.1 Text Cells
#
# ***
#
# This is a text cell. You can edit it using the Markdown format (a comprehensive tutorial [here](https://www.markdownguide.org/basic-syntax/)). Double-click a text cell (or press `enter` while selecting a text cell) to edit it. You edit the text on the left panel, and you can see the resulting format on the right panel. Here are some common text formats:
#
# *Italic text*
#
# **Bold text**
#
# # Large header
#
# ## Slightly smaller header
#
# ### Smaller header
#
# `Code-style text`
#

# %% [markdown] id="hSpDbT6hdh1i"
# # Below this line, write down what you are looking forward to learning in this class.
#
# Programming Application of matricies; images, videos, mathlab skill etc.

# %% [markdown] id="7KRL5DBZs5nB"
# ### 1.2 Code Cells
# ***

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 301, "status": "ok", "timestamp": 1727101390907, "user": {"displayName": "Bernardo Bianco Prado", "userId": "01223085289308682497"}, "user_tz": 300} id="vH6tM0Q9sM6q" outputId="7bef1cce-7cdd-4a34-f496-568d381ec756"
# <--- Press the play button to run this cell!

import sys

print(f"This is a code cell! Code cells currently run Python version {sys.version}, which may change as Google updates \nthe Colab environment. Any Python code you write here will behave the same way as if you wrote it on any other IDE!")

print("\nFor example:")

example_variable = 999

for i in range(3):
  print(i)

# %% id="l6vd1lcxuU4O"
# Using the Numpy Tutorial, learn how to create a 2 by 2 numpy array
# and create one below. You may choose any values of entries you like
# in it, as long as they are not all zeros.

# After you created your array, print it and run the cell.

import numpy as np

# =========================================================== #
#                     YOUR CODE BELOW                         #
# =========================================================== #

my_array = np.array([[1, 2], [3, 4]])
print("Array \n {}".format(my_array))






# %% [markdown] id="gB2FvE3yxQDm"
# ### 1.3 Context Matters
# ***
#
# All code cells share the same "context", so you can use variables declared in previous code cells in all future code cells. For example, run the below code cell, which seemingly uses a variable that hasn't been declared yet:

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 7, "status": "ok", "timestamp": 1727101391218, "user": {"displayName": "Bernardo Bianco Prado", "userId": "01223085289308682497"}, "user_tz": 300} id="bmyK7PYjyM7J" outputId="b9a4f98a-0fd0-4c93-a94f-d4ee6ec8bd9c"
print(example_variable + 1)

# %% [markdown] id="JkJVKoebynuK"
# Somehow, the code still works! You may have noticed the `example_variable` from the code cell under Section 1.2, and in fact, it is the exact same `example_variable` being used in this code cell!
#
# If the above code cell *didn't* work (it probably gave you the error "`name 'example_variable' is not defined`"), it's because **the code cell under Section 1.2 has not been run yet**. Variables can only be declared if the code cell containing them has already been run. Try running that code cell and then re-running this one, and it should work now. You can tell that a code cell has been run if you see a little green checkmark next to the top left of the cell.
#
# **IMPORTANT:**
#
# It's important to note that if your Colab runtime restarts (this sometimes happens if you reload the webpage of the notebook), all code cells will *reset*, and you'll have to re-run them all again.

# %% [markdown] id="kMC2H6-Qzu-r"
# ### 1.4 Order Matters
#
# ***
#
# Just like how the order of your lines of code matter during execution, the *order in which you run your code cells* also matters. Run the below code cell to change the value of `example_variable`, and then re-run the code cell in Section 1.3.

# %% id="Y1YBz2hvBqwr"
example_variable = 100

# %% [markdown] id="YhcfGKZfChuc"
# You'll see that the value being printed out is now different, and in fact uses the new value of `example_variable` that we had just set.
#
# This is a good example to illustrate that **you don't have to necessarily run all code cells from top to bottom**. Each code cell modifies and adds to the context of the overall notebook. *Every time you run a cell block, it will use the **current** context based on the cells that have already been run.*
#
# &nbsp;
#
#
# That last sentence is especially important. Consider the example of the two code blocks below. Run both `CODE BLOCK 1` and `CODE BLOCK 2` to print out `my_string`.

# %% id="nYVLhkB2EahZ"
# === CODE BLOCK 1 === #

my_string = "Hello World! Im Here..."

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 6, "status": "ok", "timestamp": 1727101391219, "user": {"displayName": "Bernardo Bianco Prado", "userId": "01223085289308682497"}, "user_tz": 300} id="YmG9JwlTEf-d" outputId="a007ee05-2900-479d-8f43-524291f23348"
# === CODE BLOCK 2 === #

print(my_string)

# %% [markdown] id="lyBEMbsIEniB"
# Now, try modifying `my_string` to be something different, and re-run `CODE BLOCK 2` (*without* re-running `CODE BLOCK 1`). You'll see that the output hasn't changed. This is because although `CODE_BLOCK_1` has changed, the *context* that `CODE_BLOCK_2` is running in hasn't changed
#
# If you run `CODE_BLOCK_1` again and then `CODE_BLOCK_2`, the output will now reflect the new value of `my_string`. This leads to a very important tip:
#
# **<center><font size='5'>AFTER CHANGING A CODE CELL, RE-RUN IT!</font></center>**

# %% [markdown] id="Pnmv5X4DGUOy"
# ### 1.5 Inserting, Deleting, and Moving Cells
#
# ***
#
# You can insert code and text cells by clicking the `+ Code` or `+ Text` buttons at the top left of the screen underneath the top menu bar.
#
# Keep in mind that the inserted cells will be placed right after the cell you have selected (or the very bottom if you have none selected), so make sure you know where you want your cell to be. Alternatively, if you hover underneath the cell you want to insert under, the `+ Code` and `+ Text` buttons will automatically appear.
#
#
# To delete cells, press the trash bin icon after selecting the cell you want to delete.
#
#
# Finally, to move cells up and down, press the up/down arrow after selecting the cell you want to move, and it will swap places with the cell above/below it.
#

# %% [markdown] id="mrINU8_8JqUv"
# # 2. Introduction to Google Colab
#
# What makes Google Colab so special compared to a normal Python notebook? The main benefit that Google Colab services provide is the ability to use the power of **GPUs** (Graphics Processing Units) hosted by Google without needing your machine to have GPUs itself.
#
# Why is this important? Many machine learning models (deep neural networks) need extensive processing power that only GPUs can provide if they ever hope to finish running in a reasonable amount of time. **You will NOT need to use GPUs for any of your CSCI 2033 homeworks**, but they are a good thing to keep in mind if you ever plan on using Colab for your own projects that may be more compute-intensive.

# %% [markdown] id="vyNOxxCQre9C"
# ### 2.1 Common Python Libraries in Colab
#
# ***
#
# Now that you've learned about how Colab can help you more effectively accomplish your coding goals (whether it be completing your homeworks or building a machine learning model), what can you actually do in the Colab environment?
#
# Another cool feature of Colab is the fact that it has many commonly used Python libraries (particularly those used most frequently in machine learning contexts) already loaded in and ready to be imported, without the hassle of installing them on your local machine. Some examples include:
#
#

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 4, "status": "ok", "timestamp": 1727101391219, "user": {"displayName": "Bernardo Bianco Prado", "userId": "01223085289308682497"}, "user_tz": 300} id="8CtcIsEX0TK5" outputId="b661eb25-0fd2-4227-f76f-fa16d107cedb"
# NumPy (which you will become very familiar with on your homework assignments!)

import numpy as np

print(f"Colab is currently using NumPy version {np.__version__}")

x = np.array([1,2,3])
A = 2 * np.eye(3)

print(A@x)

# %% colab={"base_uri": "https://localhost:8080/", "height": 448} executionInfo={"elapsed": 681, "status": "ok", "timestamp": 1727101391896, "user": {"displayName": "Bernardo Bianco Prado", "userId": "01223085289308682497"}, "user_tz": 300} id="PdG_p6Vc01mq" outputId="d1f21d63-e02e-4de5-fbc1-88b907bdcb4b"
# Matplotlib (very useful for visualizing data via plots)

# NOTE: Make sure you run the NumPy code cell first!

import matplotlib
import matplotlib.pyplot as plt

print(f"Colab is currently using Matplotlib version {matplotlib.__version__}")

x = np.arange(100)
y = (x-50)**2

plt.scatter(x,y)
plt.show()

# %% [markdown] id="zQFI5DVt-Mk1"
# # 3. Downloading your colab notebooks
#
# Once you have finished your notebook, make sure to change the name of the file to the following format
#
# *\<your x500\>Homework\<HW number\>.ipynb*
#
# For example, my file name yould be
#
# *bianc072Homework1.ipynb*
#
# After you're done changing the file name, make sure that you re-run all the files and that no errors occur.
#
# ANow, you can download it as a Python notebook (.ipynb) file. To do this, go to \texttt{ File -> Download } from the top menu bar, and select the download format for the notebook. Make sure to download it as a Python notebook and not as a regular Python file! The process for that is outlined below!
#
# **Make sure to download it as a Python notebook and not as a regular Python file!**

# %% [markdown] id="GSerPZQ6LYz3"
# # CONGRATULATIONS
#
# on making it through this tutorial! Now you have enough knowledge to be able to do the CSCI 2033 homeworks on Colab, and possibly be able to explore some more with using Colab and creating your own projects. I'm excited to see what you can do with Colab notebooks, and I wish you all a good semester!
