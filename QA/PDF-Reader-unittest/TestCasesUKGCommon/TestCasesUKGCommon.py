import unittest
import pandas as pd
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.filterwarnings("ignore", category=DeprecationWarning)
import numpy as np

class ExcelTest(unittest.TestCase):

    def test_UKGC_1(self):

        # Loads the Excel file into a DataFram
        df = pd.read_excel('QA/Output Files/OUTPUT UKGCommon/UKG Common Empty.xlsx', header=None)

        # Gets the number of rows with data beyond the headers
        num_data_rows = len(df) - 1 

        # Check if there are additional rows with data
        if num_data_rows > 0:

            self.fail("There are {} additional rows with data in the Excel file".format(num_data_rows))
        
        print(".TEST 1 UKGCommon CORRECT: The UKG Common Empty.xlsx file not contains additional rows to the header")
    
    def test_UKGC_2(self):
        # Description: Check last shift is present
        # File: Martin ppe
        # Upload Excel file
        excel_file = 'QA/Output Files/OUTPUT UKGCommon/Martin ppe 4.22.23.xlsx'
        df = pd.read_excel(excel_file, sheet_name='Sheet1')

        # Specify the search criteria
        name = 'WARREN, DANIELLE'
        date = '04/22/2023'
        paycode = 'Regular'
        hours = 11.00

        # Create a list of tuples containing the expected values and their corresponding column names
        expected_values = [
            (name, 'NAME'),
            (date, 'DATE'),
            (paycode, 'PAYCODE'),
            (hours, 'HOURS')
        ]

        missing_values = []
        for value, column in expected_values:
            if value not in df[column].values:
                missing_values.append(f"{column}: {value}")

        if missing_values:
            error_message = f"The following value(s) did not match in the Excel file:\n\n"
            error_message += "\n".join(missing_values)
            values_found = df.loc[df['NAME'] == name, ['NAME', 'DATE', 'PAYCODE', 'HOURS']]
            self.fail(f"{error_message}\n\nValues found:\n\n{values_found.to_string(index=False)}")
        else:
            filtered_df = df[
                (df['NAME'] == name) &
                (df['DATE'] == date) &
                (df['PAYCODE'] == paycode) &
                (df['HOURS'] == hours)
            ]
            if filtered_df.empty:
                self.fail("No matching row was found in the Excel file.")
            else:
                self.assertEqual(len(filtered_df), 1, 'Multiple matches found in Excel file.')
                print("TEST 2 UKGCommon CORRECT: Data for WARREN, DANIELLE was found and is correct in file Martin ppe 4.22.23.")
   
    #Methods required for test_UKGC_3

    def compare_excel_files(self, original_file, new_file):
        
        # Loads the original Excel file in a DataFrame
        original_df = pd.read_excel(original_file, sheet_name="Sheet1")

        # Loads the new Excel file in a DataFrame
        new_df = pd.read_excel(new_file, sheet_name="Sheet1")

        # Verify that the DataFrames are equal
        self.assertTrue(
            original_df.equals(new_df),
            self.generate_difference_message(original_df, new_df, original_file, new_file),
        )

    def generate_difference_message(self, original_df, new_df, original_file, new_file):
        original_df = original_df.fillna("NA")
        new_df = new_df.fillna("NA")

        diff_df = original_df != new_df
        diff_indices = diff_df.any(axis=1)

        diff_message = f"Differences found between {original_file} and {new_file}:\n"
        for index, row in diff_df[diff_indices].iterrows():
            diff_message += f"Row {index+2}:\n"
            for column, value in row.items():
                if value:
                    original_value = original_df.at[index, column]
                    new_value = new_df.at[index, column]
                    diff_message += f"  - Column '{column}': Original='{original_value}', New='{new_value}'\n"

        return diff_message

    #Descrition: Check Exe has the same data as last commit
    #Files: Martin ppe 4.22.23, martin b, time martin a ORIG

    def test_UKGC_3_1(self):
        self.compare_excel_files("QA/PDF-Reader-unittest/TestCasesUKGCommon/Martin ppe 4.22.23 ORIG.xlsx", "QA/Output Files/OUTPUT UKGCommon/Martin ppe 4.22.23.xlsx")
        print("TEST 3.1 UKGCommon CORRECT: Martin ppe 4.22.23.xlsx data match the original version")


    def test_UKGC_3_2(self):
        self.compare_excel_files("QA/PDF-Reader-unittest/TestCasesUKGCommon/martin time a ORIG.xlsx", "QA/Output Files/OUTPUT UKGCommon/martin time a.xlsx")
        print("TEST 3.2 UKGCommon CORRECT: martin time a ORIG.xlsx data match the original version")

    def test_UKGC_4(self):
        excel_file = "QA/Output Files/OUTPUT UKGCommon/Martin ppe 4.22.23.xlsx"
        sheet_name = "Sheet1"
        data = pd.read_excel(excel_file, sheet_name=sheet_name)
        name_column = "NAME"
        Comment_column = "Comments"

        # Filter rows with "AUGUSTE, LOURDJINA" in column "NAME".
        filtered_rows = data[data[name_column] == "AUGUSTE, LOURDJINA"]

        expected_comments = [
            "CC/MARTIN/MARTINNORTHHOSPITAL/CNO/NRS/INPAT-CLINICALDECISIONUNIT2W/RN |  AGRN,00,NON,DED,SNN,N",
            "CC/MARTIN/MARTINNORTHHOSPITAL/CNO/NRS/INPAT-CLINICALDECISIONUNIT2W/RN | Incorrect Soft Key Selected AGRN,00,NON,DED,SNN,N",
            ""
        ]

        for index, row in filtered_rows.iterrows():
            comment_value = row[Comment_column]

            error_message = f"Error: The Comment value for row {index + 2} is not one of the expected values"

            # Check if the comment value is NaN
            if pd.isna(comment_value):
                comment_value = ""

            self.assertIn(comment_value, expected_comments, error_message)

        print("TEST 4 UKGCommon CORRECT: For AUGUSTE, LOURDJINA the comments match the expected values")

    def test_UKGC_5(self):
        excel_file = "QA/Output Files/OUTPUT UKGCommon/Martin ppe 4.22.23.xlsx"
        sheet_name = "Sheet1"
        data = pd.read_excel(excel_file, sheet_name=sheet_name)
        name_column = "NAME"
        date_column = "DATE"
        glcode_column = "GLCODE"

        # Filter rows with "AUGUSTE, LOURDJINA" in column "NAME".
        filtered_rows = data[data[name_column] == "AUGUSTE, LOURDJINA"]

        for index, row in filtered_rows.iterrows():
            date_value = row[date_column]
            glcode_value = row[glcode_column]

            expected_glcode = "3100-3100-31812" if date_value == "04/22/2023" else "3100-3100-31429"
            error_message = f"Error: The GLCODE value for row {index + 2} is not '{expected_glcode}'"
            self.assertEqual(glcode_value, expected_glcode, error_message)

        print ("TEST 5 UKGCommon CORRECT: For AUGUSTE, LOURDJINA the GLCODES match those in the PDF")

    def test_UKGC_6_1(self):
        self.compare_excel_files("QA/PDF-Reader-unittest/TestCasesUKGCommon/martin b ORIG.xlsx", "QA/Output Files/OUTPUT UKGCommon/martin b.xlsx")
        print("TEST 6.1 UKGCommon CORRECT: martin b ORIG.xlsx data match the original version")

    def test_UKGC_6_2(self):
        self.compare_excel_files("QA/PDF-Reader-unittest/TestCasesUKGCommon/Martin Holiday Shifts 7.3 to 7.5.23 ORIG.xlsx", "QA/Output Files/OUTPUT UKGCommon/Martin Holiday Shifts 7.3 to 7.5.23.xlsx")
        print("TEST 6.2 UKGCommon CORRECT: Martin Holiday Shifts 7.3 to 7.5.23.xlsx data match the original version")

    def test_UKGC_8(self):
        filename = "QA/Output Files/OUTPUT UKGCommon/Martin Holiday Shifts 7.3 to 7.5.23.xlsx"
        target_paycode = "RNTBS-Request / Not To Be Sched"
        target_rows = [9, 10, 11, 135, 134]

        try:
            df = pd.read_excel(filename, sheet_name="Sheet1")
            error_messages = {}

            for row_num in target_rows:
                if row_num <= df.shape[0]:
                    paycode_value = df.at[row_num - 2, "PAYCODE"]
                    if pd.isna(paycode_value) or paycode_value != target_paycode:
                        if row_num not in error_messages:
                            error_messages[row_num] = []
                        if pd.isna(paycode_value):
                            error_messages[row_num].append(f"Empty PAYCODE in Row: {row_num}")
                        elif "RNTBS-Request" in paycode_value and "Not To Be Sched" not in paycode_value:
                            error_messages[row_num].append(f"Incomplete PAYCODE in Row: {row_num}, PAYCODE: {paycode_value}")
                        else:
                            error_messages[row_num].append(f"Invalid PAYCODE in Row: {row_num}, PAYCODE: {paycode_value}")

            if len(error_messages) > 0:
                error_message = ""
                for row_num, errors in error_messages.items():
                    error_message += "\n".join(errors) + "\n"
                self.fail(error_message)
            else:
                print(f"TEST 8 UKG Common CORRECT: The file {filename} column PAYCODE new PAYCODE is correct")
        except Exception as e:
            self.fail(f"An error occurred while processing {filename}: {str(e)}")
            
if __name__ == '__main__':
    unittest.main()
