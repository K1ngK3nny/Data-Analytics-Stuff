

```python
# dependencies
import csv
import pandas as pd
import numpy as np
import os

```


```python
school_file = "schools_complete.csv"
student_file = "students_complete.csv"
school_df = pd.read_csv(school_file)
student_df = pd.read_csv(student_file)


```


```python
students_df = student_df.rename(columns = {'name':'Student Name', 'school':'School Name'})
schools_df = school_df.rename(columns = {'name':'School Name'})


```


```python
avg_math_score = student_df["math_score"].mean()
total_students = student_df["Student ID"].max()
total_budget = schools_df["budget"].sum()
total_schools = schools_df["School ID"].max() + 1
students_pm = student_df.loc[(student_df["math_score"] >70)]
students_pr = student_df.loc[(student_df["reading_score"] > 70)]
num_pr = students_pr["reading_score"].count()
num_pm = students_pm["math_score"].count()
pct_passing_math = (num_pm/total_students) * 100
pct_passing_reading = (num_pr/total_students) * 100
passing_rate = (pct_passing_math + pct_passing_reading)/2


```


```python
District_Summary = pd.DataFrame({"Average Math Score": [avg_math_score],  
                                 "Total Budget": [total_budget],
                                 "Total Students": [total_students],
                                 "Total Schools": [total_schools],
                                "Percent Passing Math": [pct_passing_math],
                                "Percent Passing Reading": [pct_passing_reading],
                                "Overall Passing Rate": [passing_rate]})

District_Summary.set_index("Total Schools")
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Average Math Score</th>
      <th>Overall Passing Rate</th>
      <th>Percent Passing Math</th>
      <th>Percent Passing Reading</th>
      <th>Total Budget</th>
      <th>Total Students</th>
    </tr>
    <tr>
      <th>Total Schools</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>15</th>
      <td>78.985371</td>
      <td>77.683883</td>
      <td>72.393985</td>
      <td>82.97378</td>
      <td>24649428</td>
      <td>39170</td>
    </tr>
  </tbody>
</table>
</div>




```python
schools_df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>School ID</th>
      <th>School Name</th>
      <th>type</th>
      <th>size</th>
      <th>budget</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>Huang High School</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>Figueroa High School</td>
      <td>District</td>
      <td>2949</td>
      <td>1884411</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Shelton High School</td>
      <td>Charter</td>
      <td>1761</td>
      <td>1056600</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>Hernandez High School</td>
      <td>District</td>
      <td>4635</td>
      <td>3022020</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Griffin High School</td>
      <td>Charter</td>
      <td>1468</td>
      <td>917500</td>
    </tr>
  </tbody>
</table>
</div>




```python
school_name = schools_df.set_index(["School Name"])["type"]
school_type = schools_df.loc[:, ['type']]
total_students = (student_df["Student ID"].max()) + 1
total_budget = schools_df['budget'].sum()
per_student = total_budget/total_students
avg_ms = student_df["math_score"].mean()
avg_rs = student_df["reading_score"].mean()
students_pm = student_df.loc[(student_df["math_score"] >70)]
students_pr = student_df.loc[(student_df["reading_score"] >70)]
num_pm = students_pm["math_score"].count()
num_pr = students_pr["reading_score"].count()
pct_pm = (num_pm/total_students) * 100
pct_pr = (num_pr/total_students) * 100
ovr_pr = (pct_pm + pct_pr)/2

```


```python
School_Summary = pd.DataFrame({"School Name": school_name,
                               "School Type": school_type,
                              "Total Students": total_students,
                              "Total Budget": total_budget,
                              "Per Student Budget": per_student,
                              "Average Math Score": avg_ms,
                              "Average Reading Score": avg_rs,
                              "Percent Passing Math": pct_pm,
                              "Percent Passing Reading": pct_pr,
                              "Overall Passing Rate": ovr_pr})

School_Summary = School_Summary[['School Name', 'School Type', 'Total Students', 'Total Budget', 'Per Student Budget', 'Average Math Score', 'Average Reading Score', 'Percent Passing Math', 'Percent Passing Reading', 'Overall Passing Rate']] 
School_Summary["Total School Budget"] = School_Summary["Total Students"].map("${:,.2f}".format)
School_Summary["Per Student Budget"] = School_Summary["Per Student Budget"].map("${:,.2f}".format)
```


```python
School_Summary.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>School Name</th>
      <th>School Type</th>
      <th>Total Students</th>
      <th>Total Budget</th>
      <th>Per Student Budget</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>Percent Passing Math</th>
      <th>Percent Passing Reading</th>
      <th>Overall Passing Rate</th>
      <th>Total School Budget</th>
    </tr>
    <tr>
      <th>School Name</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Huang High School</th>
      <td>District</td>
      <td>(t, y, p, e)</td>
      <td>39170</td>
      <td>24649428</td>
      <td>$629.29</td>
      <td>78.985371</td>
      <td>81.87784</td>
      <td>72.392137</td>
      <td>82.971662</td>
      <td>77.681899</td>
      <td>$39,170.00</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <td>District</td>
      <td>(t, y, p, e)</td>
      <td>39170</td>
      <td>24649428</td>
      <td>$629.29</td>
      <td>78.985371</td>
      <td>81.87784</td>
      <td>72.392137</td>
      <td>82.971662</td>
      <td>77.681899</td>
      <td>$39,170.00</td>
    </tr>
    <tr>
      <th>Shelton High School</th>
      <td>Charter</td>
      <td>(t, y, p, e)</td>
      <td>39170</td>
      <td>24649428</td>
      <td>$629.29</td>
      <td>78.985371</td>
      <td>81.87784</td>
      <td>72.392137</td>
      <td>82.971662</td>
      <td>77.681899</td>
      <td>$39,170.00</td>
    </tr>
    <tr>
      <th>Hernandez High School</th>
      <td>District</td>
      <td>(t, y, p, e)</td>
      <td>39170</td>
      <td>24649428</td>
      <td>$629.29</td>
      <td>78.985371</td>
      <td>81.87784</td>
      <td>72.392137</td>
      <td>82.971662</td>
      <td>77.681899</td>
      <td>$39,170.00</td>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <td>Charter</td>
      <td>(t, y, p, e)</td>
      <td>39170</td>
      <td>24649428</td>
      <td>$629.29</td>
      <td>78.985371</td>
      <td>81.87784</td>
      <td>72.392137</td>
      <td>82.971662</td>
      <td>77.681899</td>
      <td>$39,170.00</td>
    </tr>
  </tbody>
</table>
</div>




```python
students_df = student_df.rename(columns = {'school': 'School Name'})
```


```python
merged_df = pd.merge(students_df, schools_df, on='School Name')
merged_df.drop(["School ID"], axis=1).head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Student ID</th>
      <th>name</th>
      <th>gender</th>
      <th>grade</th>
      <th>School Name</th>
      <th>reading_score</th>
      <th>math_score</th>
      <th>type</th>
      <th>size</th>
      <th>budget</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>Paul Bradley</td>
      <td>M</td>
      <td>9th</td>
      <td>Huang High School</td>
      <td>66</td>
      <td>79</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>Victor Smith</td>
      <td>M</td>
      <td>12th</td>
      <td>Huang High School</td>
      <td>94</td>
      <td>61</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Kevin Rodriguez</td>
      <td>M</td>
      <td>12th</td>
      <td>Huang High School</td>
      <td>90</td>
      <td>60</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>Dr. Richard Scott</td>
      <td>M</td>
      <td>12th</td>
      <td>Huang High School</td>
      <td>67</td>
      <td>58</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Bonnie Ray</td>
      <td>F</td>
      <td>9th</td>
      <td>Huang High School</td>
      <td>97</td>
      <td>84</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
    </tr>
  </tbody>
</table>
</div>




```python
#avg_ms_by_grade = merged_df.groupby('School Name').head()
#merged_df["Average Math Score"].math_score.mean().head()

```


```python
#reduced_df = avg_ms_by_grade.loc[:,['grade','School Name']]
#reduced_df.drop_duplicates('School Name')
```


```python


avg_rs_by_grade = merged_df.groupby('grade').mean()['reading_score']
avg_rs_by_grade
```




    grade
    10th    81.874410
    11th    81.885714
    12th    81.819851
    9th     81.914358
    Name: reading_score, dtype: float64


