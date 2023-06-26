# # from datetime import datetime
# # from elasticsearch_dsl import Document, Date, Nested, Boolean, analyzer, InnerDoc, Completion, Keyword, Text, Integer, \
# #     Search
# #
# # from elasticsearch_dsl.connections import connections
# #
# # # connections.create_connection(hosts=["123.60.180.204:9200"])
# # es = connections.create_connection(hosts=["123.60.180.204:9200"], timeout=60)
# #
# #
# # class Article(Document):
# #     title = Text(analyzer="snowball", fields={"raw": Keyword()})
# #     body = Text(analyzer="snowball")
# #     tags = Keyword()
# #     published_from = Date()
# #     lines = Integer()
# #
# #     class Index:
# #         name = 'my_article'  # 索引名
# #
# #     def save(self, **kwargs):
# #         self.lines = len(self.body.split())
# #         return super().save(**kwargs)
# #
# #
# # if __name__ == '__main__':
# #     Article.init(using=es)  # 创建索引映射
# #     article = Article(meta={'id': 42}, title='Hello world!', tags=['test'])
# #     article.body = "长文档"
# #     article.published_from = datetime.now()
# #     article.save()
# #     # # 保存数据
# #     # article = Article()
# #     # article.title = "test"
# #     # article.author = "lxx"
# #     # article.save()  # 保存数据
# #
# #     # 查询数据
# #     s = Article.search()
# #     s = s.filter('match', title="Hello world!")
# #     results = s.execute()
# #     print(results)
# #     #
# #     # # 删除数据
# #     # s = Article.search()
# #     # s = s.filter('match', title="test").delete()
# #     # # 修改数据
# #     # s = Article().search()
# #     # s = s.filter('match', title="test")
# #     # results = s.execute()
# #     # print(results[0])
# #     # results[0].title = "xxx"
# #     # results[0].save()
# #     # res = Search(using=es).index("teacher").query({"match": {"description": "可"}})
# #     # res2 = res.query().source(["name"]).execute()
# #     # for data in res:
# #     #     print(data.to_dict())
# #     # index_name = es.cat.indices(format="json", h="index")
#
# from elasticsearch_dsl import Q
# from functools import reduce
# SEARCH_TYPE = set(["自然资源专业档案","建设工程纸质档案","地址资料","文书"])
# type_list = ["自然资源专业档案","建设工程纸质档案","文书"]
#
# q_list = [Q("term",type=item) for item in type_list if item in SEARCH_TYPE]
# q = reduce(lambda x,y:x|y,q_list)
# # q = q_list.pop()
# # for q_item in q_list:
# #     q = q | q_item
# print("最后Q:",q)

from operator import itemgetter

a=[('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]

d = sorted(a,key=itemgetter(1,2)) # 按照元组中下标为1排序,相同在按2排序
print(d)

rank = [
    {'score': 12, 'time': '2022-08-04'},
    {'score': 23, 'time': '2022-08-01'},
    {'score': 23, 'time': '2022-07-24'},
    {'score': 10, 'time': '2022-07-16'},
    {'score': 12, 'time': '2022-07-16'},
]
d = sorted(rank,key=itemgetter("score","time"))
print(d)

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75,
}
# 1.根据value获取最大值:输出最大值的key
max_ = max(prices,key=lambda k:prices[k])
print(max_)
