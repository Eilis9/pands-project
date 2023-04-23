<h1><img align="right" width="350" src="img/ATU-Logo-Full-RGB-Green.jpg"> Project for Programming and Scripting 
</h1>
<p> 
Course: HDip in Computing in Data Analytics <br>
Module: Programming and Scripting <br>
Lecturer: Andrew Beatty
    
Student: Eilis Donohue (G00006088)

A repository for the analysis conducted as part of the Project assessment for  the Programming and Scripting Module of the HDip in Data Analytics beginning January 2023. 

Software Used: 
 - Python v3.7 and higher  
 </p>

 - - -

## Literature Review
Fisher's Iris Dataset [x] is a well known database dating from the 1930s when it was cited by the academic R.A. Fischer in the Annual Eugenics journal [XX]. R.A. Fisher was an English polymath who was active in the fields of mathematics, statistics, biology and genetics [xx]. The Iris dataset comprises 50 measurements each of three distinct classes of Iris flower found growing in the same meadow. The length and width of the sepal and petal for each flower along with the class is recorded [XXX].

The dataset is used as an example of.....

## Summary Statistics
The basic statistical measures of the data are given in the tables below.  
<style type="text/css">
</style>
<table id="T_26ffb">
  <caption>Summary All</caption>
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_26ffb_level0_col0" class="col_heading level0 col0" >Min (cm)</th>
      <th id="T_26ffb_level0_col1" class="col_heading level0 col1" >Max (cm)</th>
      <th id="T_26ffb_level0_col2" class="col_heading level0 col2" >Mean (cm)</th>
      <th id="T_26ffb_level0_col3" class="col_heading level0 col3" >Median (cm)</th>
      <th id="T_26ffb_level0_col4" class="col_heading level0 col4" >StDev (cm)</th>
      <th id="T_26ffb_level0_col5" class="col_heading level0 col5" >Variance (cm)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_26ffb_level0_row0" class="row_heading level0 row0" >Sepal Length</th>
      <td id="T_26ffb_row0_col0" class="data row0 col0" >4.30</td>
      <td id="T_26ffb_row0_col1" class="data row0 col1" >7.90</td>
      <td id="T_26ffb_row0_col2" class="data row0 col2" >5.84</td>
      <td id="T_26ffb_row0_col3" class="data row0 col3" >5.80</td>
      <td id="T_26ffb_row0_col4" class="data row0 col4" >0.83</td>
      <td id="T_26ffb_row0_col5" class="data row0 col5" >0.69</td>
    </tr>
    <tr>
      <th id="T_26ffb_level0_row1" class="row_heading level0 row1" >Sepal Width</th>
      <td id="T_26ffb_row1_col0" class="data row1 col0" >2.00</td>
      <td id="T_26ffb_row1_col1" class="data row1 col1" >4.40</td>
      <td id="T_26ffb_row1_col2" class="data row1 col2" >3.05</td>
      <td id="T_26ffb_row1_col3" class="data row1 col3" >3.00</td>
      <td id="T_26ffb_row1_col4" class="data row1 col4" >0.43</td>
      <td id="T_26ffb_row1_col5" class="data row1 col5" >0.19</td>
    </tr>
    <tr>
      <th id="T_26ffb_level0_row2" class="row_heading level0 row2" >Petal Length</th>
      <td id="T_26ffb_row2_col0" class="data row2 col0" >1.00</td>
      <td id="T_26ffb_row2_col1" class="data row2 col1" >6.90</td>
      <td id="T_26ffb_row2_col2" class="data row2 col2" >3.76</td>
      <td id="T_26ffb_row2_col3" class="data row2 col3" >4.35</td>
      <td id="T_26ffb_row2_col4" class="data row2 col4" >1.76</td>
      <td id="T_26ffb_row2_col5" class="data row2 col5" >3.11</td>
    </tr>
    <tr>
      <th id="T_26ffb_level0_row3" class="row_heading level0 row3" >Petal Width</th>
      <td id="T_26ffb_row3_col0" class="data row3 col0" >0.10</td>
      <td id="T_26ffb_row3_col1" class="data row3 col1" >2.50</td>
      <td id="T_26ffb_row3_col2" class="data row3 col2" >1.20</td>
      <td id="T_26ffb_row3_col3" class="data row3 col3" >1.30</td>
      <td id="T_26ffb_row3_col4" class="data row3 col4" >0.76</td>
      <td id="T_26ffb_row3_col5" class="data row3 col5" >0.58</td>
    </tr>
  </tbody>
</table>




<style type="text/css">
</style>
<table id="T_8888e">
  <caption>Iris-setosa Summary Statistics</caption>
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_8888e_level0_col0" class="col_heading level0 col0" >Min (cm)</th>
      <th id="T_8888e_level0_col1" class="col_heading level0 col1" >Max (cm)</th>
      <th id="T_8888e_level0_col2" class="col_heading level0 col2" >Mean (cm)</th>
      <th id="T_8888e_level0_col3" class="col_heading level0 col3" >Median (cm)</th>
      <th id="T_8888e_level0_col4" class="col_heading level0 col4" >StDev (cm)</th>
      <th id="T_8888e_level0_col5" class="col_heading level0 col5" >Variance (cm)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_8888e_level0_row0" class="row_heading level0 row0" >Sepal Length</th>
      <td id="T_8888e_row0_col0" class="data row0 col0" >4.30</td>
      <td id="T_8888e_row0_col1" class="data row0 col1" >5.80</td>
      <td id="T_8888e_row0_col2" class="data row0 col2" >5.01</td>
      <td id="T_8888e_row0_col3" class="data row0 col3" >5.00</td>
      <td id="T_8888e_row0_col4" class="data row0 col4" >0.35</td>
      <td id="T_8888e_row0_col5" class="data row0 col5" >0.12</td>
    </tr>
    <tr>
      <th id="T_8888e_level0_row1" class="row_heading level0 row1" >Sepal Width</th>
      <td id="T_8888e_row1_col0" class="data row1 col0" >2.30</td>
      <td id="T_8888e_row1_col1" class="data row1 col1" >4.40</td>
      <td id="T_8888e_row1_col2" class="data row1 col2" >3.42</td>
      <td id="T_8888e_row1_col3" class="data row1 col3" >3.40</td>
      <td id="T_8888e_row1_col4" class="data row1 col4" >0.38</td>
      <td id="T_8888e_row1_col5" class="data row1 col5" >0.15</td>
    </tr>
    <tr>
      <th id="T_8888e_level0_row2" class="row_heading level0 row2" >Petal Length</th>
      <td id="T_8888e_row2_col0" class="data row2 col0" >1.00</td>
      <td id="T_8888e_row2_col1" class="data row2 col1" >1.90</td>
      <td id="T_8888e_row2_col2" class="data row2 col2" >1.46</td>
      <td id="T_8888e_row2_col3" class="data row2 col3" >1.50</td>
      <td id="T_8888e_row2_col4" class="data row2 col4" >0.17</td>
      <td id="T_8888e_row2_col5" class="data row2 col5" >0.03</td>
    </tr>
    <tr>
      <th id="T_8888e_level0_row3" class="row_heading level0 row3" >Petal Width</th>
      <td id="T_8888e_row3_col0" class="data row3 col0" >0.10</td>
      <td id="T_8888e_row3_col1" class="data row3 col1" >0.60</td>
      <td id="T_8888e_row3_col2" class="data row3 col2" >0.24</td>
      <td id="T_8888e_row3_col3" class="data row3 col3" >0.20</td>
      <td id="T_8888e_row3_col4" class="data row3 col4" >0.11</td>
      <td id="T_8888e_row3_col5" class="data row3 col5" >0.01</td>
    </tr>
  </tbody>
</table>




<style type="text/css">
</style>
<table id="T_92afe">
  <caption>Iris-versicolor Summary Statistics</caption>
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_92afe_level0_col0" class="col_heading level0 col0" >Min (cm)</th>
      <th id="T_92afe_level0_col1" class="col_heading level0 col1" >Max (cm)</th>
      <th id="T_92afe_level0_col2" class="col_heading level0 col2" >Mean (cm)</th>
      <th id="T_92afe_level0_col3" class="col_heading level0 col3" >Median (cm)</th>
      <th id="T_92afe_level0_col4" class="col_heading level0 col4" >StDev (cm)</th>
      <th id="T_92afe_level0_col5" class="col_heading level0 col5" >Variance (cm)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_92afe_level0_row0" class="row_heading level0 row0" >Sepal Length</th>
      <td id="T_92afe_row0_col0" class="data row0 col0" >4.90</td>
      <td id="T_92afe_row0_col1" class="data row0 col1" >7.00</td>
      <td id="T_92afe_row0_col2" class="data row0 col2" >5.94</td>
      <td id="T_92afe_row0_col3" class="data row0 col3" >5.90</td>
      <td id="T_92afe_row0_col4" class="data row0 col4" >0.52</td>
      <td id="T_92afe_row0_col5" class="data row0 col5" >0.27</td>
    </tr>
    <tr>
      <th id="T_92afe_level0_row1" class="row_heading level0 row1" >Sepal Width</th>
      <td id="T_92afe_row1_col0" class="data row1 col0" >2.00</td>
      <td id="T_92afe_row1_col1" class="data row1 col1" >3.40</td>
      <td id="T_92afe_row1_col2" class="data row1 col2" >2.77</td>
      <td id="T_92afe_row1_col3" class="data row1 col3" >2.80</td>
      <td id="T_92afe_row1_col4" class="data row1 col4" >0.31</td>
      <td id="T_92afe_row1_col5" class="data row1 col5" >0.10</td>
    </tr>
    <tr>
      <th id="T_92afe_level0_row2" class="row_heading level0 row2" >Petal Length</th>
      <td id="T_92afe_row2_col0" class="data row2 col0" >3.00</td>
      <td id="T_92afe_row2_col1" class="data row2 col1" >5.10</td>
      <td id="T_92afe_row2_col2" class="data row2 col2" >4.26</td>
      <td id="T_92afe_row2_col3" class="data row2 col3" >4.35</td>
      <td id="T_92afe_row2_col4" class="data row2 col4" >0.47</td>
      <td id="T_92afe_row2_col5" class="data row2 col5" >0.22</td>
    </tr>
    <tr>
      <th id="T_92afe_level0_row3" class="row_heading level0 row3" >Petal Width</th>
      <td id="T_92afe_row3_col0" class="data row3 col0" >1.00</td>
      <td id="T_92afe_row3_col1" class="data row3 col1" >1.80</td>
      <td id="T_92afe_row3_col2" class="data row3 col2" >1.33</td>
      <td id="T_92afe_row3_col3" class="data row3 col3" >1.30</td>
      <td id="T_92afe_row3_col4" class="data row3 col4" >0.20</td>
      <td id="T_92afe_row3_col5" class="data row3 col5" >0.04</td>
    </tr>
  </tbody>
</table>


<style type="text/css">
</style>
<table id="T_078da">
  <caption>Iris-virginica Summary Statistics</caption>
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_078da_level0_col0" class="col_heading level0 col0" >Min (cm)</th>
      <th id="T_078da_level0_col1" class="col_heading level0 col1" >Max (cm)</th>
      <th id="T_078da_level0_col2" class="col_heading level0 col2" >Mean (cm)</th>
      <th id="T_078da_level0_col3" class="col_heading level0 col3" >Median (cm)</th>
      <th id="T_078da_level0_col4" class="col_heading level0 col4" >StDev (cm)</th>
      <th id="T_078da_level0_col5" class="col_heading level0 col5" >Variance (cm)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_078da_level0_row0" class="row_heading level0 row0" >Sepal Length</th>
      <td id="T_078da_row0_col0" class="data row0 col0" >4.90</td>
      <td id="T_078da_row0_col1" class="data row0 col1" >7.90</td>
      <td id="T_078da_row0_col2" class="data row0 col2" >6.59</td>
      <td id="T_078da_row0_col3" class="data row0 col3" >6.50</td>
      <td id="T_078da_row0_col4" class="data row0 col4" >0.64</td>
      <td id="T_078da_row0_col5" class="data row0 col5" >0.40</td>
    </tr>
    <tr>
      <th id="T_078da_level0_row1" class="row_heading level0 row1" >Sepal Width</th>
      <td id="T_078da_row1_col0" class="data row1 col0" >2.20</td>
      <td id="T_078da_row1_col1" class="data row1 col1" >3.80</td>
      <td id="T_078da_row1_col2" class="data row1 col2" >2.97</td>
      <td id="T_078da_row1_col3" class="data row1 col3" >3.00</td>
      <td id="T_078da_row1_col4" class="data row1 col4" >0.32</td>
      <td id="T_078da_row1_col5" class="data row1 col5" >0.10</td>
    </tr>
    <tr>
      <th id="T_078da_level0_row2" class="row_heading level0 row2" >Petal Length</th>
      <td id="T_078da_row2_col0" class="data row2 col0" >4.50</td>
      <td id="T_078da_row2_col1" class="data row2 col1" >6.90</td>
      <td id="T_078da_row2_col2" class="data row2 col2" >5.55</td>
      <td id="T_078da_row2_col3" class="data row2 col3" >5.55</td>
      <td id="T_078da_row2_col4" class="data row2 col4" >0.55</td>
      <td id="T_078da_row2_col5" class="data row2 col5" >0.30</td>
    </tr>
    <tr>
      <th id="T_078da_level0_row3" class="row_heading level0 row3" >Petal Width</th>
      <td id="T_078da_row3_col0" class="data row3 col0" >1.40</td>
      <td id="T_078da_row3_col1" class="data row3 col1" >2.50</td>
      <td id="T_078da_row3_col2" class="data row3 col2" >2.03</td>
      <td id="T_078da_row3_col3" class="data row3 col3" >2.00</td>
      <td id="T_078da_row3_col4" class="data row3 col4" >0.27</td>
      <td id="T_078da_row3_col5" class="data row3 col5" >0.08</td>
    </tr>
  </tbody>
</table>


## Data correlation

<style type="text/css">
#T_7b98f_row0_col2, #T_7b98f_row0_col3, #T_7b98f_row2_col0, #T_7b98f_row2_col3, #T_7b98f_row3_col0, #T_7b98f_row3_col2 {
  background-color: yellow;
}
</style>
<table id="T_7b98f">
  <caption>Corellation All Data</caption>
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_7b98f_level0_col0" class="col_heading level0 col0" >Sepal Length</th>
      <th id="T_7b98f_level0_col1" class="col_heading level0 col1" >Sepal Width</th>
      <th id="T_7b98f_level0_col2" class="col_heading level0 col2" >Petal Length</th>
      <th id="T_7b98f_level0_col3" class="col_heading level0 col3" >Petal Width</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_7b98f_level0_row0" class="row_heading level0 row0" >Sepal Length</th>
      <td id="T_7b98f_row0_col0" class="data row0 col0" >1.00</td>
      <td id="T_7b98f_row0_col1" class="data row0 col1" >-0.11</td>
      <td id="T_7b98f_row0_col2" class="data row0 col2" >0.87</td>
      <td id="T_7b98f_row0_col3" class="data row0 col3" >0.82</td>
    </tr>
    <tr>
      <th id="T_7b98f_level0_row1" class="row_heading level0 row1" >Sepal Width</th>
      <td id="T_7b98f_row1_col0" class="data row1 col0" >-0.11</td>
      <td id="T_7b98f_row1_col1" class="data row1 col1" >1.00</td>
      <td id="T_7b98f_row1_col2" class="data row1 col2" >-0.42</td>
      <td id="T_7b98f_row1_col3" class="data row1 col3" >-0.36</td>
    </tr>
    <tr>
      <th id="T_7b98f_level0_row2" class="row_heading level0 row2" >Petal Length</th>
      <td id="T_7b98f_row2_col0" class="data row2 col0" >0.87</td>
      <td id="T_7b98f_row2_col1" class="data row2 col1" >-0.42</td>
      <td id="T_7b98f_row2_col2" class="data row2 col2" >1.00</td>
      <td id="T_7b98f_row2_col3" class="data row2 col3" >0.96</td>
    </tr>
    <tr>
      <th id="T_7b98f_level0_row3" class="row_heading level0 row3" >Petal Width</th>
      <td id="T_7b98f_row3_col0" class="data row3 col0" >0.82</td>
      <td id="T_7b98f_row3_col1" class="data row3 col1" >-0.36</td>
      <td id="T_7b98f_row3_col2" class="data row3 col2" >0.96</td>
      <td id="T_7b98f_row3_col3" class="data row3 col3" >1.00</td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_6fc16_row0_col1, #T_6fc16_row1_col0 {
  background-color: yellow;
}
</style>
<table id="T_6fc16">
  <caption>Iris-setosa Correlation</caption>
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_6fc16_level0_col0" class="col_heading level0 col0" >Sepal Length</th>
      <th id="T_6fc16_level0_col1" class="col_heading level0 col1" >Sepal Width</th>
      <th id="T_6fc16_level0_col2" class="col_heading level0 col2" >Petal Length</th>
      <th id="T_6fc16_level0_col3" class="col_heading level0 col3" >Petal Width</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_6fc16_level0_row0" class="row_heading level0 row0" >Sepal Length</th>
      <td id="T_6fc16_row0_col0" class="data row0 col0" >1.00</td>
      <td id="T_6fc16_row0_col1" class="data row0 col1" >0.75</td>
      <td id="T_6fc16_row0_col2" class="data row0 col2" >0.26</td>
      <td id="T_6fc16_row0_col3" class="data row0 col3" >0.28</td>
    </tr>
    <tr>
      <th id="T_6fc16_level0_row1" class="row_heading level0 row1" >Sepal Width</th>
      <td id="T_6fc16_row1_col0" class="data row1 col0" >0.75</td>
      <td id="T_6fc16_row1_col1" class="data row1 col1" >1.00</td>
      <td id="T_6fc16_row1_col2" class="data row1 col2" >0.18</td>
      <td id="T_6fc16_row1_col3" class="data row1 col3" >0.28</td>
    </tr>
    <tr>
      <th id="T_6fc16_level0_row2" class="row_heading level0 row2" >Petal Length</th>
      <td id="T_6fc16_row2_col0" class="data row2 col0" >0.26</td>
      <td id="T_6fc16_row2_col1" class="data row2 col1" >0.18</td>
      <td id="T_6fc16_row2_col2" class="data row2 col2" >1.00</td>
      <td id="T_6fc16_row2_col3" class="data row2 col3" >0.31</td>
    </tr>
    <tr>
      <th id="T_6fc16_level0_row3" class="row_heading level0 row3" >Petal Width</th>
      <td id="T_6fc16_row3_col0" class="data row3 col0" >0.28</td>
      <td id="T_6fc16_row3_col1" class="data row3 col1" >0.28</td>
      <td id="T_6fc16_row3_col2" class="data row3 col2" >0.31</td>
      <td id="T_6fc16_row3_col3" class="data row3 col3" >1.00</td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_6f7ec_row0_col2, #T_6f7ec_row2_col0, #T_6f7ec_row2_col3, #T_6f7ec_row3_col2 {
  background-color: yellow;
}
</style>
<table id="T_6f7ec">
  <caption>Iris-versicolor Correlation</caption>
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_6f7ec_level0_col0" class="col_heading level0 col0" >Sepal Length</th>
      <th id="T_6f7ec_level0_col1" class="col_heading level0 col1" >Sepal Width</th>
      <th id="T_6f7ec_level0_col2" class="col_heading level0 col2" >Petal Length</th>
      <th id="T_6f7ec_level0_col3" class="col_heading level0 col3" >Petal Width</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_6f7ec_level0_row0" class="row_heading level0 row0" >Sepal Length</th>
      <td id="T_6f7ec_row0_col0" class="data row0 col0" >1.00</td>
      <td id="T_6f7ec_row0_col1" class="data row0 col1" >0.53</td>
      <td id="T_6f7ec_row0_col2" class="data row0 col2" >0.75</td>
      <td id="T_6f7ec_row0_col3" class="data row0 col3" >0.55</td>
    </tr>
    <tr>
      <th id="T_6f7ec_level0_row1" class="row_heading level0 row1" >Sepal Width</th>
      <td id="T_6f7ec_row1_col0" class="data row1 col0" >0.53</td>
      <td id="T_6f7ec_row1_col1" class="data row1 col1" >1.00</td>
      <td id="T_6f7ec_row1_col2" class="data row1 col2" >0.56</td>
      <td id="T_6f7ec_row1_col3" class="data row1 col3" >0.66</td>
    </tr>
    <tr>
      <th id="T_6f7ec_level0_row2" class="row_heading level0 row2" >Petal Length</th>
      <td id="T_6f7ec_row2_col0" class="data row2 col0" >0.75</td>
      <td id="T_6f7ec_row2_col1" class="data row2 col1" >0.56</td>
      <td id="T_6f7ec_row2_col2" class="data row2 col2" >1.00</td>
      <td id="T_6f7ec_row2_col3" class="data row2 col3" >0.79</td>
    </tr>
    <tr>
      <th id="T_6f7ec_level0_row3" class="row_heading level0 row3" >Petal Width</th>
      <td id="T_6f7ec_row3_col0" class="data row3 col0" >0.55</td>
      <td id="T_6f7ec_row3_col1" class="data row3 col1" >0.66</td>
      <td id="T_6f7ec_row3_col2" class="data row3 col2" >0.79</td>
      <td id="T_6f7ec_row3_col3" class="data row3 col3" >1.00</td>
    </tr>
  </tbody>
</table>




<style>
.yellow {
  background-color: yellow;
}
</style>
<table id="T_cc659">
  <caption>Iris-virginica Correlation</caption>
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_cc659_level0_col0" class="col_heading level0 col0" >Sepal Length</th>
      <th id="T_cc659_level0_col1" class="col_heading level0 col1" >Sepal Width</th>
      <th id="T_cc659_level0_col2" class="col_heading level0 col2" >Petal Length</th> 
      <th id="T_cc659_level0_col3" class="col_heading level0 col3" >Petal Width</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_cc659_level0_row0" class="row_heading level0 row0" >Sepal Length</th>
      <td id="T_cc659_row0_col0" class="data row0 col0" >1.00</td>
      <td id="T_cc659_row0_col1" class="data row0 col1" >0.46</td>
      <td id="T_cc659_row0_col2" class="data row0 col2" >0.86</td>
      <td id="T_cc659_row0_col3" class="data row0 col3" >0.28</td>
    </tr>
    <tr>
      <th id="T_cc659_level0_row1" class="row_heading level0 row1" >Sepal Width</th>
      <td id="T_cc659_row1_col0" class="data row1 col0" >0.46</td>
      <td id="T_cc659_row1_col1" class="data row1 col1" >1.00</td>
      <td id="T_cc659_row1_col2" class="data row1 col2" >0.40</td>
      <td id="T_cc659_row1_col3" class="data row1 col3" >0.54</td>
    </tr>
    <tr>
      <th id="T_cc659_level0_row2" class="row_heading level0 row2" >Petal Length</th>
      <td id="T_cc659_row2_col0" class="data row2 col0" >0.86</td>
      <td id="T_cc659_row2_col1" class="data row2 col1" >0.40</td>
      <td id="T_cc659_row2_col2" class="data row2 col2" >1.00</td>
      <td id="T_cc659_row2_col3" class="data row2 col3" >0.32</td>
    </tr>
    <tr>
      <th id="T_cc659_level0_row3" class="row_heading level0 row3" >Petal Width</th>
      <td id="T_cc659_row3_col0" class="data row3 col0" >0.28</td>
      <td id="T_cc659_row3_col1" class="data row3 col1" >0.54</td>
      <td id="T_cc659_row3_col2" class="data row3 col2" >0.32</td>
      <td id="T_cc659_row3_col3" class="data row3 col3" >1.00</td>
    </tr>
  </tbody>
</table>








## References:
1. Fisher's Iris Dataset: https://archive.ics.uci.edu/ml/datasets/iris
2. Iris data set wiki page: https://en.wikipedia.org/wiki/Iris_flower_data_set
3. Seaborn histograms: https://seaborn.pydata.org/generated/seaborn.histplot.html?highlight=histplot#seaborn.histplot
4. https://en.wikipedia.org/wiki/Linear_discriminant_analysis
5. https://stackoverflow.com/questions/31247198/python-pandas-write-content-of-dataframe-into-text-file (accessed Apr 15 2023).
6. Pandas documentation, https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_string.html (accessed Apr 15 2023).
7. Stack Overflow "How to delete the contents of a folder", https://stackoverflow.com/questions/185936/how-to-delete-the-contents-of-a-folder (accessed Apr 16 2023).
8. Seaborn Documentation, Pairplots https://seaborn.pydata.org/generated/seaborn.pairplot.html (accessed Apr 16 2023).
9. https://stackoverflow.com/questions/51579215/remove-seaborn-lineplot-legend-title (acccessed Apr 18 2023)
https://stackoverflow.com/questions/40950310/strip-trim-all-strings-of-a-dataframe
https://pandas.pydata.org/pandas-docs/stable/user_guide/style.html
https://jovian.com/suresh-kumar-m/python-matplotlib-data-visualization
https://stackoverflow.com/questions/60598837/html-to-image-using-python
https://stackoverflow.com/questions/29530355/plotting-multiple-histograms-in-grid
Box plots and legends https://stackoverflow.com/questions/62252493/create-a-single-legend-for-multiple-plot-in-matplotlib-seaborn
Subplotshttps://dev.to/thalesbruno/subplotting-with-matplotlib-and-seaborn-5ei8