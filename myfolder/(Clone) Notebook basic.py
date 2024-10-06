# Databricks notebook source
print("hello world")

# COMMAND ----------

# MAGIC %sql --COMANDO MAGICO
# MAGIC select "Hello world from SQL"

# COMMAND ----------

# MAGIC %md
# MAGIC # Title 1
# MAGIC ## Title 2
# MAGIC ### Title 3
# MAGIC
# MAGIC Ordered list
# MAGIC 1. first
# MAGIC 1. second
# MAGIC 1. third
# MAGIC
# MAGIC Unordered list
# MAGIC * coffee
# MAGIC * tea
# MAGIC * milk
# MAGIC
# MAGIC #Images:
# MAGIC ![Associate-badge](https://www.databricks.com/wp-content/uploads/2022/04/associate-badge-eng.svg)
# MAGIC
# MAGIC #tables
# MAGIC | user_id | user_name |
# MAGIC |---------|-----------|
# MAGIC |    1    |    Adam   |
# MAGIC |    2    |    Sarah  |
# MAGIC |    3    |    John   |
# MAGIC
# MAGIC Links (or Embedded HTML): <a href="https://docs.databricks.com/notebooks/notebooks-manage.html" target="_blank"> Managing Notebooks documentation</a>
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ## REUTILIZAR CODIGO (MODULO)
# MAGIC - %run : allow execute notebook externo

# COMMAND ----------

# MAGIC %run ./includes/setup

# COMMAND ----------

print(full_name)

# COMMAND ----------

# MAGIC %md
# MAGIC # CLI para filesystem
# MAGIC - %fs : operations filesystem (ls , cd )
# MAGIC - dbutils : utils de databricks
# MAGIC
# MAGIC | fs | dbutils |
# MAGIC |---------|-----------|
# MAGIC |      no se usa en el code  |   SDK: se usa en el code   |
# MAGIC |        |      |

# COMMAND ----------

# MAGIC %fs ls '/databricks-datasets'

# COMMAND ----------

dbutils.help()
dbutils.fs.help()
