# Life Expectancy Project
* Created a tool which able to predict the life expectancy of an individual based on numerous parameters.
* Dataset was taken from kaggle. 
* Link for dataset: https://www.kaggle.com/mmattson/who-national-life-expectancy
* Optimized Linear, Lasso, and Random Forest Regressors using GridsearchCV to reach the best model. 

## Code and Resources Used 
**Python Version:** 3.7  
**Packages:** pandas, numpy, sklearn, matplotlib, seaborn, selenium, flask, json, pickle  

## Overview Of The Dataset
The features in the dataset are as follows:

* Country
* Year
* Developed or Developing status
* Life Expectancy in age
* Adult Mortality Rates of both sexes (probability of dying between 15 and 60 years per 1000 population)
* Number of Infant Deaths per 1000 population
* Alcohol, recorded per capita (15+) consumption (in litres of pure alcohol)
* Expenditure on health as a percentage of Gross Domestic Product per capita(%)
* Hepatitis B (HepB) immunization coverage among 1-year-olds (%)
* Measles - number of reported cases per 1000 population
* Average Body Mass Index of entire population
* Number of under-five deaths per 1000 population
* Polio (Pol3) immunization coverage among 1-year-olds (%)
* General government expenditure on health as a percentage of total government expenditure (%)
* Diphtheria tetanus toxoid and pertussis (DTP3) immunization coverage among 1-year-olds (%)
* Deaths per 1 000 live births HIV/AIDS (0-4 years)
* Gross Domestic Product per capita (in USD)
* Population of the country
* Prevalence of thinness among children and adolescents for Age 10 to 19 (% )
* Prevalence of thinness among children for Age 5 to 9(%)
* Human Development Index in terms of income composition of resources (index ranging from 0 to 1)
* Number of years of Schooling(years)



## Data Cleaning
The first task was to clean the data. For that I did the following things:

*	Striped the column names out of extra white spaces
*	Checked which columns had either 0 or null values in them.
*	The null values were replaced by the mean of their respective columns.
*	Some of the columns having 0 value in them were left untouched, for eg: infant deaths, etc. And some of the columns with zero values were replaced by the mean of that column, for eg: percentage expenditure, etc.
*	There were 193 countries in the dataset. Each country had 16 entries. 10 countries had only 1 entries. They would not be beneficial while building the model. Instead of dropping those values, those countries were replaced by "Other". So the entry "Other", now had 10 entries. 


## EDA
I looked at the change in Life Expectancy of every country per year. The graph of Afghanistan and Albania are as follows:

![image](https://user-images.githubusercontent.com/56645508/122201360-93455c00-ceb9-11eb-9b6d-b54cbebdb9ee.png)
![image](https://user-images.githubusercontent.com/56645508/122201377-993b3d00-ceb9-11eb-8ef3-3ee69ad771a3.png)

I also looked at the change in adult mortality rate of every country per year. The graph of Australia and India are as follows:

![image](https://user-images.githubusercontent.com/56645508/122201568-c982db80-ceb9-11eb-94aa-d03461d567cc.png)
![image](https://user-images.githubusercontent.com/56645508/122201664-e61f1380-ceb9-11eb-98c4-484a43491bc7.png)

I also looked at the change in percentage expenditure of every country per year. The graph of Angola and Argentina are as follows:

![image](https://user-images.githubusercontent.com/56645508/122201803-0949c300-ceba-11eb-8d8d-ebf2d5e88d26.png)
![image](https://user-images.githubusercontent.com/56645508/122201818-0e0e7700-ceba-11eb-8e15-1d6552b80ec4.png)

I also looked at the change in GDP of every country per year. The graph of Bangladesh and Brazil are as follows:

![image](https://user-images.githubusercontent.com/56645508/122202010-3dbd7f00-ceba-11eb-8818-b353b352b3ed.png)
![image](https://user-images.githubusercontent.com/56645508/122202046-457d2380-ceba-11eb-95de-b26caad54657.png)

Next I looked at the distribution of developed and developing countries in my dataset:

![image](https://user-images.githubusercontent.com/56645508/122202157-6180c500-ceba-11eb-8dba-21bc55357f84.png)

I also created a heatmap of my dataset:

![image](https://user-images.githubusercontent.com/56645508/122202216-71000e00-ceba-11eb-96d3-fd5e6d7cd525.png)


## Model Building 

I keep the data for 2000-2013 as my training data and the data for 2014-2015 was used as my testing data.  

I tried three different models:
*	**Multiple Linear Regression** 
*	**Lasso Regression** 
*	**Random Forest**
I fine tuned each model using GridSearchCV 

## Model performance
The Random Forest model outperformed the other models on the test set. 
The R-squared score achieved by the three models are as follows:

*	**Random Forest** : 0.940821
*	**Linear Regression**: 0.833113
*	**Lasso Regression**: 0.833106

## Productionization 
In this step, I built a flask API  that was hosted on local server. The API took all the variables as input and gave the life expectancy as output. Below are the screenshots for the same:
![image](https://user-images.githubusercontent.com/56645508/122203632-dbfe1480-cebb-11eb-8dba-3f18dbedf1ec.png)
![image](https://user-images.githubusercontent.com/56645508/122203693-ec15f400-cebb-11eb-9fe2-1b318fe8cd9e.png)
![image](https://user-images.githubusercontent.com/56645508/122203776-03ed7800-cebc-11eb-82ae-6bce43a5c36e.png)



