# Power BI What-if Analysis

What-if Analysis is used for enabling readers of a report to switch between scenarios and compare them. In Power BI, it can be done using _numeric range parameter_.

In the same report on data engineer salary, suppose we would like to show the average salary in swedish kr and let the readers to select the usd-to-kr exchange rate from 8 to 11 as the exchange rate always fluctuates.

<a href="https://www.youtube.com/watch?v=T2s6lP6Z_qU" target="_blank">
  <img src="https://github.com/kokchun/assets/blob/main/data_visualization_powerbi/what_if.png?raw=true" alt="powerbi" width="600">
</a>


## Instructions

### Create Parameter in Semantic Model

First, create a new numeric range parameter. Edit the name, minimum, maximum and incremental value of the parameter:

<img src="https://github.com/kokchun/assets/blob/main/data_visualization_powerbi/parameter.png?raw=true" alt="powerbi" width="600">

<br><br>

You can see the parameter through DAX query view:

<img src="https://github.com/kokchun/assets/blob/main/data_visualization_powerbi/parameter_value.png?raw=true" alt="powerbi" width="600">

### Update Measure

Update the _Average Salary_ measure by citing the parameter:

<img src="https://github.com/kokchun/assets/blob/main/data_visualization_powerbi/salary_kr.png?raw=true" alt="powerbi" width="600">

<br><br>

### Adding Slicer in Report

Add a slicer with the parameter so that readers are able to select a certain value of the parameter. Now, you should see that the value of average salary in different visuals are in kr.

<img src="https://github.com/kokchun/assets/blob/main/data_visualization_powerbi/slicer.png?raw=true" alt="powerbi" width="600">

## Other videos 📹

## Read more 👓

[Use Parameter in Power BI](https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-what-if)
