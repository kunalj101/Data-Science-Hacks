# Data-Science-Hacks
Data Science Hacks is created and maintained by Analytics Vidhya for the data science community. 

It includes a variety of tips, tricks and hacks related to data science, machine learning 

These Hacks are for all the data scientists out there. It doesn’t matter if you are a beginner or an advanced professional, these hacks will definitely make you efficient!

Feel free to contribute your own data science hacks here. Make sure that your hack follows the contribution guidelines

### Hack #1 - Resource Downloader 
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
 
### Hack #2 Pandas Apply 
Pandas Apply is one of the most commonly used functions for playing with data and creating new variables. It returns some value after passing each row/column of a data frame with some function. The function can be both default or user-defined. 

### Hack #3 Pandas Boolean Indexing 
It helps to select subset of data based on the value of the data in the dataframe

### Hack #4 Pandas Pivot Table 
It is used to create MS Excel style spreadsheet. Levels in the pivot table will be stored in MultiIndex objects (hierarchical indexes) on the index and columns of the result DataFrame.

### Hack #5 Pandas crosstab 
pd.crosstab() function is used to get an initial “feel” (view) of the data.

### [Hack #6 Pandas str.split](first-and-last-name-extraction.ipynb) 
It is used to apply vectorized string functions on a pandas dataframe column.
Let’s say you want to split the names in a dataframe column into first name and last name.
pandas.Series.str along with split( ) can be used to perform this task.

### [Hack #7 Extract E-mails from text](Code/Extract-E-mails-from-text.ipynb) 
Here is an interesting hack to extract email ids present in long pieces of text by just using 2 lines of code in Python using regular expressions. Extracting information from social media posts and websites has become a common practice in data analytics but sometimes we end up trying complicated methods to achieve things that can be solved easily by using the right technique. 

### [Hack #8 Normal Distribution](/Code/Convert-normal-Distribution.ipynb)
One of the most important assumptions in linear and logistic regression is that our data must follow a normal distribution but we all know that's usually not the case in real life. We often need to transform our data into normal/ gaussian distribution.
 
### [Hack #9 Remove Emojis from text](Remove-emojis-from-text.ipynb)
Preprocessing is one of the key steps for improving the performance of a model. 
One of the main reasons for text preprocessing is to remove unwanted characters from text like punctuation, emojis, links and so on which is not required for our problem statement. 

### Hack #10 Elbow method for classifier
Elbow Method is used for identifying the value of k in k-Nearest Neighbors. It's a plot of errors at different values of k and we select the k value having least error!

### Hack #11 MinMax Scaler
An important part of data analysis is to preprocessing. Many times we need to scale our features like in the case of k-NN we always need to scale the data before building model or else it'll give spurious results.

### [Hack #12 Feature engineering for time series data](/Code/Hack-of-the-day---Time-series.ipynb)
Most of the data collected today, hold the date and time variables. There is a lot of information that you can extract from these features and you can utilize it in your analysis! 

### [Hack #13 Dummy data for linear regression](make_regression.ipynb)
Deeplearning models usually require a lot of #data for training. But acquiring massive amounts of data comes with its own challenges. Instead of spending days manually collecting data, you can make use of Image Augmentation techniques. It is the process of generating new images. These new images are generated using the existing training images and hence we don’t have to collect them manually.

### [Hack #14 Image Augmentation](Image-Augmentation---Article-Shoot.ipynb)
Tokenization is the primary task while building the vocabulary. 
HuggingFace recently created a library for tokenization which provides an implementation of today's most used tokenizers, with a focus on performance and versatility.
Key features:
Ultra-fast: They can encode 1GB of text in ~20sec on a standard server's CPU


### [Hack #15 Divide Continuous and categorical data](select_dtype.ipynb)
You can extract categorical and numeric features into seperate dataframes in just 1 line of code! 
This can be done using the select_dtypes function.

### Hack #16 Pandas Profiling
Do you want to to do perform quick data analysis on your dataframe? 
You can use pandas profiling to generate profile report of your dataset in just 1 line of code!

### Hack #17 Formatting of DataFrame
Convert wide form dataframe into long form dataframe in just 1 line of code!
In pd.melt(), one more columns are used as identifiers. "Unmelt the data", use pivot() function

### [Hack #18 Magic Function- %history](Code/HoD_history.ipynb)
Do you know how you can get the history of all the commands running inside your jupyter notebook?
Use %history, jupyter notebook's built-in magic function! 
Note - Even if you have cut the cells in your notebook, %history will print those commands as well!

### Hack #19 Heatmap on pandas dataframe
Create heatmap on pandas dataframe using seaborn!
It helps you understand the complete range of values at a glimpse.

### Hack #20 Plot confusion matrix
Scikit-learn has released its stable 0.22.1 version with new features and bug fixes.
One new function is the plot_confusion_matrix function which generates an extremely intuitive and customisable confusion matrix for your classifier.
Bonus tip: You can specify the format of the numbers appearing in the boxes using the values_format parameter('n' for whole numbers, '.2f' for float, etc)

### [Hack #21 Ipython Interactive shell](interactive_notebook.ipynb)
What will be the output if you run the following commands in single cell of your jupyter notebook?
df.shape
df.head()
Ofcourse it'll be first five rows of your dataframe. Can we get output of both the command run in same cell? 
You can do it using InteractiveShell.

### Hack #22 Python tqdm
Most of you have heard about the library #tqdm and you might be using it track the progress of forever running for loops. Most of the times we write complex functions having nested for loops. #tqdm allows tracking that too. Here is how you can track the nested loops using tdqm in python.

### [Hack #23 Image Augmentation](Image-Augmentation---Article-Shoot.ipynb)
Deeplearning models usually require a lot of #data for training. But acquiring massive amounts of data comes with its own challenges. Instead of spending days manually collecting data, you can make use of Image Augmentation techniques. It is the process of generating new images. These new images are generated using the existing training images and hence we don’t have to collect them manually.
