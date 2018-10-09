# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import pytest

from google.cloud.ndb import query
import tests.unit.utils


def test___all__():
    tests.unit.utils.verify___all__(query)


class TestConjunctionNode:
    @staticmethod
    def test_constructor():
        with pytest.raises(NotImplementedError):
            query.ConjunctionNode()


def test_AND():
    assert query.AND is query.ConjunctionNode


class TestCursor:
    @staticmethod
    def test_constructor():
        with pytest.raises(NotImplementedError):
            query.Cursor()


class TestDisjunctionNode:
    @staticmethod
    def test_constructor():
        with pytest.raises(NotImplementedError):
            query.DisjunctionNode()


def test_OR():
    assert query.OR is query.DisjunctionNode


class TestFalseNode:
    @staticmethod
    def test_constructor():
        with pytest.raises(NotImplementedError):
            query.FalseNode()


class TestFilterNode:
    @staticmethod
    def test_constructor():
        with pytest.raises(NotImplementedError):
            query.FilterNode()


def test_gql():
    with pytest.raises(NotImplementedError):
        query.gql()


class TestNode:
    @staticmethod
    def test_constructor():
        with pytest.raises(NotImplementedError):
            query.Node()


class TestParameter:
    @staticmethod
    def test_constructor():
        with pytest.raises(NotImplementedError):
            query.Parameter()


class TestParameterizedFunction:
    @staticmethod
    def test_constructor():
        with pytest.raises(NotImplementedError):
            query.ParameterizedFunction()


class TestParameterizedThing:
    @staticmethod
    def test_constructor():
        with pytest.raises(NotImplementedError):
            query.ParameterizedThing()


class TestParameterNode:
    @staticmethod
    def test_constructor():
        with pytest.raises(NotImplementedError):
            query.ParameterNode()


class TestPostFilterNode:
    @staticmethod
    def test_constructor():
        with pytest.raises(NotImplementedError):
            query.PostFilterNode()


class TestQuery:
    @staticmethod
    def test_constructor():
        with pytest.raises(NotImplementedError):
            query.Query()


class TestQueryIterator:
    @staticmethod
    def test_constructor():
        with pytest.raises(NotImplementedError):
            query.QueryIterator()


class TestQueryOptions:
    @staticmethod
    def test_constructor():
        with pytest.raises(NotImplementedError):
            query.QueryOptions()


class TestRepeatedStructuredPropertyPredicate:
    @staticmethod
    def test_constructor():
        with pytest.raises(NotImplementedError):
            query.RepeatedStructuredPropertyPredicate()