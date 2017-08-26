import pandas as pd
stu_df = pd.DataFrame()
stu_df = pd.read_excel('student.xlsx', sheet_name = 'score')
stu_df['sum'] = stu_df['python'] + stu_df['math']
stu_df.to_excel('student.xlsx', sheet_name = 'scores')