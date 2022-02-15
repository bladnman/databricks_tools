# Databricks notebook source
print("let's read!")

# COMMAND ----------

from sing import bark
bark()

# COMMAND ----------

# MAGIC %sql
# MAGIC select count(*) from SamplesDB.dog_food

# COMMAND ----------

df = table("SamplesDB.dog_food")

# COMMAND ----------

display(df)

# COMMAND ----------


