def ParseDict(records):
  L=[]
  for R in records:
   d=dict(R)
   L.append(d) 
  return(L)


def ParseSingleDict(cursor):
  schema=cursor.description
  record=cursor.fetchone()
  rec={}
  for i in range(len(record)):
      rec[schema[i][0]]=record[i]
  return (rec)


def ParseDictMultipleRecord(cursor):
 
  schema=cursor.description
  #print(schema)

  record=cursor.fetchall()
  #print("Record:",record)
  rec=[]
  for row in record:
    R={}
    for i in range(len(row)):
       R[schema[i][0]]=row[i]
    rec.append(R)    
  return(rec)