# Creating visualizations

Once you have created a semantic model containing your data, you can start to create visualizations. There are two types of visualizations that you can create with Power BI: report and dashboard. A report is an interactive and multi-page document that presents the data in your semantic model with graphs and texts. While a dashboard is a single page document that shows a selection of graphs from different Power BI reports, which gives an overview of highlights from different reports. Therefore, a report is created using a semantic model, and a dashboard is created using multiple reports. The coming sections will guide you through the creation of two reports and a dashboard. 

## Power BI Reports

### Data Engineer Salary Report
Create the first report by using the previously created semantic model. Choose a blank report:
<a href="https://youtu.be/s7hNlgqREt0" target="_blank">
  <img src="https://github.com/kokchun/assets/blob/main/data_visualization_powerbi/create_report.png?raw=true" alt="powerbi setup" width="600">
</a>

You will then see the report editor where you can continue to work on your report. You also need to save your report to your workspace:
<a href="https://youtu.be/s7hNlgqREt0" target="_blank">
  <img src="https://github.com/kokchun/assets/blob/main/data_visualization_powerbi/report_editor.png?raw=true" alt="powerbi setup" width="600">
</a>

Start by creating some layouts of your report, like creating two pages and using shapes to create a title:
<a href="https://youtu.be/s7hNlgqREt0" target="_blank">
  <img src="https://github.com/kokchun/assets/blob/main/data_visualization_powerbi/basic_layout.png?raw=true" alt="powerbi setup" width="600">
</a>

Now, set a gridline by clicking on *View* so that it is easier to place different visuals on the report. Create visuals called *Card*. In each card, you can show the calculated measures as a KPI. Continue to edit the format of the card under the *Visualizations* panel:
<a href="https://youtu.be/s7hNlgqREt0" target="_blank">
  <img src="https://github.com/kokchun/assets/blob/main/data_visualization_powerbi/metrics.png?raw=true" alt="powerbi setup" width="600">
</a>

In the second page of the report, *Further Analysis*, we will be using more types of visuals:
- slicer
- stacked column chart
- table
- treemap
  
>[!TIP]
>Check out the reference, *Visuals Overview*, at the bottom of this chapter to create more visuals on your report. Note that when choosing a visual, you need to consider if it represents interesting insights from the data. 

Follow the lecture video to create and format these visuals.Note that we can make use of the slicer called *Company Country/Territory* to zoom into a subset of data engineer records due to the relationship between the *countries* and *salaries* tables created in the semantic model. After creating all visuals, you can also notice that by default, there is cross-filtering between visuals on a report, meaning that by clicking into a data point in one visual will lead of filtering on another visuals as well. 

<a href="https://youtu.be/s7hNlgqREt0" target="_blank">
  <img src="https://github.com/kokchun/assets/blob/main/data_visualization_powerbi/further_analysis.png?raw=true" alt="powerbi setup" width="600">
</a>

>[!NOTE]
>💡 **Try it yourself** <br>
From this report, can you find out
>- which job titles are most common around the data engineer records in the data?
>- which job titles tends to earn more?

### US Economic trend Report



## Power BI Dashboard





## Other videos 📹

## Read more 👓
[Power BI report](https://learn.microsoft.com/en-us/power-bi/create-reports/power-bi-reports-overview) <br>
[Report Editor](https://learn.microsoft.com/en-us/power-bi/create-reports/service-the-report-editor-take-a-tour) <br>
[Power BI dashboard](https://learn.microsoft.com/en-us/power-bi/create-reports/service-dashboards) <br>
[Visuals Overview](https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualizations-overview)