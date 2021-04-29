from csv import reader
from ast import literal_eval
import time
import pandas as pd
import numpy as np
# {'adult': 0, 'belongs_to_collection': 1, 
# 'budget': 2, 'genres': 3, 'homepage': 4, 
# 'id': 5, 'imdb_id': 6, 'original_language': 7, 
# 'original_title': 8, 'overview': 9, 'popularity': 10, 
# 'poster_path': 11, 'production_companies': 12, 
# 'production_countries': 13, 'release_date': 14, 'revenue': 15, 
# 'runtime': 16, 'spoken_languages': 17, 'status': 18, 
# 'tagline': 19, 'title': 20, 'video': 21, 'vote_average': 22, 
# 'vote_count': 23, '': 27}


def adult_check(index, row, adult, prev):
    try:
        flag = literal_eval(adult)
        return row
    except:
        # print('+++++++++++++++')
        prev[-1] = prev[-1] + row.pop(0)
        row = prev + row
        # for h, d in zip(header, (prev+row)):
        #     print(f'{h}: {d}')
        # print(i, row)
        # print('+++++++++++++++')
        return row

def integer_check(index, row, number, prev):
    try:
        x = int(number)
        return row
    except:
        for e in row:
            print(e)
        print(index, '++++++++++++++++++++++++++++++++++++')
        for e in prev:
            print(e)
        print(index, '++++++++++++++++++++++++++++++++++++')

def readFile(f):
    with open(f, 'r') as read_obj:
        csv_reader = reader(read_obj)
        header=next(csv_reader)
        values=range(len(header))
        column=dict(zip(header, values))
        # print(column)

        df = pd.DataFrame(columns=header)

        # print(type(csv_reader))
        if header != None:
            prev = None
            for i, row in enumerate(csv_reader):
                row = adult_check(i, row, row[column['adult']], prev)
                row = integer_check(i, row, row[column['budget']], prev)
                #problematic entries, skip
                if i in [35586, 19729, 29502]:
                    prev = row
                    continue
                row = integer_check(i, row, row[column['revenue']], prev)
                df.append(pd.DataFrame(row, columns=header))
                prev = row
                # try:
                #     if '.jpg' in row[column['production_companies']]:
                #         # print(row[column['production_companies']])
                #         for h, data in zip(header, row):
                #             print(i, f'{h}: {data}')
                #         print('=============================================================')
                # except IndexError:
                #     print('+++++++++++++++')
                #     print(i, row)
                #     print('+++++++++++++++')
                # # try:
                # #     x = int(row[column["budget"]])
                # #     y = int(row[column["revenue"]])
                # # except:
                # #     print(row[column['title']])
        return df

if __name__ == "__main__":
    readFile('./data/movies_metadata.csv')

    
