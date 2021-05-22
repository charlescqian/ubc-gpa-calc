# ubc-gpa-calc
Simple script to calculate one's GPA at UBC on a 4.0 scale. Requires the user copy and paste their grade summary into a csv currently. 

## Usage Instructions

1. Install Python 3
2. Install Pip
3. Download the `gpacalc.py` file into a folder
3. Run `pip install pandas`
4. Go to your grades summary on SSC and copy paste the entire table, including the headers (Course, Section, Grade, etc.) into a `grades.csv` file in the same folder (can copy into Google Sheets and save as .csv). Make sure the headers are in the very first row. It should look something like this:

Course | Section | Grade | Letter | Session | Term | Program | Year | Credits Earned | Class Avg | Standing
 ---   | ---     | ---   | ---    | ---     | ---  | ---     | ---  | ---            |  ---      | --- 
MATH 100| 101 | 85 | A | 2020W | 1 | BASC | 1 | 3.0 | 70 | 
5. Run `python3 gpacalc.py` in your command line in the same folder

## Future
Turn this into a bookmarklet or something more user friendly


