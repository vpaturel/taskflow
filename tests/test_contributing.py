"""
Tests for CONTRIBUTING.md — verifies structure and required content.
"""
import os
import re
import pytest

CONTRIBUTING_PATH = os.path.join(os.path.dirname(__file__), "..", "CONTRIBUTING.md")


@pytest.fixture(scope="module")
def contributing_content():
    with open(CONTRIBUTING_PATH, "r", encoding="utf-8") as f:
        return f.read()


class TestContributingFileExists:
    def test_file_exists(self):
        assert os.path.isfile(CONTRIBUTING_PATH), "CONTRIBUTING.md must exist at the repo root"

    def test_file_is_not_empty(self, contributing_content):
        assert len(contributing_content.strip()) > 0, "CONTRIBUTING.md must not be empty"

    def test_file_has_reasonable_length(self, contributing_content):
        lines = contributing_content.splitlines()
        assert len(lines) >= 50, f"CONTRIBUTING.md seems too short ({len(lines)} lines); expected >= 50"


class TestContributingRequiredSections:
    REQUIRED_SECTIONS = [
        "Getting Started",
        "Development Setup",
        "Coding Standards",
        "Pull Request",
        "Reporting Issues",
    ]

    @pytest.mark.parametrize("section", REQUIRED_SECTIONS)
    def test_required_section_present(self, contributing_content, section):
        assert section in contributing_content, (
            f"Required section '{section}' not found in CONTRIBUTING.md"
        )


class TestContributingTitle:
    def test_has_h1_title(self, contributing_content):
        lines = contributing_content.splitlines()
        assert lines[0].startswith("# "), "First line must be an H1 heading"

    def test_title_references_project(self, contributing_content):
        lines = contributing_content.splitlines()
        assert "TaskFlow" in lines[0], "H1 title should reference 'TaskFlow'"


class TestContributingCommitConventions:
    def test_mentions_conventional_commits(self, contributing_content):
        assert re.search(r"conventional commit", contributing_content, re.IGNORECASE), (
            "CONTRIBUTING.md should mention conventional commit format"
        )

    def test_mentions_branch_naming(self, contributing_content):
        # Should describe branch naming (feat/, fix/, etc.)
        assert re.search(r"feat/|fix/|branch", contributing_content, re.IGNORECASE), (
            "CONTRIBUTING.md should include branch naming conventions"
        )


class TestContributingCodeOfConduct:
    def test_mentions_code_of_conduct(self, contributing_content):
        assert re.search(r"code of conduct", contributing_content, re.IGNORECASE), (
            "CONTRIBUTING.md should reference a Code of Conduct"
        )
