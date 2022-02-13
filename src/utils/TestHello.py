# Databricks notebook source
print("this is my hello")

# COMMAND ----------

import hello as h

# COMMAND ----------

# Print the path
import sys
print("\n".join(sys.path))

# COMMAND ----------

print(sys.cwd)

# COMMAND ----------

import os
 
# In the command below, replace <username> with your Databricks user name.
sys.path.append(os.path.abspath('/Workspace/Repos/bladnman@gmail.com/supplemental_files'))

# COMMAND ----------

print("\n".join(sys.path))

# COMMAND ----------


