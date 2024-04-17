from pymilvus import connections

# 1.连接server
connections.connect(
    alias="default",
    user="username",
    password="password",
    host="localhost",
    port="19530",
)

# 2.创建集合
# 2.1 准备模式
from pymilvus import Collection, CollectionSchema, DataType, FieldSchema

book_id = FieldSchema(
    name="book_id",
    dtype=DataType.INT64,
    is_primary=True,
)
book_name = FieldSchema(
    name="book_name",
    dtype=DataType.VARCHAR,
    max_length=200,
)
word_count = FieldSchema(
    name="word_count",
    dtype=DataType.INT64,
)
book_intro = FieldSchema(name="book_intro", dtype=DataType.FLOAT_VECTOR, dim=2)
schema = CollectionSchema(
    fields=[book_id, book_name, word_count, book_intro], description="Test book search"
)
collection_name = "book"
# 使用指定的模式创建集合
collection = Collection(
    name=collection_name, schema=schema, using="default", shards_num=2
)

# 3.插入数据
# 3.1 准备数据
import random

data = [
    [i for i in range(2000)],
    [str(i) for i in range(2000)],
    [i for i in range(10000, 12000)],
    [[random.random() for _ in range(2)] for _ in range(2000)],
]
# 3.2 插入数据
collection = Collection("book")  # 得到一个存在的集合
mr = collection.insert(data)  # 当数据被插入到Milvus中时，会被插入到段中。段必须达到一定大小才能被密封和索引

# 4.创建分区:Milvus 允许您将大量向量数据分成少量分区。然后，搜索和其他操作可以限制在一个分区内以提高性能
# 集合由一个或多个分区组成。在创建新集合时，Milvus 创建一个默认分区 _default

# 5.为向量建立索引:向量索引是用于加速向量相似性搜索的元数据的组织单元
index_params = {"metric_ty": "L2", "index_type": "IVF_FLAT", "params": {"nlist": 1024}}
from pymilvus import Collection, utility

# Get an existing collection.
collection = Collection("book")
collection.create_index(field_name="book_intro", index_params=index_params)

utility.index_building_progress("book")

# 6. 进行向量搜索
# 6.1 加载集合
collection = Collection("book")
collection.load()
# 6.2 准备搜索参数
search_params = {"metric_type": "L2", "params": {"nprobe": 10}, "offset": 5}
# 6.3 准备向量搜索
# 使用Milvus执行向量搜索。若要在特定的分区（partition）中进行搜索，请指定分区名称列表。
results = collection.search(
    data=[[0.1, 0.2]],
    anns_field="book_intro",
    param=search_params,
    limit=10,
    expr=None,
    output_fields=["title"],
    consistency_level="Strong",
)

# 断开连接
connections.disconnect("default")
