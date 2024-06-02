import pytest


@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user("defunkt")

    assert user["login"] == "defunkt"


@pytest.mark.api
def test_user_not_exists(github_api):
    user = github_api.get_user("butenkosergii")

    assert user["message"] == "Not Found"


@pytest.mark.api
def test_repo_can_be_found(github_api):
    request = github_api.search_repo("become-qa-auto")

    assert request["total_count"] == 57


@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    request = github_api.search_repo("sergiibutenko_repo_non_exist")

    assert request["total_count"] == 0


@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    request = github_api.search_repo("a")

    assert request["total_count"] != 0


@pytest.mark.api
def test_organization_exists(github_api):
    organization = github_api.search_organization("engineyard")

    assert organization["login"] == "engineyard"


@pytest.mark.api
def test_organization_not_exists(github_api):
    organization = github_api.search_organization("engineyardsssss")

    assert organization["message"] == "Not Found"


@pytest.mark.api
def test_topic_can_be_found(github_api):
    request = github_api.search_topic("python")

    assert request["total_count"] == 7096


@pytest.mark.api
def test_topic_cannot_be_found(github_api):
    request = github_api.search_topic("python_become_qa_topic_non_exist")

    assert request["total_count"] == 0


@pytest.mark.api
def test_topic_with_single_char_be_found(github_api):
    request = github_api.search_topic("a")

    assert request["total_count"] != 0


@pytest.mark.api
def test_topic_results_per_page(github_api):
    request = github_api.search_topic("python", 50)

    assert len(request["items"]) == 50
