import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import statsmodels.api as sm



#per leggere il file csv
df_popolazione = pd.read_csv("C:/Users/angel/OneDrive/Desktop/dataset PW/dataset ripuliti/ds_popolazione2020_21.csv",  encoding = "latin-1")
df_posti = pd.read_csv("C:/Users/angel/OneDrive/Desktop/dataset PW/dataset ripuliti/dataset2020-2021_posti_letto.csv", encoding = "latin-1")
df_giorni = pd.read_csv("C:/Users/angel/OneDrive/Desktop/dataset PW/dataset ripuliti/dataset2020-2021_giorni.csv", encoding =  "latin-1" )
df_analisi_statistiche=pd.read_csv("C:/Users/angel/OneDrive/Desktop/dataset PW/dataset ripuliti/statistica.csv", encoding = "latin-1")

#prep - drop di colonne e righe vuote
df_popolazione.dropna(axis=0, how='all')
df_popolazione.dropna(axis=1, how='all')
df_posti.dropna(axis=0, how='all')
df_posti.dropna(axis=1, how='all')
df_giorni.dropna(axis=0, how='all')
df_giorni.dropna(axis=1, how='all')
df_analisi_statistiche.dropna(axis=0, how='all')
df_analisi_statistiche.dropna(axis=1, how='all')


#1 controllo di nomi delle colonne 
headers_popolazione = df_popolazione.head()
print(headers_popolazione)
headers_posti = df_posti.head()
print(headers_posti)
headers_giorni = df_giorni.head()
print(headers_giorni)
headers_analisi_statistiche= df_analisi_statistiche.head()

#2 informazioni dataset:
print(df_popolazione.info())
print(df_popolazione.describe())
print(df_posti.info())
print(df_posti.describe())
print(df_giorni.info())
print(df_giorni.describe())
print(df_analisi_statistiche.info())
print(df_analisi_statistiche.describe())


#3 check valori duplicati 
duplicate_rows_posti = df_posti.duplicated()
duplicate_rows_popolazione = df_posti.duplicated()
duplicate_rows_giorni = df_giorni.duplicated()
duplicate_rows_analisi = df_analisi_statistiche.duplicated()
print("I valori duplicati nel dataset relativo ai giorni di degenza: ", duplicate_rows_giorni.sum())
print("I valori duplicati nel dataset relativo ai posti letto: ", duplicate_rows_posti.sum())
print("I valori duplicati nel dataset relativo alla popolazione: ", duplicate_rows_popolazione.sum())
print("I valori duplicati nel dataset propedeutico alle analisi statistiche: ", duplicate_rows_analisi.sum())

#4 salvataggio di nuovo file
df_posti.to_csv('cleaned_dataset_posti_2020-2021.csv', index=False)
df_popolazione.to_csv('cleaned_dataset_popolazione_2021_2021.csv', index=False)
df_giorni.to_csv('cleaned_dataset_giorni_2021_2021.csv', index=False)
df_analisi_statistiche.to_csv('cleaned_dataset_analisi_2021_2021.csv', index=False)


##Analisi tra la numerosità della popolazione e il numero di posti letto ospedalieri:

# Scatter plot con la linea di regressione colorata per regione
for regione in df_analisi_statistiche["Regione"].unique():
    dati_regione = df_analisi_statistiche[df_analisi_statistiche["Regione"] == regione]
    plt.scatter(dati_regione["Popolazione"], dati_regione["Posti Letto"], label=regione)

    if df_analisi_statistiche.empty:
        dati_regione_ordinati = dati_regione.sort_values(by="Popolazione")
        plt.plot(dati_regione_ordinati["Popolazione"], df_analisi_statistiche.predict(dati_regione_ordinati[["Popolazione"]]), label=f"Regressione {regione}", linestyle='dashed')

# Aggiungi la legenda
plt.legend(title="Regioni", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.ticklabel_format(style='plain', axis='x')
# Aggiungi etichette agli assi e al titolo
plt.xlabel("Popolazione")
plt.ylabel("Posti Letto")
plt.title("Relazione tra Popolazione e Posti Letto per Regione")

# Visualizza il plot
plt.show()
# Calcolo della correlazione
correlazione_popolazione_posti = df_analisi_statistiche["Popolazione"].corr(df_analisi_statistiche["Posti Letto"])
print(f"Correlazione tra Popolazione e Posti Letto: {correlazione_popolazione_posti}")

#Regressione lineare tra la numerosità della popolazione e il numero di posti letto ospedalieri:
# Regressione lineare
X_popolazione = sm.add_constant(df_analisi_statistiche["Popolazione"])
y_posti_letto = df_analisi_statistiche["Posti Letto"]

model_popolazione_posti = sm.OLS(y_posti_letto, X_popolazione).fit()

# Stampa dei risultati
print(model_popolazione_posti.summary())

# Scatter plot con la linea di regressione colorata per regione
for regione in df_analisi_statistiche["Regione"].unique():
    dati_regione = df_analisi_statistiche[df_analisi_statistiche["Regione"] == regione]
    plt.scatter(dati_regione["Popolazione"], dati_regione["Posti Letto"], label=regione)

    if df_analisi_statistiche.empty:
        dati_regione_ordinati = dati_regione.sort_values(by="Popolazione")
        plt.plot(dati_regione_ordinati["Popolazione"], df_analisi_statistiche.predict(dati_regione_ordinati[["Posti Letto"]]), label=f"Regressione {regione}", linestyle='dashed')
plt.ticklabel_format(style='plain', axis='x')
# Aggiungi la legenda
plt.legend(title="Regioni", bbox_to_anchor=(1.05, 1), loc='upper left')

# Aggiungi etichette agli assi e al titolo
plt.xlabel("Popolazione")
plt.ylabel("Posti Letto")
plt.title("Relazione tra Popolazione e Posti Letto per Regione con Regressione Lineare")
plt.plot(df_analisi_statistiche["Popolazione"], model_popolazione_posti.predict(X_popolazione), color='red')

# Visualizza il plot
plt.show()


##Analisi tra il numero di posti letto e il numero di giornate di degenza

# Scatter plot con la linea di regressione colorata per regione
for regione in df_analisi_statistiche["Regione"].unique():
    dati_regione = df_analisi_statistiche[df_analisi_statistiche["Regione"] == regione]
    plt.scatter(dati_regione["Posti Letto"], dati_regione["Giornate Degenza"], label=regione)

    if dati_regione.empty:
        dati_regione_ordinati = dati_regione.sort_values(by="Posti Letto")
        plt.plot(dati_regione_ordinati["Posti Letto"], model_popolazione_posti.predict(dati_regione_ordinati[["Posti Letto"]]), label=f"Regressione {regione}", linestyle='dashed')

# Aggiungi la legenda
plt.legend(title="Regioni", bbox_to_anchor=(1.05, 1), loc='upper left')

# Aggiungi etichette agli assi e al titolo
plt.xlabel("Posti Letto")
plt.ylabel("Giornate Degenza")
plt.title("Relazione tra Posti Letto e Giornate Degenza per Regione")

# Visualizza il plot
plt.show()


# Calcolo della correlazione
correlazione_posti_giorni = df_analisi_statistiche["Posti Letto"].corr(df_analisi_statistiche["Giornate Degenza"])
print(f"Correlazione tra Posti Letto e Giornate Degenza: {correlazione_posti_giorni}")


# Regressione lineare tra il numero di posti letto e il numero di giornate di degenza:
X_posti_letto = sm.add_constant(df_analisi_statistiche["Posti Letto"])
y_giornate_degenza = df_analisi_statistiche["Giornate Degenza"]

model_posti_giorni = sm.OLS(y_giornate_degenza, X_posti_letto).fit()

# Stampa dei risultati
print(model_posti_giorni.summary())

# Scatter plot con la linea di regressione colorata per regione
for regione in df_analisi_statistiche["Regione"].unique():
    dati_regione = df_analisi_statistiche[df_analisi_statistiche["Regione"] == regione]
    plt.scatter(dati_regione["Posti Letto"], dati_regione["Giornate Degenza"], label=regione)

    if dati_regione.empty:
        dati_regione_ordinati = dati_regione.sort_values(by="Posti Letto")
        plt.plot(dati_regione_ordinati["Posti Letto"], model_posti_giorni.predict(dati_regione_ordinati[["Posti Letto"]]), label=f"Regressione {regione}", linestyle='dashed')

# Aggiungi la legenda
plt.legend(title="Regioni", bbox_to_anchor=(1.05, 1), loc='upper left')

# Aggiungi etichette agli assi e al titolo
plt.xlabel("Posti Letto")
plt.ylabel("Giornate Degenza")
plt.title("Relazione tra Posti Letto e Giornate Degenza per Regione con Regressione Lineare")
plt.plot(df_analisi_statistiche["Posti Letto"], model_posti_giorni.predict(X_posti_letto), color='red')

# Visualizza il plot
plt.show()
