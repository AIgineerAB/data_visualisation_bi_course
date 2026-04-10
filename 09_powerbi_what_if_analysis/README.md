# Power BI What-if Analysis

What-if Analysis is used for enabling readers of a report to switch between scenarios and compare them. In Power BI, it can be done using *numeric range parameter*. 

In the same report on data engineer salary, suppose we would like to show the average salary in swedish kr and let the readers to select the usd-to-kr exchange rate from 8 to 11 as the exchange rate always fluctuates. 

## Instructions

### Create Parameter in Semantic Model
First, create a new numeric range parameter. Edit the name, minimum, maximum and incremental value of the parameter:

<a href="https://youtu.be/s7hNlgqREt0" target="_blank">
  <img src="https://github.com/kokchun/assets/blob/main/data_visualization_powerbi/parameter.png?raw=true" alt="powerbi" width="600">
</a>
<br><br>

You can see the parameter through DAX query view:
<a href="https://youtu.be/s7hNlgqREt0" target="_blank">
  <img src="https://github.com/kokchun/assets/blob/main/data_visualization_powerbi/parameter_value.png?raw=true" alt="powerbi" width="600">
</a>

### Update Measure
Update the *Average Salary* measure by citing the parameter:
<a href="https://youtu.be/s7hNlgqREt0" target="_blank">
  <img src="https://github.com/kokchun/assets/blob/main/data_visualization_powerbi/salary_kr.png?raw=true" alt="powerbi" width="600">
</a>
<br><br>


### Adding Slicer in Report
Add a slicer with the parameter so that readers are able to select a certain value of the parameter. Now, you should see that the value of average salary in different visuals are in kr.  
<a href="https://youtu.be/s7hNlgqREt0" target="_blank">
  <img src="https://github.com/kokchun/assets/blob/main/data_visualization_powerbi/slicer.png?raw=true" alt="powerbi" width="600">
</a>

## Other videos 📹

## Read more 👓
[Use Parameter in Power BI](https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-what-if)
