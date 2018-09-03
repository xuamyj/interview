import re
import sys
from pyspark import SparkConf, SparkContext

conf = SparkConf()
conf.set('spark.default.parallelism', 8)
sc = SparkContext(conf=conf)

# actual program
# ------------------------------------
lines = sc.textFile(sys.argv[1])
words = lines.flatMap(lambda l: re.split(r'[^\w]+', l))
pairs = words.map(lambda w: (w, 1))
counts = pairs.reduceByKey(lambda n1, n2: n1 + n2)
counts.saveAsTextFile(sys.argv[2])
# ------------------------------------

sc.stop()