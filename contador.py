import sys
from pyspark import SparkContext, SparkConf
if __name__ == "__main__":
    sc = SparkContext("local","PySpark Exemplo - Desafio Dataproc")
    words = sc.textFile("C:\Users\wolli\3D Objects\digital-innovatio-one-data-science\9 second-project\dataproc-challenge/livro.txt").flatMap(lambda line: line.split(" "))
    wordCounts = words.map(lambda word: (word, 1)).reduceByKey(lambda a,b:a +b).sortBy(lambda a:a[1], ascending=False)
    wordCounts.saveAsTextFile("C:\Users\wolli\3D Objects\digital-innovatio-one-data-science\9 second-project\dataproc-challenge/resultado")