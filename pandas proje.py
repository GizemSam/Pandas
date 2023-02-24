#Görev 1: Seaborn kütüphanesi içerisinden Titanic veri setini tanımlayınız.

import pandas as pd
import seaborn as sns
df = sns.load_dataset("titanic")

pd.set_option("display.width", 500)

#Görev 2: Titanic veri setindeki kadın ve erkek yolcuların sayısını bulunuz.

df.head()
pd.set_option("display.max_columns", None)

df[df["sex"] == "male"]["sex"].count()

df[df["sex"] == "female"]["sex"].count()

###df["sex"].value_counts()

#Görev 3: Her bir sutuna ait unique değerlerin sayısını bulunuz.

df.nunique()

#Görev 4: pclass değişkeninin unique değerlerinin sayısını bulunuz.

df["pclass"].unique()       # birtane ise bu

#Görev 5: pclass ve parch değişkenlerinin unique değerlerinin sayısını bulunuz.

df[["pclass","parch"]].nunique()            ##birden fazla değere bakacaksak nunique()

#Görev 6: embarked değişkeninin tipini kontrol ediniz. Tipini category olarak değiştiriniz ve tekrar kontrol ediniz

type("embarked")

df["embarked"].astype("category")

#Görev 7: embarked değeri C olanların tüm bilgelerini gösteriniz.

df[df["embarked"] == "C"].head()

#Görev 8: embarked değeri S olmayanların tüm bilgelerini gösteriniz.

df[df["embarked"] != "S"].head()

#Görev 9: Yaşı 30 dan küçük ve kadın olan yolcuların tüm bilgilerini gösteriniz.

df.loc[(df["age"] < 30) & (df["sex"] == "female")].head()

#Görev 10: Fare'i 500'den büyük veya yaşı 70’den büyük yolcuların bilgilerini gösteriniz.

df.loc[ (df["age"] > 70) | (df["fare"] > 500 )].head()

#Görev 11: Her bir değişkendeki boş değerlerin toplamını bulunuz.

df.isnull().sum()

# Görev 12: who değişkenini dataframe’den çıkarınız.

df.drop(['who'], axis=1).head()

#Görev 13: deck değikenindeki boş değerleri deck değişkenin en çok tekrar eden değeri (mode) ile doldurunuz.

df["deck"] = df["deck"].fillna(df["deck"].mode()[0])

df["deck"]

df

#Görev 14: age değikenindeki boş değerleri age değişkenin medyanı ile doldurunuz.

# df['age'].median() medyan bulma

df["age"].fillna(df['age'].median()).head()

#Görev 15: survived değişkeninin pclass ve cinsiyet değişkenleri kırılımınında sum, count, mean değerlerini bulunuz.

df.groupby(["sex", "pclass"]).agg({"survived": ["mean","count", "sum"]})

#Görev 16: 30 yaşın altında olanlar 1, 30'a eşit ve üstünde olanlara 0
# verecek bir fonksiyon yazın. Yazdığınız fonksiyonu kullanarak titanik veri
#setinde age_flag adında bir değişken oluşturunuz oluşturunuz. (apply ve lambda yapılarını kullanınız.)


df["age_flag"] = [0 if col >= 30 else 1 for col in df["age"]]

# Görev 17: Seaborn kütüphanesi içerisinden Tips veri setini tanımlayınız.
import pandas as pd
import seaborn as sns
df = sns.load_dataset("tips")

#Görev 18: Time değişkeninin kategorilerine (Dinner, Lunch) göre total_bill değerinin sum, min, max ve mean değerlerini bulunuz.

df.groupby(["time"]).agg({"total_bill": ["max","min", "sum"]})

#Görev 19: Day ve time’a göre total_bill değerlerinin sum, min, max ve mean değerlerini bulunuz.

df.groupby(["time", "day"]).agg({"total_bill": ["max","min", "sum","mean"]})

#Görev 20: Lunch zamanına ve kadın müşterilere ait total_bill ve tip değerlerinin day'e göre sum, min, max ve mean değerlerini bulunuz.


### total_bill ve tip değerlerinin day'e göre sum, min, max ve mean değerlerini bulduk
df.groupby([ "day"]).agg({"total_bill": ["max", "min", "sum","mean"],
                                 "tip": ["max", "min", "sum","mean"]})

### time ı lunch olan ve cinsiyeti kadın olanları listeledik. ilk 5 ine  baktık.

df.loc[(df["time"] == "Lunch") & (df["sex"] == "Female")].head()

###iki formülü birleştirelim.

df.loc[(df["time"] == "Lunch") & (df["sex"] == "Female")].groupby([ "day"]).agg({"total_bill": ["max", "min", "sum","mean"],
                                 "tip": ["max", "min", "sum","mean"]})

#Görev 21: size'i 3'ten küçük, total_bill'i 10'dan büyük olan siparişlerin ortalaması nedir? (loc kullanınız)

dff = df.loc[(df["size"] < 3) & (df["total_bill"] > 10)]
dff.head().mean()

#Görev 22: total_bill_tip_sum adında yeni bir değişken oluşturunuz. Her bir müşterinin ödediği totalbill ve tip in toplamını versin.

df["total_bill_tip_sum"] = df["total_bill"] + df["tip"]

df.head()


#Görev 23: total_bill_tip_sum değişkenine göre büyükten
# küçüğe sıralayınız ve ilk 30 kişiyi yeni bir dataframe'e atayınız.

new_df = df.sort_values("total_bill_tip_sum", ascending= False).head(30)


