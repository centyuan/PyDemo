import tracemalloc

tracemalloc.start()
snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('lineno')

print('最大十个')
for stat in top_stats[:10]:
    pass