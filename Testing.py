from datetime import datetime
from elasticsearch_dsl import Document, Date, Nested, Boolean, analyzer, InnerDoc, Completion, Keyword, Text, Integer, \
    Search

from elasticsearch_dsl.connections import connections

# connections.create_connection(hosts=["123.60.180.204:9200"])
es = connections.create_connection(hosts=["123.60.180.204:9200"], timeout=20)


class Article(Document):
    title = Text(fields={'title': Keyword()})
    author = Text()

    class Index:
        name = 'myindex'  # 索引名


if __name__ == '__main__':
    # Article.init()  # 创建映射
    # # 保存数据
    # article = Article()
    # article.title = "test"
    # article.author = "lxx"
    # article.save()  # 保存数据
    res = Search(using=es).index("teacher").query({"match":{"description":"可"}})
    res2 = res.query().source(["name"]).execute()
    for data in res:
        print(data.to_dict())
    index_name = es.cat.indices(format="json", h="index")
    # # 查询数据
    # s = Article.search()
    # s = s.filter('match', title="test")
    # results = s.execute()
    # print(results)
    #
    # # 删除数据
    # s = Article.search()
    # s = s.filter('match', title="test").delete()
    # # 修改数据
    # s = Article().search()
    # s = s.filter('match', title="test")
    # results = s.execute()
    # print(results[0])
    # results[0].title = "xxx"
    # results[0].save()
