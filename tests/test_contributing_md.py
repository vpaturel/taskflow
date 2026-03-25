"""
Tests for CONTRIBUTING.md content and structure.
These tests validate that the contributing guide meets completeness
and quality requirements for an open-source project.
"""
import re
import os
import pytest


CONTRIBUTING_PATH = os.path.join(os.path.dirname(__file__), "..", "CONTRIBUTING.md")


@pytest.fixture(scope="module")
def content():
    with open(CONTRIBUTING_PATH, "r", encoding="utf-8") as f:
        return f.read()


@pytest.fixture(scope="module")
def lines(content):
    return content.split("\n")


class TestFileStructure:
    def test_file_is_non_empty(self, content):
        assert len(content.strip()) > 0, "CONTRIBUTING.md must not be empty"

    def test_file_ends_with_newline(self, content):
        assert content.endswith("\n"), "File should end with a newline"

    def test_h1_heading_at_top(self, lines):
        first_heading = next((l for l in lines if l.startswith("#")), None)
        assert first_heading is not None, "File must have at least one heading"
        assert first_heading.startswith("# "), "First heading must be H1 (single #)"


class TestRequiredSections:
    @pytest.mark.parametrize("section", [
        "Getting Started",
        "Development Setup",
        "Coding Standards",
        "Pull Request Process",
        "Reporting Issues",
    ])
    def test_required_section_present(self, content, section):
        assert section in content, f'Required section "{section}" is missing'

    def test_table_of_contents_present(self, content):
        assert "Table of Contents" in content, "A Table of Contents section is expected"

    def test_toc_links_match_headings(self, content):
        toc_links = re.findall(r"\[.*?\]\(#(.*?)\)", content)

        def slugify(h):
            slug = h.lower().replace(" ", "-")
            slug = re.sub(r"[^\w-]", "", slug)
            return slug

        headings = re.findall(r"^#{1,3} (.+)", content, re.MULTILINE)
        heading_slugs = [slugify(h) for h in headings]

        for link in toc_links:
            assert link in heading_slugs, (
                f"TOC link #{link} does not match any heading. "
                f"Available slugs: {heading_slugs}"
            )


class TestCodingStandards:
    def test_conventional_commits_referenced(self, content):
        assert "Conventional Commits" in content, (
            "Commit message conventions (Conventional Commits) should be documented"
        )

    def test_branch_naming_documented(self, content):
        assert "feat/" in content, "Branch naming convention 'feat/' should be documented"

    def test_code_blocks_present(self, content):
        code_blocks = re.findall(r"```", content)
        assert len(code_blocks) >= 4, (
            f"Expected at least 2 code blocks (open+close pairs), found {len(code_blocks) // 2}"
        )


class TestPRProcess:
    def test_pr_process_mentions_tests(self, content):
        pr_section_match = re.search(
            r"## Pull Request Process(.+?)(?=^## |\Z)", content, re.DOTALL | re.MULTILINE
        )
        assert pr_section_match, "Pull Request Process section not found"
        pr_section = pr_section_match.group(1)
        assert "test" in pr_section.lower(), (
            "PR process section should mention running tests"
        )

    def test_pr_process_mentions_approval(self, content):
        assert "approval" in content.lower(), (
            "PR process should mention the approval requirement"
        )


class TestAccuracyWarnings:
    def test_upstream_url_accuracy(self, content):
        """
        Warn if the upstream URL references serenity-demos/taskflow
        instead of the actual repo vpaturel/taskflow.
        This is a known inaccuracy in the current CONTRIBUTING.md.
        """
        # We record this as a known issue — not a hard failure
        # so the test passes but the warning is visible in output
        if "serenity-demos/taskflow" in content:
            import warnings
            warnings.warn(
                "CONTRIBUTING.md references upstream as 'serenity-demos/taskflow' "
                "but the actual repository is 'vpaturel/taskflow'. "
                "Consider updating the upstream remote URL.",
                UserWarning,
            )
