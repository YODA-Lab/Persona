import pandas as pd

df = pd.read_csv('test_data.csv')
df = df.iloc[:, 17:]
df = df.iloc[:, :-6]

df = df.drop(df.columns[1:7], axis=1)

df = df.drop(0)
df = df.drop(1)

df = df[~((df['Consent Form'] != 'I agree') | (df['AI name'] != 'Blitzcrank') | (df['Suggestion place'] != 'Luminara Gardens'))]


df.insert(0, 'Number', range(1, len(df) + 1))

df.to_csv('extracted_data.csv', index=False)

