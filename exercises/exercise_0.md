# Exercise 0 - EDA in python and basics of Power BI

In this exercise, you will continue working with EDA with pandas and Power BI semantic model.

## 0. Car sales in Norway - emissions and trends

In this exercise, work with this dataset `norway_new_car_sales_by_month.csv`

&nbsp; a) Do some EDA with info, find out column names, shape of dataset, describe method to get summary descriptive statistics.

&nbsp; b) Draw a line chart of quantity for each year. Is there a year that should be skipped?

&nbsp; c) Draw a line chart of average CO2 emissions for same years that as in b)

&nbsp; d) Draw a line chart of all years and months for import

&nbsp; e) Draw a line chart of all years and months for average CO2 emissions

&nbsp; f) Draw a line chart of all years and months for electric cars import

&nbsp; g) Draw a line chart of average diesel share per year

&nbsp; h) Discuss some findings with a friend based on this dataset, and do plot more graphs

## 1. Phone prices

Use this [phone price dataset](https://www.kaggle.com/datasets/rkiattisak/mobile-phone-price) and explore this.

&nbsp; a) Find out how many different brands there are in the dataset

&nbsp; b) Draw a horizontal bar chart on number of rows per brand

&nbsp; c) Make a histogram of screen sizes

&nbsp; d) Make a histogram of the memory

&nbsp; e) Make histogram of storage

&nbsp; f) Do more data cleaning and EDAs

## 2. Power BI Semantic Model

In this exercise, you will continue working with the semantic model created in the class with bike store data. You will explore more on DAX functions to create more measures on the same semantic model. 

If you have not worked on the in-class exercise, complete the in-class exercise [here](https://github.com/kokchun/data_vizualisation_kokchun_giang_de25/blob/main/04_semantic_model/powerbi_semantic_model.md) first.

&nbsp; a) Create a measure to show the number of orders made in the store *Baldwin Bikes*. 

&nbsp; b) For each of the order, there are *order_date* and *required_date*. The number of days between these two dates shows how long a customer would like to wait before the shipping. Now, create a measure that presents the average number of days between these two dates across all order. 

You can make use of these two DAX functions to define this measure: [*DATEDIFF()*](https://learn.microsoft.com/en-us/dax/datediff-function-dax) and [*AVERAGEX()*](https://learn.microsoft.com/en-us/dax/averagex-function-dax). Check out the links of documentations of these functions to understand how to use them. What is the difference between the DAX functions *AVERAGE()* and *AVERAGEX()*?

&nbsp; c) Can you round the measure in question a) to integer? Check out the DAX function [*ROUND()*](https://learn.microsoft.com/en-us/dax/round-function-dax).


## 5. Theory questions

&nbsp; a) When can you make line charts and when can't you make line charts?

&nbsp; b) Whats wrong with this chart?

<img src="https://github.com/kokchun/assets/blob/main/data_visualization/bar_no_zero.png?raw=true" alt="bar chart and line chart" width="300">

&nbsp; c) Whats wrong with this chart?

<img src="https://github.com/kokchun/assets/blob/main/data_visualization/line_categorical.png?raw=true" alt="bar chart and line chart" width="300">

&nbsp; d) What is the difference between OOP approach and plt approach in drawing graphs.

&nbsp; e) How do you draw an arrow in matplotlib?

&nbsp; f) Why do you need to create a semantic model in Power BI?

&nbsp; g) What is the difference between data source and semantic model in Power BI?

&nbsp; h) What is the difference between Power BI desktop and Power BI service?

## Glossary

Fill in this table either by copying this into your own markdown file or copy it into a spreadsheet if you feel that is easier to work with.

| terminology         | explanation |
| ------------------- | ----------- |
| histogram           |             |
| data cleaning       |             |
| data transformation |             |
| casting             |             |
| bar chart           |             |
| semantic model      |             |
| power bi            |             |
| data visualization  |             |
| DAX                 |             |
| power query         |             |
| workspace           |             |
