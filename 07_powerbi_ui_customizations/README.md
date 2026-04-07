# UI Customerization
After creating a report that is showing the data correctly, it is also important to improve the user interface of the report. Follow this chapter to improve the UI of the report that we have built in chapter 5.

Video - part 1 for UI Features 

<a href="https://youtu.be/8F2H1Vq-ToA" target="_blank">
  <img src="https://github.com/kokchun/assets/blob/main/data_visualization_powerbi/pbi_ui.png?raw=true" alt="powerbi ui features" width="600">
</a>


Video - part 2 for Graphical Design (*TODO*)

## UI Features

### For Showing Details
#### Drilldown
Switch to the focus mode of a visual to make it easier to work with the visual:
<a href="https://youtu.be/s7hNlgqREt0" target="_blank">
  <img src="https://github.com/kokchun/assets/blob/main/data_visualization_powerbi/focus_mode.png?raw=true" alt="powerbi" width="600">
</a>
<br>

For the bar chart, add another categorical column to X-axis. This will then enable the drilldown panel on the visual. With this drilldown panel, you can choose to look at values of Y-axis by two different columns assigned to X-axis:
<a href="https://youtu.be/s7hNlgqREt0" target="_blank">
  <img src="https://github.com/kokchun/assets/blob/main/data_visualization_powerbi/drilldown.png?raw=true" alt="powerbi" width="600">
</a>

#### Tooltips
Most visuals have default tooltip. You can configure tooltip setting under *Format visual*:
<a href="https://youtu.be/s7hNlgqREt0" target="_blank">
  <img src="https://github.com/kokchun/assets/blob/main/data_visualization_powerbi/visual_tooltip.png?raw=true" alt="powerbi" width="600">
</a>
<br>

You can add additional info to be shown on the default tooltip:
<a href="https://youtu.be/s7hNlgqREt0" target="_blank">
  <img src="https://github.com/kokchun/assets/blob/main/data_visualization_powerbi/visual_tooltip_field.png?raw=true" alt="powerbi" width="600">
</a>
<br>

Create a customerize tooltip by creating a report page for the tooltip:
<a href="https://youtu.be/s7hNlgqREt0" target="_blank">
  <img src="https://github.com/kokchun/assets/blob/main/data_visualization_powerbi/customerize_tooltip.png?raw=true" alt="powerbi" width="600">
</a>
<br>

### For Highlighting Values

#### Conditional formatting
Some components of some visuals have conditional formatting enabled. For these components, you can see the *fx* sign under *Format visual*. For instance, you can configure gradient color for the bars in a bar chart: 
<a href="https://youtu.be/s7hNlgqREt0" target="_blank">
  <img src="https://github.com/kokchun/assets/blob/main/data_visualization_powerbi/conditional_formatting.png?raw=true" alt="powerbi" width="600">
</a>
<br>

#### Overlaid Analytics
Similar to conditional formatting, some visuals have overlaid analytics enabled. For these visuals, you can see options under the *Analytics* pane. You can then add analytics components on the visuals for highlighting your insights:
<a href="https://youtu.be/s7hNlgqREt0" target="_blank">
  <img src="https://github.com/kokchun/assets/blob/main/data_visualization_powerbi/analytics_pane.png?raw=true" alt="powerbi" width="600">
</a>
<br>

### Others

#### Bookmarks
You can capture selections of multiple slicers of a report page by adding a bookmark. A bookmark is very useful if you are going to present interesting insights from a certain state of the report during a presentation. <br>

You need to first show the bookmark pane: 

<a href="https://youtu.be/s7hNlgqREt0" target="_blank">
  <img src="https://github.com/kokchun/assets/blob/main/data_visualization_powerbi/add_bookmark.png?raw=true" alt="powerbi" width="600">
</a>

<br>

Then, you can add a bookmark:

<a href="https://youtu.be/s7hNlgqREt0" target="_blank">
  <img src="https://github.com/kokchun/assets/blob/main/data_visualization_powerbi/edit_bookmark.png?raw=true" alt="powerbi" width="600">
</a>
<br>

#### Buttons
A button is a shortcut on the report. Button is often used with bookmarks because the action of a shortcut can be jumping to a bookmark. This let readers to visit the bookmark easily:

<a href="https://youtu.be/s7hNlgqREt0" target="_blank">
  <img src="https://github.com/kokchun/assets/blob/main/data_visualization_powerbi/add_button.png?raw=true" alt="powerbi" width="600">
</a>
<br><br>

>[!TIP]
>Check out the reference at the bottom of this chapter, *Enhance user experience*, to find out more Power BI features for user experience

## Graphical Design
Now we are going to refine the design of our report so that it is more readable. As we do not have many visuals that analyze different aspects of the data in this report, we will put all visuals in one page. This is the final version of our report:

<a href="https://youtu.be/s7hNlgqREt0" target="_blank">
  <img src="https://github.com/kokchun/assets/blob/main/data_visualization_powerbi/report_design.png?raw=true" alt="powerbi" width="300">
</a>
<br><br>

Here are some usual considerations to improve the report design:

### Choice of Visuals
It's important to choose a suitable visual to present certain data. For instance, instead of using three cards to show the number of data engineers at different experience levels, a donut chart is a better choice to present these data:

<a href="https://youtu.be/s7hNlgqREt0" target="_blank">
  <img src="https://github.com/kokchun/assets/blob/main/data_visualization_powerbi/donut_chart.png?raw=true" alt="powerbi" width="600">
</a>
<br><br>

Two other cards are added to present other metrics, highlighting the overview of the data. 

### Alignment 
Align all elements of the report nicely to make your report look professional. 

In our report:
- we have placed the title of the dashboard and other elements for user interaction on the top panel
- size and position settings are used to align visuals. You can select multiple visuals by clicking ```ctrl``` and edit these settings for them together
<a href="https://youtu.be/s7hNlgqREt0" target="_blank">
  <img src="https://github.com/kokchun/assets/blob/main/data_visualization_powerbi/alignment.png?raw=true" alt="powerbi" width="300">
</a>
<br><br>

### Color Theme
Think about a set of colors for report wallpaper, visual background, visual font etc. Then apply the same set of colors in the entire report. In our report, we are using these choices:

<a href="https://youtu.be/s7hNlgqREt0" target="_blank">
  <img src="https://github.com/kokchun/assets/blob/main/data_visualization_powerbi/color.png?raw=true" alt="powerbi" width="300">
</a>
<br><br>

These choices consider letting readers to focus on the data itself. 

### Uniform Font
Check that all fonts appearing in different elements on the report are the same. In this report, we have used *Arial*. 

These font sizes are used:
- 18 for report title
- 12 for visual title
- 18 for card value

### Rounded Corners
We have used rounded corners for all visuals and buttons on the report because this is usually more preferrable for a softer design.

For each of the visual, under *General*, you can edit the *Visual border* to make the corners of the visual rounded:

<a href="https://youtu.be/s7hNlgqREt0" target="_blank">
  <img src="https://github.com/kokchun/assets/blob/main/data_visualization_powerbi/rounded_corner.png?raw=true" alt="powerbi" width="300">
</a>
<br><br>

### Value Format
We show the values on the cards in this way:

<a href="https://youtu.be/s7hNlgqREt0" target="_blank">
  <img src="https://github.com/kokchun/assets/blob/main/data_visualization_powerbi/value_format.png?raw=true" alt="powerbi" width="600">
</a>
<br><br>

In order to so so, you need to first customerize the *data format* of the card visual:

<a href="https://youtu.be/s7hNlgqREt0" target="_blank">
  <img src="https://github.com/kokchun/assets/blob/main/data_visualization_powerbi/data_format.png?raw=true" alt="powerbi" width="300">
</a>
<br><br>

Then, also deselect the use of the letter *K* as the suffix:

<a href="https://youtu.be/s7hNlgqREt0" target="_blank">
  <img src="https://github.com/kokchun/assets/blob/main/data_visualization_powerbi/display_unit.png?raw=true" alt="powerbi" width="300">
</a>
<br><br>

### Padding
You should always leave white space in your report. The report or any other type of visualizations should not be completely covered with information in forms of texts or data. Otherwise, it is difficult for readers to focus on the data itself. For most visuals, you can control this by adjusting *padding*:

<a href="https://youtu.be/s7hNlgqREt0" target="_blank">
  <img src="https://github.com/kokchun/assets/blob/main/data_visualization_powerbi/padding.png?raw=true" alt="powerbi" width="300">
</a>
<br><br>

## Other videos 📹

## Read more 👓
[Enhance user experience](https://learn.microsoft.com/en-us/training/modules/power-bi-effective-user-experience/)
