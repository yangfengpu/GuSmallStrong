# -*- coding: utf-8 -*-
"""Package of Data Access Object (DAO) Class.

This module demonstrates documentation as specified by the `Google Python
Style Guide`_. Docstrings may extend over multiple lines. Sections are created
with a section header and a colon followed by a block of indented text.

Example:
    Examples can be given using either the ``Example`` or ``Examples``
    sections. Sections support any reStructuredText formatting, including
    literal blocks::

        $ python example_google.py

Section breaks are created by resuming unindented text. Section breaks
are also implicitly created anytime a new section starts.

Attributes:
    module_level_variable1 (int): Module level variables may be documented in
        either the ``Attributes`` section of the module docstring, or in an
        inline docstring immediately following the variable.

        Either form is acceptable, but the two should not be mixed. Choose
        one convention to document module level variables and be consistent
        with it.

.. _Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html

"""
import pymongo
import datetime
from pymongo import MongoClient

class mongoDao:
    """The summary line for a class docstring should fit on one line.

    If the class has public attributes, they may be documented here
    in an ``Attributes`` section and follow the same formatting as a
    function's ``Args`` section. Alternatively, attributes may be documented
    inline with the attribute's declaration (see __init__ method below).

    Properties created with the ``@property`` decorator should be documented
    in the property's getter method.

    Attribute and property types -- if given -- should be specified according
    to `PEP 484`_, though `PEP 484`_ conformance isn't required or enforced.

    Attributes:
        attr1 (str): Description of `attr1`.
        attr2 (Optional[int]): Description of `attr2`.


    .. _PEP 484:
       https://www.python.org/dev/peps/pep-0484/

    """
    def __init__(self):
        """Example of docstring on the __init__ method.

        The __init__ method may be documented in either the class level
        docstring, or as a docstring on the __init__ method itself.

        Either form is acceptable, but the two should not be mixed. Choose one
        convention to document the __init__ method and be consistent with it.

        Note:
            Do not include the `self` parameter in the ``Args`` section.

        Args:
            param1 (str): Description of `param1`.
            param2 (Optional[int]): Description of `param2`. Multiple
                lines are supported.
            param3 (List[str]): Description of `param3`.

        """
        self.client = MongoClient('localhost', 80)#27017
        self.db = self.client.greency_db
        self.collection = self.db.inventory

    def add_a_record(self, record):
        """Class methods are similar to regular functions.

        Note:
            Do not include the `self` parameter in the ``Args`` section.

        Args:
            param1: The first parameter.
            param2: The second parameter.

        Returns:
            True if successful, False otherwise.

        """
        '''
        doc = { "P/N": record,#record.get_PN(),
                "supplier": "",
                "inventory": "",
                "specification": "",
                "description": "",
                "OEM": "",
                "tags": ["mongodb", "python", "pymongo"],
                "date": datetime.datetime.utcnow()}'''
        self.collection.insert(record)

    def read_records(self):
        records = self.collection.find()
        result = []
        for record in records:
            result.append(record)
        return result

if __name__ == '__main__':
    k = mongoDao()
    k.add_a_record({"aa":123})
