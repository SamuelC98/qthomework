import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
import numpy as np
from datetime import datetime
import talib as ta
import pandas as pd
import warnings
import talib.abstract
warnings.filterwarnings('ignore')


df = pd.read_excel('sz50.xlsx', sheet_name=None, index_col=0)


data = df.copy()
for i in (df.keys()):
    if(df[i].empty):
        data.pop(i)
print(data.keys())



nArray = data['600036.XSHG']['close'].values
ma10=talib.SMA(nArray, timeperiod=10)
print(type(nArray))
print(ma10[ma10.size-5:ma10.size])

ma10Series = pd.DataFrame(ma10,index=data['600036.XSHG'].index)

plt.plot(data['600036.XSHG'].index,data['600036.XSHG']['close'])
plt.plot(ma10Series.index,ma10Series)
plt.show()

#用talib计算50只股票的周期为5的ROCR100，生成Dataframe
dateIndex=data['600000.XSHG'].index
#某几支股票的date不全，取全index按索引添加
ROCR100df=pd.DataFrame(index=dateIndex)
for name in data.keys():
    closeArray = data[name]['close'].values
    ROCR100Array=talib.ROCR100(closeArray,timeperiod = 20)
    ROCR100=pd.DataFrame(ROCR100Array,index=data[name].index.values,columns=[name])
    ROCR100df=pd.merge(ROCR100df,ROCR100,left_index=True,right_index=True,how='left')

p1,=plt.plot(ROCR100df.index,ROCR100df.iloc[:,0])
p2,=plt.plot(ROCR100df.index,ROCR100df.iloc[:,1])
p3,=plt.plot(ROCR100df.index,ROCR100df.iloc[:,2])
p4,=plt.plot(ROCR100df.index,ROCR100df.iloc[:,3])
p5,=plt.plot(ROCR100df.index,ROCR100df.iloc[:,4])
plt.legend([p1,p2,p3,p4,p5],ROCR100df.columns.values[0:5])
plt.show()

