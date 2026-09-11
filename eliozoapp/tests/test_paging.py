"""Tests for the page navigation shared by the Filter page and search results."""

import pytest
from flask import Flask

from blueprints.paging import page_links, page_offsets, parse_offset, shown_page_numbers


@pytest.fixture
def app():
    app = Flask(__name__)
    app.add_url_rule("/search", "search", lambda: "")
    with app.test_request_context():
        yield app


def numbers(items):
    """Page bar items as page numbers, with "..." for a gap."""
    return ["..." if item.get("gap") else item["number"] for item in items]


@pytest.mark.parametrize("value, expected", [
    (None, 0), ("", 0), ("abc", 0), ("-10", 0), ("0", 0), ("20", 20), (30, 30),
])
def test_parse_offset(value, expected):
    assert parse_offset(value) == expected


@pytest.mark.parametrize("total, expected", [
    (0, []), (1, []), (10, []), (11, [0, 10]), (20, [0, 10]), (23, [0, 10, 20]),
])
def test_page_offsets(total, expected):
    assert page_offsets(total) == expected


def test_page_offsets_with_other_page_size():
    assert page_offsets(7, page_size=3) == [0, 3, 6]


def test_page_links(app):
    links = page_links(23, 10, "search", {"keyword": "\\frac", "searchMode": "regex"})
    assert numbers(links) == [1, 2, 3]
    assert [link["current"] for link in links] == [False, True, False]
    assert links[2]["url"] == "/search?keyword=%5Cfrac&searchMode=regex&offset=20"


def test_page_links_empty_when_one_page_is_enough(app):
    assert page_links(10, 0, "search", {}) == []


# --------------------------------------------------------------------------
# Long page bars
# --------------------------------------------------------------------------

def test_up_to_the_limit_every_page_is_listed(app):
    assert numbers(page_links(300, 0, "search", {})) == list(range(1, 31))


def test_beyond_the_limit_first_page(app):
    assert numbers(page_links(310, 0, "search", {})) == [1, 2, 3, "...", 31]


def test_beyond_the_limit_middle_page(app):
    links = page_links(3202, 1590, "search", {})
    assert numbers(links) == [1, "...", 158, 159, 160, 161, 162, "...", 321]
    assert [item["number"] for item in links if item.get("current")] == [160]


def test_beyond_the_limit_last_page(app):
    assert numbers(page_links(3202, 3200, "search", {})) == [1, "...", 319, 320, 321]


def test_single_left_out_page_is_shown_instead_of_an_ellipsis():
    assert shown_page_numbers(321, 5, limit=30) == [1, 2, 3, 4, 5, 6, 7, 321]
    assert shown_page_numbers(321, 317, limit=30) == [1, 315, 316, 317, 318, 319, 320, 321]


def test_limit_parameter(app):
    assert numbers(page_links(100, 0, "search", {}, limit=5)) == [1, 2, 3, "...", 10]


def test_gap_links_keep_the_query_parameters(app):
    links = page_links(3202, 1590, "search", {"keyword": "a"})
    assert links[-1]["url"] == "/search?keyword=a&offset=3200"
