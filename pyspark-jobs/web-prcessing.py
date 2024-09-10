from pyspark.sql import SparkSession
from pyspark.sql.functions import col, regexp_replace
from config import DATA_DIR, SPARK_MASTER

spark = SparkSession.builder \
    .appName("VNExpress Data Processing") \
    .master(SPARK_MASTER) \
    .getOrCreate()

input_path = os.path.join(DATA_DIR, 'articles.json')
df = spark.read.json(input_path)

df_clean = df.withColumn('title', regexp_replace(col('title'), '[^\\w\\s]', ''))

df_clean.show(truncate=False)

output_path = os.path.join(DATA_DIR, 'processed_articles.csv')
df_clean.write.csv(output_path, header=True)

spark.stop()
