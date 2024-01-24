>title: Note

```
#### git commit 标准：
feat：新功能（feature）。
fix/to：修复bug，可以是QA发现的BUG，也可以是研发自己发现的BUG。
fix：产生diff并自动修复此问题。适合于一次提交直接修复问题
to：只产生diff不自动修复此问题。适合于多次提交。最终修复问题提交时使用fix
docs：文档（documentation）。
style：格式（不影响代码运行的变动）。
refactor：重构（即不是新增功能，也不是修改bug的代码变动）。
perf：优化相关，比如提升性能、体验。
test：增加测试。
chore：构建过程或辅助工具的变动。
revert：回滚到上一个版本。
merge：代码合并。
sync：同步主线或分支的Bug。

#### URL规范:
1. 不用大写 （强制）
2. 用中杠-不用下杠_（强制）
3. 参数列表要encode，编码使用utf-8（强制）
4. URI中的名词表示资源集合，使用复数形式。（建议）
5. 增加版本号（建议）

#### 双因子认证:又称作两步验证
认证因素按计算采用的近似顺序列举如下
1. 认知因素(用户知道的事物,密码/PIN码)
2.  持有物因素指用户拥有的东西，比如身份证，安全令牌，智能手机或其它移动设备。
3.  特征因素，更多时候被称为生物识别因素，是用户自身固有的特性。这些可能是从物理特征映射出来个人属性，比如通过指纹阅读器认证的指纹；其它特征因素还包括面部识别和语音识别。此外还包括一些行为特征，比如击键力度，步态或语音模式。
4.  位置因素，通常是指尝试认证时所处的位置，可以特定位置的特定设备来强制限定认证，更常见的方式是跟踪认证来源的 IP 地址或来源于移动电话或其他设备（如GPS数据）的地理信息。
5.  时间因素限制用户在特定的时间窗口内认证登录，并在该时间之外限制对系统的访问。

例如：短信验证、微信或者QQ授权验证、USB令牌、OTP令牌等等。举例1：当你进入公司时，必须打卡（你在公司的身份证件）+指纹验证，这就是双因子认证机制举例2：登录某web网站，输入账号密码之后，还要再输入接收到的短信验证码，这也是双因子认证机制举例3：你在一台新的设备上第一次登录你的微信，除了输入账号密码，还要有一个确认好友的步骤，即在微信给你的N个头像中正确的选出你的好友，或者在原设备登录中的微信，扫描现在微信的授权登录二维码。以上二选其一即可在新设备上登录。


#### 匹配方式:
1. str in str
2. re.findall("词库",input)
3. 三方库thefuzz 
https://www.jianshu.com/p/ed22a82b45d1
https://blog.csdn.net/u010454729/article/details/124231419
"""
两个字符串之间的Levenshtein Distance莱文斯坦距离指的是将一个字符串变为另一个字符串需要进行编辑操作最少的次数。其中，允许的编辑操作有以下三种。不难看出其可用于衡量两个字符串之间的差异，故被广泛应用于拼写纠错检查、DNA分析、语音识别等领域
「替换」：将一个字符替换成另一个字符
「插入」：插入一个字符
「删除」：删除一个字符
ratio计算关键原理：
源代码：/opt/anaconda3/lib/python3.8/difflib.py

解释：T分别是两个序列的元素长度和，M是匹配到的个数。
abc、a：匹配了a，故结果是(2*1)/(3+1) = 0.5
aabc、a：也只匹配了a，虽然前面有两个a，但可以理解为后面匹配到了的a用掉了，故(2*1)/(4+1)=0.4
aabc、aa：匹配到了第一个a、第二个a，共两个，故(2*2)/(4+2)=2/3



#### 文本文件和字符串之间的差异
1.标准类库: diffib 
from difflib import SequenceMatcher
SequenceMatcher(None,"hello world","hi world").ratio()

2.thefuz 四种模糊匹配计算方式：依据 Levenshtein Distance 算法，计算两个序列之间的差异
from thefuzz  import fuzz
from thefuzz  import process 
简单匹配fuzz.ratio :直接调用SequenceMatcher
非完全匹配fuzz.partial_ratio: 
做了简单的处理。再调用Ratio
处理：将两个字符串空格分割开来，得到两个集合a、b。其中
a&b排序拼接在一起得到sorted_sect，交集
(a-b、a&b)排序拼接一起得到combined_1to2。差集+交集
(b-a、a&b)排序拼接一起combined_2to1。另外一个差集+交集
计算ratio(sorted_sect)、ratio(combined_1to2)、ratio(combined_2to1)三者之间的最大值。
忽略顺序匹配fuzz.token_sort_ratio: 做了简单的处理。再调用Ratio
去重子集匹配fuzz.token_set_ratio:  做了简单的处理。再调用Ratio
非完全忽略顺序匹配fuzz.partial_token_sort_ratio: 
非完全去重子集匹配fuzz.partial_token_set_ratio
choices = ["河南省", "郑州市", "湖北省", "武汉市"]
process.extract("郑州", choices, limit=2)

#### ssh代理
ssh   gxac@192.168.100.197 -fNL  0.0.0.0:40122:20.120.47.211:22

##### Linux登录时:
首先启动/etc/profile ,在启动用户目录下:~/.bash_profile,~/.bash_login, ~/.profile,如果~/.bash_profile文件存在的话,一般还会执行~/.bashrc
if [ -f ~/.bashrc ]; then
    . ~/.bashrc
fi 
执行顺序:/etc/profile→ (~/.bash_profile | ~/.bash_login | ~/.profile)→~/.bashrc →/etc/bashrc
```

```
#### 
fastapi==0.104.1
pydantic==2.5.3
httpx==0.25.2
uvicorn[standard]
tortoise-orm==0.20.0
asyncmy==0.2.9
aerich==0.7.2
python-jose==3.3.0
cryptography==41.0.7
pandas==2.1.4
thefuzz==0.20.0
bson==0.5.10
dashscope==1.13.6
qianfan==0.2.4

https://lanhuapp.com/link/#/invite?sid=qx07jWaa
opentelemetry-instrument uvicorn gptserver:app  --host 0.0.0.0 --port 8081 --http httptools --loop uvloop  --proxy-headers --forwarded-allow-ips='*' --no-server-header
./configure --enable-optimizations --with-openssl=/usr/local/openssl --prefix=/usr/local/python-3.10
gunicorn gptserver:app --workers 2 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8888
PROCESS=`ps -ef | grep gunicorn | grep -v grep  | awk '{print $2}'`
for i in $PROCESS
do
    echo "kill the gunicorn process  ${i} "
    sudo kill -9 ${i}
done
nohup python3 app.py >> ./flask.log 2>&1 &
https://192.168.100.197/#/
hl:a.123123

pip install modelscope -i https://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com --default-timeout=100
```



**原型图**

PII身份信息识别统计

```
身份证/护照
电话号码
银行卡
```

操作日志

>会话日志/操作日志/PII日志

>策略配置(处理方式下拉)，组织架构，人员管理，告警通知，

>日志审计(会话日志，操作日志，PII日志(配置/展示))
>
>**会话日志**
>
>```
>用户名(user_id,user_name),提示词(prompt_text),complete_text，是否违禁(is_break)，处理方式
>```
>
>







**知识库**

**Embedding Model**

[用万字长文聊一聊 Embedding 技术](https://cloud.tencent.com/developer/article/1749306)

**分类**

>- 基于矩阵分解的方式，代表方式是SVD
>- 基于内容的Embedding：1.静态Embedding(如 word2vec、GloVe 和 FastText), 2.动态Embedding(如 ELMo、GPT 和 BERT)
>- 基于物品序列：item2vec
>- 基于图的Embedding: 分为浅层图模型和深层图模型。浅层图模型有deepwalk、Node2vec、EGES，深层图模型有GCN、GraphSAGE等



>1.BAAI/bge-large-zh-v1.5         # HuggingFaceBgeEmbeddings(model="BAAI/bge-large-zh-v1.5")
>2.text2vec-large-chinese /text2vec-base-chinese    #  开源版本
>3.text-embedding-ada-002            # openai 需要付费
>4.models/embedding-001            # google embedding 
>
>```
>result = genai.embed_content(
>    model="models/embedding-001",
>    content="What is the meaning of life?",
>    task_type="retrieval_document",
>    title="Embedding of single string")
>```
>
>5.GanymedeNil/text2vec-large-chinese

```
嵌入算法:
词嵌入Word Embedding: 
句子/文档嵌入 Sentence/Document Embedding： 
图嵌入Graph Embedding: 
常用嵌入技术: 
Word2Vec: Google开发的一种计算词向量的模型，有两种训练架构：CBOW（Continuous Bag of Words）和Skip-gram
Glove:斯坦福大学开发的模型，通过对词与词之间共现概率的矩阵进行分解来学习词向量
FastText（Global Vectors for Word Representation）：Facebook开发，和Word2Vec类似，但它在训练过程中考虑了词的内部结构，即子词（subwords）信息
ELMo（Embeddings from Language Models）：使用双向LSTM训练得到的深度语言模型来生成词嵌入，能够捕捉词在不同语境中的用法。
BERT（Bidirectional Encoder Representations from Transformers）：Google开发，使用了Transformer的Encoder来预训练深度双向表示，可以产生依赖于上下文的词嵌入。
Transformer：不单独是一个嵌入模型，但其编码器和解码器都使用自注意力机制来处理序列信息，并被广泛用于生成上下文敏感的嵌入。
每种嵌入技术都有它的特点和适用场景，选择哪种技术取决于具体的任务需求和资源限制。随着深度学习的发展，越来越多的嵌入模型被提出，并在各种自然语言处理任务中取得了优异的性能
```

**向量数据库**

推荐使用milvus

| 向量数据库 | URL                                    | GitHub Star | Language      | Cloud |
| :--------- | :------------------------------------- | :---------- | :------------ | :---- |
| chroma     | https://github.com/chroma-core/chroma  | 7.4K        | Python        | ❌     |
| milvus     | https://github.com/milvus-io/milvus    | 21.5K       | Go/Python/C++ | ✅     |
| pinecone   | https://www.pinecone.io/               | ❌           | ❌             | ✅     |
| qdrant     | https://github.com/qdrant/qdrant       | 11.8K       | Rust          | ✅     |
| typesense  | https://github.com/typesense/typesense | 12.9K       | C++           | ❌     |
| weaviate   | https://github.com/weaviate/weaviate   | 6.9K        | Go            | ✅     |



**影响最后实际效果的因素很多**

>1.知识库本身语料的格式问题。如果有大量的短文本占据一行或冗余的数据，其表示的意思和信息很有限。因此在做本地知识库的时候，如果前后语句的语义是连贯的但又不在一行，我们需要人工将这些段落做一下整理，将短的文本凑到一行。尽量避免多行的短文本
>
>2.文本分割的效果。很多文本分割的处理方式比较粗暴，就是单纯的按照标点如句号、分号来分割，这其实打断了原本比较连贯的文本，效果不一定好。当然，如果多加上前后几句文本，效果可能会有改善，但是这个度不好控制。比较理想的方式是采用语义分割
>
>```
>1.中文标点符号(正则匹配标点符号)
>
>2.Langchain 的 text_splitter
>from langchain.text_splitter import CharacterTextSplitter  # 按照指定分隔符分割 默认"\n\n"chunk_size=字符长度,chunk_overlap=重复字符(中间重复)
>from langchain.text_splitter import MarkdownTextSplitter   # 沿着Markdown的标题,代码块或水平规则来分割文本
>from langchain.text_splitter import PythonCodeTextSplitter  # 沿着Python类和方法的定义分割文本
>from langchain.text_splitter import RecursiveCharacterTextSplitter # 用于通用文本的分割器。它以一个字符列表为参数，尽可能地把所有的段落(然后是句子，然后是单词)放在一起
>from langchain.text_splitter import TokenTextSplitter      # 根据openAI的token分割器
>from langchain.text_splitter import SpacyTextSplitter   # spaCy是一个NLP领域的文本预处理Python库(包括分词,词性标注,依存分析,词性还原,命名实体识别)
>from langchain.text_splitter import NLTKTextSplitter   # 
>或处理html的分块方式
>3.Spacy Text Splitter
>
>阿里达摩院开源的语义分割:nlp_bert_document-segmentation_chinese-base(https://modelscope.cn/models/damo/nlp_bert_document-segmentation_chinese-base/summary)
>百度PaddleNLP
>```
>
>3.Embedding 模型计算向量以及向量间的相似度，选择不同的模型，这个效果肯定会有差异
>
>MTEB: Massive Text Embedding Benchmark 大规模文本嵌入基准测试
>
>榜单地址:https://huggingface.co/spaces/mteb/leaderboard
>
>**[text-embeddings-inference](https://github.com/huggingface/text-embeddings-inference)**加速推理
>
>````
>1.BAAI/bge-large-zh-v1.5         # HuggingFaceBgeEmbeddings(model="BAAI/bge-large-zh-v1.5")
>2.text2vec-large-chinese /text2vec-base-chinese    #  开源版本
>3.text-embedding-ada-002            # openai 需要付费
>4.models/embedding-001            # google embedding 
>```
>result = genai.embed_content(
>model="models/embedding-001",
>content="What is the meaning of life?",
>task_type="retrieval_document",
>title="Embedding of single string")
>```
>5.GanymedeNil/text2vec-large-chinese
>````
>
>4.大模型本身的能力，如现在 chatgpt-4 应该是傲视群雄，大模型基本是分为 chatgpt-4 和其他了。当然，使用 chatgpt 本身有信息安全问题以及费用问题。国内清华开源的 chatGLM-6b 是一个效果和性价比尚可的替代



[适合的文本分块策略](https://zhuanlan.zhihu.com/p/670771195)

>[llama_index](https://github.com/run-llama/llama_index)
>
>> LlamaIndex (formerly GPT Index) is a data framework for your LLM applications

**参考项目**

>**LangChain-ChagGLM-Webui**
>
>https://github.com/X-D-Lab/LangChain-ChatGLM-Webui/tree/master
>
>**Langchain-Chatchat**
>
>https://github.com/chatchat-space/Langchain-Chatchat?tab=readme-ov-file
>
>**LongChainKBQA**
>
>https://github.com/wp931120/LongChainKBQA
>
>https://blog.csdn.net/zyqytsoft/article/details/131159174
>
>[一文读懂BERT](https://blog.csdn.net/sunhua93/article/details/102764783)
>
>[NLP的巨人肩膀](https://zhuanlan.zhihu.com/p/50443871)
>
>[李宏毅Transformer](https://www.youtube.com/watch?v=ugWDIIOHtPA&list=PLJV_el3uVTsOK_ZK5L0Iv_EQoL1JefRL4&index=61)
>
>```
>1.AIGC生成系统
>2.GPT和AI agent
>3.知识库问答
>```
>
>

**文档分块**

**召回文档怎么结合LLM**

>1. Sutff：将检索retrieval的相应文档给到prompt上下文context中
>2. refine: 不断拿出一个检索的文档给到prompt的上下文，在将这个过程进行迭代
>3. map reduce: 每个文档给到prompt得到答案，将所有答案合并再去推理
>4. map re-rank: 每个文档的回答进行打分，rank后拿到最佳

