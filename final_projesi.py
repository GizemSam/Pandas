import numpy as np
import pandas as pd

df = pd.read_csv('persona.csv')
pd.set_option("display.width", 500)
pd.set_option("display.max_columns", None)

################## GÖREV 1 ########################
# Soru 1: persona.csv dosyasını okutunuz ve veri seti ile ilgili genel bilgileri gösteriniz
df.head()
df.shape    #boyut bilgisi
df.info #değişkenlere ait tip bilgisi

# Soru 2:Kaç unique SOURCE vardır? Frekansları nedir?
df["SOURCE"].nunique()  #nunique() sayısını verir unique() bunlar neler onları gösterir
df["SOURCE"].value_counts() # frekans = gözlem sayısı

# Soru 3: Kaç unique PRICE vardır?
df["PRICE"].nunique()

# Soru 4: Hangi PRICE'dan kaçar tane satış gerçekleşmiş?

df["PRICE"].value_counts()

#Soru 5: Hangi ülkeden kaçar tane satış olmuş?

df["COUNTRY"].value_counts()
df.groupby("COUNTRY")["PRICE"].count()

# Soru 6: Ülkelere göre satışlardan toplam ne kadar kazanılmış?

df.groupby("COUNTRY")["PRICE"].sum()
#2.yol
df.groupby("COUNTRY").agg({"PRICE":"sum"})

#Soru 7: SOURCE türlerine göre satış sayıları nedir?

df.groupby("SOURCE")["PRICE"].count()

#2.yol
df["SOURCE"].value_counts()

#Soru 8: Ülkelere göre PRICE ortalamaları nedir?

df.groupby("COUNTRY").agg({"PRICE":"mean"})

# Soru 9: SOURCE'lara göre PRICE ortalamaları nedir?

df.groupby("SOURCE").agg({"PRICE":"mean"})

#Soru 10 :COUNTRY-SOURCE kırılımında PRICE ortalamaları nedir?

df.groupby(by=["COUNTRY", "SOURCE"]).agg({"PRICE":"mean"})

################## GÖREV 2 ########################
#Görev 2: COUNTRY, SOURCE, SEX, AGE kırılımında ortalama kazançlar nedir?

df.groupby(by=["COUNTRY", "SOURCE","SEX","AGE"]).agg({"PRICE":"mean"}).head()


################## GÖREV 3 ########################
#Görev 3: Çıktıyı PRICE’a göre sıralayınız.
df_krlm = df.groupby(by=["COUNTRY", "SOURCE","SEX","AGE"]).agg({"PRICE":"mean"})                #head ı kaldırıyoruz
df_krlm.sort_values("PRICE", ascending= False)
agg_df = df_krlm.sort_values("PRICE", ascending= False)

################## GÖREV 4 ########################
 # Görev 4: Indekste yer alan isimleri değişken ismine çeviriniz.

agg_df = agg_df.reset_index()
agg_df.head()

################## GÖREV 5 ########################
#Görev 5: Age değişkenini kategorik değişkene çeviriniz ve agg_df’e ekleyiniz.

agg_df["AGE"].describe()        ## bi bölme işlemi yapacağımız için

##Ayırma  işlemi yapıyoruz.

age_ktg = [0, 18, 23, 30, 40, agg_df["AGE"].max()]

##Ayırdıklarımızı isimlendiriyoruz

age_name = ["0_18","19_23","24_30","31_40","41 " + str(agg_df["AGE"].max())]

#age yi böldük

agg_df["AGE_CAT"]= pd.cut(agg_df["AGE"], age_ktg, labels = age_name)

agg_df.head()

################## GÖREV 6 ########################

#Görev 6: Yeni seviye tabanlı müşterileri (persona) tanımlayınız.  Örnek çıktı : USA_ANDROID_MALE_31_40
#Dikkat! List comprehension ile customers_level_based değerleri oluşturulduktan sonra bu değerlerin tekilleştirilmesi gerekmektedir.
#Örneğin birden fazla şu ifadeden olabilir: USA_ANDROID_MALE_0_18. Bunları groupby'a alıp price ortalamalarını almak gerekmektedir.


agg_df.columns      #değişkenlerin isimleri

for col in agg_df.values:
    print(col)

# bize lazım olanlarını seçip örnekteki gibi birleştiriyoruz. Bize 0,1,2,5. indexler bize lazım.
agg_df.columns  # indexlerine bakalım (COUNTRY   SOURCE     SEX  AGE  PRICE AGE_CAT)

[col[0].upper() + "_" + col[1].upper() + "_" +col[2].upper() + "_" + col[5].upper() for col in agg_df.values]

# veri setine ekleyelim.

agg_df["customers_level_based"] = [col[0].upper() + "_" + col[1].upper() + "_" +col[2].upper() + "_" + col[5].upper() for col in agg_df.values]

# gereksiz  değişkenleri çıkartalm

agg_df=agg_df[["customers_level_based", "PRICE"]]
agg_df.head()


#customers_level_based 'ın alt tirelerini boşluk ile değiştirmek    için:  (gei almak)


for i in agg_df["customers_level_based"].values:
    print(i.split("_"))
#kontrol edelim.
agg_df["customers_level_based"].value_counts()
#segmentlere göre grupby yapalım sonra price ortalamalarını alalım sonra da teklilleştirmeliyiz.

agg_df = agg_df.groupby("customers_level_based").agg({"PRICE":"mean"})

#index bilgisi elde emek için

agg_df =agg_df.reset_index()
agg_df.head()

#kontrol edelim.
agg_df["customers_level_based"].value_counts()
agg_df.head()


################## GÖREV 7 ########################
#Görev 7: Yeni müşterileri (personaları) segmentlere ayırınız.
"• Yeni müşterileri (Örnek: USA_ANDROID_MALE_0_18) PRICE’a göre 4 segmente ayırınız."
"• Segmentleri SEGMENT isimlendirmesi ile değişken olarak agg_df’e ekleyiniz."
"• Segmentleri betimleyiniz (Segmentlere göre group by yapıp price mean, max, sum’larını alınız)."
agg_df["SEGMENT"] =pd.cut(agg_df["PRICE"],4,labels=["D","C","B","A"])
agg_df.head(30)

################## GÖREV 8 ########################
#Görev 8: Yeni gelen müşterileri sınıflandırıp, ne kadar gelir getirebileceklerini tahmin ediniz.

"• 33 yaşında ANDROID kullanan bir Türk kadını hangi segmente aittir ve ortalama ne kadar gelir kazandırması beklenir?"


new_user = "TUR_ANDROID_FEMALE_31_40"
agg_df[agg_df["customers_level_based"] == new_user]


"• 35 yaşında IOS kullanan bir Fransız kadını hangi segmente aittir ve ortalama ne kadar gelir kazandırması beklenir?"

new_user = "FRA_IOS_FEMALE_31_40"
agg_df[agg_df["customers_level_based"] == new_user]





