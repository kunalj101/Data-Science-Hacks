# Data Science Hacks
Data Science Hacks is created and maintained by Analytics Vidhya for the data science community. 

It includes a variety of tips, tricks and hacks related to data science, machine learning 

These Hacks are for all the data scientists out there. It doesn’t matter if you are a beginner or an advanced professional, these hacks will definitely make you efficient!

Feel free to contribute your own data science hacks here. Make sure that your hack follows the contribution guidelines


- ### Data Science Hack #1 - Resource Downloader 
How can you extract image data directly from chrome in one click?
Imagine that you want to make your own machine learning project but you don't have enough data, it becomes a daunting task
Worry not you can use the ResourceSaver extension to directly download data! Let's see how!

Steps:
1. Install the chrome extension from the given URL.
1. Go to Google Images or any webpage from where you want to save the data.
1. Open Inspect Element and click to ResourceSaver Tab
1. Click on the button Save All Resources and a zip file will be created.
1. Unzip the file and open folder encrypted-tbn0.gstatic.com
1. You can find the images here.
 
- ### [Data Science Hack #2 Pandas Apply](./Code/Pandas%20Apply.ipynb) 
Pandas Apply is one of the most commonly used functions for playing with data and creating new variables. It returns some value after passing each row/column of a data frame with some function. The function can be both default or user-defined. 

- ### [Data Science Hack #3 Pandas Boolean Indexing](./Code/Pandas_boolean%20indexing.ipynb) 
It helps to select subset of data based on the value of the data in the dataframe

- ### [Data Science Hack #4 Pandas Pivot Table](./Code/pandas_pivot_table.ipynb) 
It is used to create MS Excel style spreadsheet. Levels in the pivot table will be stored in MultiIndex objects (hierarchical indexes) on the index and columns of the result DataFrame.

- ### [Data Science Hack #5 Pandas crosstab](./Code/pandas_crosstab.ipynb) 
pd.crosstab() function is used to get an initial “feel” (view) of the data.

- ### [Data Science Hack #6 Pandas str.split](./Code/first%20and%20last%20name%20extraction.ipynb) 
It is used to apply vectorized string functions on a pandas dataframe column.
Let’s say you want to split the names in a dataframe column into first name and last name.
pandas.Series.str along with split( ) can be used to perform this task.

- ### [Data Science Hack #7 Extract E-mails from text](./Code/Extract%20E-mails%20from%20text.ipynb) 
Here is an interesting hack to extract email ids present in long pieces of text by just using 2 lines of code in Python using regular expressions. Extracting information from social media posts and websites has become a common practice in data analytics but sometimes we end up trying complicated methods to achieve things that can be solved easily by using the right technique. 

- ### [Data Science Hack #8 Normal Distribution](./Code/Convert%20normal%20Distribution.ipynb)
One of the most important assumptions in linear and logistic regression is that our data must follow a normal distribution but we all know that's usually not the case in real life. We often need to transform our data into normal/ gaussian distribution.
 
- ### [Data Science Hack #9 Remove Emojis from text](./Code/Removing%20emojis%20from%20text.ipynb)
Preprocessing is one of the key steps for improving the performance of a model. 
One of the main reasons for text preprocessing is to remove unwanted characters from text like punctuation, emojis, links and so on which is not required for our problem statement. 

- ### Data Science Hack #10 Elbow method for classifier
Elbow Method is used for identifying the value of k in k-Nearest Neighbors. It's a plot of errors at different values of k and we select the k value having least error!

- ### Data Science Hack #11 MinMax Scaler
An important part of data analysis is to preprocessing. Many times we need to scale our features like in the case of k-NN we always need to scale the data before building model or else it'll give spurious results.

- ### [Data Science Hack #12 Feature engineering for time series data](.Code/Hack%20of%20the%20day%20-%20Time%20series.ipynb)
Most of the data collected today, hold the date and time variables. There is a lot of information that you can extract from these features and you can utilize it in your analysis! 

- ### [Data Science Hack #13 Dummy data for linear regression](./Code/make_regression.ipynb)
Deeplearning models usually require a lot of #data for training. But acquiring massive amounts of data comes with its own challenges. Instead of spending days manually collecting data, you can make use of Image Augmentation techniques. It is the process of generating new images. These new images are generated using the existing training images and hence we don’t have to collect them manually.

- ### [Data Science Hack #14 HuggingFace Tokenization](./Code/av_hack.ipynb)
Tokenization is the primary task while building the vocabulary. 
HuggingFace recently created a library for tokenization which provides an implementation of today's most used tokenizers, with a focus on performance and versatility.
Key features:
Ultra-fast: They can encode 1GB of text in ~20sec on a standard server's CPU


- ### [Data Science Hack #15 Divide Continuous and categorical data](./Code/select_dtype.ipynb)
You can extract categorical and numeric features into seperate dataframes in just 1 line of code! 
This can be done using the select_dtypes function.

- ### [Data Science Hack #16 Pandas Profiling](./Code/pandas%20profiling.ipynb)
Do you want to to do perform quick data analysis on your dataframe? 
You can use pandas profiling to generate profile report of your dataset in just 1 line of code!

- ### [Data Science Hack #17 Formatting of DataFrame](./Code/melt().ipynb)
Convert wide form dataframe into long form dataframe in just 1 line of code!
In pd.melt(), one more columns are used as identifiers. "Unmelt the data", use pivot() function

- ### [Data Science Hack #18 Magic Function- %history](./Code/HoD_history.ipynb)
Do you know how you can get the history of all the commands running inside your jupyter notebook?
Use %history, jupyter notebook's built-in magic function! 
Note - Even if you have cut the cells in your notebook, %history will print those commands as well!

- ### [Data Science Hack #19 Heatmap on pandas dataframe](./Code/Styling%20pandas.ipynb)
Create heatmap on pandas dataframe using seaborn!
It helps you understand the complete range of values at a glimpse.

- ### [Data Science Hack #20 Plot confusion matrix](./Code/plot_confusion_matrix.ipynb)
Scikit-learn has released its stable 0.22.1 version with new features and bug fixes.
One new function is the plot_confusion_matrix function which generates an extremely intuitive and customisable confusion matrix for your classifier.
Bonus tip: You can specify the format of the numbers appearing in the boxes using the values_format parameter('n' for whole numbers, '.2f' for float, etc)

- ### [Data Science Hack #21 Ipython Interactive shell](./Code/interactive_notebook.ipynb)
What will be the output if you run the following commands in single cell of your jupyter notebook?
df.shape
df.head()
Ofcourse it'll be first five rows of your dataframe. Can we get output of both the command run in same cell? 
You can do it using InteractiveShell.

- ### Data Science Hack #22 Python tqdm
Most of you have heard about the library #tqdm and you might be using it track the progress of forever running for loops. Most of the times we write complex functions having nested for loops. #tqdm allows tracking that too. Here is how you can track the nested loops using tdqm in python.

- ### [Data Science Hack #23 Image Augmentation](./Code/Image%20Augmentation%20-%20Article%20Shoot.ipynb)
Deeplearning models usually require a lot of #data for training. But acquiring massive amounts of data comes with its own challenges. Instead of spending days manually collecting data, you can make use of Image Augmentation techniques. It is the process of generating new images. These new images are generated using the existing training images and hence we don’t have to collect them manually.
