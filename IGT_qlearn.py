>>> agent_df()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/cristinabanuelos/Downloads/IGT_qlearn.py", line 437, in agent_df
    agent = Qagent(alpha_r=alpha_r, alpha_p=alpha_p, beta=beta)
  File "/Users/cristinabanuelos/Downloads/IGT_qlearn.py", line 93, in __init__
    self.IGT = IowaGamblingTask()
  File "/Users/cristinabanuelos/Downloads/IGT_qlearn.py", line 45, in __init__
    self.all_cards = pd.read_csv('IGTCards.csv')
  File "/Users/cristinabanuelos/anaconda3/lib/python3.6/site-packages/pandas/io/parsers.py", line 702, in parser_f
    return _read(filepath_or_buffer, kwds)
  File "/Users/cristinabanuelos/anaconda3/lib/python3.6/site-packages/pandas/io/parsers.py", line 429, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/Users/cristinabanuelos/anaconda3/lib/python3.6/site-packages/pandas/io/parsers.py", line 895, in __init__
    self._make_engine(self.engine)
  File "/Users/cristinabanuelos/anaconda3/lib/python3.6/site-packages/pandas/io/parsers.py", line 1122, in _make_engine
    self._engine = CParserWrapper(self.f, **self.options)
  File "/Users/cristinabanuelos/anaconda3/lib/python3.6/site-packages/pandas/io/parsers.py", line 1853, in __init__
    self._reader = parsers.TextReader(src, **kwds)
  File "pandas/_libs/parsers.pyx", line 387, in pandas._libs.parsers.TextReader.__cinit__
  File "pandas/_libs/parsers.pyx", line 705, in pandas._libs.parsers.TextReader._setup_parser_source
FileNotFoundError: [Errno 2] File b'IGTCards.csv' does not exist: b'IGTCards.csv'
>>> 