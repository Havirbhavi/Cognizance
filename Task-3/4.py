import pandas as pd
ser = pd.Series(['amrita', 'school', 'of', 'engineering', 'chennai' , 'campus'])
Series = ser.map(lambda x: x[0].upper() + x[1:-1] + x[-1].lower())
print(' '.join(Series))
