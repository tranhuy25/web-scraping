from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Tạo SparkSession
spark = SparkSession.builder \
    .appName("VNExpress Processing") \
    .getOrCreate()

# Đọc dữ liệu từ file txt đã thu thập
df = spark.read.text("/path/to/data/vnexpress/articles.txt")

# Tách các trường dữ liệu từ chuỗi
articles_df = df.select(
    col("value").substr(1, col("value").rlike("-")).alias("title"),
    col("value").substr(col("value").rlike("-") + 1, len("value")).alias("url")
)

# Lưu kết quả vào PostgreSQL
articles_df.write \
    .format("jdbc") \
    .option("url", f"jdbc:postgresql://{config.Config.DB_HOST}:{config.Config.DB_PORT}/{config.Config.DB_NAME}") \
    .option("dbtable", "vnexpress_articles") \
    .option("user", config.Config.DB_USER) \
    .option("password", config.Config.DB_PASSWORD) \
    .save()

spark.stop()
