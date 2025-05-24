#!/usr/bin/env python3

from sqlalchemy import create_engine
chmod +x app/sqlalchemy_sandbox.py


engine = create_engine('sqlite:///students.db')
Base.metadata.create_all(engine)


