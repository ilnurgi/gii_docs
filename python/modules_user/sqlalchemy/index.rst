.. title:: python sqlalchemy

.. meta::
    :description:
        Справочная информация по python модулю sqlalchemy.
    :keywords:
        python sqlalchemy

.. py:module:: sqlalchemy

sqlalchemy
==========

.. code-block:: py

    import sqlalchemy as sa

    conn = sa.create_engine("sqlite://")
    conn.execute(create_table_sql)
    conn.execute(insert_sql)
    rows = conn.execute(select_sql)
    for row in rows:
        print(row)

.. code-block:: py

    import sqlalchemy as sa

    conn = sa.create_engine("sqlite://")
    meta = sa.MetaData()
    some_table = sa.Table(
        'table_name',
        meta,
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("count", sa.Integer, nullable=False),
        sa.Column("title", sa.String(16), nullable=False),
        sa.Column("text", sa.Text, nullable=False),
        sa.Column("is_published", sa.Boolean, default=False),
    )

    meta.create_all(conn)

    conn.execute(some_table.insert((1, 1)))
    conn.execute(some_table.select())
    rows = conn.fetchall()

.. code-block:: py

    import sqlalchemy as sa
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy.orm import sessionmaker

    conn = sa.create_engine("sqlite://")
    Base = declarative_base()

    class SomeTable(Base):
        __tablename__ = 'table_name'
        id = sa.Column('id', sa.Integer, primary_key=True)
        count = sa.Column('count', sa.Integer)

        user_id = sa.Column(sa.Integer, ForeignKey('users.id'), nullable=False)

        user = relationship('User', back_populates='posts') # , lazy='joined')
        # posts = relationship('Post', back_populates='user')

        tags = relationship('Tag', secondary=tags_posts_table, back_populates='posts')
        
        def __init__(self, id, count):
            self.id = id
            self.count = count

        def __repr__(self):
            return "<SomeTable({}, {})>".format(self.id, self.count)

    Base.metadata.create_all(conn)

    Session = sessionmaker(bind=conn)
    session = Session()
    session.add(SomeTable(1, 1))
    session.add_all((SomeTable(1, 1), SomeTable(2, 2)))
    session.commit()

.. code-block:: py

    engine = sqlalchemy.create_engine('sqlite:///blog.db')
    metadata = sqlalchemy.MetaData()
    posts_table = sqlalchemy.Table('posts', metadata, autoload=True, autoload_with=engine)
    print([c.name for c in posts_table.columns])
    # ['id', 'user_id', 'title', 'text', 'is_publised']
    post = session.query(Post).first() # select from posts
    print(post.user.username) # select from users

.. toctree::
    :maxdepth: 2

    meta
    engine/index
    dialects/index
    inspection/index
    schema/index
    sql/index
    types/index


create_engine()
---------------

.. py:function:: create_engine(url, **kwargs)

    Возвращает объект :py:class:`sqlalchemy.engine.Engine()`, для работы с базой данных

    * **url** - строка, подключение к базе данных
    * **echo** - булево, включить логирование запросов

    .. code-block:: py

        engine = create_engine('sqlite:///:memory:', echo=True)
        engine = create_engine('sqlite:///some.db')

