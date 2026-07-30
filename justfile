@_default:
    just --list

# Install development dependencies
@bootstrap:
    python -m pip install --upgrade pip uv
    python -m uv pip install --upgrade nox

# Run test coverage report
@coverage *ARGS="--no-install --reuse-existing-virtualenvs":
    uv tool run nox {{ ARGS }} --session "coverage"

# Format justfile
@fmt:
    just --fmt --unstable

# Run linting checks
@lint *ARGS="--no-install --reuse-existing-virtualenvs":
    uv tool run nox {{ ARGS }} --session "lint"

# Compile the uv lock file
@lock *ARGS:
    uv lock {{ ARGS }}

# Run all nox sessions
@nox *ARGS="--no-install --reuse-existing-virtualenvs":
    uv tool run nox {{ ARGS }}

# Build and publish a release to PyPI
@release:
    rm -rf build dist
    uv build
    git push --tags
    uv publish

# Run all tests
@test *ARGS="--no-install --reuse-existing-virtualenvs":
    uv tool run nox {{ ARGS }}

# Run tests in current environment
@test-env *ARGS="--no-install --reuse-existing-virtualenvs":
    uv tool run nox {{ ARGS }} --session "tests_env"

# Run tests with latest Python and Django versions
@test-latest *ARGS="--no-install --reuse-existing-virtualenvs":
    uv tool run nox {{ ARGS }} --session "tests-3.14(django='6.1')"
